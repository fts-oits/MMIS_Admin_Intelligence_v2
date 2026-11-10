# MMIS Enterprise Intelligence, Design System, Dashboard & RBAC Implementation Plan

**Date:** 10 November 2026  
**Scope:** `oits-dhaka/MarketMasterERP`, `oits-dhaka/MarketMasterApi`, previously approved MMIS V5 Intelligence Suite  
**Status:** Architecture and implementation proposal, not live application changes or production acceptance.  
**Repository governance:** Never modify `dev`, `main`, `dev_basic`, or `staging` directly in either application repo. Use a separate purpose-built branch and manually/local acceptance; do not add workflow files.

## 1. Decision record

**Decision: modular adoption, no wholesale framework migration.** Retain the MarketMasterERP React/Vite/TanStack Router/TanStack Query application and the existing MarketMasterApi authority. Port selected, reviewed shadcn/studio components into the existing Base UI design-system family. Use the MMIS V5 prototype as visual specification, not as production code or financial evidence.

**Verified ERP `dev_basic` baseline:** React `^18.3.1`; Vite `^7.3.0`; TanStack Router `1.170.19`; TanStack Query `^5.95.2`; TanStack Table `^8.21.3`; Tailwind CSS `^4.2.2`; Base UI `^1.4.0`; `shadcn ^4.2.0`; TanStack Form `^1.28.6`; Zod `^4.3.6`. `components.json`: `style: base-vega`, `rsc: false`, Tailwind CSS variables enabled; frontend theme in `style.css` already has cream/dark-green semantic light and dark tokens, Fraunces/DM Sans local font references, accessible reduced-motion handling. These are source snapshots; do not assume dependencies have been upgraded without checking exact branch heads.

**Reference compatibility warning:** Recent Arham templates use React 19 and TanStack Table 9, while Next variants use Next.js 16 and may depend on server components. Copying their application shells, auth flows, routing, table hooks, or generated component style definitions directly is not safe. The TanStack reference is TanStack **Start**, not just the Router plugin already used in MMIS. Base UI version also differs. Port *patterns or reviewed individual components*, not the entire template.

## 2. Source-by-source assessment

| Source | Verified contents | Value to MMIS | Adoption decision |
|---|---|---|---|
| `arhamkhnz/studio-blocks` | Installable KPI, chart, list, navigation/sidebar, table, form blocks; source included, MIT | Strongest discrete card/worklist/charts prototypes | **High / selective port**; replace sample data, inspect dependencies |
| `arhamkhnz/next-shadcn-admin-dashboard` | Next 16 Studio Admin, many domain dashboard views, sidebar/header, search, layout controls, forms | Visual page patterns / dashboard layout and admin oversight | **High visual reference, low direct code reuse** |
| `arhamkhnz/next-colocation-template` | Next App Router route-local components, hooks and schema organization | Feature-ownership model in large codebase | **High architecture reference**; adapt to TanStack route conventions |
| `arhamkhnz/next-shadcn-admin-dashboard-baseui` | Next Admin with `base-nova` shadcn styling | Closer primitive family; modal/menu/dialog behavior | **High reference / compatibility bridge**; map to MMIS `base-vega` |
| `arhamkhnz/next-shadcn-admin-dashboard-aria` | React Aria, `aria-nova`, different primitive APIs | Accessibility ideas, keyboard/focus patterns | **Selective reference only**; don't mix primitives by default |
| `arhamkhnz/tanstack-shadcn-admin-dashboard` | TanStack Start dashboard, file-based routes, cards, admin navigation, tables | Closest router/composition pattern to MMIS | **Highest architecture reference**, not a Start migration |
| `arhamkhnz/web-resources` | Curated visual inspiration, typography/effects/design utilities | Optional brand research | **Low runtime relevance**; avoid decoration-heavy UX |
| `shadcn-ui/ui` | Main source/official components, dashboard example, tasks/data tables, charts, sidebar | Core semantic accessible components | **Foundational**; use MMIS-compatible Base UI variants |
| `shadcn-ui/registry-template` | `registry.json` item files, `shadcn build`, static JSON artifacts | Reusable internal design-system distribution | **High when components stabilize** |
| `shadcn-ui/alpine-registry` | Namespaced registry, design-system tokens, composite blocks, auth example | Multi-team internal component registry and theme governance | **High later-stage inspiration**; isolate build-time access from runtime RBAC |
| `shadcn-ui/taxonomy` | Archived Next.js 13 early App Router experiment; repository explicitly warns outdated | Historical IA/architectural inspiration | **Do not transplant** for production |
| `shadcn-ui/cn` | Alternative Tailwind 4 class join/merge engine and migration tools | Potential build/runtime micro-optimization | **P2 experiment**; benchmark on MMIS, don't preemptively migrate |
| `ui.shadcn.com/docs` | Official open-code components, Vite, data table, chart, sidebar and registry docs | Primary implementation instructions | **Required reference** |
| `ui.shadcn.com/docs/theming` | Semantic CSS-variable-based theming | Map V5 to MMIS tokens and accessible dark mode | **Required reference** |

