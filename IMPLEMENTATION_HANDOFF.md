# After PM Signoff — Implementation & Acceptance Handoff

## Release sequence

**P0 — Design and data truth:** exact base commit, compatibility/licensing audit, AppShell, persistent auth header, Market selector, semantic design tokens, reporting envelope, card/list/export parity, partial/held/unavailable states.

**P0 — Vendor/Facility/Finance:** canonical physical units, RentContract eligibility, invoice-based exclusive aging, Market+UGX+confirmed payment-source separation, credit concurrency and native PostgreSQL proof. Implement read-only reports ahead of write capabilities.

**P0 — Request Center and RBAC:** source-case adapters, mutually exclusive case categories, honest SLA state, ownership, role/Market/target authorization, read-only and explicit denies, domain-specific action handoff. No generic approval bypass.

**P1 — Market, Import, Staff:** real registry and staffing analytics, import provenance and promotion safety, evidence-rich worklists and authorized exports.

**P1 — Supplier, Gate, Stock:** explicit Market eligibility, PO issuance/evidence, Supplier acknowledgment/fulfillment rights, Gate admission, Stock receipt and financial stages; coordinate with responsible procurement module owner.

**P1 — Role dashboards and UAT:** real pending/active Vendor/Supplier and Gate Staff/Stock Counter experiences, authenticated public Shop finder, accessibility, browser and negative security tests.

**P2 — UI registry and advanced measures:** versioned internally approved UI components, measured bundling/latency improvements and forecasting based on sufficient source data.

## Proposed core DTO contracts

```ts
interface IntelligenceScope {
  type: 'GLOBAL' | 'MARKET';
  marketId: string | null;
  role: string;
  asOf: string;
}
interface MetricEvidence {
  definitionVersion: string;
  metricId: string;
  grain: 'MARKET'|'VENDOR'|'FACILITY'|'INVOICE'|'CASE'|'PO'|'TOKEN';
  timeBasis: 'CURRENT'|'ISSUED_PERIOD'|'PAYMENT_ALLOCATION'|'DUE_DATE';
  currencyCode: string | null;
  available: boolean;
  dataQuality: 'VERIFIED'|'HELD'|'PARTIAL'|'UNAVAILABLE';
  value: number | null;
  filtersApplied: Record<string, unknown>;
  drilldown: { route: string; filters: Record<string, unknown> };
}
interface CaseListRow {
  caseId: string; sourceDomain: string; sourceId: string;
  marketId: string; requesterId?: string; ownerId?: string;
  submittedAt: string; dueAt?: string; priority: string;
  status: string; allowedActions: string[];
}
```

These are **proposals**, not current API responses. Stable offset-based pagination, deterministic sort and filtered export are required. Do not use cursor pagination under the project decision. API must recheck authorized Market/role/record/entitlement on every request.

## Non-negotiable evidence

- Current exact remote base and feature SHA, `npm ci`, tests, TypeScript, production build and lint with no dependency conflicts.
- Accessibility (keyboard, focus, semantically labeled chart data, reduced motion), desktop/mobile responsive tests, screenshot comparisons against the approved PM demo.
- Multi-Market, read-only, SuperAdmin, MarketMaster, pending Vendor, active Vendor, pending/active Supplier, Gate Staff and Stock Counter authenticated UAT.
- Native PostgreSQL reconciliation (invoice liability/verified allocations/credit/overdue), multi-session concurrency and idempotency, no unauthorized financial write.
- Request Center case count -> category -> filtered worklist -> export exact grain and as-of parity; provenance of every state.
- Supplier Market eligibility and PO/Gate/Stock custody consistency; import identity/facility preservation; no synthetic paid-through cash promotion.
- Finance policy approval for carry-forward arrears and final selected-invoice posting before deployment. Reviewer/PM signoff remains distinct from engineering/Finance acceptance.
- Isolated UAT runtime: verify runner label, host identity and destination before any deployment. Never deploy UAT jobs to production runners by using generic labels.
- Never directly modify `main`, `dev`, `dev_basic`, `staging` or add workflow YAML. Separate feature branches/PRs and manual/local testing only.

## Recommended PR granularity

AppShell and navigation; Design System; reporting kernel; Vendor/Facility reporting; unique Request Center read API; role/access inspector; Market/Import/Staff aggregations; Supplier/PO and Gate/Stock read models; business-persona dashboards. Keep invoice posting, contract activation migrations, credit/ledger changes and government fiscal work separately reviewed and Finance-approved.

## V6.1 prototype parity acceptance (new)

The approved V6.1 PM demonstration now includes richer synthetic workflow transitions, but not live domain writes. Before implementing any transition, introduce role/ownership/Market checks on the backend, immutable state changes, event versioning/idempotency, documented consent and acceptance evidence, and audit/notification persistence. Do not reuse the demo's local state mutation as production business logic.

**Required live P0 acceptance cases:** Facility `GAP` count→list/export, Import `(NEEDS_REVIEW ∪ BLOCKED)` count→list/export, Vendor exclusive invoice 61–90-day aging per eligible invoice and Unit Type intersection, user-return intent preservation for public Shop finder, separate Vendor account/rental/Contract approval/acceptance, rental-policy effective/first-liable date and existing invoice-period collision, distinct request case identity/dueAt/owner, role-specific Supplier PO/Gate/Stock event ordering, and URL Back/Forward/deep-link scope revalidation.

The self-contained browser demo passed 177 baseline, 34 functional, and 16 financial/filter/RBAC assertions. Production gates remain HOLD until native PostgreSQL, backend authorization, multi-session concurrency, exact-head builds, authenticated browser and Finance-specific approvals.
