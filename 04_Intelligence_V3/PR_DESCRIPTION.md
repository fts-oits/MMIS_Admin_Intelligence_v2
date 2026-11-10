## Summary

Enhances all existing MMIS intelligence prototype pages while retaining visual theming and historic screenshots. Adds an additive role-aware v3 intelligence overlay for seven page views, a searchable/filterable 179-group KPI library, and evidence/drill-down documentation.

## Scope

- Global Operations: cross-domain decision signals and Market scope/certification.
- Vendor: onboarding and tenancy; invoice-backed overdue rent, credits and source evidence.
- Facility: physical-unit integrity, Unit Type rent and Shop 61–90-day Vendor drilldown.
- Supplier: bids→PO→delivery→Gate→Stock→invoice→settlement lifecycle and OTIF evidence.
- Staff & Managers: assigned-Market vs cross-Market coverage and permission boundaries.
- Vendor/Supplier business: operating insight cards with pending-account gating.
- 179 intelligence groups V01–V45, F01–F41, S01–S57, searchable by domain/priority/maturity.
- PM and engineering contracts, CSV export of **KPI definitions only** (not financial exports).

## Compatibility and safety

- In-place enhancement; no replacement of prior dashboards, unchanged theme colors/typography.
- No backend requests, transaction actions, notifications, new workflows, migrations or protected branch edits.
- Example data remains clearly labeled and non-authoritative.
- Does not represent completed backend financial intelligence or certification.

## Validation checklist

- [ ] HTML loads locally and in GitHub Pages/static hosting.
- [ ] Search/priority/maturity and domain filters return expected KPI definitions.
- [ ] Seven pages display v3 enhancements and preserve existing role/account gating.
- [ ] Shop 61–90 drillthrough opens Vendor context.
- [ ] CSV downloads KPI *definitions* only.
- [ ] Screenshots checked at mobile/desktop widths.
- [ ] No page-wide overflow or script errors.
- [ ] PM signs off visualization/labels separately from backend acceptance.

## Follow-up engineering

See `04_Intelligence_V3/IMPLEMENTATION_GUIDE.md`. Source-backed KPIs, permission-safe exports, approved notification preview/dispatch, and authenticated FE→BE→PostgreSQL integration require separate implementation and acceptance.
