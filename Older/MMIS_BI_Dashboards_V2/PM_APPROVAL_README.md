# MMIS Extended Intelligence — Product Manager Visual Approval

**Prepared:** November 9, 2026  
**Status:** UI/UX proposal for review; no application, GitHub, Linear, or production changes.  
**Design baseline:** Current MarketMasterERP `style.css` color tokens and DM Sans styling.

## 1. Contents

- `MMIS_Expanded_Intelligence_Interactive_Prototype.html`: interactive four-page, role-aware prototype (works offline in Chrome/Edge).
- Desktop and mobile PNG screenshots of Admin Supplier Overview, Staff & Managers, Vendor Business Insights, Supplier Business Insights, and pending-account states.
- The consolidated ZIP adds the **previous** three-page designs: Global Operations Dashboard, Vendor Overview, and Facility Intelligence.

All names, figures, periods, account statuses, and records in prototypes are fictional.

## 2. Prototype interactions

1. Open HTML locally in Chrome/Edge.
2. Select one of four pages with the page selector or sidebar.
3. In Admin pages, switch SuperAdmin / MarketMaster. SuperAdmin may select a Market or global portfolio; MarketMaster is locked to their assigned Market (simulation).
4. In Vendor and Supplier business pages, switch Approved / Awaiting approval to confirm entitlement gating.
5. In Admin Supplier Overview click a KYC, readiness or order KPI to filter the sample Supplier list; search sample Supplier rows.
6. In Staff & Managers Overview click coverage/status cards to filter staff rows. MarketMaster must not be shown cross-Market manager coverage or the SuperAdmin management roster.
7. In Supplier Business Insights search the sample accepted-order table.
8. Click Export, record link or Refresh to see a descriptive prototype-only action preview. No real export, payment, contact or notification is issued.
9. Review screenshots at desktop and mobile widths. Wide tables scroll within their own container.

## 3. Existing application source findings (read-only)

| Page | Verified current route/component | Present data / constraints | Proposed extension |
|---|---|---|---|
| Admin Supplier Overview | `/suppliers/overview`, `components/supplier/SupplierOverview.tsx` | `total`, `active`, `pendingKyc`, `verifiedKyc` | Market grants/readiness, PO worklist, supplier delivery performance, approval queue |
| Admin Staff Overview | `/staff/overview`, `components/staff/StaffOverview.tsx` | `totalAssigned`, `activeCount`, `totalMarkets`, `unassignedMarkets` for Gate staff | Manager coverage and permissions, staffing/shift gaps if backend evidence exists |
| SuperAdmin Market Managers | `/users/marketmasters`; `/staff/marketmasters` redirects | SuperAdmin-only manager list and lifecycle | Linked management coverage summaries; not exposed to MarketMaster |
| Vendor Business Dashboard | `/dashboard` renders `FacilityJourney` and `VendorPaymentsOverview` for Vendors | Rent invoices, payment attempts, onboarding; Inventory and requisitions routes exist | Unified rent + Shop + inventory + purchasing; sales/profit only with verified sales/cost sources |
| Supplier Portal | `/dashboard` currently redirects Suppliers to `/requisitions`; `/supplier-fulfillment` exists | Published requisitions, accepted bids, Supplier deliveries | Optional `/supplier/insights` route with bid pipeline, gate-received performance and settlement when validated |

**Backend limitations that must remain visible to PM:** Current Supplier overview has no actor/Market-scoped financial or order analytics contract. Supplier performance and Market eligibility require authoritative grant/PO/delivery evidence. Staff shift coverage is not established by account status alone. Vendor sales/margin cannot be inferred from inventory or rent payments. Supplier settled/paid amounts cannot be inferred from accepted bids.

## 4. Role-specific page ownership

| Persona | Main decisions | Headlines | Secondary information and worklists |
|---|---|---|---|
| SuperAdmin — Supplier Overview | Who is verified, approved for a Market, and delivering on commitments? | Registered Suppliers; KYC requiring review; Market-ready Suppliers (proposed); Orders requiring attention (proposed) | Approval progress, grants, Supplier list, PO/delivery exceptions |
| SuperAdmin — Staff & Managers | Which Markets lack managers/staff and whose access needs review? | Markets with manager; missing manager; active Gate staff; assignment exceptions | Market-manager roster, Gate staff, audit/access history |
| MarketMaster — Staff & Managers | Is this Market properly staffed and are assignments safe? | Active Gate staff; gaps; assigned staff; access needing review | Own-Market staff table, local assignment queue; NO global manager roster |
| Vendor — My Business | What rent must I pay, what stock is low, which supply requests need action? | Rent to pay; next due; low-stock products; open requisitions | Invoice/payment evidence, inventory alerts, purchase requests; sales/margins only when supported |
| Supplier — My Supply Business | Which requisitions can I bid on, what did I win, and which deliveries need attention? | Open requests; accepted bids; deliveries needing action; pending settlement (proposed) | Awarded bids, dispatch tasks, receiving/fulfillment, verified financial settlement |

