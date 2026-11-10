# MMIS v3 standalone design QA — 2026-11-10

## Verified locally

- HTML links and shared JS/CSS asset paths: all checked and resolved in the provided ZIP.
- JavaScript syntax: Node `--check` passed for `insights-v3.js` and `kpi-catalog.js`.
- Catalog IDs: 179 unique groups, comprising 45 Vendor, 41 Facility, 57 Supplier, 24 Cross-domain, 12 Staff/Manager.
- Browser DOM tests: seven original page views have v3 extensions (Global, Vendor, Facility, Supplier Admin, Staff/Managers, Vendor Business, Supplier Business).
- Filters: Supplier domain yields 57 groups; Cross-domain yields 24 groups; Vendor search for `credit` filters to matching curated group.
- Facility → Vendor example drill-through: selecting Stall / 61–90 days sets the original Unit Type `STALL`, aging `DAYS_61_90`, and Vendor page active.
- KPI detail modal opens and closes; information includes source evidence, priority, maturity and intended backend population.
- Pending Vendor hides the v3 business-intelligence section; approved Vendor reveals it. The original app gate remains unchanged.
- 390px and desktop browser DOM tests had zero page-wide horizontal overflow and no unhandled JavaScript errors in tested views.
- Screenshots included for Global, Vendor, Facility, Supplier Admin, Staff/Managers, Vendor Business, Supplier Business and the KPI library.

## Verification scope

Playwright's browser navigation to file and local HTTP addresses was blocked by the runtime's administrator policy. The QA harness therefore rendered the actual HTML and the same JS/CSS code together with `page.set_content()`; external asset path existence was independently verified. This supports visual/interaction QA but is not a full network-hosted smoke test.

**Not verified:** real GitHub-hosted preview, browser-opened ZIP HTML on a user's machine, backend APIs, Market scope, data accuracy, source reconciliation, authentic financial exports, notifications, role token enforcement, or native PostgreSQL UAT. Those require separate engineering/PM gates.
