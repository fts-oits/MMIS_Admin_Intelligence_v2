# MMIS Global Operations Dashboard — SuperAdmin & MarketMaster

**Visual design proposal:** 9 November 2026  
**Purpose:** PM/UI sign-off before implementation. Not a code PR or financial UAT certificate.  
**Related UX issue:** https://linear.app/oits-dhaka/issue/MMIS-893/fe-refine-insights-cards-and-responsive-dashboard-layouts

## How to review the exact design

1. Extract this ZIP and open `MMIS_Global_Operations_Admin_Prototype.html` in Chrome or Edge. No server, login or internet connection is needed.
2. Switch **Preview admin role** from `SuperAdmin` to `MarketMaster`.
3. As SuperAdmin, review `All Markets`, then `Example Market A` or `Example Market B`.
4. As MarketMaster, confirm the Market selector is fixed to the example **assigned Market**, with no Global or other Market option.
5. Switch **Rent reporting period** between Current month and Last three months. Finance measures update as examples; the due-balance metric represents an as-of position.
6. Click any KPI, queue item, domain shortcut or Market comparison row. The prototype shows the intended destination and Market scope; it does not navigate to a live MMIS service.
7. Compare desktop and mobile screenshots. Resize the browser to assess additional viewport widths.
8. Record explicit approvals and section-specific change requests before development.

## Intended page structure

1. **Context bar** — effective role, authorized Market scope, rent reporting period and reporting freshness.
2. **Only four main KPIs** — SuperAdmin Global: Markets in operation, payments applied to rent, verified overdue rent, items requiring review. MarketMaster: Active Vendor accounts, payments applied, verified overdue, items requiring review.
3. **Needs Your Attention** — actionable work queues, not duplicated summaries: payment mismatch, occupied-without-contract, online verification, Vendor review and offline payment review. Counts represent work items, not distinct Vendors.
4. **Rent & Payments at a Glance** — rent billed, payments applied to the same invoice cohort, rent still unpaid, and separately identified amounts needing reconciliation. Financial history and aging remain in Vendor Overview.
5. **Overview by Area** — compact Vendor, Facility, Payments, Supplier, Staff/Gate and Markets-or-RentContracts panels with full-report links.
6. **Role-specific section** — Global SuperAdmin: Compare Markets; selected-Market SuperAdmin: focused Market priorities; MarketMaster: assigned-Market priorities.
7. **Data Quality & Reporting Notes** and Quick Navigation — evidence limitations, shared exceptions and links.

## Explicit design limitations / backend dependencies

| Design element | Existing dashboard contract | Proposed/required change |
|---|---|---|
| Vendor status, payments review, Facility/staff counts and Market totals | Present in `AdminDashboard` | Reuse with role/Market authorization and correct statuses |
| Reported collection and overdue amounts | Existing `financial.*` attributes | Before labeling "verified" or comparing billed/paid/unpaid, source from reconciled invoice-cohort evidence and certified/held separation |
| Facility contract-gap queue | Available through Facility Intelligence separately | Reuse authorized Facility exception/reporting contract for shared queue; do not infer from raw occupancy alone |
| Supplier readiness, PO/delivery performance | **Not present** in current admin dashboard API | Use explicit unavailable state until Supplier-scope and procurement contracts are accepted |
| Market-by-Market collections/overdue comparison | **Not present** in current admin dashboard API | New authorized aggregation or materialized read model needed, with deduplication and basis parity |
| Four-KPI summary | Current code displays repeated large panels | Consolidate; do not reintroduce all detailed rent/Facility reports on Global Dashboard |
| As-of/partial/refresh status | Existing API returns `asOf`, `partial`, `unavailableSections` | Retain and prominently display actual availability rather than zeros or placeholders |

**Important:** All sample counts, amounts, Market names and Vendor totals are fabricated for GUI review. They are not current MMIS operational data, and the example amounts are not financially certified. The reviewer's role switch exists only in this offline prototype, not as a proposed production control.

## Theme and layout preservation

Retain MarketMasterERP `style.css` palette: background `#f7f4eb`, card `#fffdf8`, primary `#263e32`, muted `#eeece2`, border `#dcded0`, existing chart and warning semantics, DM Sans / Arial font stack, and existing sidebar/header patterns.

On narrow screens, show two KPI columns when readable, single-column actionable queues and responsive domain panels; permit horizontal scrolling only inside the labeled Market comparison table. Existing authenticated account controls remain in the header.

## Required PM approval decisions

- [ ] Labels, order and meaning of the four headline KPIs are understandable.
- [ ] SuperAdmin Global is clearly separated from SuperAdmin selected-Market and MarketMaster assigned-Market views.
- [ ] No MarketMaster can select All Markets or a foreign Market in the final system.
- [ ] Needs Your Attention is more prominent than duplicate chart/report sections, and every queue has an authorized destination.
- [ ] Rent billed, payments applied, still unpaid, verified overdue and held amounts are not conflated.
- [ ] Vendor, Facility, Supplier, Payments, Staff and Market/RentContract domains are sufficiently covered, without copying their full detailed reports.
- [ ] Supplier domain data and cross-Market comparison are identified as backend-dependent, not ready-made features.
- [ ] Global Market comparison includes the correct business columns and filtering direction.
- [ ] Data quality, partial/failed refresh, authorization and evidence handling are acceptable.
- [ ] Desktop/mobile responsive styling matches MMIS and passes readability and keyboard requirements.
- [ ] Proposed destinations and drill-down context are consistent with Vendor/Facility Intelligence designs.

## Developer acceptance after visual approval

- No modifications to `dev`, `main`, `dev_basic` or `staging` except through existing protected processes; use separate feature/test branches.
- No new GitHub Actions workflow files.
- Do not create a parallel financial calculation or rely on the current `monthlyRent` rate as issued rent.
- MarketMaster server authorization must resolve assigned Market; SuperAdmin can access only permitted Market/global scope.
- Integrate with shared Vendor–Facility–RentContract intelligence and authoritative invoice/reporting evidence.
- No financial certification from unverified/held/partial sections; do not show unavailable values as zero.
- Every dashboard card and queue drill-down keeps the effective Market and reporting context.
- Validate at 320, 375, 390, 768, 1024, 1280, 1440px plus zoom/keyboard.
- Exact-head unit/build plus authenticated frontend/API/native PostgreSQL UAT and finance reconciliation required before launch.

## Recorded local prototype QA

Standalone HTML was rendered in headless Chromium on the 1440px desktop, 1280px selected-Market desktop and 390px mobile roles. UI assertions verified the SuperAdmin Global comparison, selected-Market focus mode, MarketMaster's disabled Market selector, KPI preview dialogs and no JS errors or page-wide overflow in these viewports. This is **visual/prototype QA only**, not implementation/UAT evidence.

## Proposed PM sign-off phrase

"I reviewed the attached MMIS Operations Dashboard prototype for SuperAdmin and MarketMaster roles. I approve the role-aware page hierarchy, four primary KPI cards, prioritized attention queue, concise rent position, compact domain shortcuts, global Market comparison, single-Market priorities and responsive use of the existing MMIS visual theme, subject to the noted backend reporting/authorization gates. The following changes are requested before implementation: ________ ."
