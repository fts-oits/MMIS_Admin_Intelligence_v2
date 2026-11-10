# MMIS V5 — Engineering Integration & Acceptance Contract

This document specifies **what the finished prototype means** and what a production-grade implementation must prove. V5 includes no backend calls and no source modifications.

## 1. Domain boundaries and canonical IDs

- `Market`: legal/operational administrative scope, selected only within effective user authorization.
- `Vendor`: canonical reviewed identity. Active user status is not equivalent to active physical tenancy.
- `Facility`: canonical physical Shop-backed unit and subtype (`SHOP`, `STALL`, `PITCH`, `CAGE`, `LOCK_UP`). Deduplicate legacy companion/default Stalls; report standalone historical Stalls separately until dedup decisions are approved.
- `RentContract`: effective, approved and Vendor-accepted tenancy evidence; identify Facility, tenant, rate, billing activation, start/end dates, approval/version.
- `Invoice`: issued obligation and applicable policy; distinguish billing period, first liable date, issue date, due date.
- `Payment allocation`: confirmed source and invoice attribution; source budget, Market/currency, state, CAS/concurrency invariants, credits/advance and held evidence.
- `Supplier`: canonical account identity separate from Market service eligibility and actual purchase activity.
- `Requisition/Bid/PO/Delivery/Gate Token/Goods Receipt`: separate evidence stages. Never infer settlement from a bid or inventory acceptance from Gate admission.
- `ImportRecord`: staging/review/consolidation evidence; never count a staged record as a live approved Vendor.
- `Request Case`: a discrete administrative case with one stable identity and source reference. Operational exceptions are separate from user-submitted cases.

## 2. Proposed reporting contracts

Each KPI-driven response should specify:

```json
{
  "scope": {"type":"GLOBAL_OR_MARKET", "marketId":"AUTHORIZED_MARKET_OR_NULL"},
  "asOf":"OFFSET_AWARE_TIMESTAMP",
  "reportingBasis":"CURRENT_BALANCE_OR_BILLING_COHORT_OR_EVENT_DATE",
  "currencyCode":"UGX_OR_SUPPORTED_CURRENCY",
  "partial":false,
  "unavailableSections":[],
  "dataQuality":"VERIFIED_OR_HELD_OR_PARTIAL_OR_UNAVAILABLE",
  "definitionsVersion":"v1",
  "filtersApplied":{"marketId":"AUTHORIZED", "status":"..."},
  "summary":{"metricKey":{"count":0,"amount":null,"available":true,"evidenceBasis":"..."}},
  "drilldown":{"queryKey":"STABLE_FILTERED_POPULATION", "sourceRoute":"/authorized/route"}
}
```

Use this as a contract proposal, **not** as a claim that the live API already returns this shape. Avoid echoing or exposing unnecessary raw UUIDs in user-facing URLs.

### Proposed read-only endpoints

Design-level endpoints (exact REST naming subject to backend API review):

1. Admin Market portfolio and readiness (`marketId`, `asOf`, comparison window; SuperAdmin Global only).
2. Vendor onboarding/tenancy/finance scoped intelligence with exact Vendor list population references.
3. Facility Unit Type rent matrix joined from canonical units through approved Contracts, invoice liability and verified allocation evidence.
4. Supplier qualification, eligibility, requisition, PO, goods-receipt and invoice/settlement reporting.
5. Gate/Stock custody and token exception summary with stable links to PO/receipt evidence.
6. Import-review stage and batch-quality summaries aligned with import detail list filters.
7. Unified Request Center case list and counts with type/source adapters, SLA and ownership.
8. Staff assignment/workload/permission coverage reporting.

## 3. Request Center case model

```text
Case {
  caseId, type, sourceSystem, sourceId, marketId, requesterKind,
  submittedAt, status, priority, dueAt, assigneeId,
  subjectReference, currentSourceStatus, allowedActions[],
  dataQuality, asOf, evidenceRefs[]
}
```

**Distinct cases**: group by canonical `caseId`, not person, Vendor account, or underlying event count. A KYC task attached to an onboarding case may or may not be a separate case depending on approved identity semantics. Count only actionable nonterminal status states. Category components must be mutually exclusive *if the UI says their sum equals total*.

**Recommended source adapters:** User/registration approvals, Vendor KYC, rental application approvals, Contract approvals/acceptance, dispute/reconciliation cases, support ticket cases, ImportRecord reviews, Gate/Stock custody exceptions. An exception qualifies as a request only when an actual authorized case exists in that domain.

**Buttons:** Route to the authoritative source reviewer. A generic Request Center `Approve/Reject` endpoint must not bypass TIN verification, Stock clearance, policy approval, identity adoption, settlement evidence or RBAC checks. Track SLA due time and owner in a timezone-aware, independently audited manner.

## 4. Navigation, filters and exports