**Vendor-level caveat:** The Arham README states RBAC with configuration-driven UI and multi-tenancy are **planned**, not certified implemented security. Their Users/Roles pages must not be assumed to enforce backend permission checks.

## 3. Target layered architecture

1. **AppShell / UX**: persistent logged-in header (also when using public Shop finder), sidebar, command search, Market selector, notifications, accessibility, breadcrumbs, locale/currency.
2. **Design-system primitives**: existing shadcn Base Vega, Base UI controls, tokens, card, table, combobox, dialog, sheet, skeleton, chart wrapper.
3. **Shared intelligence widgets**: `MetricCard`, `MetricStrip`, `ChartPanel`, `ScopeBar`, `EvidenceBadge`, `DataQualityBanner`, `DrilldownLink`, `FilterableWorklist`, `EvidenceDrawer`, `RequestQueueTile`, `ExportMenu`.
4. **Route-local feature modules**: `features/intelligence/global`, `markets`, `vendors`, `facilities`, `suppliers`, `staff`, `imports`, `gate-stock`, `requests`, plus business-owner views; keep only truly reusable components in shared layer.
5. **Query/authorization adapters**: typed TanStack Query hooks, URL search validation, scoped query keys, permission-aware route metadata, server-issued allowed actions, active filters.
6. **API domain reports**: read-only summary/detail endpoints composed from existing canonical services; domain-owned approvals/changes remain under their original APIs.
7. **Evidence base**: PostgreSQL/MDA financial rules, invoice/allocations, RentContract status, imported identity review, Supplier PO/delivery, Gate/Stock events, request cases and immutable audit events.

Suggested non-disruptive directory organization (adapt to current repo root convention, rather than physically moving all existing routes):

```text
components/ui/                    # existing Base Vega shadcn primitives
components/intelligence/          # shared approved KPI, chart, table, evidence views
lib/intelligence/                 # metric definitions, money/date/scoping, filter contracts
lib/navigation/                   # existing navigation policy, extended via permission metadata
gateway/intelligence/             # typed API contract and query hooks
features/intelligence/markets/    # route-local charts/tables, tests
features/intelligence/vendors/
features/intelligence/facilities/
features/intelligence/suppliers/
features/intelligence/requests/
features/intelligence/gate-stock/
features/intelligence/imports/
features/intelligence/staff/
routes/_protected/_app/...        # keep existing TanStack Router paths and guards
```

## 4. Design tokens and navigation

**Keep approved palette and fonts**. Current `style.css` already supplies light tokens: background `#f7f4eb`, primary/foreground `#263e32`, card `#fffdf8`, muted `#eeece2`, border `#dcded0`, chart tokens, and a separate dark token set. Fraunces is used for headings, DM Sans for body. Use semantic tokens (`bg-background`, `bg-card`, `text-foreground`, `text-muted-foreground`, `border-border`), not hard-coded colors for individual imported blocks.

**Sidebar groups**: Overview, Intelligence (Vendor/Facility/Supplier/Market), Operations (Market Registry, Vendors, Shops, Imports, Gate & Stock, Staff), Finance (Invoices, Payments, Reconciliation, URA/EFRIS evidence), Requests & Support, Administration (MarketMasters, RBAC, settings). Role- and Market-appropriate links only. Keep existing route names; do not let a template change primary URLs.

**Header**: Market selector + context / reporting period; notification bell; accountable user name and account menu; no Sign In button for an authenticated user when navigating to public Shop finder. Read-only badge only where meaningful. Sticky header and responsive navigation, keyboard search, focus restoration, reduced motion, accessible mobile drawers.

