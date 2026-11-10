# MMIS V6.1 — Corrective Implementation and Independent Verification

**Version:** V6.1 functional-demo revision, 10 November 2026  
**Original:** Approved V6 design ZIP (`MMIS_V6_PM_Design_Approval_2026-11-10.zip`)  
**Independent finding:** `PM_FUNCTIONAL_COMPLETENESS_REPORT.md` reproduced 13 vs 7 Facility gap and 12 vs 6 Import attention, Vendor invoice-aging mismatch, missing application and source-review transitions, history and permission-explanation gaps.

## Overall verdict

**PROTOTYPE FIXES: PASS (targeted functional scenarios)**  
**UI DESIGN: retained**  
**BACKEND AND FINANCE ACCEPTANCE: HOLD / not tested**

### Before / after traceability

| ID | Initial problem | Correction | Verified synthetic result | Remaining live requirement |
|---|---|---|---|---|
| F0-01 | Occupied without active Contract card `13` opened only `7` `MISSING` rows | KPI now uses `contractGap=GAP` predicate | **13 / 13** canonical Facility rows | Live backend physical-unit/Contract truth; exact filtered export |
| F0-02 | Import attention `12` opened only `6` `NEEDS_REVIEW` | Add `reviewGroup=ACTION_REQUIRED` for `NEEDS_REVIEW` ∪ `BLOCKED` | **12 / 12** staged records | Import authority, identity/facility preservation, promotion audit |
| F0-03 | Overdue liability card led to general Vendor overview | Route to `invoiceList` where `debtStatus=OVERDUE`; same invoice grain and source amounts | **UGX 4,392,000** = 44 overdue invoice records = exported 44 rows | Approved Finance receivables semantics and native PG reconciliation |
| F0-04 | Vendor 61–90 group used oldest overdue invoice per Vendor | Cohort based on whether **any eligible unpaid invoice** falls into the exclusive age band | **11 / 11** distinct Vendors (may occur in other age bands) | Authoritative invoice status/time policy |
| F0-05 | Shop × 61–90 filter incorrectly reused first assigned Unit Type/oldest Vendor age | Join qualifying invoices → canonical Facility Unit Type; expose exact cohort amount in worklist and CSV | **3 / 3** Vendors, **UGX 447,000** matching overdue source invoices | Server-side exact grain, Market scope and filter/export parity |
| F0-06 | Public Shop “apply” only opened a read-only drawer; guest login lost listing | Preserve selected Facility across login; application note and submission reference, case count, role-separated KYC/onboarding/rental/Contract decisions | `FAC-0003` → `DEMO-APP-FAC-0003` → accepted terms in simulator | Actual auth, KYC records, rental API, approvals, accepted immutable Contract |
| F0-07 | Rental preflight lacked period, liable date, policy, terms, collision | Selected period and first-liability day, mock date-effective Market policy, selected override, source availability/terms flags, invoice collision reason codes | `FAC-0001` November sample yields `EXISTING_PERIOD_INVOICE` + terms evidence unavailable + `FINANCE_POLICY_HOLD` | Finance approval, policy registry, actual terms version/effective acceptance, no double posting |
| F0-08 | Request list only showed case age, no SLA source or actions | Synthetic `dueAt`, reviewer assignment, request more evidence, escalation, audit timeline, notification inbox | Case state and notification transitions tested | Actual SLA policies, source ownership and notifications service |
| F0-09 | PO/Gate/Stock only read-only evidence drawer | Multi-role state transitions with qualification, bid, PO, ACK, dispatch, Gate, Stock variance, receipt | Supplier, Gate and Stock role checks; **95/100** units received with variance | Real procurement/receiving services, ledger, government evidence |
| F0-10 | Browser Back changed hash without state | History and refreshed route search restore scoped Market/filter/page; Market switch clears dependent filters | Back, Forward, deep-link and Market-reset tests passing | TanStack Router production integration and access enforcement |
| F0-11 | RBAC governance did not explain access or Gate/Stock capabilities | Effective-permission decision simulator, explicit read-only and foreign-Market denial, Gate/Stock columns; hide request mutation controls for read-only | Denied mutation and foreign Market inspection tested | Server effective grants/denies and target resource authorization |

### Financial caution

The demo follows invoice-source `billed`, `allocated`, and `unpaid` fields. It does **not** establish the receivables policy. The `UGX` totals here are fictional checks of internal parity only. No invoice, credit, payment, VAT, PRN, EFRIS, fiscal document, supplier payable, or government settlement was posted.

### Synthetic request semantics

55 initial open cases across eight categories. Each has a fictional `dueAt` and sample timeline. Submitting an additional rental application adds one separately trackable case in the current session. Assigning/requesting-info/escalating changes only local state and creates a session notification. Source-domain approval remains a separate simulated story; no universal approval action bypasses the underlying reviewer prerequisites.

### QA evidence

| Suite | Passing / total | Scope |
|---|---:|---|
| Functional role and journey assertions | **34/34** | Six requested workstreams, KYC/Stock safeguards, Contract acceptance, Supplier roles, no posting, browser exception checks |
| Additional parity, export and history assertions | **16/16** | Exact invoice sums, 61–90 age groups, Shop filter & amount, CSV, Market/back/forward/deep link and negative role scenarios |
| Browser matrix | **177/177** | 19 workspace views, 8 widths 320/375/390/768/1024/1280/1440/1920, plus targeted UI tests |
| Browser smoke | **0 errors** | All 19 pages and role switches; successful offline local HTML rendering |

These are overlapping assertions, not 227 independent requirements. Reports are machine-readable, and the corrected source/tests are included.

### Outstanding gates beyond the approved design

- Finance signoff and MMIS-881 interrupted-run/historical arrears policy acceptance remain HOLD.
- Runtime authentication, credential continuity, live Market/role/tenant ACLs and backend negative tests were not exercised.
- Actual Vendor KYC, URA/EFRIS/PRN, Contract terms versions and approvals require domain-services integration.
- PO/Gate/Stock and receipt posting are real operational systems with further event, isolation, reconciliation and document acceptance requirements.
- All 179 KPI families remain a specification; not 179 validated server aggregations. Complete P0 metric source definitions during engineering.
- Saved views, advanced Market/Level/Section drill-down, import workbook reconciliation and notifications delivery belong to wider P1/P2 implementation.

**Recommendation:** PM may accept the corrected **F0 prototype interactions** while retaining production, financial, identity, fiscal, and authorized-write acceptance on HOLD. Do not change protected application branches or merge the unrelated ERP V6 foundation PR merely because the prototype passes.