- Use one shared **authorized Market** context, and reset dependent Facility Level/Section, pagination and selection when Market changes.
- Preserve URL query filters, back/forward history, deep links and verified scope; stale previous-Market content must not be shown while another Market is loading.
- Paginate using **offset and stable sort**, not cursor (project-approved rule). Return server-side total matching count. Every row comes from actual filtered population.
- If a requested Unit Type/Market/financial filter cannot be supported, render an unavailable/reject state, **not silently unfiltered data**.
- Card count = exact corresponding filter-result count (for same grain/as-of). Export should include all authorized matching rows, not only currently visible page.
- On bulk selection across pages, preserve current filters and recheck server-side eligibility at execution.
- Display `asOf`, `definitionVersion`, `partial`, `held`, `unverified`, `unavailable` states. Do not display missing data as zero.

## 5. Financial reconciliation

For invoice cohort `C` at time `t`:

```text
eligible_billed(C) = sum(issued approved invoice liability within C)
verified_allocations(C,t) = sum(confirmed eligible allocations attributed to C)
eligible_unpaid(C,t) = eligible_billed(C) - verified_allocations(C,t) - valid documented adjustments
```

Do not equate received payments to applied allocations; the dates and accounting basis can differ. Do not count pending/held/foreign-Market/foreign-currency source, unconfirmed attempts, or imported historical "paid-through" metadata as verified rent cash. Credit consumption must honor exact Market+currency+confirmed source and concurrency safeguards. VAT/URA/EFRIS/PRN issuer and municipal revenue authority assumptions must be explicitly approved before any certification status.

**Invoice aging**: Decide invoice due-time, timezone and calendar convention. Clearly label exclusive `1-30`, `31-60`, `61-90`, `90+` bands separately from cumulative `30+`, `60+`, `90+` cohorts. Existing frontend reports already use cumulative semantics in some views; keep those names intact unless new contracts are established.

**Facility revenue**: Attribute issued invoices/allocations to the canonical physical Facility at the relevant financial date, and identify multiple Contracts or tenant changes without double counting. A Contract monthly rate is **not** actual collections.

## 6. RBAC and ownership

| Role | Permitted high-level views | Required safeguards |
|---|---|---|
| SuperAdmin | All authorized admin scope; optional Global or specific Market | Permission checks for mutation, approval, override and export |
| MarketMaster | Assigned Market only | Reject foreign Market and unresolved Market context server-side; no SuperAdmin MarketMaster governance |
| Read-only administrator | Authorized read/report paths | No approvals, invitations, merges, import execute or mutations |
| Vendor (pending) | My registration and rental application state | No Inventory/Payments/Invoices before approval and eligible Contract |
| Vendor (approved) | Own eligible Facilities, rent and business | Vendor ownership and Contract entitlement validated on every API |
| Supplier (pending) | Own profile and qualification | No trading, PO/settlement actions until eligible |
| Supplier (approved) | Own requisitions, bids, POs, verified deliveries | Supplier ownership and Market participation validated |
| Gate Staff | Assigned Gate operations and permitted token actions | Cannot perform Stock-only reconciliation or unrelated financial operations |
| Stock Counter | Assigned Stock reconciliation workflow | No Gate admission or arbitrary financial mutation |

Do not trust role-switching UI as an authorization mechanism; this is only a visual demo. The authoritative `req.authorization` effective permissions, Market scope and target authorization remain required.

## 7. P0/P1/P2 promotion gates

**P0 / truth and scope:** canonical IDs, accounting grain, Market scope, current vs historical basis, distinct case semantics, import/Facility reconciliation, status eligibility, no forbidden access.

**P1 / domain integrations:** Market intelligence, Supplier/PO/Delivery, Gate & Stock custody, workforce case assignment, synchronized filters, full-population CSV, authored empty/error/partial states.

**P2 / advanced decisions:** Supplier scorecards and minimum sample thresholds, forecasting, maintenance, vacancy opportunity, Vendor trading margin and other features requiring new evidence.

## 8. Testing requirements

- Exact-head frontend typecheck/unit/build and backend unit/integration checks on dedicated feature/test branches.
- Native PostgreSQL multi-session financial reconciliation and concurrency where applicable.
- Authenticated frontend → API → PostgreSQL browser journeys (SuperAdmin, MarketMaster, read-only, Vendor pending/active, Supplier pending/active, Gate Staff, Stock Counter).
- Market-switch stale-query denial, foreign Market payload denial, corrupted/unsupported filter refusal, deep-link/back-forward preservation.
- Card ↔ filtered rows ↔ export equality; individual and bulk pagination selection; financial as-of/period distinctions.
- Gate/Stock event ordering; Stock discrepancy review; Supplier Market eligibility; import identity preservation; rental TIN/Stock-clearance approval prerequisites.
- UAT in locally/manual controlled environment; do not add new workflow files merely for acceptance.

No live backend implementation is included in the ZIP. The online source repositories and protected branches were not modified.
