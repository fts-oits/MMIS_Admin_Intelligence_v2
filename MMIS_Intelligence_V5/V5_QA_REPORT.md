# V5 Prototype Browser QA — 2026-11-10

### Actual rendered checks (Chromium / Playwright)

- All 10 admin/reference pages rendered on 1440px without JavaScript exceptions.
- Desktop and mobile screenshots were captured for the admin pages; role-specific approved/pending Vendor and Supplier, Gate Staff, Stock Counter and MarketMaster screenshots were captured.
- No page-wide horizontal overflow at **320, 375, 390, 768, 1024, 1440 or 1920px** in the tested ten admin/reference views. Data tables scroll internally as needed.
- Global `Requests awaiting action` count equaled the sum of its eight exclusive open-request category counts: **55 = 55** in the illustrative dataset.
- Clicking a Rental Applications category opened Request Center with the matching category filter.
- Clicking Request Center record opened a source-evidence drawer.
- Filtered Request Center CSV export matched table filtered count (**7 rows = 7**).
- Facility Unit Type (Shop) matrix drill-down populated the right Unit Type filter.
- MarketMaster had locked assigned Market A and did not see SuperAdmin governance details.
- Pending Vendor view contained onboarding/rental journey but withheld payment, invoice and inventory cards.
- Pending Supplier view showed qualification journey, not purchase commitments.
- Stock Counter sidebar contained only Gate & Stock.
- Read-only admin displayed an explicit read-only banner and no execution controls.
- Additional filtered CSV parity checks passed for Vendor overdue, Facility Contract gaps, Import review, Gate awaiting Stock, Request category, Supplier status and Staff role populations.

### Caveat

Only local illustrative data and client-side behavior were tested. No authenticated frontend/backend integration, settlement, live permissions, native PostgreSQL, or true finance-certification tests were performed. The sandbox browser disallows direct `file://` navigation, so tests rendered the **identical, self-contained** HTML through Playwright page content; users can open extracted `index.html` in Chrome/Edge locally.

See the machine-readable `QA_RESULTS.json` and `MATRIX_QA_RESULTS.json` for exact checks.
