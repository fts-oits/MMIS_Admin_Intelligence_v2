# MMIS V6 — PM Functional Completeness, Insights and User-Journey Verification

**Date:** 10 November 2026 | **Review mode:** independent, read-only evaluation of the delivered V6 PM demo ZIP | **PM visual design decision:** APPROVED (assumed, per request)

## Decision

**Status: CONDITIONAL DESIGN GO / FUNCTIONAL COMPLETENESS HOLD / PRODUCTION RELEASE NOT ASSESSED.**

The V6 interface is suitable as an approved visual/structural baseline. It demonstrates connected intelligence workspaces, evidence drill-downs, a sample unified Request Center and simulated role-specific navigation. **It does not yet satisfy all required insight-to-record accuracy or end-to-end user journey requirements.** In particular, five observed drill-down/filter contradictions, broken browser history, incomplete rental application/return journeys, a nonfunctional selected-invoice preflight and static governance workflows prevent declaring the PM's functional-coverage question satisfied.

The prior 153/153 Chromium checks measured 128 responsive combinations and 25 selected interactions; they were not a requirements coverage audit. In a separate 19-observation independent browser-and-source assessment, **6 passed and 13 unmet or not implemented**. These are intentionally broader requirements tests, so the difference is not a regression of the original QA tests. No browser JavaScript errors were observed.

**Data disclaimer:** All counts, financial amounts, roles, identities, PO, Supplier, Facility, Requests and statuses are synthetic; this assessment does not identify defects in the live MMIS database or source APIs. Actual authorization, financial correctness and accepted contractual/legal authority were not tested.

## 1. Evidence and artifacts reviewed

- `MMIS_V6_PM_Design_Approval_2026-11-10.zip`: 62 entries, ZIP CRC integrity passed.
- `index.html` (self-contained, ~267 KB) and `source/app.js` (UI navigation, data rendering and events), `source/synthetic_data.json`, `KPI_CATALOG_179.json`.
- `README_START_HERE.md`, `ARCHITECTURE_AND_SOURCE_ALIGNMENT.md`, `IMPLEMENTATION_HANDOFF.md`, `PM_APPROVAL_CHECKLIST.md`, `QA_SUMMARY.md`.
- `qa/BROWSER_QA_MATRIX.json` and `qa/SMOKE_REPORT.json`; reproduced selected interactions in independent Chromium/Playwright tests.
- Approved MMIS V5/V6 decisions (prior architecture reviews and source-to-page mapping), including MMIS-872 onboarding, MMIS-862/893 Facility Intelligence, MMIS-881 selected-rent invoicing Finance HOLD, Supplier PO/Gate/Stock custody, Market/RBAC scope.

### Coverage inventory

| Evidence | Verified extent | Interpretation |
|---|---:|---|
| Intended V6 UI destinations | 17 | 16 general named routes plus role-specific My Workspace |
| Distinct open fictional requests | 55 | Eight categories reconcile in current fixed dataset |
| KPI families | 179 | 45 Vendor, 41 Facility, 57 Supplier, 24 cross-domain, 12 Staff |
| KPI priority distribution | 42 P0, 84 P1, 53 P2 | A roadmap, not 179 active source-backed KPI endpoints |
| Original browser responsive/interactions | 153/153 passed | Legitimate narrow UI QA evidence, not full functional coverage |
| Independent requirement-oriented probes | 19 observations; 6 satisfied, 13 unmet | Four confirmed dataset/drilldown discrepancies plus missing workflows and route behavior; not a single product quality score |
| Browser runtime exceptions | 0 | No JS exception during independent checks |

## 2. Workspace requirement traceability

**Legend:** PASS = requirements demonstrated at the intended prototype level; PARTIAL = representation exists but important information, exact drill-down, or actual journey missing; MISSING = no substantive workflow; HOLD = intentionally disabled and awaiting external authority. `Implementation` applies to this **offline demo**, not to the live ERP.

