from playwright.sync_api import sync_playwright
from pathlib import Path
import json,traceback
html=(Path(__file__).resolve().parents[1]/'index.html').read_text()
problems=[]
with sync_playwright() as p:
 b=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage'])
 page=b.new_page(viewport={'width':1440,'height':900},accept_downloads=True)
 page.on('pageerror',lambda error:problems.append('JS:'+str(error)))
 page.on('console',lambda m:problems.append('CONSOLE:'+m.text) if m.type=='error' else None)
 page.set_content(html,wait_until='domcontentloaded')
 print('INITIAL',page.title(),page.locator('.page-title').all_text_contents())
 pages=['global','requests','markets','vendors','facilities','suppliers','finance','staff','roles','imports','gate','rental','journey','supply-journey','shop-finder','my-business','library','design','review']
 for pg in pages:
  page.evaluate('(p)=>window.MMIS_V6.go(p)',pg)
  page.wait_for_timeout(25)
  title=page.locator('.page-title').first.inner_text()
  print(pg,':',title,'cards:',page.locator('.metric-card').count())
  if not title:problems.append('No title for '+pg)
 print('REQUEST COUNT=',page.evaluate('window.MMIS_V6.getReport().openCases'))
 print('FIN=',page.evaluate('window.MMIS_V6.getReport().financial'))
 print('DARK',page.evaluate('document.documentElement.dataset.theme'))
 page.locator('[data-act="theme"]').first.click()
 print('DARK AFTER',page.evaluate('document.documentElement.dataset.theme'))
 page.evaluate('()=>window.MMIS_V6.go("requests")')
 page.locator('select[data-filter-table="requestsList"][data-field="type"]').select_option('RENTAL')
 print('RENTAL ROWS',page.evaluate('window.MMIS_V6.tableResults("requestsList").length'))
 with page.expect_download() as dw:page.locator('[data-act="export-csv"][data-table="requestsList"]').click()
 fn=str(Path(__file__).resolve().parent/'export-smoke.csv');dw.value.save_as(fn)
 print('CSV LINES',len(Path(fn).read_text().splitlines()))
 page.locator('[data-act="detail"][data-kind="request"]').first.click()
 print('DRAWER',page.locator('.drawer h2').inner_text())
 page.keyboard.press('Escape')
 print('DRAWER CLOSED',page.locator('.drawer').count())
 for role in ['master','readonly','vendor-pending','vendor','supplier-pending','supplier','gate','stock','public']:
  page.locator('#role-select').select_option(role)
  print('ROLE',role,'PAGE',page.locator('.page-title').inner_text(),'NAV',page.locator('.nav-item').count())
  if role=='vendor-pending' and ('Inventory Management' not in page.content()):problems.append('missing restricted content explanation')
 b.close()
print('FAILURES',json.dumps(problems,indent=2))
(Path(__file__).resolve().parent/'SMOKE_REPORT.json').write_text(json.dumps({'pages':pages,'failures':problems},indent=2))
