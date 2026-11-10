# MMIS Intelligence v3 — Implementation and evidence contract

**Status:** PM-approved information architecture / visual prototype. All displayed application figures are illustrative. Do not interpret this design package as authenticated, financially certified or production-ready application behavior.

## Pages covered

| Page | Existing entrypoint | V3 addition |
| --- | --- | --- |
| SuperAdmin / MarketMaster Global Operations | `01_Global_Dashboard/MMIS_Global_Operations_Admin_Prototype.html` | Shared exceptions, Market-scope readiness, authenticated reporting contract |
| Admin Vendor Overview | `02_Vendor_Facility/MMIS_Vendor_Facility_Interactive_Prototype.html` (`Vendor`) | Onboarding/tenancy funnel, invoices, aging, payments, credits, 12 curated evidence cards |
| Admin Facility Intelligence | Same HTML (`Facility`) | Occupancy/Contract hierarchy, Unit Type financial matrix, source-backed Shop 61–90-day drilldown, 12 curated cards |
| Admin Supplier Overview | `03_Expanded_Intelligence/MMIS_Expanded_Intelligence_Interactive_Prototype.html` (`supplier-admin`) | Sourcing→PO→Gate→Stock→settlement lifecycle, 12 curated cards |
| Admin Staff & Managers | Same HTML (`staff-admin`) | Coverage, permissions, staffing evidence and SuperAdmin versus MarketMaster distinction |
| Vendor Business Insights | Same HTML (`vendor-business`) | Rent, product/stock, procurement and activity; pending account gate preserved |
| Supplier Business Insights | Same HTML (`supplier-business`) | Bid, PO, delivery, receipt, settlement; pending account gate preserved |

The new **KPI Library** lists **V01–V45, F01–F41, S01–S57 = 143 core insight groups**, plus **C01–C24 cross-domain** and **M01–M12 staffing/management** groups (179 total), searchable by domain, priority and evidence maturity. One group can represent multiple individually implemented KPI measures.

## Architecture

**Three layers:** Overview (four primary KPIs), Intelligence (grouped charts, matrices, trends and exceptions), Investigation/Action (source rows, exports, notices, audit).

**Financial truth contract:**
- Scope every result by authorized Market. A MarketMaster must never read a foreign Market. SuperAdmin's All Markets is explicit.
- Separate registered Vendor accounts from unique assigned Vendors and active-Contract tenants. For multi-Market Vendors, physical-unit and invoice Market are authoritative for Facility/rent attribution.
- Count physical Shop-backed units once; legacy standalone Stalls must be segregated from companion Stall records.
- For `unitType=SHOP` plus `agingBucket=DAYS_61_90`, the invoice, RentContract, Shop, Market and Vendor must belong to the same qualifying relationship.
- Define exclusive 1–30, 31–60, 61–90 and >90 days separately from cumulative 30+/60+/90+ reports; use the due date with an approved as-of/timezone policy.
- Keep approved contracted rent, issued billed rent, confirmed receipts, invoice-applied payments, eligible consumed credits, verified unpaid rent and held amounts separate. Never treat accepted bids or PO value as Supplier cash revenue.
- Every report carries contract version, role/scoped Market, period, as-of timestamp, source basis, certification state and optional reproducible snapshot identity.
- Shared Vendor/Facility discrepancies carry the same exception identity, related source records and certification consequences. An error in one frontend's calculation is not propagated as truth to another page.

**Supplier evidence:**
- Global Supplier registration does not prove Market eligibility or Market procurement participation.
- Requisition, submitted bid, accepted bid, approved PO, arrived goods, Gate verification, Stock receipt, Supplier invoice and confirmed settlement have distinct states and amounts.
- OTIF is calculated on a specified order-line or delivery grain from promised dates and verified accepted receipts. Supplier scores need explicit weighting, evidence and sample sizes.

**Controls:**
- Card count, detail records and CSV/XLSX must reconcile for the same authorized snapshot. Export the complete filtered result, not only the current page.
- Filters preserve authorized Market, Unit Type, Level/Section, eligible Vendor/Supplier, aging, status, source provenance, time range, comparison basis and quality/certification state as appropriate.
- Recheck notification eligibility at dispatch. Never send or post payments from a read-only intelligence view.
- Unavailable evidence is not zero; display incomplete or unavailable and do not invent certified trend lines.
- Preserve theme values `#f7f4eb`, `#fffdf8`, `#263e32`, `#eeece2`, `#e9ecdf`, `#dcded0` and DM Sans fallback.

## Priority release gates

**P0:** Identity/Market scope, canonical Facility counts, assignment and tenancy integrity, billing and overdue attribution, source-payment/credit reconciliation, shared discrepancy parity.

**P1:** Unit Type rent and Vendor drill-down, Supplier PO/quality/delivery/custody insights, bidirectional filtered navigation, CSV/XLSX, review queues, approved collection notices.

**P2:** Predictive analytics, forecasting, gross margin where POS+COGS exist, maintenance/inspection if observed, Supplier risk and optional saved views.

**Explicit acceptance test:** Selecting `Shop → 61–90 days → affected Vendors` must show only unique Vendors with qualifying Shop-linked overdue invoices; aggregate invoice amount must reconcile exactly to the Source Facility card, excluding held amounts from verified collectible value. The reverse Vendor→Shop navigation returns to the same authorized scope.

## Prototype validation and restrictions

The HTML prototype is static and runs locally. V3 overlays add explanatory drilldowns, local KPI-catalog search and **KPI definition CSV download only**. They do not call MMIS APIs, generate financial CSV, send notifications, approve identities or change application state. The legacy screenshots in this package predate v3 and are retained for visual reference. New v3 screenshots, if included, are marked accordingly.

No GitHub Actions files should be created. Production integration requires separate BE/FE branches and manual/local verification. Do not modify MarketMasterApi/ERP protected `main`, `dev`, `dev_basic` or `staging` branches directly.
