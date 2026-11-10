from pathlib import Path
from playwright.sync_api import sync_playwright
import json
u=Path('/mnt/data/MMIS_Intelligence_Suite_V5/index.html').resolve().as_uri()
root=Path('/mnt/data/MMIS_Intelligence_Suite_V5/previews');root.mkdir(parents=True,exist_ok=True)
results={'pages':[],'errors':[],'overflow':[],'checks':[]}
with sync_playwright() as p:
 b=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage','--disable-gpu'])
 page=b.new_page(viewport={'width':1440,'height':960},accept_downloads=True)
 page.set_default_timeout(3000)
 page.on('pageerror',lambda e:results['errors'].append(str(e)))
 page.set_content(Path('/mnt/data/MMIS_Intelligence_Suite_V5/index.html').read_text(),wait_until='load');page.wait_for_timeout(180)
 print('INITIAL',page.title(),page.locator('h1.page-title').all_text_contents(),flush=True)
 pages=['global','markets','vendor','facility','supplier','staff','gate','imports','requests','catalog']
 for name in pages:
  print('TEST PAGE',name,flush=True)
  page.locator(f'[data-nav="{name}"]').click();page.wait_for_timeout(100)
  title=page.locator('h1.page-title').first.inner_text() if page.locator('h1.page-title').count() else 'MISSING'
  errs=page.locator('text=This preview section encountered a rendering error').count()
  dims=page.evaluate('({scroll:document.documentElement.scrollWidth,inner:window.innerWidth})')
  results['pages'].append({'page':name,'title':title,'renderError':errs,'dimensions':dims})
  if dims['scroll']>dims['inner']+1:results['overflow'].append((name,dims))
  if name in ['global','markets','vendor','facility','supplier','staff','gate','imports','requests','catalog']:
   page.screenshot(path=str(root/f'{name}_desktop.png'),full_page=False)
 # KPI click and detail
 page.locator('[data-nav="global"]').click()
 req_total=int(page.locator('.metric').nth(3).locator('.value').inner_text().replace(',',''))
 cat_counts=[int(t) for t in page.locator('.cat-count').all_text_contents()]
 results['checks'].append({'case':'request totals equal category sum','pass':req_total==sum(cat_counts),'total':req_total,'categories':sum(cat_counts)})
 page.locator('[data-category="RENTAL"]').click();results['checks'].append({'case':'category opens filtered request center','pass':page.locator('h1.page-title').inner_text()=='Request Center' and page.locator('select[data-f="filter"]').input_value()=='RENTAL'})
 page.locator('[data-open="request"]').first.click();results['checks'].append({'case':'request drawer','pass':page.locator('[role="dialog"]').count()==1});page.screenshot(path=str(root/'request_detail_drawer_desktop.png'),full_page=False);page.locator('[data-action="close-drawer"]').first.click()
 # export exact displayed rows when filtered
 with page.expect_download() as dl:
  page.locator('button[data-action="export"]').first.click()
 download=dl.value; path=root/'filtered_requests_sample.csv';download.save_as(path)
 exported=max(0,len(path.read_text().splitlines())-1)
 visible_total=int(page.locator('.table-foot').first.inner_text().split('matching rows')[0].split('·')[-1].strip())
 results['checks'].append({'case':'filtered request csv parity','pass':exported==visible_total,'exported':exported,'matching':visible_total})
 # Unit Type drill
 page.locator('[data-nav="facility"]').click();page.locator('[data-unit="SHOP"]').first.click()
 results['checks'].append({'case':'facility unit type matrix drill','pass':page.locator('select[data-f="filter"]').input_value()=='SHOP'})
 # roles
 page.locator('#role-select').select_option('master');page.wait_for_timeout(50)
 results['checks'].append({'case':'MarketMaster scope locked','pass':page.locator('#market-select').is_disabled() and page.locator('#market-select').input_value()=='A'})
 results['checks'].append({'case':'MarketMaster cannot see foreign Market records','pass':page.evaluate('window.__MMIS_V5.getState().market')=='A'})
 results['checks'].append({'case':'MarketMaster hides SuperAdmin governance','pass':page.locator('text=SuperAdmin manager governance').count()==0})
 page.locator('#role-select').select_option('vendor-pending');page.wait_for_timeout(70)
 body=page.locator('#content').inner_text()
 results['checks'].append({'case':'pending vendor gating','pass':'No Inventory, Payments, Invoices' in body and 'My rent unpaid' not in body})
 page.locator('#role-select').select_option('supplier-pending');page.wait_for_timeout(70)
 results['checks'].append({'case':'pending supplier gating','pass':'qualification pending' in page.locator('#content').inner_text() and page.locator('text=My procurement lifecycle').count()==0})
 page.locator('#role-select').select_option('stock');page.wait_for_timeout(70)
 results['checks'].append({'case':'Stock Counter scoped navigation','pass':page.locator('.nav').count()==1 and page.locator('h1.page-title').inner_text()=='Gate & Stock Intelligence'})
 page.locator('#role-select').select_option('readonly');page.wait_for_timeout(70)
 results['checks'].append({'case':'read-only admin banner','pass':page.locator('.read-only').count()==1})
 # mobile
 page.set_viewport_size({'width':390,'height':844});page.locator('#role-select').select_option('super');page.wait_for_timeout(80)
 for name in ['global','requests','vendor','facility','supplier','staff','gate','imports','markets']:
  page.locator('button.mobile-bar').click(timeout=3000);page.locator(f'.sidebar [data-nav="{name}"]').click(timeout=3000);page.wait_for_timeout(25)
  dim=page.evaluate('({scroll:document.documentElement.scrollWidth,inner:window.innerWidth})')
  if dim['scroll']>dim['inner']+1:results['overflow'].append((name,dim))
  if name in ['global','requests','gate','markets','facility','imports']:
   page.screenshot(path=str(root/f'{name}_mobile.png'),full_page=False)
 page.set_viewport_size({'width':320,'height':750});page.locator('button.mobile-bar').click(timeout=3000);page.locator('.sidebar [data-nav="global"]').click(timeout=3000)
 dim=page.evaluate('({scroll:document.documentElement.scrollWidth,inner:window.innerWidth})')
 if dim['scroll']>dim['inner']+1:results['overflow'].append(('global_320',dim))
 results['checks'].append({'case':'all page render no runtime errors','pass':not any(r['renderError'] for r in results['pages']) and not results['errors']})
 b.close()
print(json.dumps(results,indent=2))
Path('/mnt/data/MMIS_Intelligence_Suite_V5/QA_RESULTS.json').write_text(json.dumps(results,indent=2))
