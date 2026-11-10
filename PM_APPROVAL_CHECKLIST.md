# MMIS V6 — PM Design Approval Checklist

This checklist is for **product design and interaction signoff**, not a merge, production deployment, finance policy, or security acceptance.

### Executive Dashboard and Requests

- [ ] Four headline KPIs and position of **Requests Awaiting Action** are approved.
- [ ] Request Center distinguishes unique submitted cases from review tasks and operational exceptions.
- [ ] Onboarding, rental, KYC, reconciliation, support, RentContract, import and Gate/Stock case groups are appropriately labeled.
- [ ] Case count, category count, filtered list and CSV semantics match a single source population.
- [ ] Pending requests highlight ownership, aging and priority without inventing regulatory SLAs.

### Vendor / Facility / Rental

- [ ] Registered Vendor ≠ approved business ≠ assigned Facility ≠ active accepted RentContract is clear.
- [ ] Pending Vendor first-login dashboard hides operational inventory, payment and invoice modules.
- [ ] Logged-in public Shop Finder persists notification, account identity and logout controls.
- [ ] Facility matrix distinguishes registered physical units, recorded occupancy, contracts, distinct Vendors, invoice liability and verified allocations.
- [ ] Companion/default Stalls are excluded from separate physical-unit counts.
- [ ] Unit Type × 61–90-day overdue → affected Vendor / invoice drill-down is intelligible and accurately labeled as exclusive aging.
- [ ] Rental Readiness is demonstrably read-only, with selected-invoice generation disabled pending Finance and API approval.

### Supplier / Gate / Import / Staff

- [ ] Global Supplier registration and Market-granted eligibility are separate.
- [ ] Supplier bid/PO/delivery/Gate/Stock receipt/AP settlement transitions are unambiguous.
- [ ] Import record staging and review do not imply canonical Vendor promotion or verified cash.
- [ ] Gate Staff vs Stock Counter and MarketMaster role-specific access is understandable.
- [ ] RBAC matrix displays effective access, explicit denies and target Market/ownership principles.

### Design System and Release

- [ ] MMIS cream/deep green appearance retained, with Base Vega and Base UI compatibility.
- [ ] Desktop/mobile workspaces, tables, density, responsive header and drawer interactions are approved.
- [ ] External design patterns are selectively adapted; no React/Next/TanStack framework migration authorized.
- [ ] Motion kept out of financial, approval and Gate interactions; reduced-motion behavior accepted.
- [ ] PM approval explicitly does not certify backend data APIs, actual authorization, Finance or database acceptance.

**Decision record:** Use the interactive `PM Approval` workspace to export the completed local approval selection and freeform comments as JSON. Record unresolved points in the exported comments.

### Additional V6.1 functional acceptance

- [ ] Facility Contract-gap card **13** opens **13** matching Facility records; Import attention **12** opens **12** blocked/review-needed rows.
- [ ] Exclusive 61–90 invoice aging counts **11** distinct Vendors; combined Shop+61–90 yields **3** matching Vendors and UGX 447,000 matching eligible invoice liability in demo.
- [ ] Guest selection and authenticated public Shop Finder preserve selected Shop and account controls; a Vendor can submit and track the sample application.
- [ ] Admin KYC/TIN/Stock checks cannot be skipped, onboarding/rental/Contract approvals are separate, and only intended Vendor acceptance completes the demo journey.
- [ ] Rental preflight exposes first-liability day, effective policy version, existing-period invoice conflict, reason codes and never-post/Finance HOLD.
- [ ] Request assignment, review/evidence timeline, status transitions and local notifications are understandable and permission-aware.
- [ ] Supplier qualification, award, PO, acknowledgment, dispatch, Gate, 95/100 Stock verification and receipt preserve custody and settlement HOLD.
- [ ] Back/Forward/deep link restore Market+filters and RBAC denial explanations are visible.
- [ ] PM understands these are **simulated, in-memory transitions** and do not approve live MMIS functionality or financial posting.

**Verification:** `FIXES_ACCEPTANCE_REPORT.md` and the QA JSON evidence are the authoritative correction-specific handoff.
