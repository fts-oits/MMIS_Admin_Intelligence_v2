# MMIS V6.1 — Functional Corrections & Independent PM Acceptance Report

**Date:** 2026-11-10  
**Scope:** Offline synthetic PM demo only, derived from the approved V6 design; no MMIS application repository, production service, database, or financial record changed.  
**Status:** **GO for renewed PM functional-design review**; **HOLD for authenticated production/financial acceptance**.

## A. What was interrupted and what is now finished

The V6 demo had been independently audited and six P0 functional gaps had been identified. Implementation files and focused browser QA existed before interruption, but the revised package and final delivery were not completed. The resumed work verified the source against the final self-contained HTML, reran three test suites, captured corrected workflow screenshots, and assembled a new delivery package with these acceptance notes.

**Existing style retained:** original approved cream/green MMIS appearance, 179 KPI definitions, Base Vega-style patterns and role-aware dashboard hierarchy. These corrections are not another visual redesign.

## B. Six requested fixes: acceptance status

| Fix | Previously reproduced | Corrected V6.1 offline behavior | Evidence and outcome |
|---|---|---|---|
| 1. Exact KPI-to-worklist counts and combined filters | Facility Contract gaps 13 → 7; Import attention 12 → 6; 61–90-day Vendor count 11 → 8 | Contract gap uses the actual `GAP` condition; Import attention combines `NEEDS_REVIEW + BLOCKED`; Vendor aging tests invoice-level eligible 61–90-day entries rather than a single maximum/oldest invoice. Market switching resets dependent filters. | **PASS:** Facility **13=13**, Import **12=12**, 61–90-day Vendor **11=11**, Shop+61–90 **3=3**; matching liability **UGX 447,000=447,000**; filtered CSV **3=3** |
| 2. Vendor discovery → login → application → review → Contract | Informational drawer only; selected Shop lost after login | Guest selection retains `FAC-0003` through simulated sign-in; pending Vendor submits a trackable case; administration reviews KYC, then separately approves onboarding, verifies TIN and Stock clearance, approves rental, issues approved terms, and the intended Vendor accepts. | **PASS:** Guest→login return; application `DEMO-APP-FAC-0003`; prerequisite denial; independent approvals; Vendor acceptance. **No real tenancy activation.** |
| 3. Rental Readiness | Missing first-liability date, policy version, existing-period collisions, Contract approval evidence | Selected-unit preflight shows billing period, first liable day, separate issue date, selected version, selection basis, Contract override rule, existing invoice-period conflict, reason-coded ineligibility and Finance policy HOLD. | **PASS:** evidence drawer contains `MARKET-2026-07-V2`, `EXISTING_PERIOD_INVOICE`, `FINANCE_POLICY_HOLD`, `READ-ONLY · NEVER POST`. **No posting API.** |
| 4. Request Center simulated workflow | No true `dueAt`/SLA; no assignment/evidence/status timeline/inbox demonstration | Request records expose dueAt and timeline; authorized admin can self-assign, request information, escalate; notification inbox shows case-related events; detail panel keeps source-only review/decision boundary. | **PASS:** assignment adds timeline and inbox item; `WAITING_INFO` transition; request inbox; read-only action controls absent. **No real messages sent.** |
| 5. Supplier qualification → PO → Gate → Stock → receipt | Purchase and Gate details inspectable but no end-to-end role transition | Separate admin qualification, bid award, approved PO; Supplier acknowledgment/dispatch; Gate Staff admission; Stock Counter verifies actual **95 / 100 units**; admin receipt acceptance retains variance and settlement HOLD. | **PASS:** all stage and role transitions; no automatic payment or fiscal certification. |
| 6. Browser history and RBAC explanation | Browser Back updated URL but page did not restore; unclear effective-denial reason | Browser Back/Forward and refreshed deep links restore validated filters and Market scope. Effective-permission inspector explains read-only and foreign-Market denials. | **PASS:** Back/Forward and deep link; read-only approval denied; foreign-Market denial; pending Vendor prohibited navigation. |

## C. Additional verified parity

- Global overdue invoice liability **UGX 4,392,000** equals the corresponding unpaid balance summed over **44** eligible invoice worklist records; CSV export includes **44** filtered records.
- Request category and worklist parity is verified for the submitted-case sample. Categories represent distinct actionable cases; operational exceptions are separately labeled. Cases additionally contain illustrative due dates and activity timelines.
- The public Shop Finder retains the authenticated account name, notification action and Logout, without showing Sign In to a signed-in Vendor.
- MarketMaster scope remains assigned-Market; pending Vendor does not gain Inventory, Payment or Invoice pages; read-only Admin cannot execute Request Center actions.
- No JavaScript exceptions were observed during the rerun, and no whole-page horizontal overflow was found in the independently checked widths. Table areas may scroll horizontally inside their containers.

