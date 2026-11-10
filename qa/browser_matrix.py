from pathlib import Path
from playwright.sync_api import sync_playwright
import json
html=Path('/mnt/data/MMIS_Intelligence_Suite_V5/index.html').read_text()
checks=[]
with sync_playwright() as p:
 b=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage'])
 page=b.new_page(viewport={'width':1440,'height':900},accept_downloads=True)
 page.set_default_timeout(3000)
 page.set_content(html,wait_until='domcontentloaded')
 for width in [320,375,390,768,1024,1440,1920]:
  page.set_viewport_size({'width':width,'height':800})
  for pg in ['global','markets','vendor','facility','supplier','staff','gate','imports','requests','catalog']:
   page.evaluate('(p)=>window.__MMIS_V5.openPage(p)',pg)
   vals=page.evaluate('({doc:document.documentElement.scrollWidth,width:innerWidth})')
   if vals['doc']>width+1: checks.append({'kind':'OVERFLOW','width':width,'page':pg,'val':vals})
 for role,expected in [('super',10),('master',10),('readonly',10),('vendor',1),('vendor-pending',1),('supplier',1),('supplier-pending',1),('gate',1),('stock',1)]:
  page.locator('#role-select').select_option(role)
  a=page.locator('.sidebar .nav').count()
  if a!=expected:checks.append({'kind':'ROLE_NAV','role':role,'count':a,'expected':expected})
 page.locator('#role-select').select_option('super')
 # request CSV and filter parity, vendor overdue, facility GAP and import review
 for pg,filterval in [('vendor','OVERDUE'),('facility','GAP'),('imports','NEEDS_REVIEW'),('gate','ITEMS_RECORDED'),('requests','RENTAL'),('supplier','ACTIVE'),('staff','GateStaff')]:
  page.evaluate('(p)=>window.__MMIS_V5.openPage(p)',pg)
  page.locator('select[data-f="filter"]').first.select_option(filterval)
  match=None
  tables=page.locator('.table-card:has(.table-foot)')
  table=tables.first
  import re
  ptxt=table.locator('.table-foot').inner_text()
  m=re.search(r'(\d+) matching rows',ptxt)
  if m:match=int(m.group(1))
  try:
   with page.expect_download(timeout=2500) as d:table.locator('button[data-action="export"]').first.click()
   save=Path('/mnt/data/mmis_v5_build/tmp-'+pg+'.csv');d.value.save_as(save)
   exported=len(save.read_text().splitlines())-1
   if exported!=match:checks.append({'kind':'CSV_PARITY','page':pg,'filter':filterval,'visible':match,'exported':exported})
  except Exception as e:
   if match!=0:checks.append({'kind':'CSV_FAIL','page':pg,'error':str(e)[:200],'expected':match})
 b.close()
print('MATRIX FAILURES',json.dumps(checks,indent=2))
Path('/mnt/data/MMIS_Intelligence_Suite_V5/MATRIX_QA_RESULTS.json').write_text(json.dumps({'failures':checks,'widths':[320,375,390,768,1024,1440,1920],'roleScenarios':9,'csvCases':7},indent=2))
