# MMIS Consolidated Intelligence, Design-System, Dashboard and RBAC Master Plan

**Version:** Consolidated 2026-11-10 (V5 approved prototype -> production-ready V6 implementation program)  
**Systems:** `oits-dhaka/MarketMasterERP` and `oits-dhaka/MarketMasterApi`  
**Status:** Read-only architecture research and proposed implementation; not an implemented, merged or production-validated feature  
**Reference scope:** The previous 14-source shadcn/TanStack review, the additional 15 user-provided sources, the current ERP source snapshot, and the V5 GUI / engineering contract.  
**Governance:** Never write directly to `dev`, `main`, `dev_basic` or `staging` in either MMIS repo. Work in purpose-built branches; no new GitHub Actions workflow files. Deployment must use a UAT-isolated runner/host and explicit server identity checks.

## 0. Executive decisions

1. **Do not replatform.** Retain React 18, Vite, TanStack Router, TanStack Query 5, TanStack Table 8, TanStack Form, Zod and MarketMasterApi. The shadcn/TanStack templates are component and information-architecture references only. No Next.js App Router / React 19 / TanStack Start / TanStack Table 9 migration in this program.
2. **Preserve the approved MMIS look.** `components.json` is `style: base-vega`, `rsc: false`; `style.css` defines cream and deep-green tokens, Fraunces / DM Sans, light/dark themes and reduced motion. Avoid replacing the entire theme from third-party generators or templates.
3. **Choose Base UI variants by default.** Select only compatible, license-vetted, accessible components from shadcn/ui, Studio Blocks, Shadcn UI Kit, Shadcn Studio and PaceUI. The source owner, component version and third-party dependencies must be recorded.
4. **Treat MMIS services as the source of truth.** Cards, charts, exports and filters never reconstruct payable or collectible financial balances from decorative UI arrays. Authorization is enforced by MarketMasterApi and the relevant domain service.
5. **Use one intelligence experience, not a parallel application.** KPI -> exact scoped records -> evidence -> permitted action. Canonical Vendor List, Shop/Facility management, Market Registry, Import Review, Supplier management, Gate/Stock and domain approval forms remain authoritative action destinations.
6. **Separate cases, tasks and operational exceptions.** The Request Center headline counts distinct actionable cases; operational exceptions have a separate queue and measure. Track request ownership and SLA only when domain evidence supports them.
7. **Accessibility and operational clarity override visual motion.** Reserve animation for non-essential, reduced-motion-safe feedback. No GSAP, animated counters, parallax, or autoplay around financial balances, government receipts, approval dialogs or Gate scanning.
8. **Licensing is a release gate.** Public MIT/Apache repo code may be incorporated with required attribution/notice, but websites may offer separately licensed premium bundles. Do not copy Pro/private source into public redistributable UI kits; examine precise item licenses.

## 1. Current verified compatibility baseline

| Technology | MMIS source snapshot | Risk when copying example code |
|---|---|---|
| React | `^18.3.1` | Newer starter templates often require React 19 |
| Routing | `@tanstack/react-router 1.170.19` | Next App Router and TanStack Start files are incompatible as-is |
| Server state | `@tanstack/react-query ^5.95.2` | Keep query keys Market/role/period-scoped; invalidate on context changes |
| Tables | `@tanstack/react-table ^8.21.3` | Studio Blocks / newer Arham table use Table 9 `useTable` and feature registry |
| Design primitives | `@base-ui/react ^1.4.0`; `shadcn ^4.2.0` | Avoid blindly mixing Base UI, Radix and React Aria variants |
| Styling | Tailwind 4; `base-vega` shadcn style | Template styles use `base-nova`/`aria-nova` and conflicting CSS variables |
| Forms and validation | TanStack Form; Zod 4 | Form libraries may assume React Hook Form or Zod 3 |
| Tooling | Vite 7; TypeScript 5.5; npm 11 | No framework or package-manager migration by default |

**Existing semantic colors:** `#f7f4eb` background, `#fffdf8` cards, `#263e32` foreground/primary, `#eeece2` muted, `#dcded0` borders. The ERP already includes `@media (prefers-reduced-motion: reduce)`. Retain these unless PM approves a documented contrast-preserving token change.

## 2. New source evaluation (15 supplied resources)