| V6 workspace | Information / insight coverage | End-to-end journey coverage | Verdict and required change |
|---|---|---|---|
| Global Operations | Four headline cards, eight case categories, Market comparison, exceptions | Cross-domain KPI → linked list mostly present; **exception links inconsistent** | **PARTIAL/P0** — correct gap/import/overdue drill-downs; preserve market/filter/as-of |
| Request Center | 55 unique open cases by 8 types, owner, priority, age, CSV | Filter/list/detail pass; no case decision, assignment, service timeline, trackable disposition; dueAt absent | **PARTIAL/P0–P1** — distinct cases vs tasks/exceptions, dated SLA and domain-review actions |
| Market Intelligence | Registry list, physical population, recorded occupancy, manager and allocated sample rent | Detail drawer but no editable Registry/Level/Section navigation and deeper readiness | **PARTIAL/P1** — Level/Section cross-filters, staffing, readiness, portfolio drill-down |
| Vendor Overview | Registration/KYC, assigned Facilities, active-Contract status, invoices and overdue | Vendor drawer exists; 61–90-day Vendor cohort incorrect; full onboarding/claim process absent | **PARTIAL/P0** — invoice-source aging, Vendor/Contract relationship and accurate drill-through |
| Facility Intelligence | Shop-backed Unit Type matrix, occupancy, contract-gap status, invoice allocations | Unit Type→Facility and unit drawer work; Shop×61–90 Vendor journey not implemented | **PARTIAL/P0** — correct cross-domain invoice/Facility/Vendor filters and contract states |
| Supplier Intelligence | Supplier qualification, Market participation, PO commitments, late delivery | Supplier/PO/Gate evidence drawer; no RFQ→bid→award→PO→ACK→goods receipt→settlement state changes | **PARTIAL/P1** — storyboard full handoffs, permissions, line quantity/quality/invoice matching |
| Finance & Evidence | Issued liability, confirmed allocation, unpaid and overdue, exclusive sample aging | Read-only invoice details; no reconciliation, approval/policy version, PRN, EFRIS, refunds or ledger recovery | **HOLD/P0** — respect Finance carry-forward policy HOLD; source-safe detailed read model first |
| Staff & MarketMasters | Staff by role/status, assigned Market, flagged read-only, case counts | Directory drawer; no invite→claim→assign→revoke, workload ownership or audit timeline | **PARTIAL/P1** — effective permission and staffing actions via source pages |
| RBAC Governance | Five-column representative matrix, nine persona previews, restricted navigation | Role switch simulation works; no per-account grants/denies/targets/expiry/audit; no backend tests | **PARTIAL/P0 security contract** — add effective-access explanation and negative scenarios |
| Import Integrity | Staged/review/ready/blocked/consolidated sample, provenance | Exact stage filtering; no workbook upload/column mapping/dedup/adoption/review/promotion replay | **PARTIAL/P1** — enrich reviewer worklist and safe promotion storyboard |
| Gate & Stock | Tokens, PO links, admission/Stock stage, variance, assigned-role narratives | Read-only stages; no scan→capture→handover→partial receipt→variance resolution or actual role actions | **PARTIAL/P1** — full PO→Gate→Stock custody and fiscal evidence separation |
| Rental Readiness | Facility contract readiness count, review reasons, multi-select, NEVER POST drawer | Select→read-only preview passes; no Vendor selection, period/date/policy, termsVersion, invoice conflict, reviewer approval or recovery | **HOLD/P0** — complete authoritative read-only preflight, wait for Finance approval for writes |
| Public Shop Finder | Vacant listings, price/Market, authenticated account controls | Pending Vendor header pass; `See details & apply` has **no form**, Guest→login loses selected listing | **PARTIAL/P0** — application, tracking, return URL and saved identity context |
| My Workspace | Pending/active Vendor/Supplier, Gate/Stock persona overviews | Account gating works; no actual Vendor/Supplier own workflow transactions or application/Contract acceptance | **PARTIAL/P0–P1** — linked lifecycle panels with distinct states and ownership |
| 179 KPI Library | 179 searchable/exportable families and priority/maturity | Definition detail and exports present, but no metric-grain/time/source/filter/exact-query executable contract | **PARTIAL/P1** — formalize **42 P0** metric definitions before implementation |
| Design System | MMIS Base Vega/cream/green tokens, density/theme, sample controls | Theme/density works; no actual third-party implementation/import migration | **PASS for PM design; implementation outstanding** |
| PM Approval | Checklist and locally exported approval decisions JSON | Local approval workflow works; no authoritative approval recording or issue integration | **PASS for design review; not formal release signoff** |