## 5. Non-negotiable access rules

- All views are **role- and owner-scoped on the backend**, not only hidden in frontend.
- MarketMaster does not inherit SuperAdmin Market comparison or MarketMaster-management privileges.
- Vendor account with unapproved onboarding / no active eligible Facility–RentContract does not see inventory, rent-payment, invoice, or revenue management UI. Keep public Shop discovery accessible to authenticated users, with logged-in header and no guest Sign In button.
- Supplier pending KYC or Market eligibility sees only explicitly permitted pre-approval steps, not other Suppliers' bids or private Vendor requests.
- Active Vendor financial figures are strictly their own Vendor+Market+RentContract+Invoice evidence.
- Accepted Supplier bids are not payments, delivered goods, or settled amounts; only independent confirmed evidence can certify each stage.
- Exported information and notifications must match server-authorized filtered cohorts and applicable data-protection policy.

## 6. PM review checklist

- [ ] **Admin Supplier Overview:** approves simple labels, four headline metrics, readiness funnel, action queue and Supplier worklist.
- [ ] **SuperAdmin Staff & Managers:** approves cross-Market coverage and manager ownership boundaries.
- [ ] **MarketMaster Staff:** approves own-Market staff/worklist only; confirms no manager-lifecycle leakage.
- [ ] **Vendor Business Insights:** approves onboarding-pending state and active rental/stock/procurement layout; sales/margin clearly future.
- [ ] **Supplier Business Insights:** approves sourcing/bidding/accepted delivery journey; no presumed settlements.
- [ ] **MMIS theme:** same primary, background, cards, muted, warning, borders, font, navigation and responsive style.
- [ ] **Responsive:** desktop and mobile layouts; focus, labels, filter wrapping, and horizontally scrollable tables.
- [ ] **Cross-page consistency:** Admin Global summary links to domain pages, but does not duplicate their entire detailed analyses.
- [ ] **Metrics:** approve definitions, evidence requirements and ownership before building new APIs.
- [ ] **Release gates:** UI approval does not authorize database migrations, PO/credit changes, payments, exports or notification dispatch.

## 7. Recommended engineering slices

1. **Frontend read-only UX foundation:** common insight header, metrics, action queue, filters, detail table, source notes, responsive components; adapt existing admin Supplier/Staff overviews.
2. **Backend scope/eligibility:** Supplier Market grant and role authorization; staff manager coverage and owner scoping; versioned contracts and cache keys.
3. **Supplier procurement evidence:** reconcile requisition → bid → accepted PO → dispatch → Gate/Stock accepted delivery; never derive on-time delivery from dispatch alone.
4. **Vendor Business Metrics:** reuse verified rent/payment and inventory data; introduce sales and margins only after validated transaction and cost contracts.
5. **Supplier Business Metrics:** accepted bid and delivery read models; settlement only on separate payment evidence.
6. **Authenticated acceptance:** SuperAdmin and MarketMaster scope, Vendor/Supplier pending and active states, cross-Market denial, 320/375/768/1280/1440px, 200%/400% zoom, empty/partial/stale data, user-owned filter/export parity.

## 8. Suggested PM signoff message

> Attached are the next four MarketMaster intelligence designs: Admin Supplier Overview, Admin Market Staff & Managers Overview (SuperAdmin/MarketMaster), Vendor Business Insights, and Supplier Business Insights. The package also includes the previously reviewed Global Operations, Vendor Overview and Facility Intelligence prototypes. Please inspect the interactive HTML, switch roles and business onboarding states, and review desktop/mobile screenshots. Approve the **visual hierarchy, labels, navigation and role-specific visibility** or return comments by page and section. Metrics marked Proposed need separate backend source/financial approval before implementation. No code or financial changes are authorized by a visual approval.

**Repositories:** `oits-dhaka/MarketMasterApi` and `oits-dhaka/MarketMasterERP`. Do not modify `dev`, `main`, `dev_basic`, or `staging` directly. No new workflow files; local/manual exact-head UAT.
