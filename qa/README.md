# Repeat V6.1 offline browser acceptance

Requirements: Python 3 with `playwright`, an installed Chromium browser at `/usr/bin/chromium` (adjust `executable_path` if your OS differs). No internet/API/backend connection is required after dependencies exist. For Windows, replace the hardcoded Chromium executable with your Playwright-managed browser path.

Run from extracted package:

```
python qa/browser_smoke_playwright.py
python qa/browser_matrix_playwright.py
python qa/test_v6_1_functional.py
python qa/test_v6_1_extra.py
```

Outputs are written to the extracted package's `qa/` and root QA result JSON files. The acceptance scripts inspect identical self-contained HTML via `page.set_content` because the test sandbox blocks navigating to local `file://` URLs. A PM can open `index.html` directly in Chrome/Edge.

Synthetic sample values and due dates are fixed as of 2026-11-10, and must not be interpreted as real service SLAs or financial obligations.