## 3. Independent reproduced analytical defects (must fix before functional PM signoff)

| ID | Severity | Reproduction | Observed | Required acceptance |
|---|---|---|---|---|
| **P0-D01** | P0 | Global Operations → `Recorded occupied without active Contract` | Card **13**, linked `facList|contract|MISSING` list **7** | Use the same derived `contractGap=GAP` predicate for both card and detail; all 13 match under same Market/as-of |
| **P0-D02** | P0 | Global Operations → `Import records blocked / needing review` | Card **12** (`BLOCKED`+`NEEDS_REVIEW`), link only `NEEDS_REVIEW` **6** | Add multi-status/`requiresAction` filter preserving both groups; card=filtered rows=export |
| **P0-D03** | P0 | Global Operations → `Overdue invoice balance` | Amount card opens **all 48 Vendors**, no overdue preset | Navigate to invoice-backed overdue list/financial cohort; amount must reconcile and linked affected distinct Vendors must be filtered |
| **P0-D04** | P0 | Vendor list `DAYS_61_90` | **11** Vendors have any qualifying unpaid 61–90-day invoice; current `maxAging` cohort shows **8**, excluding 3 with older invoices | Define exclusive invoice cohort, distinguish oldest debt from band-specific exposure, use invoice-level matching and distinct Vendor ID |
| **P0-D05** | P0 | Shop Unit Type × 61–90 days overdue → Vendor | Exact illustrative Shop cohort **3 Vendors**; current unscoped aging cohort **8 Vendors** | Add combined `facilityType=SHOP`, `aging=DAYS_61_90`, Market/as-of and invoice-source drill-down, preserve source cohort; 3 exact records in sample |
| **P1-N01** | P1 | From Vendor Overview, click Global then Browser Back | URL changed to `#global` but displayed page remained `Vendor Overview` | Listen to `hashchange`/history and restore authorized view, filters and focus; reject foreign/unauthorized deep links |

**Source:** `source/app.js`: `globalPage` exception presets; `vendorRows().maxAging`; navigation uses `window.location.hash` but has no `hashchange` listener. **Data:** `source/synthetic_data.json` has 92 Facilities, 48 Vendors, 80 invoices, 31 import records; cohort numbers above are derived from those records, not guesses.

Important semantic distinction: an `oldest-overdue-age` Vendor classification can be useful but is **not equivalent** to “Vendors with an invoice aged 61–90 days.” Both may be displayed if explicitly and separately labeled.

## 4. Journey walk-through verification