## D. Browser evidence rerun

| Test suite | Assertions | Passed | Failure |
|---|---:|---:|---:|
| Baseline responsive/navigation/QA matrix | 177 | 177 | 0 |
| Focused functional journey checks | 34 | 34 | 0 |
| Financial/filter/export/RBAC checks | 16 | 16 | 0 |
| **Total executed assertions** | **227** | **227** | **0** |

These are **227 executed checks across overlapping suites**, not 227 independent business requirements. The matrix covers **19 renderable views × 8 responsive widths = 152 visual-width checks**, plus interaction assertions. The original demo's 153-result report is superseded for this package.

**Reproducibility:** `qa/browser_matrix_playwright.py`, `qa/browser_functional_playwright.py`, `qa/browser_financial_parity_playwright.py` and `qa/browser_smoke_playwright.py` use the self-contained `index.html`. They require Python Playwright and a local Chromium installation, but **no backend server**. Machine-readable JSON summaries are provided.

## E. PM demonstration: exact walkthrough

1. **Global Operations → Facility gap KPI**: note 13 → inspect 13 matching Facility records.
2. **Global Operations → Import attention**: note 12 → inspect 12 blocked/review-required rows.
3. **Vendor Overview → 61–90-day aging**: inspect 11 Vendors, or select Shop + 61–90 to inspect 3 distinct Vendors and UGX 447,000 invoice liability; export those three rows.
4. **Public Shop Finder as Guest → select FAC-0003 → simulate login**: the selected Shop must remain chosen. Submit rental application; verify trackable demo reference.
5. **Switch to MarketMaster on Vendor journey**: attempt onboarding before KYC (blocked), check KYC, approve onboarding, then attempt rental approval before TIN/Stock (blocked). Check both prerequisites, approve rental, and approve proposed Contract terms.
6. **Switch to pending Vendor**: accept approved terms. Inspect the timeline; no actual Contract/financial posting occurs.
7. **Rental Readiness**: select a Facility, preview; inspect first-liability day, applicable policy version, invoice-period collision, evidence, reason codes, and `NEVER POST`.
8. **Request Center**: inspect a case, self-assign, request information, inspect the timeline and notification inbox. Switch to read-only Admin to verify mutation controls absent.
9. **Supplier workflow**: admin qualifies/awards/issues PO; Supplier acknowledges/dispatches; Gate admits; Stock verifies 95 of 100; admin accepts receipt with variance and settlement HOLD.
10. **RBAC Governance**: select read-only and foreign Market/approval to view effective-access denial reasons. Test Browser Back, Forward and refresh on filtered deep links.

## F. Explicitly NOT accepted or implemented

- No real authentication, RBAC policy enforcement, backend API writes, Market-specific PostgreSQL isolation, email/notification delivery, PO booking, tenancy activation, actual payment/credit application, URA/EFRIS/PRN issuance, or invoice posting.
- Demo persona switching is a visual test harness, not an authorization system. Administrative decisions are synthetic state transitions held only in the browser session; no server audit ledger is written.
- The selected-rental-invoice and historical arrears policies remain on a **separate Finance/Engineering HOLD**. The preflight preview is **never** a posting authorization.
- The 179-family catalog is an approved candidate library, not 179 integrated endpoints or certified reports. Production backend report contracts, snapshot semantics and reconciled financial metrics still require individual acceptance.
- Do not treat these checks as proof that current ERP PR #372 or any live source branch implements the P0 user journeys. PR #372 is a separate Draft foundation.

## G. Product decision

**UI and offline functional demonstration:** recommend **GO for PM re-review**, provided the six corrected journeys and evidence are approved.  
**Production/financial/security readiness:** **HOLD** until independent authenticated frontend/API/PostgreSQL tests, real authorization denials, Finance approval and release-isolation evidence are complete.

## H. Artifacts

- `index.html`: no-external-dependency, self-contained corrected demo.
- `FIXES_ACCEPTANCE_REPORT.md`: this report.
- `QA_RESULTS_FUNCTIONAL.json`, `QA_RESULTS_EXTRA.json`, `qa/BROWSER_QA_MATRIX.json`: actual browser run results.
- `previews/fix_*.png`: 14 screenshots specifically documenting corrected journeys and evidence.
- `source/`: HTML's standalone CSS/JS/fictional data for engineering inspection.
- `V6_ALL_WORKSPACES_CONTACT_SHEET.png`: original visual baseline reference.

**Branch rule preserved:** no direct modification of `dev`, `main`, `dev_basic`, or `staging`; no GitHub workflow files added; no external repository actions taken in this correction pass.
