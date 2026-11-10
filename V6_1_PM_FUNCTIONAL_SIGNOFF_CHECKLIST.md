# MMIS V6.1 — PM Functional Demo Signoff

Use the extracted `index.html`. Mark each only after exercising the actual interaction, not from screenshots alone.

- [ ] **Global KPIs:** Clicking Facility Contract gap shows all 13 qualifying units; Import attention shows all 12 blocked/review-required staged records.
- [ ] **Finance parity:** Overdue invoice balance equals the filtered invoice population and downloaded CSV. Synthetic amount UGX 4,392,000; Finance posting remains disabled.
- [ ] **Shop × 61–90:** Vendor Overview shows 11 Vendors with any eligible 61–90-day unpaid invoice and exactly 3 with Shop-specific invoices; qualifying Shop amount UGX 447,000.
- [ ] **Market scope:** Filter Market to Kabale and confirm only authorized sample records; changing Market clears dependent filter state; Back/Forward preserves validated pages and filters.
- [ ] **Public Shop:** Open guest public finder, choose FAC-0003, click Apply and Sign in. Correct Facility remains selected; authenticated header shows notification/account controls rather than Sign In.
- [ ] **Rental application:** Pending Vendor can enter note, submit and track a case; KYC and account approval remain distinct from rental review and Contract acceptance.
- [ ] **Rental admin:** Reviewer cannot approve onboarding before KYC confirmation; cannot approve rental until both TIN and Stock clearance; cannot treat Contract approval as Vendor acceptance.
- [ ] **Contract acceptance:** Only applicant Pending Vendor can accept approved terms in the simulator. Business entitlement remains a preview until real backend validates.
- [ ] **Rental Readiness:** Select a Facility and period; verify first liable date, mock applicable policy, terms approval/acceptance evidence, duplicate invoice conflict, reason-coded preflight and unconditional Finance HOLD/no posting.
- [ ] **Request Center:** Due-at targets, assignment, request-more-info, escalation, timeline, source-action preview and notification inbox are usable; no generic financial/rental approval bypass.
- [ ] **Supplier custody:** Demonstrate qualification → bid → approved PO → Supplier ACK → dispatch → Gate admission → Stock verification (95/100) → receipt; confirm no settlement or fiscal posting.
- [ ] **RBAC:** Read-only Admin cannot assign cases; foreign Market permission inspector explains denial; Gate and Stock are separate capabilities; pending Vendor/Supplier cannot access unauthorized modules.
- [ ] **Browser QA:** Check desktop/mobile visual screenshots and zero script errors. All test scripts and fixture files run offline.
- [ ] **Approval boundary:** Confirm this signoff covers synthetic demo F0 interactions only; not live API, financial authority, UAT, PostgreSQL, government compliance, or full P1/P2 scope.

Suggested decision: **PM Functional Demo — GO / CONDITIONAL GO / HOLD** with typed comments, noting that only live engineering acceptance can authorize production release.