| ID | Required end-to-end user journey | Demonstrated | Missing and PM decision |
|---|---|---|---|
| **J01** | Guest finds Shop → selects listing → signs in/registers → returns to same listing | Discovery, account simulation | Selected `FAC-0003` lost after simulated login; no preserved `listingId`, no application submission |
| **J02** | Authenticated pending Vendor browses public Shop catalogue with account header | **PASS at demo level** | Production session/refresh/logout and real listing URL acceptance separate |
| **J03** | Vendor registers → email verifies → identity/KYC/TIN/NIN → Admin approves Vendor access | Steps described as static notes | No forms, document review, status history, rejection/resubmission/notifications or reviewer decision demo |
| **J04** | Approved Vendor claims existing Facility **or** applies to rent → verification/approval → Contract offer → terms acceptance → activation | Flow narrative/Facility drawer | Missing distinct request track, proof upload, administrative allocation, approved terms/version, acceptance and effective-liability handling |
| **J05** | Approved active Vendor opens own Inventory, Invoice and Payment modules through qualifying tenancy | Static role-specific summary; pending gating **PASS** | No actual entitled Facility-specific business navigation, invoice/payment/inventory workflows |
| **J06** | Admin clicks Shop, 61–90 overdue → exact affected Vendors → invoice evidence → authorized reminder/reconciliation | Summary matrix, list and evidence drawer | Exact cross-filter is wrong/missing; reminders, source ledger and authorized actions not implemented |
| **J07** | Admin selects one/multiple Vendors/Contracts for billing period → eligibility and policy preview → Finance-approved generation/recovery | **Safe NEVER POST selection** | Current selection is Facility-based; missing period, first liable day, policy date/version, conflicts, idempotent recovery; financial writes intentionally HOLD |
| **J08** | Request Center intake → categorization → assignment → evidence → due/SLA → approve/reject/request-more-info → notification and audit | Count/filter/list/drawer, CSV | No assignment/action workflow, dueAt, case audit and downstream status transitions; 55 sample records have ageDays only |
| **J09** | Supplier global discovery → SuperAdmin Market participation grant → requisition/bid → Vendor award issues PO → Supplier acknowledgment/dispatch | Global+Market participation narrative, PO records | No grants, bids, award/acknowledgment, Market-specific execution checks; merely static stages |
| **J10** | PO → Gate/QR admission → item capture → Stock verification/partial receipt → inventory ledger → VAT/EFRIS/PRN evidence and settlement | PO/Token connected static drawers | No ordered event transaction, partial/quality resolution, actual Gate/Stock role actions or financial evidence lifecycle |
| **J11** | Workbook import → validate/map → duplicate/identity/facility review → safe adoption and promotion → evidence | Stage graph and source workbook records | No upload, preview errors, field decisions, idempotent adoption, authorizer, audit, preservation checks |
| **J12** | SuperAdmin invites MarketMaster / staff → assigns Market → sets role/denies → login → effective permission explanation → revoke | Role switching and illustrative matrix | No invitation/revocation, person-level granted/denied capability list, effective authorization reason, event trail |
| **J13** | Support ticket created → assigned → message/reply/escalation → resolution | Support category present | No ticket detail, transcript/messages, due date, workflow, notifications or live route |
| **J14** | Market registry -> Level/Section -> Unit -> Vendor/Contract -> rent and financial insight | Market/Facility/Vendor separate screens, drawer | No complete level/section/Market-scoped chained deep link/return context |
| **J15** | Read-only Admin, MarketMaster, Gate Staff, Stock Counter invalid actions | Role navigation simulation **PASS** | Server-side request-denial test, restricted exports, target-ID attack tests outstanding |
| **J16** | PM reviews and exports local decisions | **PASS** | Manual upload/action needed to make decision official; production release not implied |

## 5. Cross-cutting information/content gaps

### 5.1 KPI definition maturity

The **179-group catalog is present**, but its entries only have `id`, `domain`, `title`, `priority`, `definition`, `maturity`, `drilldown`, `source`. For all 179 entries the production-contract metadata `grain`, `timeBasis`, `eligibleStatuses`, `filtersApplied`, `currencyCode`, `evidenceSource` and `dataQuality` is absent. The visible descriptions are proposals; only selected KPIs are actual cards.

**Do not require 179 live cards for MVP.** Require the **42 P0 groups** to have complete approved source definitions and explicit page/route/filters; classify the remaining 84 P1 and 53 P2 as staged design backlog. A KPI should have a stable server-filtered population, `asOf`, category/grain, evidence maturity, partial/unavailable behavior, and a source detail route.

### 5.2 Request evidence and governance

The 55 synthetic cases are all `OPEN`; they have `ageDays`, `type`, `priority`, `assignee` and `sourceId`, but no `dueAt`. “Aged >15 days” is appropriately labeled as an illustrative age, **not an SLA**. Do not misrepresent it as a compliance deadline. Need unique source-key, owner/queue and activity history for real acceptance.

### 5.3 Rental and financial authority

