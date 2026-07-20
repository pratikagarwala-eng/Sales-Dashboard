# Sales Dashboard

A live, self-refreshing sales dashboard that reads directly from a Google Sheet
(`deals`, `meetings`, `partners` tabs) and updates automatically every 60 seconds.

## Features

- **KPI cards** — open pipeline, closed won, win rate, avg won deal, total deals, meetings.
- **Deals by stage** — bar chart with a stage filter; each bar shows total amount **and** deal count.
- **Deals by AE India × stage** — table; each cell shows deal count and amount.
- **Deals by partner × stage** — table; each cell shows deal count and amount.
- **Stage filters** on every view (default: open pipeline only, i.e. stages 1–7).
- **Drill-down** — click any number cell to see the underlying deals; click a deal
  name to open it in Clarify in a new tab.

## Deployment (Vercel)

This is a pure static site — no build step. Vercel serves `index.html` at the
root. `vercel.json` disables framework detection and sets caching headers. Any
push to `main` auto-deploys.

The dashboard fetches the sheet client-side via Google's CSV endpoint, which
reflects CORS for `http(s)` origins — so it works on Vercel (https) out of the box.

## Running it locally

Google's CSV endpoint does not allow reads from a `file://` origin, so it must be
served over HTTP — don't just double-click the file.

```bash
python3 serve.py
```

Then open <http://127.0.0.1:8777/>.

## Files

| File | Purpose |
|------|---------|
| `index.html` | The dashboard (self-contained; all logic inline). |
| `chart.min.js` | Chart.js (bundled locally). |
| `vercel.json` | Static-hosting config for Vercel. |
| `serve.py` | Tiny static file server for local use (port 8777). |

## Data source

Reads a public Google Sheet via the gviz CSV endpoint. The sheet ID is configured
at the top of the `<script>` in `dashboard.html` (`SHEET_ID`). The sheet must be
shared as "anyone with the link can view" for the browser to read it.
