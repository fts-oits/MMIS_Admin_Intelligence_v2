# MMIS Intelligence Suite v3 — upgraded PM approval package

**Status:** Completed local design package; **GitHub publication blocked by connector permission** (403 on creating `dev-v2`). The package uses the prior seven-page ZIP as its visual baseline and retains its original screenshots.

## How to review

1. Extract the ZIP without flattening directories.
2. Open `START_HERE_V3.html` in Chrome or Edge (or serve the directory from a trusted local static web server).
3. Review Global Operations, Vendor Overview, Facility Intelligence, Supplier Overview, Staff & Managers, Vendor Business and Supplier Business.
4. Open `04_Intelligence_V3/KPI_LIBRARY.html` to inspect the 179 categorized insight groups and filter by domain/priority/maturity.
5. Inspect the `04_Intelligence_V3/*_V3_Insights_Desktop.png` screenshots and `04_Intelligence_V3/PM_REVIEW_CHECKLIST.md`.

## What's new

- 143 approved Vendor/Facility/Supplier KPI groups and 36 supplementary cross-domain/staff groups.
- Evidence maturity and P0/P1/P2 badges; search and filter; drill-down specification per card.
- Additional analytics panels for each of the seven existing page views, without replacing their original UI.
- Unit Type investigation controls, invoice-cohort rent safeguards, Supplier PO/Gate/Stock/settlement hierarchy, pending-account gating, scope rules.
- CSV export of the **KPI definitions**, not the underlying financial sample numbers.
- Non-destructive installer to apply the enhancement to a live repository clone without overwriting post-package changes.

## Repository upgrade

**Do not overwrite newer repository HTML files with the older HTML copies in this ZIP.** The repository's `main` may contain subsequent refinements. Instead apply the additive upgrade:

`python3 tools/apply_v3.py --source /path/to/extracted/package --repo /path/to/clone`

Follow `04_Intelligence_V3/BRANCH_AND_PR_HANDOFF.md` for the requested `main → dev-v2 → dev-v3 → PR to main` workflow. No protected branch is directly modified.

All business metrics and persons in these mockups are illustrative. The prototype does not alter records or send notifications.