The demo correctly warns that Vendor approval ≠ Facility assignment ≠ effective accepted RentContract, and invoice issuance ≠ confirmed payment ≠ verified allocation. However, the read-only preflight only checks a simplified `ACTIVE` contract and `APPROVED` Vendor flag; it does not validate immutable acceptance, Market reviewer, terms version, liability period, invoice collision or Finance-approved arrears treatment. The `Finance HOLD` is correct and must remain.

### 5.4 RBAC, row ownership, export protection

The offline role selector is a visual simulation, not authentication. The RBAC panel's capability matrix covers SuperAdmin, MarketMaster, read-only, Vendor, Supplier but not Gate Staff/Stock Counter per-capability columns. Effective denials, target record and service grants are not shown at user level. Real API authorization and Market/tenant ownership/export tests are required for engineering acceptance.

### 5.5 Navigation and notifications

The simulated public finder retains authenticated account controls (PASS), but Shop selection is not retained after sign-in. App routing updates hash without a corresponding hash-change navigation handler, so Browser Back can desynchronize URL and content. Notification bell presents a synthetic toast, not a task inbox or case deep-link.

## 6. Prioritized remediation before PM functional signoff

### Gate F0 — Required even for prototype-level functional signoff (P0)

1. **Fix all five exact-data drill-down issues:** facility Contract gap, import combined exception, overdue balance, Vendor aging cohort and Shop×61–90 Vendor list. Use a shared filter constructor, stable grain/Market/as-of, cardinality checks and exact filtered CSV.
2. **Complete two navigable applicant storyboards** without live writes: Guest Shop → login return → rental application draft/submission simulation → own tracking; Vendor access/KYC → Admin review → approval separately from rental/Contract → acceptance/activation eligibility. Clearly label simulated outcomes.
3. **Enrich Rental Readiness without posting:** selection by Vendor and Contract (possibly multiple Facilities), billing period and first liable day, effective policy and terms version, existing-invoice collision, reason-coded failures, authority status and retry/recovery preview.
4. **Fix browser history/deep-link behavior**, including back/forward, refresh, Market/role scope changes and restoration of filters.
5. **Add scope/authorization outcome screens**: permission denied, Market mismatch, read-only action disabled, pending account no entitlement, missing source, partial evidence.

### Gate F1 — Full journey demonstration (P1)

6. **Request Center**: interactive sample case state machine with assignment, due-at/SLA mock, evidence, More Info / Approve / Reject handoff, notification, audit timeline, without bypassing underlying domain checks.
7. **Supplier and PO/Gate/Stock**: interactive *simulated* Market grant → bid award creates PO → Supplier ACK → dispatch → Gate → Stock/partial variance → receipt → AP/fiscal evidence. Keep role permissions and source-stage transitions separate.
8. **Import**: fake workbook validation/field mapping and safe duplicate-review/promotion storyboard; no actual Vendor/Contract/finance writes.
9. **RBAC/Staff**: person-level effective permission inspector, Market assignments, explicit deny/revocation consequences, audit and Gate/Stock capability rows.
10. **Market and Vendor360**: Level/Section/Unit/Contract detail chain, history; own Vendor Business scope, dates/policy, billing and payment timeline.
11. **Support tickets and Notifications**: case status, messages, assignment and source-linked inbox; overdue severity and escalation states.

### Gate F2 — Production integration and acceptance (not a PM-demo prerequisite)

12. Implement on separate ERP/API feature branches from live exact `dev_basic`. Preserve React 18/Vite/TanStack Table 8/Base Vega/Base UI; no wholesale template migration.
13. Add backend source-owned read models and correct scoped filtered endpoints; exact-head tests/build, native PostgreSQL reconciliation and credit concurrency, role/Market/ownership negative tests, authenticated frontend→API→DB browser UAT.
14. Obtain Finance approval for carry-forward receivables policy and independent authorization for any selected-invoice or government fiscal posting. Maintain HOLD until established.
15. Preserve no protected-branch direct writes, no workflow YAML and no production/shared database mutations; isolate UAT host/runner identities.

## 7. PM acceptance scenarios (Given / When / Then)