| Source | Verified characteristics | Adopt/avoid | MMIS target |
|---|---|---|---|
| [`bundui/shadcnadmin-free-nextjs-dashboard-template`](https://github.com/bundui/shadcnadmin-free-nextjs-dashboard-template) | Public repository presently empty: no README or package.json to review | **Do not use as code source** | Refer instead to the `bundui/shadcn-ui-kit` free dashboard or the separate `bundui/shadcn-admin-dashboard-free` repository, after checking its revision |
| [`bundui/shadcn-ui-kit`](https://github.com/bundui/shadcn-ui-kit) | Free MIT repository with 527 free components across 49 categories, dashboard, data table, forms and registry; project uses React 19 / Next 16, but TanStack Table 8 | **P0/P1 selective** | Dense filter/toolbars, review dialogs, evidence drawers, pagination, empty states, tables |
| [`bundui/components`](https://github.com/bundui/components) | MIT, Tailwind + Motion, shadcn-compatible copy/paste blocks | **P2 optional** | Restrained loading, expandable information, rare non-essential polish |
| [`shadcnstudio` org repositories](https://github.com/orgs/shadcnstudio/repositories?type=all) | `shadcn-studio`, free AdminCN, TanStack dashboard demo, table/form examples, theme guides and others | **P1 selective** | Base UI component styling, AdminCN table/form/role page patterns, TanStack patterns; don't treat examples as implemented MMIS RBAC |
| [`paceui.com`](https://paceui.com/) | Commercial/free blocks and templates; marketing claims Next.js and TanStack Start support | **P1 visual reference** | Chart pacing, dashboard composition, compact cards; verify specific item access/licensing |
| [`paceui/shadcn-nextjs-free-dashboard`](https://github.com/paceui/shadcn-nextjs-free-dashboard) | MIT, Next 16/React 19; free sales and logs dashboards, responsive sidebar | **P1 visual selective** | Technical operations/health views, error-rate and processing dashboards, compact sidebar layout |
| [`paceui/gsap`](https://github.com/paceui/gsap) | MIT animation library showcasing GSAP interactions | **Not for core workflows** | Optional onboarding/public marketing transitions only after reduced-motion/performance gate |
| [`arhamkhnz/awesome-shadcn-ui`](https://github.com/arhamkhnz/awesome-shadcn-ui) | Curated directory, not an application template | **Discovery only** | Candidate sourcing with security/license review; not a dependency |
| [`paceui.com/templates/ai-saas-template`](https://paceui.com/templates/ai-saas-template) | Linked product page could not be verified directly; related PaceUI AI SaaS preview emphasizes support-agent UX | **Design reference only** | Future support-ticket summaries, staff-assist drafts, human review; no unsupervised approval or fiscal action |
| [`shadcnstudio.com`](https://shadcnstudio.com/) | Free and paid components/blocks, Base UI/Radix options, design-theme/registry tools | **P1 selective** | Evidence drawers, charts, responsive form layouts, UI tokens; paid license and redistribution restrictions apply |
| [`jnsahaj/tweakcn`](https://github.com/jnsahaj/tweakcn) | Apache-2.0 visual shadcn theme editor | **Design-time only** | Contrast-tested theme experiments; do not wholesale replace MMIS tokens |
| [`ui-layouts/ui-tools`](https://github.com/ui-layouts/ui-tools) | Shadow, background pattern, SVG, gradient tools; license not confirmed from standard root filenames | **Low priority** | Design-time illustrations/background treatment, not dense dashboards |
| [`DarkInventor/easy-ui`](https://github.com/DarkInventor/easy-ui) | MIT visual web templates, legacy Next/React/Tailwind versions | **Low priority** | Public/marketing or onboarding page inspiration; do not transplant app shell |
| [`ibelick/motion-primitives`](https://github.com/ibelick/motion-primitives) | MIT Motion/Tailwind components, repository states beta | **P2 controlled pilot** | Non-critical success states, skeleton transitions; no motion for authorization decisions |
| [`uidotdev/usehooks`](https://github.com/uidotdev/usehooks) | MIT, React >=18, hooks including debounce, media query, click-away, measure, copy | **Selective utility** | Use only where current custom hooks/React Query/Router are insufficient; never use browser local storage as auth truth |

**Precise license distinction:** The checked MIT licenses belong to the specified public repositories. Premium Shadcn Studio / Shadcn UI Kit / PaceUI offerings have their own license terms and may forbid redistributing their components as a competing UI kit or publishing paid source publicly. Keep a source attribution manifest with license and pinned revision for each imported component.

## 3. Consolidated source stack (previous + new)

**Foundational**: official `shadcn-ui/ui`, official shadcn installation/theming docs, existing MMIS `base-vega` style and in-house authorization/navigation, TanStack Router/Query/Table 8 APIs.

**Best source of discrete components**: Studio Blocks (but port Table 9 examples), BundUI Shadcn UI Kit free Base UI variants, Shadcn Studio free Base UI components, official shadcn examples.

**Best layout / feature ownership references**: Arham TanStack Studio Admin (not TanStack Start migration), Arham Next Colocation Template (concept not Next-specific files), Shadcn Studio AdminCN, PaceUI free dashboard.

**Design-time and future-only**: tweakcn for token exploration, shadcn registries for internal distribution, `cn` for a measured optional class-merge experiment, motion-primitives/GSAP/UI Tools for non-critical interactions, curated awesome list for discovery. Exclude archived taxonomy production patterns and empty repositories.

**Decision:** Start with **MMIS + official shadcn Base UI + BundUI Kit/Studio Blocks/Studio Admin targeted patterns**. Do not install entire template repositories, a second router, a new authentication solution, or an unreviewed component registry.

## 4. Target reference architecture

```text
MarketMasterERP (React 18 + Vite + TanStack Router)
  AppShell
    persistent authenticated header, notifications, account, Market scope
    role-aware sidebar, permission-gated search, breadcrumbs, context/help
  Design system
    components/ui/                 existing shadcn Base Vega + Base UI
    components/intelligence/       MetricCard, Comparison, ChartPanel, Worklist
    components/evidence/           EvidenceDrawer, AuditTimeline, SourceStatus
    components/requests/           RequestSummary, Assignment/SLA, CaseDetail
    lib/intelligence/              MetricDefinition registry, reporting specs
    lib/permissions/               server-verified capabilities display/guards
    lib/filtering/                 URL contract, validated Market/period/filter
  Domain pages
    global, markets, vendors, facilities, suppliers, staff,
    gate-stock, imports, requests, financial/fiscal,
    vendor-business, supplier-business, Gate Staff and Stock Counter
  Typed gateway/query adapters
    Market/role/as-of scoped caching, fetch/cancel/invalidation
    offset pagination, server-side filter validation, export parity
MarketMasterApi
  authorization and Market isolation, source domain services
  read-only aggregate APIs, immutable evidence links and audit
PostgreSQL / approved government/payment integration evidence
```

**Every card:** `metricId`, `version`, `title`, `unit`, `grain`, `timeBasis`, `scope`, `dataMaturity`, `aggregation`, `eligibleStatuses`, `evidenceSource`, `filterSchema`, `drilldown`, `refreshAsOf`, `allowedActions`. No chart should invent or silently fill missing values.

**Report contract:** return `scope`, `asOf`, `definitionVersion`, `reportingBasis`, `currency`, `summary`, `breakdowns`, `filtersApplied`, `dataQuality`, `unavailableSections`, stable detail-filter token or validated URL filters, and export descriptor. Use `null`+"Unavailable" rather than fabricated zero when source coverage is missing.

## 5. Shared UX/page contract

- Header remains authenticated even when logged-in user opens publicly searchable Shop listings. Notification/account/logout controls stay persistent.
- Four headline KPIs maximum as first-row anchors. Requests Awaiting Action goes beside Markets, verified collections and overdue rent.
- Put **Requests Needing Attention** directly after KPI row; **Operational Exceptions** is a separate panel.
- All workspace pages share Market selector (subject to role), time basis/as-of indicator, evidence status, period control only when metric dates are compatible, filter chips, save view when authorized, accessible table and full filtered export.
- Three-step investigation: KPI/chart slice -> exact Market/role-scoped worklist (offset pagination, stable ordering) -> 360-degree detail/evidence/authorized action.
- Preserve distinct Market, Unit Type, Level/Section, Vendor/Supplier, policy period, aging, source and approval filters in typed route search params. Do not silently drop unsupported filters on navigation.
- Mobile: responsive sidebar/drawer, stacked cards, keyboard-operable charts/tables, focus management; avoid horizontal page overflow; tables may scroll within their own container.
- Default to no data animation for money/requests/risks; reserve subtle hover/focus and skeleton behavior. Respect reduced motion.

## 6. Workspaces and domain-specific intelligence

| Workspace | First-row KPIs | Main sections / authoritative drill-down |
|---|---|---|
| **Global Operations** | Active Markets, verified rent collected, overdue rent, distinct pending cases | Request board, exceptions, Market comparison, health by domain -> canonical operational records |
| **Market Registry & Intelligence** | Active Markets, rentable physical units, recorded occupied units, Markets without staffed management | Market/Level/Section composition, government-revenue context (not issuer proof), Market financial performance, staffing, Supply coverage |
| **Vendor Overview** | Registered Vendors, eligible active tenant Vendors, overdue tenant Vendors, verified overdue amount | Onboarding/KYC, import provenance, Facility/Contract gap, billing and credit, aging, recovery -> Vendor List/Contract/Invoice |
| **Facility Intelligence** | Physical units, recorded occupied, units with active Contracts, integrity exceptions | Shop/Stall/Pitch/Cage/Lock-up matrix, occupancy/assignment vs Contract gap, billed/applied/outstanding by Unit Type; avoid double count companion Stalls |
| **Supplier Overview** | Active qualified Suppliers, KYC pending, approved open POs, late verified delivery commitments | Classification, Market participation vs registration, bids, PO, OTIF, quality, Gate/Stock, payable/settlement -> Supplier/PO/Receipt |
| **Gate & Stock** | Open tokens, Stock reconciliation due, custody exceptions, completed tokens | QR/token lifecycle, custody, variance, VAT/PRN evidence distinct, Gate Staff vs Stock Counter role worklist |
| **Vendor Import Integrity** | Staged records, requiring review, eligible for promotion, successfully consolidated | Batch provenance, duplicate/identity/facility conflicts, reviewed promotion, verification, existing-record preservation |
| **Staff & MarketMaster** | Active assigned staff, Market coverage, open assigned cases, overdue assignments | MarketMaster directory, invitation state, read-only/denies, staffing gaps, ownership/SLA, audit |
| **Request Center** | Distinct pending cases, past-due cases, assigned-to-me, unassigned | Cases by KYC/onboarding/rental/Contract/support/etc.; separate operational exception queue; source-specific reviewer handoff |
| **Vendor Business** | Approved tenancy, rent due, eligible invoices, stock readiness | Pending Vendor sees only onboarding/Shop finder/applications/Contract steps; post-entitlement features gated per Facility |
| **Supplier Business** | Qualification status, eligible bids, open POs, receipt/settlement stage | Pending Supplier setup; active Supplier owns bids/PO/delivery only; no cross-supplier leakage |
| **RBAC Governance** | Users by role, unassigned Markets, expiring restrictions, permission conflicts | Effective permission inspector, assignment history, role & Market matrix, read-only, audit; not an invitation to build a parallel auth system |

### Requests and approval safety

Distinct `CASE`, `TASK` and `EXCEPTION` entity types must not be summed as a single case count. Rental application approval retains TIN and Stock-clearance preconditions; onboarding and identity promotion retain proof review; financial reconciliation actions revalidate eligible evidence and scoped permissions. Source-domain controls remain responsible for mutation; Request Center issues review links/allowed actions but cannot bypass them. Support tickets must have a routed UI destination matching backend links.

### Financial and reporting integrity

- Approved Contract obligation != issued invoice != confirmed receipt != invoice allocation != unpaid liability.
- Vendor credit and advance application is Market+currency+confirmed-source isolated and concurrency protected; no double spending across overlapping invoices.
- Government rent beneficiary, MDA/URA PRN, EFRIS issuer, VAT and fiscal evidence are distinct with separate statuses, approved legal mappings and sandbox/production boundaries.
- Supplier bid != accepted PO != goods receipt != approved invoice != settled payable.
- Aging buckets are explicitly exclusive (1-30/31-60/61-90/90+) or cumulative (30+/60+/90+); never blend.
- Global Market scope cannot leak to MarketMaster, and Supplier Market eligibility cannot be inferred from global registration alone.

## 7. RBAC and entitlement matrix

| Persona | Read scope | Allowed UI experiences | Explicit deny examples |
|---|---|---|---|
| SuperAdmin | All authorized Markets or selected Market | Executive reports, global requests, authorized administration | No implied government issuer/fiscal privileges |
| MarketMaster | Assigned Market | Market's operations, Vendor/Facility/Staff/requests | No foreign Market or global user governance |
| Read-only Admin | Authorized reporting scope | Analytics, source evidence and permitted exports | No approval, sending, imports, edits, bulk changes |
| Pending Vendor | Own registration and public listings | Onboarding, rental application, KYC, Contract status | Inventory, invoice/payment business panels without eligible active tenancy |
| Approved/active Vendor | Own authorized Contract-bound units | Rent/own invoices, stock, requisitions, notifications | Unrelated unit or another Vendor's records |
| Pending Supplier | Own account/qualification | KYC, capability, status and required documents | Bidding, delivery and settlement before authorization |
| Approved Supplier | Own authorized transactions | Requisitions, bids, accepted POs, deliveries and payment evidence | Another Supplier's records or foreign Market |
| Gate Staff | Assigned Gate/Market | Entry/token capture, shift queue | Stock-only reconciliation and settlement |
| Stock Counter | Assigned Market stock workflow | Receiving/verification/custody queue | Gate entry authorization, privileged fiscal actions |

Use `effectivePermissions`, explicit denies, Market assignment and resource relationship, not bare role names, for permission decisions. Frontend can hide/disable, but backend must check every API and bulk/export action. Revalidate assigned Market, current user status, entitlement and source facts at execution time. Record authorized denial explanations without exposing protected data.

## 8. Sequenced delivery plan and gates

| Wave | Priority | Deliverables | Non-negotiable exit gate |
|---|---|---|---|
| **0. Baseline and license** | P0 | Exact `dev_basic` reads/working branch, V5 visual baseline, component inventory, React/Base UI/Table compatibility, per-item license BOM | No branch-protection breach; no unlicensed source; verified tests/build at source head |
| **1. Design shell** | P0 | Theme tokens, normalized shell/sidebar/header, persistent user account, scoped Market switcher, load/error/empty/partial visual states | Authenticated public-Shop header, role+read-only navigation, 320-1920px accessibility |
| **2. Intelligence kernel** | P0 | MetricDefinition registry, report envelope, ScopeBar, MetricCard, ChartPanel, EvidenceDrawer, server offset Worklist, ExportDescriptor | Card=count/list/export exact parity; stale Market data cleared; no mixed time bases |
| **3. Vendor/Facility finance** | P0 | Tenant/physical unit KPIs, Unit Type rent matrix, Contract, billing, collection/aging and advances | Native PostgreSQL integration, confirmed source/credit concurrency, no double count |
| **4. Request Center + RBAC** | P0 | Case adapter model, request/exception separation, own-vs-Market queues, permission matrix/inspector and source-specific actions | Unique cases, authorization denials, true approval prerequisites, audit |
| **5. Markets, Imports, Staff** | P1 | Market Registry analytics, import quality/promotion review, staff/MarketMaster accountability | Exact Market scope, provenance and safe promotion; no unauthorized state transitions |
| **6. Supplier/Gate/Stock** | P1 | Sourcing-to-receipt chain, Supplier scorecards, custody/quantity variance, role-specific queues | PO->Gate->Stock evidence, partial delivery, 3-way match and fiscal states separated |
| **7. Role dashboards and UX** | P1 | Vendor/Supplier pending vs active, Gate Staff/Stock Counter queues, saved views, responsive/keyboard/RTL where needed | Authenticated end-to-end browser UAT; export parity; role isolation |
| **8. Registry + measured enhancements** | P2 | Optional private component registry, measured `cn` test, restrained animations, forecast pilots | Stable components, license/security/a11y approvals, real measured bundle/runtime gains |

### Work packages / proposed implementation tickets

- `DS-01` Component compatibility and source-license inventory (Base Vega, React 18, Table 8, primitive selection).
- `DS-02` MMIS shell/header/sidebar, Market selector, notifications, saved appearance; persistent authenticated public Shop header.
- `DS-03` Accessible reusable KPI, chart, empty/loading/partial, evidence UI primitives.
- `INT-01` Typed MetricDefinition registry and report envelopes with time basis, provenance and quality state.
- `INT-02` Validated scope/URL filter and server-offset Worklist; filter-preserving full CSV/XLSX.
- `INT-03` Vendor/Facility rent financial and physical-unit reconciliation with aging and credits.
- `REQ-01` Request source adapters: registration, KYC, rental, Contract, ticket, import, eligible reconciliation.
- `REQ-02` Request Center SLA/owner routing, distinct case counts, domain-action handoffs and audit.
- `AUTH-01` Effective-capability/RBAC inspector and backend-authenticated test matrix.
- `MARK-01` Market registry portfolio/capacity/readiness intelligence.
- `IMP-01` Import batch quality/review/promotion provenance and safe preservation.
- `STA-01` Staff and MarketMaster workforce/coverage and action workload.
- `SUP-01` Supplier qualification, purchase commitments, delivery evidence and scorecard.
- `GATE-01` Token/Gate/Stock custody evidence, variance, fiscal-status separation.
- `OWN-01` Pending vs active Vendor/Supplier and Gate/Stock role dashboards.
- `UIREG-01` Optional versioned internal MMIS registry with attribution manifest.

**Definition of done for every ticket:** exact head, route/component source, permission contract, Zod query DTO, backend count/detail/export parity, empty/partial/denied states, a11y/keyboard/mobile, correct Market behavior, native PG where financial or operational truth requires it, screenshot/visual comparison, deployment isolation and manual UAT evidence.

## 9. Quality gates and non-goals

- **Security:** server-side authorization, forbidden deep links, read-only mutation denial, Market switching, explicit denies, supplier/vendor resource ownership, export privacy and injection-safe CSV.
- **Financial:** multi-session credit concurrency, Market/currency isolation, payments/source allocation, rent invoice aging, fiscal evidence and error states. No payment simulation accepted as end-to-end evidence.
- **Workflow:** reviewed import promotion, approved tenancy activation, rental TIN/Stock clearance, PO-to-Gate/Stock and receiving differences, support ticket navigation.
- **UI:** no app-wide horizontal overflow (320/375/390/768/1024/1440/1920px), accessible contrast, focus restoration, reduced motion, keyboard-only operation, no flaky animation required for user understanding.
- **Performance:** representative 10k+ row filtering on backend, offset pagination, sensible chart downsampling, stable query keys, bounded payload sizes, response time budgets decided with engineering (do not invent measured latencies).
- **Source/security:** dependency vulnerability scan and license provenance for copied components; avoid accidental default routes or conflicting shadcn components; no template example API secrets, mock roles or fake production data.
- **Deployment:** dedicated UAT runner/host labels and host-identity validation; no cross-environment UAT/prod runner shared-selection risk; don't add workflow files; do not modify protected branches.

**Non-goals:** wholesale Next.js/TanStack Start migration; full theme replacement; generic third-party RBAC code as authority; AI-generated approvals or settlement; decorative animations on financial records; automatic promotion of unverified imports; unbounded dashboard KPI proliferation; public redistribution of private/premium component libraries.

## 10. Source verification and limits

The publicly accessible source code/README/license/package metadata was inspected for all listed new GitHub repos where available. The user-supplied BundUI empty repo is not an adoptable code source. PaceUI's exact AI SaaS product URL was not directly retrievable, so AI capabilities noted here are design ideas, not verified functionality of the paid download. Shadcn Studio and BundUI Pro claims and terms come from vendor websites; use current purchased-license text before any copy. This review did **not** run or benchmark third-party packages inside the live MMIS application. The plan is therefore a proposed integration and validation program, not a tested compatibility certification.

## Appendix A. Previous 14-source detailed plan (retained)

The following originally approved 14-source architecture and contract-level plan is retained as the detailed foundation. Where its wording differs from sections 0-10 above, the consolidated decisions and expanded source/compatibility gates above take precedence.

---
# MMIS Enterprise Intelligence, Design System, Dashboard & RBAC Implementation Plan

**Date:** 10 November 2026  
**Scope:** `oits-dhaka/MarketMasterERP`, `oits-dhaka/MarketMasterApi`, previously approved MMIS V5 Intelligence Suite  
**Status:** Architecture and implementation proposal, not live application changes or production acceptance.  
**Repository governance:** Never modify `dev`, `main`, `dev_basic`, or `staging` directly in either application repo. Use a separate purpose-built branch and manually/local acceptance; do not add workflow files.

## 1. Decision record

**Decision: modular adoption, no wholesale framework migration.** Retain the MarketMasterERP React/Vite/TanStack Router/TanStack Query application and the existing MarketMasterApi authority. Port selected, reviewed shadcn/studio components into the existing Base UI design-system family. Use the MMIS V5 prototype as visual specification, not as production code or financial evidence.

**Verified ERP `dev_basic` baseline:** React `^18.3.1`; Vite `^7.3.0`; TanStack Router `1.170.19`; TanStack Query `^5.95.2`; TanStack Table `^8.21.3`; Tailwind CSS `^4.2.2`; Base UI `^1.4.0`; `shadcn ^4.2.0`; TanStack Form `^1.28.6`; Zod `^4.3.6`. `components.json`: `style: base-vega`, `rsc: false`, Tailwind CSS variables enabled; frontend theme in `style.css` already has cream/dark-green semantic light and dark tokens, Fraunces/DM Sans local font references, accessible reduced-motion handling. These are source snapshots; do not assume dependencies have been upgraded without checking exact branch heads.

**Reference compatibility warning:** Recent Arham templates use React 19 and TanStack Table 9, while Next variants use Next.js 16 and may depend on server components. Copying their application shells, auth flows, routing, table hooks, or generated component style definitions directly is not safe. The TanStack reference is TanStack **Start**, not just the Router plugin already used in MMIS. Base UI version also differs. Port *patterns or reviewed individual components*, not the entire template.

## 2. Source-by-source assessment

| Source | Verified contents | Value to MMIS | Adoption decision |
|---|---|---|---|
| `arhamkhnz/studio-blocks` | Installable KPI, chart, list, navigation/sidebar, table, form blocks; source included, MIT | Strongest discrete card/worklist/charts prototypes | **High / selective port**; replace sample data, inspect dependencies |
| `arhamkhnz/next-shadcn-admin-dashboard` | Next 16 Studio Admin, many domain dashboard views, sidebar/header, search, layout controls, forms | Visual page patterns / dashboard layout and admin oversight | **High visual reference, low direct code reuse** |
| `arhamkhnz/next-colocation-template` | Next App Router route-local components, hooks and schema organization | Feature-ownership model in large codebase | **High architecture reference**; adapt to TanStack route conventions |
| `arhamkhnz/next-shadcn-admin-dashboard-baseui` | Next Admin with `base-nova` shadcn styling | Closer primitive family; modal/menu/dialog behavior | **High reference / compatibility bridge**; map to MMIS `base-vega` |
| `arhamkhnz/next-shadcn-admin-dashboard-aria` | React Aria, `aria-nova`, different primitive APIs | Accessibility ideas, keyboard/focus patterns | **Selective reference only**; don't mix primitives by default |
| `arhamkhnz/tanstack-shadcn-admin-dashboard` | TanStack Start dashboard, file-based routes, cards, admin navigation, tables | Closest router/composition pattern to MMIS | **Highest architecture reference**, not a Start migration |
| `arhamkhnz/web-resources` | Curated visual inspiration, typography/effects/design utilities | Optional brand research | **Low runtime relevance**; avoid decoration-heavy UX |
| `shadcn-ui/ui` | Main source/official components, dashboard example, tasks/data tables, charts, sidebar | Core semantic accessible components | **Foundational**; use MMIS-compatible Base UI variants |
| `shadcn-ui/registry-template` | `registry.json` item files, `shadcn build`, static JSON artifacts | Reusable internal design-system distribution | **High when components stabilize** |
| `shadcn-ui/alpine-registry` | Namespaced registry, design-system tokens, composite blocks, auth example | Multi-team internal component registry and theme governance | **High later-stage inspiration**; isolate build-time access from runtime RBAC |
| `shadcn-ui/taxonomy` | Archived Next.js 13 early App Router experiment; repository explicitly warns outdated | Historical IA/architectural inspiration | **Do not transplant** for production |
| `shadcn-ui/cn` | Alternative Tailwind 4 class join/merge engine and migration tools | Potential build/runtime micro-optimization | **P2 experiment**; benchmark on MMIS, don't preemptively migrate |
| `ui.shadcn.com/docs` | Official open-code components, Vite, data table, chart, sidebar and registry docs | Primary implementation instructions | **Required reference** |
| `ui.shadcn.com/docs/theming` | Semantic CSS-variable-based theming | Map V5 to MMIS tokens and accessible dark mode | **Required reference** |

**Vendor-level caveat:** The Arham README states RBAC with configuration-driven UI and multi-tenancy are **planned**, not certified implemented security. Their Users/Roles pages must not be assumed to enforce backend permission checks.

## 3. Target layered architecture

1. **AppShell / UX**: persistent logged-in header (also when using public Shop finder), sidebar, command search, Market selector, notifications, accessibility, breadcrumbs, locale/currency.
2. **Design-system primitives**: existing shadcn Base Vega, Base UI controls, tokens, card, table, combobox, dialog, sheet, skeleton, chart wrapper.
3. **Shared intelligence widgets**: `MetricCard`, `MetricStrip`, `ChartPanel`, `ScopeBar`, `EvidenceBadge`, `DataQualityBanner`, `DrilldownLink`, `FilterableWorklist`, `EvidenceDrawer`, `RequestQueueTile`, `ExportMenu`.
4. **Route-local feature modules**: `features/intelligence/global`, `markets`, `vendors`, `facilities`, `suppliers`, `staff`, `imports`, `gate-stock`, `requests`, plus business-owner views; keep only truly reusable components in shared layer.
5. **Query/authorization adapters**: typed TanStack Query hooks, URL search validation, scoped query keys, permission-aware route metadata, server-issued allowed actions, active filters.
6. **API domain reports**: read-only summary/detail endpoints composed from existing canonical services; domain-owned approvals/changes remain under their original APIs.
7. **Evidence base**: PostgreSQL/MDA financial rules, invoice/allocations, RentContract status, imported identity review, Supplier PO/delivery, Gate/Stock events, request cases and immutable audit events.

Suggested non-disruptive directory organization (adapt to current repo root convention, rather than physically moving all existing routes):

```text
components/ui/                    # existing Base Vega shadcn primitives
components/intelligence/          # shared approved KPI, chart, table, evidence views
lib/intelligence/                 # metric definitions, money/date/scoping, filter contracts
lib/navigation/                   # existing navigation policy, extended via permission metadata
gateway/intelligence/             # typed API contract and query hooks
features/intelligence/markets/    # route-local charts/tables, tests
features/intelligence/vendors/
features/intelligence/facilities/
features/intelligence/suppliers/
features/intelligence/requests/
features/intelligence/gate-stock/
features/intelligence/imports/
features/intelligence/staff/
routes/_protected/_app/...        # keep existing TanStack Router paths and guards
```

## 4. Design tokens and navigation

**Keep approved palette and fonts**. Current `style.css` already supplies light tokens: background `#f7f4eb`, primary/foreground `#263e32`, card `#fffdf8`, muted `#eeece2`, border `#dcded0`, chart tokens, and a separate dark token set. Fraunces is used for headings, DM Sans for body. Use semantic tokens (`bg-background`, `bg-card`, `text-foreground`, `text-muted-foreground`, `border-border`), not hard-coded colors for individual imported blocks.

**Sidebar groups**: Overview, Intelligence (Vendor/Facility/Supplier/Market), Operations (Market Registry, Vendors, Shops, Imports, Gate & Stock, Staff), Finance (Invoices, Payments, Reconciliation, URA/EFRIS evidence), Requests & Support, Administration (MarketMasters, RBAC, settings). Role- and Market-appropriate links only. Keep existing route names; do not let a template change primary URLs.

**Header**: Market selector + context / reporting period; notification bell; accountable user name and account menu; no Sign In button for an authenticated user when navigating to public Shop finder. Read-only badge only where meaningful. Sticky header and responsive navigation, keyboard search, focus restoration, reduced motion, accessible mobile drawers.

**Typography/density**: Four headline KPI cards (desktop; mobile two-column where feasible), one urgent-work section, progressive charts and a canonical worklist. Use KPI units, descriptions, as-of timestamps, and source-status labels; no animated fake data.

## 5. Dashboard and domain specification

### 5.1 Global Operations

Top cards: active Markets, verified rent collections, eligible unpaid/overdue rent, distinct Requests Awaiting Action. Below: Requests Needing Attention (onboarding, KYC, rental applications, Contract approvals, support, qualifying reconciliation cases), Operational Exceptions (separate), Market performance, Vendor/Facility/Supplier/Staff/Gate/Import health. Drill-down each card to precise backend-filtered records; don't equate the existing `attention.total` aggregation with distinct requests.

### 5.2 Market Intelligence

Portfolio totals/status by Market type; physical unit capacity; Level/Section occupancy; MarketMaster/Gate staffing coverage; contracted vs invoiced vs applied rent; Market readiness by explainable dimensions; Market comparison table. Registry is authoritative action destination; don't infer government beneficiary from Market ownership label.

### 5.3 Vendor Overview

Registration/identity/KYC/onboarding funnel; staged import provenance; unassigned Facility; Contract awaiting approval/acceptance; rent billing, confirmed allocation, held sources, unpaid, aging (exclusive vs cumulative), future coverage and receivable recovery. On click navigate to the current Vendor List/Contract/Invoice report with the exact filters, not a duplicated sample table. Vendor360 evidence drawer shows physical units, Contracts, policy dates, invoices, allocation, permitted actions.

### 5.4 Facility Intelligence

Canonical Shop-backed physical unit population, five Unit Types, separate historical standalone Stalls, recorded occupancy, assignment/active-contract gap, listing availability, Contract renewal; Unit Type rent matrix (expected, billed, confirmed allocations, unpaid, overdue Vendor count) with exact Vendor+Facility+invoice drill-down. Physical occupancy is not asserted unless inspection evidence is available.

### 5.5 Supplier Intelligence

Registered/qualified Suppliers (global registry basis); approved Market eligibility separate from actual participation; requisitions/bids/award, approved PO commitments, dispatched/received goods, Gate and Stock custody, OTIF with denominator/sample, invoice/settlement. Supplier360 timeline must preserve accepted bid != PO != delivered != Stock-verified != paid.

### 5.6 Staff/MarketMaster Intelligence

SuperAdmin global MarketMaster assignment, uncovered Markets, effective read-only exceptions, denied capabilities, invitation backlog, staff coverage and assigned case workload. MarketMaster only assigned-Market Gate/Stock staff and cases. Permissions panel must use real authorization metadata, not template dummy roles.

### 5.7 Gate/Stock Intelligence

Gate token stage, time in state, arrival/verification/custody, variance, Stock pending/reconciled, approved VAT evidence; incident queues, double/posting discrepancies; Gate Staff vs Stock Counter role restrictions. Navigate to existing `/gate-control` tabs/details rather than rebuilding the terminal.

### 5.8 Import Integrity

Batch status/staged records, validation failures, duplicate identity resolution, field decisions, ready-to-promote count, successfully consolidated count, existing-record adoption, reporting-period data and reconciliation evidence. Never treat staged records as live Vendors; keep selective and filter-scope execution safeguards.

### 5.9 Request Center

Backend-owned typed adapters: Vendor registration, KYC, rental application, Facility claim, RentContract approval, support ticket, true payment-review case, import review, Gate/Stock exception case. Separate **requests**, **review tasks**, and **operational exceptions**. A `caseId` is unique and stable; category counts sum only if mutually exclusive. Each item exposes allowed actions and links to authoritative domain review; generic approval must not bypass TIN verification, Stock clearance, payments or role restrictions.

### 5.10 Role-specific business dashboards

Pending Vendor: own onboarding, KYC, rental applications, Shop search and tenancy acceptance only; no inventory/payment/invoice prematurely. Approved Vendor: authorized Contract-owned units, due invoices, payments, stock and requisitions. Pending Supplier: KYC/profile only. Approved Supplier: own requisitions, bids, accepted POs and delivery/settlement evidence. Gate Staff: entry processing queue. Stock Counter: receiving/reconciliation queue. Read-only admin: data and authorized export only, no mutations.

## 6. Shared component contracts

### Proposed `MetricDefinition`

```ts
type MetricDefinition = {
  id: string; title: string;
  grain: 'VENDOR' | 'FACILITY' | 'INVOICE' | 'CASE' | 'PO' | 'TOKEN' | 'MARKET';
  source: string; definitionVersion: string;
  timeBasis: 'CURRENT_SNAPSHOT' | 'BILLING_PERIOD' | 'PAYMENT_EVENT' | 'DUE_DATE';
  aggregation: 'COUNT_DISTINCT' | 'SUM_ELIGIBLE' | 'RATIO';
  eligibleStatuses: string[];
  breakdowns: string[];
  drilldownRoute: string;
  capability?: string;
  dataMaturity: 'VERIFIED' | 'PARTIAL' | 'PROPOSED';
};
```

This is a proposed metadata shape; implement with the current TypeScript/Zod approach. Never compute authoritative finance in a visual component.

### Proposed report envelope

```ts
type IntelligenceResponse<T> = {
  scope: { type: 'GLOBAL' | 'MARKET'; marketId: string | null };
  asOf: string;
  definitionVersion: string;
  reportingBasis: string;
  currencyCode: string | null;
  partial: boolean;
  unavailableSections: string[];
  filtersApplied: Record<string, unknown>;
  summary: T;
  dataQuality: 'VERIFIED' | 'HELD' | 'PARTIAL' | 'UNAVAILABLE';
};
```

Counts and details must share a repeatable-read or equivalent reconciled snapshot where accuracy demands. Use null/unavailable, not zero, when evidence cannot be established.

### Drill-down rule

`KPI card -> validated URL filter -> server-scoped offset-paginated list -> evidence/details -> authorized domain action`. Persist selected Market, Unit Type, Level/Section, period, status, owner, as-of where supported; reset dependent filters on Market change. If a filter cannot be supported by a destination, reject or explicitly flag it; never silently show broader data. Provide a stable secondary sort, backend total, page bounds recovery, and export for the **entire matching authorized population**.

## 7. RBAC and ABAC/tenancy controls

Effective access is the intersection of role permissions, effective authorization grants/denials, assigned Market, record ownership, approved tenancy or Supplier qualification, operation type, and read-only/mutation restrictions. Server enforces target authorization and continues to enforce domain prerequisites.

| Persona | Read scope | Actions / restrictions |
|---|---|---|
| SuperAdmin | Authorized global/all Market or selected Market | Admin capabilities only when granted; no implied fiscal authority |
| MarketMaster | Assigned Market | No foreign Market or SuperAdmin MarketMaster governance |
| Read-only Admin | Authorized reports | No review/approval/invitation/import execute/bulk mutation |
| Pending Vendor | Own onboarding/Shop search/applications | No Inventory/Payments/Invoices absent required approval+Contract entitlement |
| Active Vendor | Own qualifying units/contracts/transactions | Recheck entitlement per request; no others' accounts |
| Pending Supplier | Own KYC/profile | No bidding/fulfillment/settlement until qualified |
| Active Supplier | Own eligible bids/POs/deliveries | Market participation and source ownership checked |
| Gate Staff | Authorized Market Gate and token flow | No Stock-only reconciliation |
| Stock Counter | Authorized stock/reconciliation flow | No Gate admission or arbitrary fiscal/payment action |

**RBAC panel** should include: role catalogue (view), permission matrix, effective permission explanation, Market assignments, explicit denies/read-only expiry, audit trail, pending invitations, and permission-diff preview. Any role mutation requires dual review/strong authorization as applicable; no ability to grant self privileges by editing frontend config.

## 8. Source-truth and financial gates

- Physical Facility counts exclude companion/default Stalls, separately disclose historical standalone Stalls; Vendor counts use distinct Vendor ID per defined grain.
- Active Vendor != active tenancy; Contract monthly rate != billed amount; billed != confirmed receipt; receipt != eligible invoice allocation; held/imported paid-through metadata != verified cash.
- Rent balance is invoice-based, reconciled with source payment eligibility and documented credits/adjustments; Market+currency isolation, confirmed payment-source budget, transactional concurrency safeguards must remain intact.
- Aging uses defined timezone/due date; exclusive 1–30, 31–60, 61–90, 90+ separate from cumulative 30+/60+/90+.
- Revenue beneficiary, MDA, URA/EFRIS/PRN issuer and VAT status must use approved legal/fiscal evidence; no invented fiscal compliance certification.
- Supplier bid != accepted PO != goods receipt != approved payable != settlement. Record proven event stages separately.
- KYC, documents and support-ticket records are sensitive. Limit exposed fields, sanitize CSV, avoid raw identifiers in URLs, audit privileged exports.

## 9. Adoption phases with deliverables and exit gates

| Stage | Priority | Deliverable | Exit gate |
|---|---|---|---|
| 0: baseline + compatibility audit | P0 | Exact frontend/backend commits, V5 screenshot parity, inventory package/primitive/Tailwind/Table compat, capture component licenses and third-party dependencies | No protected-branch writes; build/test baseline captured |
| 1: design tokens + AppShell | P0 | MMIS Base Vega component wrappers, header/nav/Market selector, accessible mobile/sidebar, correct authenticated public header | Role/Market navigation, focus, responsive, no broken public header |
| 2: intelligence kernel | P0 | MetricDefinition registry, typed API envelope, scope bar, partial/held states, MetricCard, FilterableWorklist, EvidenceDrawer | Card->list->export exact count/value; stale data denied on Market change |
| 3: Vendor + Facility | P0 | Vendor Overview, Facility Intelligence, rent/aging matrix, canonical physical/tenancy/financial drill-down | Native PG reconciliation and exact Vendor/Facility populations |
| 4: Request Center + RBAC | P0 | Unified cases, true distinct pending count, linked authoritative domain reviewers, role-specific queues, staff permission views | TIN/Stock preconditions, ownership, read-only and cross-Market tests |
| 5: Market + Import + Staff | P1 | Market readiness, import integrity, assignment and workload analysis | Correct provenance, scoped counts, no destructive import bypass |
| 6: Supplier + Gate/Stock | P1 | Qualification/PO/delivery, token/custody, Stock exceptions, verified settlement states | PO->receipt chain, role-specific Gate and Stock actions |
| 7: Role business dashboards + UI hardening | P1 | Active/pending Vendor/Supplier, Gate Staff/Stock Counter, saved views, print/export/accessibility | Authenticated role journeys, device/mobile UAT |
| 8: internal registry + optimization | P2 | Versioned MMIS UI registry, conventions, optional `cn` benchmark, selected forecasts and scoring | License/security review, a11y regression, real bundle/latency improvement |

No new GitHub Actions workflows: run manual/local CI-equivalent scripts, disposable PostgreSQL, browser/UAT and exact-head acceptance. Preserve purpose-built integration branches, create PRs for review; never write to `dev`, `main`, `dev_basic`, or `staging` directly.

## 10. Exact-head acceptance checklist

**Build and component tests:** typecheck/build, accessible keyboard roles/focus/aria, light/dark, RTL where needed, 320/375/390/768/1024/1440px, reduced motion, desktop/mobile, no JS error, CSS compatibility; role-context fetch on mount.

**Identity/authorization:** unauthenticated/pending/active/restricted/read-only; global vs assigned Market; forbidden deep link, malformed scope, cross-Market ID, stale query response, role-switch demo not treated as authentication, action permission rechecked server-side.

**Data truth:** exact card/list/export count and sum; distinct Vendor and canonical Facility counting; active Contract rights; date-policy selection; confirmed rent allocations, credits, held/reversed transactions, native PG multi-session race tests; aging boundary and timezone fixtures.

**Operational workflows:** public Shop finder persistent authenticated header, KYC/onboarding, applicant rental TIN/Stock clearance approvals, Supplier eligibility and PO/receipt chain, import review and adoption, Gate handover/Stock reconciliation, support ticket URLs and case audit trails.

**Operations:** real selected-Market switching, request ownership/SLA, notifications and retry behavior, load/empty/partial/offline views, full filtered export, all selected rows across offset pages, safe stale-cache invalidation, manual UAT and screenshot diffs against V5.

## 11. Implementation tickets (recommended sequence)

- `DS-01`: Base Vega component compatibility audit; tokens; brand/contrast; local typography.
- `DS-02`: AppShell header, notifications, Market selector, nav/search, user account persistence across public Shop browsing.
- `INT-01`: Metric registry + reporting envelope + financial basis/data-quality declarations.
- `INT-02`: Scoped URL filters, server-driven offset pagination, canonical export and evidence drill-down.
- `INT-03`: Vendor/Facility reconciliation contract, Unit Type rent performance, aging boundaries.
- `RC-01`: Request source-adapter inventory and case identity/status mapping.
- `RC-02`: Request Center backend count/detail with domain reviewer handoffs, SLA and ownership.
- `AUTH-01`: Effective permission and Market-scope capability map for UI; RBAC overview; read-only exceptions.
- `MI-01`: Market portfolio and readiness;
- `IMP-01`: Vendor import batch/stage/exception reporting with preservation checks.
- `STAFF-01`: MarketMaster/staff staffing coverage, case assignment, restrictions.
- `SUP-01`: Supplier eligibility, PO, delivery, Gate receipt and settlement stage reporting.
- `GATE-01`: Token/custody/Stock reconciliation worklists and source-linked exceptions.
- `OWN-01`: Vendor/Supplier active/pending business dashboards and Gate/Stock role queues.
- `REG-01`: Optional internal registry with versioned components, tests, license/lockfile and upgrade procedures.

Every ticket requires linked source service, route, Zod DTO, correct Market scope, loading/error/partial behavior, accessibility QA, role test set and visual acceptance screenshot.

## 12. Risk ledger / explicit non-goals

| Risk | Control |
|---|---|
| React 18 -> React 19 incompatibility | No blanket dependency updates; port compatible source, focused tests |
| TanStack Table 8 -> 9 API break | Adapt patterns, not `useTable`/feature registry from v9 |
| `base-vega` vs `base-nova`/`aria-nova` | Keep existing primitives; inspect imports and accessibility per block |
| Next App Router/TanStack Start assumptions | Do not copy route, server action, SSR or auth code |
| Theme style leakage | Semantic CSS variables, explicit tokens, dark/contrast checks |
| Role screen spoofing | Server-side effective auth+target Market/ownership; frontend only reflects it |
| Request total double count | Case identity model and separate request/task/exception populations |
| Financial misstatement | Invoice/report source truth, held status, source allocations, snapshot basis |
| Insecure public registry | Build-time access only, token/secret handling; never embed tenant data in component assets |
| Unverified use of examples | All sample figures visibly labeled until real data and UAT acceptance |
| Deployment isolation | Use manually verified environment/runner labels and destination before UAT deployment; no assumption any self-hosted runner is UAT |

## 13. Links and sources reviewed

- https://github.com/arhamkhnz/studio-blocks
- https://github.com/arhamkhnz/next-shadcn-admin-dashboard
- https://github.com/arhamkhnz/next-colocation-template
- https://github.com/arhamkhnz/next-shadcn-admin-dashboard-baseui
- https://github.com/arhamkhnz/next-shadcn-admin-dashboard-aria
- https://github.com/arhamkhnz/tanstack-shadcn-admin-dashboard
- https://github.com/arhamkhnz/web-resources
- https://github.com/shadcn-ui/ui
- https://github.com/shadcn-ui/registry-template
- https://github.com/shadcn-ui/alpine-registry
- https://github.com/shadcn-ui/taxonomy
- https://github.com/shadcn-ui/cn
- https://ui.shadcn.com/docs
- https://ui.shadcn.com/docs/theming
- https://ui.shadcn.com/docs/registry
- https://ui.shadcn.com/docs/components/data-table
- https://ui.shadcn.com/docs/components/chart
- https://ui.shadcn.com/docs/installation/vite
- MMIS source reviewed via GitHub connector at `dev_basic`: `package.json`, `components.json`, `style.css`, `components/dashboard/AdminOperationsDashboard.tsx`, `lib/utils.ts`; plus previously inspected Vendor/Facility/Supplier/Gate/Staff/Import/authorization services.
- MMIS V5 prototype handoff: `MMIS_Intelligence_Suite_V5/V5_ENGINEERING_CONTRACT.md` and `V5_SOURCE_MAPPING.md`.

**End verdict:** Build one design system and one evidence-backed intelligence layer on the existing MMIS platform. Use Studio Blocks and Studio Admin for curated, tested presentation patterns, shadcn for primitives and distribution, and original MMIS services as the sole source of permissions and financial/operational truth.
