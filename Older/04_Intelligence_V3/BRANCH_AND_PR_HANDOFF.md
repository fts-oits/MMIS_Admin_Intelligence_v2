# GitHub handoff: dev-v2 → dev-v3 → PR to main

Target repository: `fts-pro/mmis-intel-dashboards-v2`.

GitHub connector attempted branch creation twice on 2026-11-10; both attempts returned **403 Resource not accessible by integration**. No remote branches or PR could be created through that connection. The local implementation is complete as a non-destructive overlay and must be applied only after repository write permissions are restored.

Use a GitHub connection with **Contents: Read and write** and **Pull requests: Read and write** on this repository, or run the following commands through an authorized local Git session. These commands intentionally do not modify main directly.

```bash
git clone https://github.com/fts-pro/mmis-intel-dashboards-v2.git
cd mmis-intel-dashboards-v2
git fetch origin main
git switch -c dev-v2 origin/main
git push -u origin dev-v2
git switch -c dev-v3 dev-v2
python3 /path/to/MMIS_Intelligence_V3_Upgrade/tools/apply_v3.py --source /path/to/MMIS_Intelligence_V3_Upgrade --repo .
# Inspect changes and verify browsers before commit.
git status --short
git diff --check
git add 01_Global_Dashboard 02_Vendor_Facility 03_Expanded_Intelligence MMIS_BI_Dashboards_V2 index.html START_HERE_V3.html 04_Intelligence_V3
# Include tools/apply_v3.py if needed for repeatable upgrades.
git add tools/apply_v3.py
git commit -m "feat(intelligence): add approved v3 KPI catalog and scoped drilldown designs"
git push -u origin dev-v3
gh pr create --repo fts-pro/mmis-intel-dashboards-v2 --base main --head dev-v3 --title "[MMIS Intelligence V3] Approved KPI library and role-aware dashboard enhancements" --body-file 04_Intelligence_V3/PR_DESCRIPTION.md
```

Note: If either branch already exists after permissions are restored, inspect its head and branch history before proceeding; do not force-reset or overwrite it.
