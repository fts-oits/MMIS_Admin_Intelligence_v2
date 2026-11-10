# MMIS V6.1 — Functional Completeness & Journey Corrections (PM Review)

**Date:** 10 November 2026  
**Basis:** PM-approved V6 visual design and independent PM functional audit.  
**Delivery:** Standalone interactive HTML, corrected JavaScript / source dataset, reproducible browser tests, PM signoff evidence, desktop/mobile screenshots.  
**Production impact:** **None.** This package changes no GitHub branch/PR, database, API, rental posting, government fiscalization, or real user account.

## Launch the demo

1. Extract the ZIP using **Extract All**.
2. Open **`index.html`** with Chrome or Edge. Every script, style and fictional dataset is embedded in this file. No local server, login, internet, external font or dependency download is necessary.
3. Select a **Role** in the top header, then click destinations in the sidebar. Use **SuperAdmin** for cross-Market intelligence and **MarketMaster** for Kabale-only administrative journeys.
4. Review the **`previews/v6_1_functional/`** folder for the latest screenshots. Older screenshots in `previews/` are retained as original V6 visual references.
5. Read `V6_1_FIX_VERIFICATION_REPORT.md` and `V6_1_PM_FUNCTIONAL_SIGNOFF_CHECKLIST.md` before signing off.

In-chat HTML viewers may restrict JavaScript. If the inline preview is blank, use the extracted `index.html` in a desktop browser.

## What V6.1 fixes

| Functional signoff gap | V6.1 demo result | Test evidence |
|---|---|---|
| KPI → exact population and combined Market/Unit Type/aging | Fixed Facility Contract-gap and Import attention links; invoice-level overdue balance; Vendor 61–90 inclusive-per-invoice population; Shop×61–90 exact Vendor and invoice cohort amounts | 13/13 Facility, 12/12 Import, 11/11 61–90 Vendors, 3/3 Shop Vendors, UGX 447,000 Shop cohort, UGX 4,392,000 invoice overdue |
| Public Shop → login → application → approval → Contract acceptance | Added simulated stateful journey, selected Shop preserved across sign-in, application draft/reference, separate onboarding/KYC, rental TIN/Stock and Contract-terms approval and Vendor acceptance | Browser-tested complete role handoffs |
| Rental Readiness | Added billing period, first-liable day, mock applicable policy date/version, terms evidence, existing-invoice collision and reason-coded preflight; **no invoice posting** | Browser-tested selected Facility preview |
| Request Center | Added dueAt, sample review target, assignment, info request/escalation states, audit log, notifications inbox and source decision preview (not a generic approve) | Browser-tested case state and inbox |
| Supplier → PO → Gate → Stock → receipt | Added fictional, role-gated qualification, bid award, PO, supplier ACK/dispatch, Gate admission, Stock quantity verification, variance, receipt acceptance, distinct fiscal/settlement HOLD | Browser-tested MarketMaster, Supplier, Gate Staff and Stock Counter sequence |
| Browser history and RBAC | Added hash/URL filter state restoration, Back/Forward, Market switch dependent-filter reset, refreshed deep-link restoration, effective permission inspector with read-only/foreign-Market denial and Gate/Stock capability columns | Browser-tested navigation and negative checks |

## Guided applicant story — try this first

1. In the **Role** menu, select `Public Guest`; open **Public Shop Finder**.
2. Select the first vacant Kabale unit, `FAC-0003` (Lock-up), click **See details & apply**, then **Apply for this Shop**.
3. The selected unit is retained. Click **Sign in** and verify the header changes to the authenticated pending Vendor, without Inventory/Payments/Invoices navigation.
4. Complete the application note, click **Submit application (simulation)** and observe the trackable `DEMO-APP-FAC-0003` reference.
5. Click **Switch to authorized MarketMaster reviewer**. Check the canonical identity/KYC evidence and approve Vendor onboarding (demo). This **does not** approve a rental or activate tenancy.
6. Review/checkbox TIN evidence and Stock clearance; approve the rental separately. Approve a Contract terms version; it is **not yet accepted**.
7. Switch to the applicant Pending Vendor and click **Accept issued terms as Vendor**. Review the timeline and preview-only entitlement. Real backend authorization is still required.

## Guided procurement story

1. Select SuperAdmin or MarketMaster and open **Supplier → Gate Journey**.
2. Confirm qualification/Market participation, award an eligible bid, issue a PO.
3. Switch to **Approved Supplier** in the guided role panel; acknowledge the PO and dispatch it.
4. Switch to **Gate Staff**; record Gate admission. This is *not* Stock receipt.
5. Switch to **Stock Counter**; verify `95` of `100` units. A 5-unit variance remains visible.
6. Switch to **MarketMaster**; accept the goods-receipt evidence, while AP, VAT, URA/EFRIS and settlement stay **HOLD / not posted**.

## PM audit and testing

- `QA_RESULTS_FUNCTIONAL.json`: 34 focused scenario assertions after corrected KYC and date/policy safeguards.
- `QA_RESULTS_EXTRA.json`: 16 additional source-row, sum, CSV, Market-filter, history, deep-link and negative-permission assertions.
- `qa/BROWSER_QA_MATRIX.json`: 177 browser checks across 19 workspaces and 8 viewport widths (320–1920px), all passing.
- `qa/SMOKE_REPORT.json`: all 19 workspaces loaded without JavaScript/console errors.
- `previews/v6_1_functional/`: 30 updated screenshots, including the full applicant and supplier journeys.
- `V6_1_FUNCTIONAL_ACCEPTANCE_CONTACT_SHEET.png`: visual index of the main corrected states.

Testing runs only against the self-contained synthetic demo. Do not conflate these tests with an authenticated MMIS backend, real Market authorization, native PostgreSQL, approved financial reporting or legal RentContract acceptance.

## Source of truth and outstanding release gates

The prototype code (`source/app.js` and `source/synthetic_data.json`) documents proposed behavior, not production contracts. Existing MMIS operational lists and domain services remain the authoritative destinations after integration. The prior [ERP V6 foundation PR #372](https://github.com/oits-dhaka/MarketMasterERP/pull/372) is separate and not changed here.

**Finance acceptance remains HOLD** under MMIS-881 because historical carry-forward arrears, authoritative receivables totals, posting recovery and invoice financial authority require approved policy and authenticated PostgreSQL acceptance. URA/EFRIS/PRN and government settlement have not been validated. Case due dates, KYC evidence, Stock clearances, permissions and Contract approvals in this package are fictional.

**PM decision scope:** V6.1 is suitable for **prototype-level F0 functional demonstration review** after inspection of the included reproducible evidence. It is *not* production acceptance, not full P1/P2 domain completion, and not proof of 179 implemented KPI endpoints.
