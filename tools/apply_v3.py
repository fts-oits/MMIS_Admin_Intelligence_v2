#!/usr/bin/env python3
"""Non-destructively layer MMIS Intelligence v3 onto a checkout of mmis-intel-dashboards-v2.

Usage: python tools/apply_v3.py --source /path/to/MMIS_Intelligence_V3_Upgrade --repo .
The script edits only the established HTML entrypoints, and copies additive V3 assets.
It is idempotent and never touches Git branches, workflows, screenshots, or source financials.
"""
from pathlib import Path
import argparse, shutil
parser=argparse.ArgumentParser()
parser.add_argument('--source',required=True)
parser.add_argument('--repo',required=True)
args=parser.parse_args()
src=Path(args.source).resolve(); dst=Path(args.repo).resolve()
assets=src/'04_Intelligence_V3'; target=dst/'04_Intelligence_V3'
if not assets.is_dir():raise SystemExit(f'Missing asset directory {assets}')
if assets.resolve()!=target.resolve():
 target.mkdir(parents=True,exist_ok=True)
 for f in assets.iterdir():
  if f.is_file():shutil.copy2(f,target/f.name)
for f in ['START_HERE_V3.html']:
 if (src/f).is_file() and (src/f).resolve()!=(dst/f).resolve():shutil.copy2(src/f,dst/f)
paths=[
 ('01_Global_Dashboard/MMIS_Global_Operations_Admin_Prototype.html','../'),
 ('02_Vendor_Facility/MMIS_Vendor_Facility_Interactive_Prototype.html','../'),
 ('03_Expanded_Intelligence/MMIS_Expanded_Intelligence_Interactive_Prototype.html','../'),
 ('MMIS_BI_Dashboards_V2/01_Global_Dashboard/MMIS_Global_Operations_Admin_Prototype.html','../../'),
 ('MMIS_BI_Dashboards_V2/02_Vendor_Facility/MMIS_Vendor_Facility_Interactive_Prototype.html','../../'),
 ('MMIS_BI_Dashboards_V2/03_Expanded_Intelligence/MMIS_Expanded_Intelligence_Interactive_Prototype.html','../../')]
changed=0
for name,prefix in paths:
 p=dst/name
 if not p.is_file():continue
 s=p.read_text(encoding='utf-8-sig');end='\r\n' if '\r\n' in s else '\n'
 if 'MMIS_KPI_CATALOG_V3' in s or 'insights-v3.js' in s:
  print('SKIP already enhanced:',name);continue
 if '</head>' not in s:raise SystemExit(f'Missing </head> in {name}')
 addition='\n<!-- MMIS v3 additive insights; original page layout and data remain intact. -->\n'
 addition+=f'<link rel="stylesheet" href="{prefix}04_Intelligence_V3/insights-v3.css">\n'
 addition+=f'<script defer src="{prefix}04_Intelligence_V3/kpi-catalog.js"></script>\n'
 addition+=f'<script defer src="{prefix}04_Intelligence_V3/insights-v3.js"></script>\n'
 s=s.replace('</head>',addition+'</head>',1)
 p.write_text(s,encoding='utf-8',newline='' if end=='\n' else None)
 changed+=1;print('ENHANCED',name)
for name,prefix in [('index.html',''),('START_HERE.html',''),('MMIS_BI_Dashboards_V2/START_HERE.html','../')]:
 p=dst/name
 if not p.is_file():continue
 s=p.read_text(encoding='utf-8-sig');mark='<!-- MMIS-V3-LAUNCH -->'
 if mark in s:continue
 if '</body>' not in s:continue
 link=f'{prefix}START_HERE_V3.html' if prefix else 'START_HERE_V3.html'
 s=s.replace('</body>',f'{mark}<a style="position:fixed;right:14px;bottom:14px;padding:12px 16px;background:#263e32;color:#fffdf8;border:2px solid #fffdf8;border-radius:9px;z-index:200;font:700 12px DM Sans,Arial,sans-serif;box-shadow:0 3px 18px #263e3250" href="{link}">View approved Intelligence v3 ↗</a></body>',1)
 p.write_text(s,encoding='utf-8');changed+=1;print('LINKED',name)
print('Updated',changed,'existing HTML entrypoints; no existing panels removed.')