**Typography/density**: Four headline KPI cards (desktop; mobile two-column where feasible), one urgent-work section, progressive charts and a canonical worklist. Use KPI units, descriptions, as-of timestamps, and source-status labels; no animated fake data.

## 5. Dashboard and domain specification

### 5.1 Global Operations

Top cards: active Markets, verified rent collections, eligible unpaid/overdue rent, distinct Requests Awaiting Action. Below: Requests Needing Attention (onboarding, KYC, rental applications, Contract approvals, support, qualifying reconciliation cases), Operational Exceptions (separate), Market performance, Vendor/Facility/Supplier/Staff/Gate/Import health. Drill-down each card to precise backend-filtered records; don't equate the existing `attention.total` aggregation with distinct requests.

### 5.2 Market Intelligence

Portfolio totals/status by Market type; physical unit capacity; Level/Section occupancy; MarketMaster/Gate staffing coverage; contracted vs invoiced vs applied rent; Market readiness by explainable dimensions; Market comparison table. Registry is authoritative action destination; don't infer government beneficiary from Market ownership label.

### 5.3 Vendor Overview

Registration/identity/KYC/onboarding funnel; staged import provenance; unassigned Facility; Contract awaiting approval/acceptance; rent billing, confirmed allocation, held sources, unpaid, aging (exclusive vs cumulative), future coverage and receivable recovery. On click navigate to the current Vendor List/Contract/Invoice report with the exact filters, not a duplicated sample table. Vendor360 evidence drawer shows physical units, Contracts, policy dates, invoices, allocation, permitted actions.

### 5.4 Facility Intelligence

Canonical Shop-backed physical unit population, five Unit Types, separate historical standalone Stalls, recorded occupancy, assignment/active-contract gap, listing availability, Contract renewal; Unit Type rent matrix (expected, billed, confirmed allocations, unpaid, overdue Vendor count) with exact Vendor+Facility+invoice drill-down. Physical occupancy is not asserted unless inspection evidence is available.

### 5.5 Supplier Intelligence

Registered/qualified Suppliers (global registry basis); approved Market eligibility separate from actual participation; requisitions/bids/award, approved PO commitments, dispatched/received goods, Gate and Stock custody, OTIF with denominator/sample, invoice/settlement. Supplier360 timeline must preserve accepted bid != PO != delivered != Stock-verified != paid.

### 5.6 Staff/MarketMaster Intelligence

SuperAdmin global MarketMaster assignment, uncovered Markets, effective read-only exceptions, denied capabilities, invitation backlog, staff coverage and assigned case workload. MarketMaster only assigned-Market Gate/Stock staff and cases. Permissions panel must use real authorization metadata, not template dummy roles.

### 5.7 Gate/Stock Intelligence

Gate token stage, time in state, arrival/verification/custody, variance, Stock pending/reconciled, approved VAT evidence; incident queues, double/posting discrepancies; Gate Staff vs Stock Counter role restrictions. Navigate to existing `/gate-control` tabs/details rather than rebuilding the terminal.

### 5.8 Import Integrity

Batch status/staged records, validation failures, duplicate identity resolution, field decisions, ready-to-promote count, successfully consolidated count, existing-record adoption, reporting-period data and reconciliation evidence. Never treat staged records as live Vendors; keep selective and filter-scope execution safeguards.

### 5.9 Request Center

Backend-owned typed adapters: Vendor registration, KYC, rental application, Facility claim, RentContract approval, support ticket, true payment-review case, import review, Gate/Stock exception case. Separate **requests**, **review tasks**, and **operational exceptions**. A `caseId` is unique and stable; category counts sum only if mutually exclusive. Each item exposes allowed actions and links to authoritative domain review; generic approval must not bypass TIN verification, Stock clearance, payments or role restrictions.

### 5.10 Role-specific business dashboards

Pending Vendor: own onboarding, KYC, rental applications, Shop search and tenancy acceptance only; no inventory/payment/invoice prematurely. Approved Vendor: authorized Contract-owned units, due invoices, payments, stock and requisitions. Pending Supplier: KYC/profile only. Approved Supplier: own requisitions, bids, accepted POs and delivery/settlement evidence. Gate Staff: entry processing queue. Stock Counter: receiving/reconciliation queue. Read-only admin: data and authorized export only, no mutations.

