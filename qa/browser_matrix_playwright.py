from playwright.sync_api import sync_playwright
from pathlib import Path
import json, re, csv
html=(Path(__file__).resolve().parents[1]/'index.html').read_text(); failures=[];checks=[]
def check(name,result,detail=None):
 checks.append({'check':name,'pass':bool(result),'detail':detail})
 if not result: failures.append({'check':name,'detail':detail})
with sync_playwright() as p:
 b=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage'])
 page=b.new_page(viewport={'width':1440,'height':900},accept_downloads=True)
 page.set_default_timeout(3000)
 page.on('pageerror',lambda error:failures.append({'check':'browser_js_error','detail':str(error)}))
 page.set_content(html,wait_until='domcontentloaded')
 pages=['global','requests','markets','vendors','facilities','suppliers','finance','staff','roles','imports','gate','rental','journey','supply-journey','shop-finder','my-business','library','design','review']
 for width in [320,375,390,768,1024,1280,1440,1920]:
  page.set_viewport_size({'width':width,'height':870})
  for pg in pages:
   page.evaluate('(p)=>window.MMIS_V6.go(p)',pg)
   w=page.evaluate('({inner:innerWidth,scroll:document.documentElement.scrollWidth})')
   check(f'no page overflow {width}px / {pg}',w['scroll']<=w['inner']+1,w if w['scroll']>w['inner']+1 else None)
 # representative navigation, filtering, all filtered CSV rows
 page.set_viewport_size({'width':1440,'height':900})
 page.evaluate('()=>window.MMIS_V6.setRole("super")')
 cases=page.evaluate('window.MMIS_V6.getReport().openCases')
 groups=page.evaluate('Object.entries({ONBOARDING:11,RENTAL:9,KYC:7,RECONCILIATION:6,SUPPORT:8,CONTRACT:5,IMPORT:5,GATE:4}).reduce((n,[k,v])=>n+window.MMIS_V6.data.requests.filter(x=>x.type===k&&x.status==="OPEN").length,0)')
 check('global request category parity',cases==groups==55,{'headline':cases,'categories':groups})
 page.evaluate('()=>window.MMIS_V6.go("requests")')
 page.locator('[data-filter-table="requestsList"][data-field="type"]').select_option('RENTAL')
 count=page.evaluate('window.MMIS_V6.tableResults("requestsList").length');check('rental case filter',count==9,count)
 with page.expect_download() as d:page.locator('button[data-act="export-csv"][data-table="requestsList"]').click()
 file=Path(__file__).resolve().parent/'matrix_case.csv';d.value.save_as(file)
 with file.open(encoding='utf-8-sig',newline='') as f:rows=list(csv.reader(f))
 check('rental filter CSV row parity',len(rows)-1==count,{'exported':len(rows)-1,'matching':count})
 check('CSV Market labels use display value',all('Market' in rows[0] for _ in [0]) and any('Market' in r[3] for r in rows[1:]),rows[1][:4])
 page.locator('[data-act="detail"][data-kind="request"]').first.click()
 check('source evidence drawer opened',page.locator('.drawer').count()==1)
 page.keyboard.press('Escape');check('escape dismisses drawer',page.locator('.drawer').count()==0)
 # scope switch and exact population
 page.locator('#market-select').select_option('kabale')
 mCases=page.evaluate('window.MMIS_V6.tableResults("requestsList").length')
 should=page.evaluate('window.MMIS_V6.data.requests.filter(x=>x.marketId==="kabale"&&x.status==="OPEN").length')
 check('market scoping on Request Center',mCases==should,{'actual':mCases,'expected':should})
 page.locator('#market-select').select_option('all')
 # facility matrix and active contract gap
 page.evaluate('()=>window.MMIS_V6.go("facilities")')
 gap=page.evaluate('window.MMIS_V6.data.facilities.filter(f=>f.status==="OCCUPIED"&&f.contract!=="ACTIVE").length')
 page.locator('[data-preset="facList|contractGap|GAP"]').first.click()
 selected=page.evaluate('window.MMIS_V6.tableResults("facList").length')
 check('Facility Contract gap card and filtered source parity',gap==selected,{'gap':gap,'matchingRows':selected})
 page.evaluate('()=>window.MMIS_V6.go("rental")')
 page.locator('input[data-select]').first.check()
 check('rental preflight selection state',page.evaluate('window.MMIS_V6.state.select.size')==1)
 page.locator('[data-act="preview-selected"]').first.click()
 check('selected preview does not offer invoice POST',page.locator('.drawer .warn-box').count()==1 and 'NEVER POST' in page.locator('.drawer').inner_text())
 page.keyboard.press('Escape')
 # catalogs
 page.evaluate('()=>window.MMIS_V6.go("library")')
 check('KPI catalog complete',page.evaluate('window.MMIS_V6.tableResults("kpiList").length')==179)
 page.locator('select[data-filter-table="kpiList"][data-field="domain"]').select_option('VENDOR')
 check('Vendor KPI family count',page.evaluate('window.MMIS_V6.tableResults("kpiList").length')==45)
 # Role nav denial / scoping
 expected={'vendor-pending':3,'vendor':3,'supplier-pending':2,'supplier':2,'gate':3,'stock':3,'public':2}
 for role,count in expected.items():
  page.locator('#role-select').select_option(role)
  check(f'{role} restricted nav length',page.locator('.nav-item').count()==count,page.locator('.nav-item').all_text_contents())
  if role=='vendor-pending':check('pending Vendor no payment/invoice nav',not any('Payment' in n or 'Invoice' in n or 'Inventory' in n for n in page.locator('.nav-item').all_text_contents()))
  if role=='public':check('public header has Sign in',page.locator('.topbar [data-act="simulate-login"]').count()==1)
 page.locator('#role-select').select_option('vendor-pending')
 page.locator('.nav-item[data-page="shop-finder"]').click()
 check('logged-in public Shop finder has account and Logout not Sign In',page.locator('.public-header [data-act="simulate-logout"]').count()==1 and page.locator('.public-header [data-act="simulate-login"]').count()==0)
 page.locator('#role-select').select_option('readonly')
 page.evaluate('()=>window.MMIS_V6.go("roles")')
 check('read-only role cannot make RBAC changes','grant access' not in page.content().lower())
 # theme + feedback
 page.locator('#role-select').select_option('super')
 page.evaluate('()=>window.MMIS_V6.go("review")')
 page.locator('input[data-pm="shell"]').check()
 with page.expect_download() as d:page.locator('[data-act="export-feedback"]').first.click()
 f=Path(__file__).resolve().parent/'matrix_pm.json';d.value.save_as(f);r=json.loads(f.read_text())
 check('PM feedback exports local approval',any(x['id']=='shell' and x['approved'] for x in r['approvals']))
 # no requests to external domains and no remote scripts
 check('fully offline html',not re.search(r'<(?:script|link)[^>]+(?:src|href)=[\'\"]https?://',html))
 b.close()
report={'testedPages':pages,'responsiveWidths':[320,375,390,768,1024,1280,1440,1920],'checks':len(checks),'passed':sum(c['pass'] for c in checks),'failures':failures}
(Path(__file__).resolve().parent/'BROWSER_QA_MATRIX.json').write_text(json.dumps(report,indent=2))
print(json.dumps({'checks':report['checks'],'passed':report['passed'],'failureCount':len(failures),'failures':failures[:25]},indent=2))
