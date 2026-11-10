# MMIS Intelligence v3 — PM design approval checklist

**Review date:** 2026-11-10  
**Reviewer:** __________  
**Decision:** ☐ Approved ☐ Approved with changes ☐ Changes requested

## UI and information architecture

- [ ] Preserve MMIS cream/forest-green colors, DM Sans typography, card spacing and accessible navigation.
- [ ] Four headline KPIs per dashboard; other groups use progressive disclosure and detail panels.
- [ ] Global, Vendor, Facility, Supplier, Staff, Vendor Business and Supplier Business are distinctly purposeful pages.
- [ ] Labels are operationally clear: "Rent billed", "Payments applied", "Rent still unpaid", "Verified overdue rent", "Amounts needing review".
- [ ] Shared date/Market/Unit Type/status filter context and explicit report freshness/quality are visible.
- [ ] Mobile and desktop layouts retain readable tables and operable controls.

## Vendor & Facility

- [ ] Shop/Stall/Pitch/Cage/Lock-up counts and assigned-Vendor counts are distinguished.
- [ ] Physical Shop/companion Stall double counting is excluded by definition.
- [ ] Facility/Contract mismatch and missing Contract exceptions are visible on both pages.
- [ ] Shop→61–90 overdue→matching Vendor records→invoice evidence is supported conceptually in both directions.
- [ ] Onboarding approvals are different from Facility assignment and Contract activation.
- [ ] Financial periods distinguish expected/billed/received/applied/unpaid/held evidence.

## Supplier & staff

- [ ] Supplier qualification, bid, PO, Gate, Stock, invoice and settlement states are separate.
- [ ] OTIF, lead times, price and quality comparison reveal underlying event requirements and sample sizes.
- [ ] Supplier Market coverage is not inferred from global registration.
- [ ] MarketMaster only has assigned-Market staffing/manager access; SuperAdmin may compare Markets.

## Vendor and Supplier business

- [ ] Pending Vendor hides inventory, financial and invoice business controls until authorized tenancy activation.
- [ ] Pending Supplier hides approved-order, fulfillment and financial controls.
- [ ] Sales and margins remain future-only without verified POS/COGS evidence.

## Drill-down, exports and actions

- [ ] Full 179 intelligence groups V01–V45/F01–F41/S01–S57 can be searched/filtered in the library.
- [ ] Every selected KPI exposes a sensible record population, source basis, priority and business drill-down.
- [ ] Production CSV/XLSX and notifications are explicitly gated on backend authorization and authoritative filters.
- [ ] `P0 / P1 / P2` and `Foundation / New aggregation / Proposed capability` distinguish maturity.

**Notes / requested adjustments:**

________________________________________________________________________

**PM sign-off:** _____________________  **Date:** _____________________