**AC-01 Card parity:** Given SuperAdmin selects Kabale and as-of 2026-11-10, When the Contract-gap card says `N`, Then the exact filtered source list and export contain the same `N` canonical Facility IDs; do not count companion Stalls twice.

**AC-02 Import exception parity:** Given blocked and needs-review import records, When clicking the combined exception card, Then both stage populations are included, without unrelated staged/promoted records; no promotion occurs.

**AC-03 Shop aging:** Given Shop-type invoices with 61–90-day eligible unpaid balances and other older invoices, When selecting Shop and exclusive 61–90 days, Then only Vendors with at least one qualifying Shop invoice appear, together with those invoices and exact overdue amounts. Vendor's maximum age from another unit does not suppress them.

**AC-04 Application return:** Given Guest selects public listing `L`, When signing in and completing Vendor access, Then the intended `L` remains in the authorized return target; clicking Apply opens the specific listing's application, and submitting yields a trackable request without creating a Contract.

**AC-05 Pending Vendor:** Given email-verified but not approved Vendor, When opening My Workspace or public finder, Then account/notifications/logout persist, but Inventory, Payments and Invoices are absent until qualifying tenancy is verified.

**AC-06 Distinct approvals:** Given Vendor onboarding approved, When their rental application is still pending, Then the system does not assert active tenancy; approved RentContract terms and acceptance remain separate actions.

**AC-07 Rental readiness:** Given selected Vendor(s), Contract(s) and billing period, When previewing, Then eligibility, policy, first-liability date, contract terms/acceptance, invoice conflicts and Finance HOLD are shown; no generation/posting action is possible.

**AC-08 Request lifecycle:** Given a case with source, owner, priority, submittedAt and dueAt, When reviewer examines it, Then age/SLA, evidence, permitted source-domain action and audit are visible and cross-Market/unauthorized actions denied.

**AC-09 Supplier/PO:** Given Vendor awards eligible Supplier bid, When award is accepted, Then a canonical PO is issued; Supplier acknowledgment and fulfillment remain Market/role-gated, and Gate admission is not Stock acceptance or settlement.

**AC-10 History and scope:** Given MarketMaster navigates KPI → detail → Back/Forward, Then content, hash, Market and validated filters remain synchronized; foreign Market deep links are refused.

**AC-11 Finance boundary:** Given financially pending evidence or disputed carry-forward totals, When opening financial dashboards, Then unavailable/held amounts are not presented as verified cash, and no invoice/PRN/EFRIS/settlement posting is available until approved.

**AC-12 RBAC and imports:** Given read-only Admin, Gate Staff, Stock Counter or a pending Vendor/Supplier, When attempting an unauthorized domain action, Then the UI refuses the action and the real backend denies a constructed direct request; import review cannot forge tenancy or verified cash.

## 8. Decision for the PM

**Recommend keeping V6's visual design approved**, recording this audit as a **functional enhancement punch list**, and requiring **F0 acceptance** before announcing “all P0 insights and user journeys satisfied.” F1 completes the wider product journey narrative. **Do not demand 179 production KPI endpoints for a PM demo**, but do require the 42 P0 families to be adequately defined for their intended integration wave.

**Not approved by this audit:** Finance policy, rental posting, backend RBAC, Government/URA/EFRIS compliance, native PostgreSQL production numbers, actual email/token security, PR merge or staging deployment.

## 9. Reproducible audit evidence

- `INDEPENDENT_TESTS.json` — 19 independent observations with expected/actual and severity; no JavaScript exceptions.
- `independent_audit.py` — Playwright test code; reads the original V6 extracted HTML and runs offline.
- `01_13_Facility_gap_count_opens_7_filtered_units.png` — Facility mismatch after clicking the Global exception.
- `02_12_Import_exception_count_opens_6_filtered_rows.png` — Import mismatch after clicking the Global exception.
- `03_Apply_button_opens_readonly_information_drawer.png` — Public Shop apply CTA lacking a form.

The delivered V6 ZIP itself was **not altered** during this read-only review.
