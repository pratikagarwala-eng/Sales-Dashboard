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

## Running it

The dashboard fetches the sheet client-side via Google's CSV endpoint, which only
allows cross-origin reads from an `http(s)` origin — so it must be served over HTTP,
not opened as a `file://` double-click.

```bash
python3 serve.py
```

Then open <http://127.0.0.1:8777/dashboard.html>.

## Files

| File | Purpose |
|------|---------|
| `dashboard.html` | The dashboard (self-contained; all logic inline). |
| `serve.py` | Tiny static file server on port 8777. |
| `chart.min.js` | Chart.js (bundled locally). |

## Data source

Reads a public Google Sheet via the gviz CSV endpoint. The sheet ID is configured
at the top of the `<script>` in `dashboard.html` (`SHEET_ID`). The sheet must be
shared as "anyone with the link can view" for the browser to read it.
