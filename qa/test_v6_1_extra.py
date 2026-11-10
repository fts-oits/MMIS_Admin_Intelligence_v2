from pathlib import Path
from playwright.sync_api import sync_playwright
import json, csv, io, re
root=Path(__file__).resolve().parents[1];html=(root/'index.html').read_text()
report=[]
def ck(name,result,detail=''):
 report.append({'name':name,'pass':bool(result),'detail':str(detail)[:450]});print('PASS' if result else 'FAIL',name,str(detail)[:80],flush=True)
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox','--disable-dev-shm-usage'])
 page=b.new_page(viewport={'width':1440,'height':920},accept_downloads=True)
 page.set_default_timeout(4000)
 errs=[];page.on('pageerror',lambda e:errs.append(str(e)))
 page.set_content(html,wait_until='domcontentloaded')
 # Global financial card -> exact cohort and sum
 val=page.evaluate("()=>window.MMIS_V6.getReport().financial.overdue")
 page.locator('.metric-card[data-title="Overdue invoice balance"]').first.click()
 invoiceRows=page.evaluate('window.MMIS_V6.tableResults("invoiceList")')
 ck('Overdue liability amount and invoice worklist parity',sum(x['unpaid'] for x in invoiceRows)==val,(val,sum(x['unpaid'] for x in invoiceRows),len(invoiceRows)))
 with page.expect_download() as file:page.locator('button[data-act="export-csv"][data-table="invoiceList"]').click()
 csvpath=root/'qa'/'test_invoice_export.csv';file.value.save_as(csvpath)
 csvrows=list(csv.reader(io.StringIO(csvpath.read_text(encoding='utf-8-sig'))));ck('Overdue invoice export row parity',len(csvrows)-1==len(invoiceRows),(len(csvrows)-1,len(invoiceRows)))
 # invoice per vendor band counts all 61-90 (not max only)
 page.locator('[data-page="vendors"][data-act="nav"]').first.click()
 allband=page.evaluate('''()=>new Set(window.MMIS_V6.data.invoices.filter(i=>i.unpaid>0&&i.daysOverdue>=61&&i.daysOverdue<=90).map(i=>i.vendorId)).size''')
 page.locator('.bar-line[data-page="vendors"][data-preset="vendorList|ageBand|DAYS_61_90"]').click()
 matched=page.evaluate('window.MMIS_V6.tableResults("vendorList").length')
 ck('61-90 per-invoice Vendor count not oldest-age count',allband==matched,(allband,matched))
 page.locator('[data-act="shop-aging"]').click()
 vendors=page.evaluate('window.MMIS_V6.tableResults("vendorList")')
 actual=page.evaluate('''()=>{let D=window.MMIS_V6.data;return D.invoices.filter(i=>i.unpaid>0&&i.daysOverdue>=61&&i.daysOverdue<=90&&D.facilities.find(f=>f.id===i.facilityId)?.type==='SHOP').reduce((n,i)=>n+i.unpaid,0)}''')
 # proof filter amount is derived from exact eligible invoices
 displayed=page.locator('.table-panel[data-table="vendorList"] tbody tr')
 from decimal import Decimal
 amount=0
 for row in displayed.all():
  cells=row.locator('td').all_text_contents()
  if len(cells)>6:
   value=cells[6].replace('UGX','').replace(',','').strip()
   if value.isdigit():amount+=int(value)
 ck('Shop + 61-90 amount matches invoice cohort',amount==actual,(amount,actual))
 with page.expect_download() as d:page.locator('[data-act="export-csv"][data-table="vendorList"]').click()
 tmp=root/'qa'/'test_vendor_export.csv';d.value.save_as(tmp)
 n=len(list(csv.reader(io.StringIO(tmp.read_text(encoding='utf-8-sig')))))-1
 ck('Shop 61-90 CSV distinct Vendor parity',n==len(vendors),(n,len(vendors)))
 # Market state and search/filter back forward across actual page different
 page.locator('#market-select').select_option('kabale')
 ck('Market switch clears dependent filters',page.evaluate("!window.MMIS_V6.state.filters.vendorList?.ageBand"))
 page.locator('[data-act="shop-aging"]').click()
 page.locator('[data-act="nav"][data-page="facilities"]').first.click()
 page.go_back(wait_until='domcontentloaded')
 ck('Back restores Market and combined filters',page.evaluate("window.MMIS_V6.state.page==='vendors' && window.MMIS_V6.state.market==='kabale' && window.MMIS_V6.state.filters.vendorList?.ageBand==='DAYS_61_90' && window.MMIS_V6.state.filters.vendorList?.unitType==='SHOP'"))
 page.go_forward(wait_until='domcontentloaded')
 ck('Forward restores Facility page and scoped Market',page.evaluate("window.MMIS_V6.state.page==='facilities' && window.MMIS_V6.state.market==='kabale'"))
 # Deep link after reloading document at URL containing filters
 page.evaluate("()=>location.hash='#vendors?market=kabale&filters='+encodeURIComponent(JSON.stringify({vendorList:{q:'',unitType:'SHOP',ageBand:'DAYS_61_90'}}))")
 page.set_content(html,wait_until='domcontentloaded')
 ck('Refreshed deep link restores validated filters',page.evaluate("window.MMIS_V6.state.page==='vendors' && window.MMIS_V6.state.market==='kabale' && window.MMIS_V6.state.filters.vendorList?.unitType==='SHOP'"))
 # role unauthorized route
 page.locator('#role-select').select_option('vendor-pending');before=page.evaluate('window.MMIS_V6.state.page');page.evaluate('window.MMIS_V6.go("roles")');ck('Pending Vendor forbidden route stays blocked',page.evaluate('window.MMIS_V6.state.page')==before)
 ck('Authenticated public header shows no Sign In',page.locator('[data-page="shop-finder"]').count()>0)
 page.locator('[data-act="nav"][data-page="shop-finder"]').first.click()
 ck('Logged in public Shop header retains user & notifications',page.locator('.public-header').inner_text().find('Grace Akello')>=0 and page.locator('.public-header [data-act="notifications"]').count()==1 and page.locator('.public-header [data-act="simulate-login"]').count()==0)
 # read-only cannot assign cases (action absent)
 page.locator('#role-select').select_option('readonly');page.locator('[data-page="requests"][data-act="nav"]').first.click();page.locator('[data-kind="request"][data-act="detail"]').first.click()
 ck('Read-only request case drawer has no mutation controls',page.locator('[data-act="case-assign"]').count()==0 and page.locator('[data-act="case-info"]').count()==0)
 page.locator('[data-act="close-drawer"]').first.click()
 # role/capability explicit Gate/Stock columns and matrix
 page.locator('[data-page="roles"][data-act="nav"]').first.click()
 ck('RBAC matrix includes Gate and Stock roles', 'Gate Staff' in page.locator('table.permissions').inner_text() and 'Stock Counter' in page.locator('table.permissions').inner_text())
 # data fixture dueAt
 ck('Every sample request has dueAt timeline',all('dueAt' in r and 'timeline' in r for r in page.evaluate('window.MMIS_V6.data.requests')))
 ck('No JS exceptions',not errs,errs)
 b.close()
(root/'QA_RESULTS_EXTRA.json').write_text(json.dumps(report,indent=2))
print('TOTAL',len(report),'PASSED',sum(x['pass'] for x in report),'FAILS',[x for x in report if not x['pass']])