## 6. Shared component contracts

### Proposed `MetricDefinition`

```ts
type MetricDefinition = {
  id: string; title: string;
  grain: 'VENDOR' | 'FACILITY' | 'INVOICE' | 'CASE' | 'PO' | 'TOKEN' | 'MARKET';
  source: string; definitionVersion: string;
  timeBasis: 'CURRENT_SNAPSHOT' | 'BILLING_PERIOD' | 'PAYMENT_EVENT' | 'DUE_DATE';
  aggregation: 'COUNT_DISTINCT' | 'SUM_ELIGIBLE' | 'RATIO';
  eligibleStatuses: string[];
  breakdowns: string[];
  drilldownRoute: string;
  capability?: string;
  dataMaturity: 'VERIFIED' | 'PARTIAL' | 'PROPOSED';
};
```

This is a proposed metadata shape; implement with the current TypeScript/Zod approach. Never compute authoritative finance in a visual component.

### Proposed report envelope

```ts
type IntelligenceResponse<T> = {
  scope: { type: 'GLOBAL' | 'MARKET'; marketId: string | null };
  asOf: string;
  definitionVersion: string;
  reportingBasis: string;
  currencyCode: string | null;
  partial: boolean;
  unavailableSections: string[];
  filtersApplied: Record<string, unknown>;
  summary: T;
  dataQuality: 'VERIFIED' | 'HELD' | 'PARTIAL' | 'UNAVAILABLE';
};
```

Counts and details must share a repeatable-read or equivalent reconciled snapshot where accuracy demands. Use null/unavailable, not zero, when evidence cannot be established.

### Drill-down rule

`KPI card -> validated URL filter -> server-scoped offset-paginated list -> evidence/details -> authorized domain action`. Persist selected Market, Unit Type, Level/Section, period, status, owner, as-of where supported; reset dependent filters on Market change. If a filter cannot be supported by a destination, reject or explicitly flag it; never silently show broader data. Provide a stable secondary sort, backend total, page bounds recovery, and export for the **entire matching authorized population**.

## 7. RBAC and ABAC/tenancy controls

Effective access is the intersection of role permissions, effective authorization grants/denials, assigned Market, record ownership, approved tenancy or Supplier qualification, operation type, and read-only/mutation restrictions. Server enforces target authorization and continues to enforce domain prerequisites.

| Persona | Read scope | Actions / restrictions |
|---|---|---|
| SuperAdmin | Authorized global/all Market or selected Market | Admin capabilities only when granted; no implied fiscal authority |
| MarketMaster | Assigned Market | No foreign Market or SuperAdmin MarketMaster governance |
| Read-only Admin | Authorized reports | No review/approval/invitation/import execute/bulk mutation |
| Pending Vendor | Own onboarding/Shop search/applications | No Inventory/Payments/Invoices absent required approval+Contract entitlement |
| Active Vendor | Own qualifying units/contracts/transactions | Recheck entitlement per request; no others' accounts |
| Pending Supplier | Own KYC/profile | No bidding/fulfillment/settlement until qualified |
| Active Supplier | Own eligible bids/POs/deliveries | Market participation and source ownership checked |
| Gate Staff | Authorized Market Gate and token flow | No Stock-only reconciliation |
| Stock Counter | Authorized stock/reconciliation flow | No Gate admission or arbitrary fiscal/payment action |

**RBAC panel** should include: role catalogue (view), permission matrix, effective permission explanation, Market assignments, explicit denies/read-only expiry, audit trail, pending invitations, and permission-diff preview. Any role mutation requires dual review/strong authorization as applicable; no ability to grant self privileges by editing frontend config.

## 8. Source-truth and financial gates

- Physical Facility counts exclude companion/default Stalls, separately disclose historical standalone Stalls; Vendor counts use distinct Vendor ID per defined grain.
- Active Vendor != active tenancy; Contract monthly rate != billed amount; billed != confirmed receipt; receipt != eligible invoice allocation; held/imported paid-through metadata != verified cash.
- Rent balance is invoice-based, reconciled with source payment eligibility and documented credits/adjustments; Market+currency isolation, confirmed payment-source budget, transactional concurrency safeguards must remain intact.
- Aging uses defined timezone/due date; exclusive 1–30, 31–60, 61–90, 90+ separate from cumulative 30+/60+/90+.
- Revenue beneficiary, MDA, URA/EFRIS/PRN issuer and VAT status must use approved legal/fiscal evidence; no invented fiscal compliance certification.
- Supplier bid != accepted PO != goods receipt != approved payable != settlement. Record proven event stages separately.
- KYC, documents and support-ticket records are sensitive. Limit exposed fields, sanitize CSV, avoid raw identifiers in URLs, audit privileged exports.

