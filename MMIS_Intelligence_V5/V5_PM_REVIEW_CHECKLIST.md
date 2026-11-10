# V5 PM Review & Approval Checklist

## Visual design

- [ ] Preserve MMIS cream, green, warm-white cards and responsive typography.
- [ ] Approve 4 executive KPI labels and the priority order of Global Dashboard sections.
- [ ] Approve separate Request Center cases versus operational exceptions.
- [ ] Approve Market Intelligence, Gate/Stock Intelligence, and Import Integrity as dedicated areas.
- [ ] Approve the proposed Vendor and Facility 360-degree investigation drawers.
- [ ] Approve Supplier qualification/PO/Delivery/Stock/settlement stage distinction.
- [ ] Approve MarketMaster local-only view and SuperAdmin cross-Market access.
- [ ] Approve pending Vendor/Supplier screens without unauthorized business functions.
- [ ] Approve mobile navigation, filters, table horizontal scrolling and right-hand drawers.
- [ ] Confirm browser/local preview works from extracted `index.html` without external assets.

## Metric definitions

- [ ] Confirm canonical physical-unit and standalone legacy Stall counting conventions.
- [ ] Confirm Vendor account, KYC, assignment and Contract distinct populations.
- [ ] Confirm rent billed/applied/current-unpaid/overdue/held distinct measures.
- [ ] Confirm exclusive and cumulative aging bands and dates.
- [ ] Confirm whether Market-specific Supplier eligibility is approved or a proposed relationship.
- [ ] Confirm PO, Gate, Stock, tax and settlement evidence stage policy.
- [ ] Confirm unique Request Center case semantics, source adapters and SLA ownership.
- [ ] Confirm source and data-quality labels for partial/unavailable sections.

## Engineering sign-off required after visual approval

- [ ] Backend exact-head contracts for all promoted P0/P1 insights.
- [ ] Native PostgreSQL reconciliation and invoice cohort parity.
- [ ] RBAC and read-only server-side proof; approved Vendor/Supplier ownership gate.
- [ ] Market-scoped filtered list/export and pagination acceptance.
- [ ] Authenticated, end-to-end browser UAT on purpose-built branches.

**Approval boundary:** This ZIP is a fully interactive design prototype. PM signoff of V5 UI is not UAT or production acceptance of unimplemented backend intelligence.
