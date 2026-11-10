# MarketMaster MMIS — Intelligence Suite V5

**Deliverable:** Complete, fully offline interactive design prototype, dated 2026-11-10.

## Open the preview

1. Unzip this package into a normal folder.
2. Double-click **`index.html`** in Chrome or Edge. This is the COMPLETE V5 application launcher; it does not require internet, a server, NPM, GitHub or an MMIS login.
3. Use the **Role** selector in the upper toolbar to preview SuperAdmin, MarketMaster, read-only Admin, approved/pending Vendor, approved/pending Supplier, Gate Staff and Stock Counter experiences.
4. SuperAdmin can choose `All Markets` or an individual Market. MarketMaster and operations staff are restricted to their illustrative assigned Market.
5. Click any active KPI, request category, Unit Type, record row or **Details** to inspect a filtered list or evidence drawer. Export the filtered example dataset as CSV.

**If an in-chat HTML preview is blank:** download the ZIP, use **Extract All**, and open `index.html` in a desktop browser. All styles, scripts, sample data and KPI definitions are embedded in this single HTML file. There are no missing runtime assets or external dependencies.

## What's in V5

V5 contains twelve navigable destinations (nine administrative workspaces, two account-specific business workspaces, and the KPI evidence library):

| Workspace | Functionality in offline V5 |
|---|---|
| 1. Global Operations Dashboard | Four headline KPIs, unified Request Center counts, exceptions, Market comparison and domain shortcuts |
| 2. Market Intelligence | Market Registry, capacity, occupancy, finance and manager/readiness comparisons |
| 3. Vendor Overview | Registration/KYC/tenancy, rent billed, verified invoice allocations, unpaid debt, aging and Vendor drill-down |
| 4. Facility Intelligence | Physical-unit counts, Shop/Stall/Pitch/Cage/Lock-up matrix, occupancy, Contracts, invoice attribution, gaps |
| 5. Supplier Overview | Qualification, Market coverage, procurement stages, POs, late commitments, quality and delivery evidence |
| 6. Staff & Managers | Role scope, assignments, staff restrictions, MarketMaster coverage, work owner concepts |
| 7. Gate & Stock Intelligence | Token stages, Stock reconciliation, custody/quantity variance and fiscal evidence context |
| 8. Vendor Import Integrity | Import stage distribution, blocked records, review, consolidation and provenance |
| 9. Request Center | Eight request categories, open/overdue/mine/unassigned queues, priority, filter/search, evidence drawer, export |
| 10. My Vendor Business | Approved Vendor: own financial/Stock/Supply view; pending Vendor: onboarding and rental journey only |
| 11. My Supplier Business | Approved Supplier: own POs and delivery evidence; pending Supplier: qualification journey only |
| 12. KPI & Evidence Library | All **179 approved groups**: Vendor 45, Facility 41, Supplier 57, Cross-domain 24, Staff 12 |

### Enhanced from V4

- New dedicated Market Intelligence, Import Intelligence and Gate/Stock Intelligence.
- One shared navigation, role switcher and Market scope instead of independent disconnected previews.
- Distinct **requests awaiting action** and **operational exceptions**; categories sum to the same unique open case total.
- Record-level evidence drawers for Markets, Vendors, Facilities, Suppliers, staff, imports, POs, Gate tokens, request cases and KPIs.
- Unit Type Financial Matrix attributes invoices to Shop-backed physical units and distinguishes distinct Vendors from physical-unit counts.
- End-to-end sample Supplier → PO → Gate → Stock custody references.
- Filtered full-population CSV export, without needing a remote API.
- Approved and pending Vendor/Supplier dashboards with an explicit restricted experience.
- 34 actual browser screenshots in `previews/`; desktop and mobile views.
- The previous self-contained V4 pages are retained in `V4_Approved_Reference/` for visual comparison.

## Evidence warnings

**All names, business transactions, Market names, financial numbers, Counts, cases, POs, payments and statuses in V5 are fictional demonstration data.** A same-source, deterministic local dataset is used for internally consistent interactions; it is **not** the live MMIS database, a real account, or a legally/financially certified report.

The current `dev_basic` code has genuine domain workflows, but not every V5 metric is backed by a production aggregation endpoint. See `V5_ENGINEERING_CONTRACT.md` and `V5_SOURCE_MAPPING.md`. Mock clickable actions only show proposed paths; they do **not** execute approvals, mutate records, call an MMIS API, create an email, or submit financial documents.

## Package structure

- `index.html` — **fully self-contained V5 interactive application**.
- `KPI_CATALOG_V5.json` — 179 grouped KPI definitions with priority, maturity and drill-down descriptions.
- `V5_SOURCE_MAPPING.md` — mapping to current MMIS operational pages and implementation status.
- `V5_ENGINEERING_CONTRACT.md` — integration, data, filtering, reconciliation, RBAC and acceptance requirements.
- `V5_PM_REVIEW_CHECKLIST.md` — product/design approval checklist.
- `V5_QA_REPORT.md`, `QA_RESULTS.json`, `MATRIX_QA_RESULTS.json` — browser QA evidence.
- `engineering_source/` — optional editable development sources (NOT required to run `index.html`).
- `qa/` — reproducible Chromium/Playwright smoke scripts, optional.
- `previews/` — actual V5 desktop/mobile screenshots.
- `V4_Approved_Reference/` — existing approved V4 offline prototype pages.

## Governance and publication

No live MMIS backend or frontend code, production database, GitHub branch, Pull Request, workflow, or Linear issue was changed. Do not alter the `dev`, `main`, `dev_basic` or `staging` branches of either application repository for convergence/testing. Use dedicated purpose-built branches, local/manual validation, and evidence-first acceptance. The separate design repository `fts-pro/mmis-intel-dashboards-v2` was not changed: the previously encountered GitHub connector 403 write restriction was not bypassed.
