# V6.1 functional corrections — START HERE

**This is the corrected PM demo revision.** Open `README_V6_1_START_HERE.md` first. Use `index.html` to run the updated 19-workspace demo, `V6_1_FIX_VERIFICATION_REPORT.md` for before/after findings, and `previews/v6_1_functional/` for new screenshots. The original V6 design notes below are retained as historical baseline context. This is a synthetic, read-only/no-posting prototype; Finance and production acceptance remain on HOLD.

---

# MarketMaster MMIS · Enterprise Intelligence V6.1 (Functional Corrections)

## Corrected PM Functional Review Demo — 10 November 2026

This is a **complete, interactive, fully offline UI prototype** for product-management review. Its appearance reflects the prior V5 design, the 179-family intelligence catalog, and the consolidated 29-reference shadcn/TanStack design-system research.

**Open the demo:** Unzip `MMIS_V6_1_Functional_Corrections_PM_Review_2026-11-10.zip` and double-click `index.html` in Chrome or Edge. No Node, NPM, build command, web server, authentication, internet connection, third-party font, or external CSS/JS is required. The entire application, sample data, styles and interactions are embedded in `index.html`. The top-level ZIP includes the complete launcher and documentation.

### Your first 10-minute product-management walkthrough

1. Start on **Global Operations**. Review 4 executive cards, the distinct Requests Awaiting Action count, the 8 request categories, and the operational exceptions panel.
2. Click **Rental applications** in the Request chart. Confirm the Request Center opens filtered to the exact matching cases. Review a case drawer and export its filtered CSV; filters use the same population as the displayed matching-row count.
3. Open **Facility Intelligence**. Review the five-Unit-Type rent performance matrix. Click `SHOP`, and use the physical-unit table filters. Open a Unit and see its Vendor, recorded occupation, RentContract and invoice allocations.
4. Open **Vendor Overview**. Click `61–90 days` to filter the Vendor investigation table, then inspect Vendor, facilities, contract and money evidence. Separate verified invoice allocations from liability and overdue balances.
5. Open **Supplier Intelligence**. Switch between qualified Supplier records and Purchase Orders, then inspect PO-linked Gate/Stock status. A bid/PO/Gate admission is never automatically an accepted receipt or settlement.
6. Open **Rental Readiness**. Select one or more Facilities and choose `Preview selected`. It must display **READ-ONLY / NEVER POST**, including the unresolved MMIS-881 Finance HOLD. There are no financial mutation buttons.
7. Open **RBAC Governance**. Switch personas using the header: MarketMaster, read-only Admin, pending/active Vendor, pending/active Supplier, Gate Staff and Stock Counter. The sidebar narrows to each persona's allowed demonstration pages. **This is a visual simulation, not actual security enforcement.**
8. Choose **Pending Vendor**, open **Public Shop Finder**, and verify that the public page's header retains account identity, Notifications and Logout—without Sign In. The first-login dashboard does not provide Inventory, Invoices or Payments navigation.
9. Open **Design System**, check MMIS Base Vega theme tokens, compact density and dark-mode variants. Review the 29-reference adoption decisions in the architecture notes.
10. Open **PM Approval**, check the desired design decisions and export the **local feedback JSON**. This does not update GitHub, Linear or production MMIS.

### Included interactive workspaces (17 primary workspaces + 2 scenario destinations)

Global Operations; Request Center; Market Intelligence; Vendor Overview; Facility Intelligence; Supplier Intelligence; Finance & Evidence; Staff & MarketMasters; RBAC Governance; Import Integrity; Gate & Stock; Rental Readiness; Public Shop Finder; My Workspace (role-specific); 179 KPI Library; Design System; and PM Approval.

### Other interactive features

- SuperAdmin can switch All Markets / Kabale / Mbarara / Gulu / Lira. MarketMaster and other roles have fixed illustrative Market scope.
- Header role selector with 10 demo personas (including unauthenticated guest).
- Market-scoped filterable, sortable, offset-paginated data tables (10 rows/page) and all-filtered CSV export.
- Clickable KPI/Unit Type/request category drilling to the exact example population; evidence/detail drawers; keyboard Escape to dismiss; `/` to focus worklist search; dark-mode and density toggles.
- Source-appropriate warning states for missing/historical/held data and Finance decisions.
- Exportable PM design decisions (JSON) — browser-only and local, without automatic upload.
- A consistent fixed as-of date, `2026-11-10`. Financial and request numbers are deterministic and internally computed from one sample dataset.

