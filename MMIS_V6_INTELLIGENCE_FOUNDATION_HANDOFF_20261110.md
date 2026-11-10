# MMIS V6 — Intelligence Design System Foundation

**Date:** 2026-11-10  
**Source:** feat/mmis-v6-intelligence-ui-foundation-20261110  
**Integration base:** `dev_basic`  
**Status:** Focused frontend increment; review required. No production deployment or financial acceptance.

## Consolidated architecture decisions

This increment is the first production-code step derived from the approved V5 interactive intelligence suite and the 29-reference source review.

1. Keep React 18, Vite, TanStack Router/Query, TanStack Table 8, Tailwind 4 and Base Vega/Base UI. Do not introduce Next.js, TanStack Start, a new auth provider or a second table engine.
2. Use existing MarketMasterApi read models and authoritative operational routes. Do not calculate verified rent, overdue or tax cash in UI components.
3. Every drill-down must reconcile card -> exact filtered list -> full filtered export at the same Market, as-of and definition version.
4. A source-reported dashboard is not Finance-certified. Missing/held evidence must be displayed separately from zero.
5. Keep **unique submitted request cases**, review tasks, and operational exceptions separate. Existing `attention.total` mixes Vendor/payment signals; it is NOT a deduplicated Request Center count.
6. Server-side permission/Market/Contract/Supplier eligibility and read-only checks remain authoritative. Frontend role switches are never security controls.
7. Maintain existing role-specific Vendor onboarding and Contract gating, Supplier qualification, and Gate/Stock custody workflows.
8. No direct writes to protected branches; no workflow YAML changes; no shared DB/financial/government posting.

## Actual files delivered in this PR

| File | Function |
|---|---|
| `lib/intelligence-reporting-policy.ts` | Read-only parity classifier, evidence display, scope-aware query-key builder |
| `lib/intelligence-reporting-policy.test.ts` | Matching/mismatched/incomparable counts, amounts, scope, currency, date, filter/definition; held/unavailable/zero; cache key identity |
| `components/intelligence/IntelligenceEvidenceBar.tsx` | Accessible evidence status, authorized scope and as-of presentation, including partial/unavailable sections |
| `components/dashboard/AdminOperationsDashboard.tsx` | Uses evidence bar and clarifies that operational signals are not unique Request Center cases |
| `package.json` | Registers `test:intelligence` inside standard `npm test` chain; no dependency modifications |

**No new API endpoints, migrations, mutations, framework changes, or accounting semantics.** This is intentionally the narrow compatibility-safe first slice.

## To test on a local or isolated exact-head worktree

```bash
git fetch origin feat/mmis-v6-intelligence-ui-foundation-20261110
git worktree add --detach ../MarketMasterERP-V6-Review origin/feat/mmis-v6-intelligence-ui-foundation-20261110
cd ../MarketMasterERP-V6-Review
npm ci
npm run test:intelligence
npm test
npm run typecheck
npm run build
```

Also run visual browser review of `/dashboard` with SuperAdmin Global, SuperAdmin selected Market, MarketMaster assigned Market, partial dashboard source, failed refresh and read-only accounts. Confirm `IntelligenceEvidenceBar` preserves user navigation, as-of label and existing financial totals.

## Independent acceptance required

- Actual exact-head test/build logs; no such claims are made merely by registering tests.
- Authenticated frontend/API/PostgreSQL Market isolation, read-only, loading/partial/error UAT.
- Reconcile financial reporting definitions before any card presents verified receivables.
- Distinct Request Center case model and domain adapters before a new "pending requests" total is shown.
- Security review of release environment and dedicated UAT runner/host (prior UAT/prod runner collision incident).

## Deferred implementation backlog (preserve for subsequent atomic PRs)

**P0:** typed intelligence backend/report contracts; stable scope-filter-export parity; unique case adapters and Request Center; role/Market access inspector; canonical physical Unit Type + tenancy + invoice attribution and aging/credit reconciliation; approved Vendor/Supplier entitlement gates.

**P1:** Market portfolio intelligence; import integrity batch/identity preservation; staff workload/MarketMaster coverage; Supplier procurement, PO, Gate and Stock cross-evidence; business dashboards; saved views with explicit ownership and permission model; enhanced accessibility.

**P2:** private versioned component registry, optional contrast-safe theme tooling, measurable performance improvements, nonessential motion, evidence-supported forecasting and constrained AI support summaries.

These are **not implemented** in this increment. The approved V5 prototype is a design baseline, not production-ready API data or RBAC.