## 9. Adoption phases with deliverables and exit gates

| Stage | Priority | Deliverable | Exit gate |
|---|---|---|---|
| 0: baseline + compatibility audit | P0 | Exact frontend/backend commits, V5 screenshot parity, inventory package/primitive/Tailwind/Table compat, capture component licenses and third-party dependencies | No protected-branch writes; build/test baseline captured |
| 1: design tokens + AppShell | P0 | MMIS Base Vega component wrappers, header/nav/Market selector, accessible mobile/sidebar, correct authenticated public header | Role/Market navigation, focus, responsive, no broken public header |
| 2: intelligence kernel | P0 | MetricDefinition registry, typed API envelope, scope bar, partial/held states, MetricCard, FilterableWorklist, EvidenceDrawer | Card->list->export exact count/value; stale data denied on Market change |
| 3: Vendor + Facility | P0 | Vendor Overview, Facility Intelligence, rent/aging matrix, canonical physical/tenancy/financial drill-down | Native PG reconciliation and exact Vendor/Facility populations |
| 4: Request Center + RBAC | P0 | Unified cases, true distinct pending count, linked authoritative domain reviewers, role-specific queues, staff permission views | TIN/Stock preconditions, ownership, read-only and cross-Market tests |
| 5: Market + Import + Staff | P1 | Market readiness, import integrity, assignment and workload analysis | Correct provenance, scoped counts, no destructive import bypass |
| 6: Supplier + Gate/Stock | P1 | Qualification/PO/delivery, token/custody, Stock exceptions, verified settlement states | PO->receipt chain, role-specific Gate and Stock actions |
| 7: Role business dashboards + UI hardening | P1 | Active/pending Vendor/Supplier, Gate Staff/Stock Counter, saved views, print/export/accessibility | Authenticated role journeys, device/mobile UAT |
| 8: internal registry + optimization | P2 | Versioned MMIS UI registry, conventions, optional `cn` benchmark, selected forecasts and scoring | License/security review, a11y regression, real bundle/latency improvement |

No new GitHub Actions workflows: run manual/local CI-equivalent scripts, disposable PostgreSQL, browser/UAT and exact-head acceptance. Preserve purpose-built integration branches, create PRs for review; never write to `dev`, `main`, `dev_basic`, or `staging` directly.

## 10. Exact-head acceptance checklist

**Build and component tests:** typecheck/build, accessible keyboard roles/focus/aria, light/dark, RTL where needed, 320/375/390/768/1024/1440px, reduced motion, desktop/mobile, no JS error, CSS compatibility; role-context fetch on mount.

**Identity/authorization:** unauthenticated/pending/active/restricted/read-only; global vs assigned Market; forbidden deep link, malformed scope, cross-Market ID, stale query response, role-switch demo not treated as authentication, action permission rechecked server-side.

**Data truth:** exact card/list/export count and sum; distinct Vendor and canonical Facility counting; active Contract rights; date-policy selection; confirmed rent allocations, credits, held/reversed transactions, native PG multi-session race tests; aging boundary and timezone fixtures.

**Operational workflows:** public Shop finder persistent authenticated header, KYC/onboarding, applicant rental TIN/Stock clearance approvals, Supplier eligibility and PO/receipt chain, import review and adoption, Gate handover/Stock reconciliation, support ticket URLs and case audit trails.

**Operations:** real selected-Market switching, request ownership/SLA, notifications and retry behavior, load/empty/partial/offline views, full filtered export, all selected rows across offset pages, safe stale-cache invalidation, manual UAT and screenshot diffs against V5.

## 11. Implementation tickets (recommended sequence)

