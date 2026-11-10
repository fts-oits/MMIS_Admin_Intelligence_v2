# V5 → Current MMIS Page & Codebase Mapping

Read-only inspection basis (November 10, 2026):

- Frontend: `oits-dhaka/MarketMasterERP`, `dev_basic` tree `dec4f5c46eb4206161dbff82c3efdfd0bd727d78`.
- Backend: `oits-dhaka/MarketMasterApi`, `dev_basic` tree `fa935feacc1dd37c97171961f54e14ef4b61ff2a`.
- V4 baseline: `MMIS_Dashboards_Fixed_Offline_Preview_V4.zip` (self-contained standalone pages).

These references identify what was *inspected*, not what was deployed or fully tested at runtime. A design proposal is not evidence of a current API capability.

| V5 page | Operational route or frontend component | Verified source foundation | New API/reporting requirement |
|---|---|---|---|
| Global Operations | `/dashboard`, `components/dashboard/AdminOperationsDashboard.tsx` | Vendor/finance overview, payment queues, Facility/Staff and SuperAdmin Market summaries; partial/unavailable state | Distinct Request Center case count, cross-Market finance, Import/Gate/Supplier actionable exceptions |
| Market Intelligence | `/markets`, `MarketRegistry.tsx`, `MarketList.tsx`, `MarketDetails.tsx` | Registry search, status/type, Market details, Levels and Shops; Analytics tab currently placeholder | Authorized Market × Unit Type × Vendor × finance × staff comparison, readiness KPIs |
| Vendor Overview | `/vendors/overview`, `VendorOverview.tsx`, `VendorTable.tsx` | Identity, rent period, invoice aging, advances, recovery, physical assignments; URL-backed List filters and export | Unified but accounting-basis-aware financial panels and consistent filtered cross-page drill-down |
| Facility Intelligence | `/shops/insights`, `/shops`, `facility-insights.service.js`, `vendor-facility-preview.service.js` | Shop-backed Unit Type, recorded occupancy, Contract gaps, distinct Vendor count; separate legacy Stalls | Invoice/allocations by canonical physical Unit Type, location financial slices, physical inspection provenance |
| Supplier Overview | `/suppliers/overview`, `/suppliers/list`, `supplier.service.js` | Registry status + KYC totals, Supplier directory and import | Authoritative Market service association, bids, POs, delivery quality, AP and settlement reporting |
| Staff & Managers | `/staff/overview`, `/staff/gate-staff`, `/users/marketmasters` | Gate Staff statistics, management; SuperAdmin MarketMaster listing, read-only override | Ownership and SLA workload, management coverage, granular effective permission audit |
| Gate & Stock | `/gate-control`, `GateTerminal.tsx`, `StockReconciliation.tsx`, `VatSettlement.tsx` | Token creation, item capture, Stock reconciliation and VAT display; role-specific tabs | Token lifecycle summary, verified PO/receiving joins, custody exception analytics |
| Import Intelligence | `/vendors/imported-data`, `import-workflow.service.js`, `market-register-consolidation.service.js` | Staged records, batch/review decisions, versioned resolutions, consolidation | Batch/stage trend, duplicate classification, preservation diagnostics, idempotency reporting |
| Request Center | `/users/registrations`, `/billing/rental-applications`, `/billing/reconciliation`, `/vendors/imported-data`, `/gate-control` | Domain-specific existing worklists | Aggregated case adapter, assignment, SLA, dedup, permission-filtered source list |
| Support tickets | `src/routes/ticket.routes.js`, `src/services/ticket.service.js` | Backend ticket create/list/details/messages, scoped access and notification | Verify/add `tickets` frontend list/detail route; service currently builds `/tickets/:id` URLs |
| Vendor Business | `/dashboard`, `FacilityJourney`, `VendorPaymentsOverview` | Vendor onboarding & payment overview | Verified Contract-based eligibility, inventory and supply intelligence scoped to own facilities |
| Supplier Business | `/dashboard` currently redirects Supplier to `/requisitions` | Requisition and Supplier fulfillment entry points | Own Supplier dashboard and eligible bid/PO/delivery/settlement aggregations |
| Gate Staff / Stock Counter | `/gate-control`, `/dashboard` | Gate terminal role policy; Stock Counter dashboard route currently placeholder | Role-specific work queue, exact permitted tokens and outstanding handover status |
| RBAC / access | `hooks/useAuthorization.ts`, role helpers, backend `rbac.middleware.js`, `permission-authorization.middleware.js`, target authorization | Role and effective permission checks; selected Market handling | Enforce each new reporting endpoint's scope and allowedActions server-side |

## Important evidence distinctions

1. Registered Vendor ≠ physically assigned Vendor ≠ approved account ≠ active accepted RentContract tenant.
2. Recorded occupancy ≠ inspected physical occupancy; companion/default Stalls must not inflate canonical unit counts.
3. Billed / applied / unpaid / held evidence must be reconciled by invoice cohort; mere payment attempts or imported historical payment status must not become certified cash.
4. A Supplier's registered home Market ≠ approved service Market ≠ actual order participation. Current Supplier Overview is a global account population.
5. An accepted bid ≠ approved PO ≠ verified receiving ≠ payable invoice ≠ confirmed settlement.
6. Support Ticket is a submitted case. Webhook reconciliation exceptions and imported records needing review are *not automatically* submitted requests.
7. Existing `InvoiceAgingPanel` contains cumulative thresholds; V5 exclusive age bands would require a separately authorized report contract.

## Do not replace established operational pages

Existing `VendorTable.tsx` includes URL-backed search/filter, offset pagination, partial-data handling and CSV. Existing Import records include selection limits, review version and consolidation rules. Existing rental reviewer checks TIN and Stock clearance; Gate/Stock tab restrictions are role-specific. New V5 intelligence pages should deep link to these pages, preserve their security and filters and implement extensions only where current filters lack the needed semantics.