## What V6.1 fixes beyond the approved original V6

The six P0 PM audit findings have been corrected **in this fictional offline prototype**: exact Facility 13/13 and Import 12/12 KPI drilldowns; invoice-based Vendor 61–90 bands and Shop+aging filtered export; guest-to-login Shop retention and a trackable rental application/approval/Contract-acceptance simulation; non-posting rental policy/version/collision/first-liability preflight; Request Center assignments/status/timeline/notification inbox; Supplier→PO→Gate→Stock→receipt role-driven simulation; browser history and effective-permission explanation.

Open the **Vendor application flow** and **Supplier custody flow** scenario destinations from the relevant buttons. These are the two additional renderable pages beyond the primary 17 navigation destinations.

The entire corrected suite was rerun: **177/177 baseline browser checks, 34/34 functional scenario checks and 16/16 financial/filter/RBAC checks** passed (some assertions overlap). See `FIXES_ACCEPTANCE_REPORT.md` for exact reconciled cohorts, screenshots and explicit production HOLD boundaries.

### New PM review artifacts

- `FIXES_ACCEPTANCE_REPORT.md` — verified six-fix traceability and 10-step PM walkthrough.
- `QA_RESULTS_FUNCTIONAL.json` and `QA_RESULTS_EXTRA.json` — independent-focused rerun results.
- `previews/fix_01_...png` through `fix_14_...png` — before/after-targeted screenshots of actual corrected flows.
- `qa/browser_functional_playwright.py` and `qa/browser_financial_parity_playwright.py` — optional rerunnable browser tests.

## Important distinction: design approval vs implementation

**All persons, Markets, vendors, physical units, rent amounts, purchase orders, request cases, Supplier identities, staff assignments, and statuses shown in the prototype are fictional, deterministic demonstration values.** They must not be used as MMIS accounting reports, evidence of legal tenancy, a real KYC decision, government compliance or live application data.

The prototype contains **no API calls, no external resources, no authentication, no PostgreSQL access, no writes, no fiscal API or payments, and no invoice generation**. Buttons only navigate within the sample UI, export the local sample, or open illustrative evidence dialogs. Role restrictions in this file are NOT an authorization mechanism; production authorization must be enforced by MarketMasterApi.

Current V6 production-code progress is separate. **MarketMasterERP PR #372** (`feat/mmis-v6-intelligence-ui-foundation-20261110`) is a Draft, scoped to evidence-safe UI/reporting primitives. It does not contain every dashboard in this package, nor does it authorize Finance posting. MMIS-881 API #545 / ERP #366 and historical carry-forward policy remain HOLD pending separate technical, Finance and release approval.

## Package structure

- `index.html` — **standalone, self-contained application**. Only file required for preview.
- `KPI_CATALOG_179.json` — 179 grouped KPI definitions (45 Vendor + 41 Facility + 57 Supplier + 24 cross-domain + 12 Staff). These are candidate definitions, not 179 implemented API endpoints.
- `PM_APPROVAL_CHECKLIST.md` — recommended review gates and decision points.
- `ARCHITECTURE_AND_SOURCE_ALIGNMENT.md` — consolidated source decisions and MMIS integration boundaries.
- `IMPLEMENTATION_HANDOFF.md` — specific implementation phases, endpoint expectations and acceptance tests.
- `previews/` — original 45 Chromium screenshots plus 14 corrected-journey screenshots.
- `qa/BROWSER_QA_MATRIX.json` — machine-readable 177-test expanded browser QA report.
- `qa/SMOKE_REPORT.json` — smoke-run screenshots, interactive testing results.
- `source/` — readable source and deterministic fictional JSON data. These are optional; runtime uses only `index.html`.
- `PACKAGE_MANIFEST.json` — verified file checksums and sizes.
- `FIXES_CONTACT_SHEET.png` — overview of correction-specific screenshots.

## Security, license and delivery boundaries

No third-party template code, paid shadcn Pro content, authentication key, MarketMaster credential, production database string, or external library was copied into the standalone prototype. Its aesthetic takes inspiration from approved open-code dashboard conventions; all HTML/CSS/JS was freshly authored for MMIS's review needs.

The user-defined project rule remains: do not modify `main`, `dev`, `dev_basic`, or `staging` directly in MarketMasterERP or MarketMasterApi. Use purpose-built feature branches for any production implementation, with exact-head builds/tests, native PostgreSQL testing, authenticated browser UAT, business/Finance approval, and deployment-host isolation. No workflow files are added.