- `DS-01`: Base Vega component compatibility audit; tokens; brand/contrast; local typography.
- `DS-02`: AppShell header, notifications, Market selector, nav/search, user account persistence across public Shop browsing.
- `INT-01`: Metric registry + reporting envelope + financial basis/data-quality declarations.
- `INT-02`: Scoped URL filters, server-driven offset pagination, canonical export and evidence drill-down.
- `INT-03`: Vendor/Facility reconciliation contract, Unit Type rent performance, aging boundaries.
- `RC-01`: Request source-adapter inventory and case identity/status mapping.
- `RC-02`: Request Center backend count/detail with domain reviewer handoffs, SLA and ownership.
- `AUTH-01`: Effective permission and Market-scope capability map for UI; RBAC overview; read-only exceptions.
- `MI-01`: Market portfolio and readiness;
- `IMP-01`: Vendor import batch/stage/exception reporting with preservation checks.
- `STAFF-01`: MarketMaster/staff staffing coverage, case assignment, restrictions.
- `SUP-01`: Supplier eligibility, PO, delivery, Gate receipt and settlement stage reporting.
- `GATE-01`: Token/custody/Stock reconciliation worklists and source-linked exceptions.
- `OWN-01`: Vendor/Supplier active/pending business dashboards and Gate/Stock role queues.
- `REG-01`: Optional internal registry with versioned components, tests, license/lockfile and upgrade procedures.

Every ticket requires linked source service, route, Zod DTO, correct Market scope, loading/error/partial behavior, accessibility QA, role test set and visual acceptance screenshot.

## 12. Risk ledger / explicit non-goals

| Risk | Control |
|---|---|
| React 18 -> React 19 incompatibility | No blanket dependency updates; port compatible source, focused tests |
| TanStack Table 8 -> 9 API break | Adapt patterns, not `useTable`/feature registry from v9 |
| `base-vega` vs `base-nova`/`aria-nova` | Keep existing primitives; inspect imports and accessibility per block |
| Next App Router/TanStack Start assumptions | Do not copy route, server action, SSR or auth code |
| Theme style leakage | Semantic CSS variables, explicit tokens, dark/contrast checks |
| Role screen spoofing | Server-side effective auth+target Market/ownership; frontend only reflects it |
| Request total double count | Case identity model and separate request/task/exception populations |
| Financial misstatement | Invoice/report source truth, held status, source allocations, snapshot basis |
| Insecure public registry | Build-time access only, token/secret handling; never embed tenant data in component assets |
| Unverified use of examples | All sample figures visibly labeled until real data and UAT acceptance |
| Deployment isolation | Use manually verified environment/runner labels and destination before UAT deployment; no assumption any self-hosted runner is UAT |

## 13. Links and sources reviewed

- https://github.com/arhamkhnz/studio-blocks
- https://github.com/arhamkhnz/next-shadcn-admin-dashboard
- https://github.com/arhamkhnz/next-colocation-template
- https://github.com/arhamkhnz/next-shadcn-admin-dashboard-baseui
- https://github.com/arhamkhnz/next-shadcn-admin-dashboard-aria
- https://github.com/arhamkhnz/tanstack-shadcn-admin-dashboard
- https://github.com/arhamkhnz/web-resources
- https://github.com/shadcn-ui/ui
- https://github.com/shadcn-ui/registry-template
- https://github.com/shadcn-ui/alpine-registry
- https://github.com/shadcn-ui/taxonomy
- https://github.com/shadcn-ui/cn
- https://ui.shadcn.com/docs
- https://ui.shadcn.com/docs/theming
- https://ui.shadcn.com/docs/registry
- https://ui.shadcn.com/docs/components/data-table
- https://ui.shadcn.com/docs/components/chart
- https://ui.shadcn.com/docs/installation/vite
- MMIS source reviewed via GitHub connector at `dev_basic`: `package.json`, `components.json`, `style.css`, `components/dashboard/AdminOperationsDashboard.tsx`, `lib/utils.ts`; plus previously inspected Vendor/Facility/Supplier/Gate/Staff/Import/authorization services.
- MMIS V5 prototype handoff: `MMIS_Intelligence_Suite_V5/V5_ENGINEERING_CONTRACT.md` and `V5_SOURCE_MAPPING.md`.

**End verdict:** Build one design system and one evidence-backed intelligence layer on the existing MMIS platform. Use Studio Blocks and Studio Admin for curated, tested presentation patterns, shadcn for primitives and distribution, and original MMIS services as the sole source of permissions and financial/operational truth.
