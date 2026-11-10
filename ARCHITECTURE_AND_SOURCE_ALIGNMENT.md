# Architecture and Source Alignment — MMIS V6 PM Demo

## What this prototype consolidates

The last series of MMIS reviews reached the following decisions. This implementation demonstrates them in the **UI layer only**:

1. Keep the current MarketMasterERP React 18 + TypeScript + Vite 7 + TanStack Router/Query/Table 8 + Tailwind 4 ecosystem. Do not adopt Next.js or TanStack Start merely to import template pages.
2. Continue MMIS `base-vega` / Base UI conventions, existing cream/deep-green tokens, accessible responsive layouts and reduced-motion preferences.
3. Build a common intelligence/reporting vocabulary: headline cards, charts, Market/role/as-of filters, exact-detail lists, stable offset pagination, source-evidence drawers, and all-filtered exports.
4. Organize Global Operations, Market, Vendor, Facility, Supplier, Staff, Gate/Stock, Import, Request Center and Finance intelligence under one role-aware application shell; preserve existing domain operation pages as authoritative action destinations.
5. Keep the **179 KPI families** as a catalog/roadmap, not 179 immediate dashboard cards or automatic production calculations.
6. Enforce all RBAC/ABAC and tenancy rights on the backend; the prototype intentionally shows that pending Vendor/Supplier roles are restricted.
7. Keep financial basis distinctions explicit: RentContract vs invoice vs payment receipt vs confirmed invoice allocation vs outstanding. Historical carry-forward/approved arrears policy remains HOLD.
8. Ensure Supplier identity, approved Market participation, canonical PO, Gate admission, goods acceptance, invoice matching and settlement are separate facts.
9. Include source-quality and release-confidence states, and avoid presenting a Draft PR as merged/accepted.
10. Apply component licensing, compatibility, exact-head testing and UAT/deployment isolation before live implementation.

## 29-reference adoption hierarchy

**Foundation:** official shadcn/ui + MMIS Base Vega / Base UI + existing ERP Router/Query/Table + MarketMasterApi. **Best reusable UI patterns:** Arham Studio Blocks, Arham TanStack Studio Admin, BundUI shadcn-ui-kit free, Shadcn Studio free Base UI blocks, official shadcn table/chart/sidebar examples. **Feature composition ideas:** Next Colocation Template adapted conceptually, without Next route code. **Visual composition:** PaceUI free dashboard and operational-logs patterns. **Optional/design-time:** Tweakcn, Shadcn registries, uidotdev/usehooks, `cn` benchmark, motion-primitives, GSAP, UI Tools, Easy UI, curated awesome-shadcn-ui list. **Excluded:** archived taxonomy code or the empty BundUI repo as production baseline.

No third-party source-code fragments were vendored into this preview. Before any future library import: pin commit, identify license, review dependency versions, check Base UI compatibility, avoid Pro/private-source redistribution, run a11y/security tests.

## Current source status boundaries (10 Nov 2026)

- **MarketMasterERP PR #372**: V6 evidence-safe reporting/UI foundation, open Draft. It adds reporting-policy utilities, query-cache key help, and evidence bar; it is not the full suite displayed in this offline PM demo.
- **API #545 / ERP #366**: MMIS-881 selected-Vendor invoice-generation release remains Engineering/Finance HOLD, with financial carry-forward and other acceptance obligations.
- Financial and workflow operations shown here use invented records. The demo has no live integration.
- The current `dev_basic` baseline should be read afresh before engineering changes. Historical source heads in October/early November plans are dated checkpoints, not automatic release authority.

## Visual -> production mapping

| Demo view | Intended existing MMIS route / service family | Production work needed |
|---|---|---|
| Global Operations | `/dashboard` / AdminOperationsDashboard | Real unique Request Center adapter, grouped true exceptions, evidence-safe read reporting |
| Market Intelligence | `/markets`, Market Registry | Readiness/role/financial aggregations; no hypothetical legal/fiscal authority |
| Vendor Overview | `/vendors/overview`, Vendor List | Exact financial and tenancy population, filtered export and 360 drill-down |
| Facility Intelligence | `/shops/insights`, `/shops` | Physical-unit counting, Unit Type finance, occupancy-vs-Contract reconciliation |
| Supplier Intelligence | `/suppliers/overview`, Supplier management and PO | Market grants and stage-aware read models |
| Gate & Stock | `/gate-control` | Source-linked PO/token/custody/Stock evidence; role-specific execution |
| Import Integrity | `/vendors/imported-data` | Reviewed staging/adoption provenance; safe existing-Vendor preservation |
| Finance & Evidence | Billing/Payments/Invoices/Reconciliation | Source-budget/credit isolation, verified allocation and Finance policy acceptance |
| Rental Readiness | API #539 / ERP #365 and selected-invoice work | Contract eligibility and Finance-approved generation controls |
| Staff & RBAC | Staff, MarketMasters, effective permissions | Secure capability inspect, role/Market assignment, audit; no parallel auth |
| Public Shop Finder | `/available-shops` and shared auth header | Persistent session, listing/rental handoff and safe ownership proof |

## Demo dataset provenance

All demo IDs, people, Market names, financial amounts, Cases, POs, tokens and statuses are synthetic and generated deterministically by `source/synthetic_data.json`. The 179-family catalog is a source-consistent design proposal aligned with the approved domain-family counts and not an exact claim of deployed API coverage. The fixed **as-of date is 2026-11-10**. A sample user's displayed entitlement is simulated; it is not cryptographic or server-side authorization.
