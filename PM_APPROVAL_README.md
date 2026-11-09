# MMIS Vendor Overview + Facility Intelligence -- PM Design Approval

**Version:** 1.0 (2026-11-09)
**Related Linear issue:** https://linear.app/oits-dhaka/issue/MMIS-893/fe-refine-insights-cards-and-responsive-dashboard-layouts
**Delivery:** Visual/UI approval package, not an implementation PR.

## How the PM reviews the exact mockup

1. Download and extract this ZIP.
2. Open `MMIS_Vendor_Facility_Interactive_Prototype.html` in Chrome, Edge or Firefox. No local server, login or external dependencies are required.
3. Switch between **Facility Intelligence** and **Vendor Overview** using the sidebar (or `Switch page` button on narrow screens).
4. Under Facility Intelligence, click the **Shop / 61-90 days Vendors / UGX** matrix cell, or click the **See Shops overdue 61-90 days** link. This opens Vendor Overview with `Shop` and `61-90 days` filters selected.
5. Inspect the Vendor list, Export preview, and Rent reminder preview. No real export, reminders or API requests are performed.
6. Resize the browser to approx. 390px wide (or inspect supplied mobile screenshots), and review readability of cards, filter controls, table overflow and actions.
7. Compare against the desktop/mobile screenshots included in this archive.

## Requested PM design decisions

- [ ] Approve the names and labels on all main cards and tables.
- [ ] Approve page ownership: Facility Intelligence owns the Unit Type and physical-asset matrix; Vendor Overview owns Vendor/tenancy, invoice aging and collections worklists.
- [ ] Approve the compact four-card KPI layout and removal of repeated full Facility Type cards from Vendor Overview.
- [ ] Approve the Unit Type rent table (units, assigned Vendors, rent billed, payments applied, unpaid rent, and age-based Vendor/UGX drill-down).
- [ ] Approve the 1-30 / 31-60 / 61-90 / over-90 aging interaction and matched Vendor drill-down.
- [ ] Approve Market/period/unit/aging filters, additional location/Contract filters, and bidirectional navigation.
- [ ] Approve the placement of CSV/XLSX export and administrator notification/reminder preview.
- [ ] Approve the shared Contract mismatch and financial-review notices across both pages.
- [ ] Approve desktop/mobile responsiveness and existing MMIS theme preservation.
- [ ] Record change requests clearly against screenshot/section names.

## What this preview is and is not

- The preview reflects the two coordinated designs presented in the ChatGPT discussion.
- Colors use the verified MarketMasterERP `style.css` light-theme tokens: `#f7f4eb` background, `#fffdf8` card, `#263e32` primary/foreground, `#eeece2` muted and `#dcded0` border; typography follows the current DM Sans / Arial stack.
- ALL Vendor names, Market choices, amounts, counts, statuses and discrepancy IDs are **illustrative sample data**.
- Changing a filter only demonstrates selected UI context and example-row availability; it does not recompute real financial results.
- The file does **not** implement or validate the backend financial attribution, API permission model, reconciliation, exports or notification dispatch.
- Approval of this design is separate from Finance approval of data definitions and from production deployment approval.

## Suggested PM approval response

"Reviewed the attached MMIS Vendor Overview and Facility Intelligence HTML prototype and four screenshots. I approve the overall page layout, labels, shared Market/Unit Type/aging filters, clickable Unit Type to Vendor investigation, issue visibility, responsive structure, and placement of CSV/XLSX export and reminder-preview controls, subject to the linked financial-contract/permission acceptance gates. Please implement on dedicated feature branches without changing protected branches or the existing MMIS theme. Any exceptions or requested design adjustments are listed below: ..."
