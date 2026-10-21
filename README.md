# Finora

Personal finance web app. Open `index.html` in a browser to run it (no install needed).

- `index.html` is the built, self-contained app.
- `src/` holds the editable sources: `style.css`, `core.js` (data, maths, screenshot parser), `views.js` (screens), `app.js` (events), `logo.svg`.
- Rebuild after editing: `python3 build.py`

Notes
- Accounts and records are stored in the browser (localStorage) only.
- Screenshot reading uses Tesseract.js loaded from a CDN. If it can't load, the review form opens empty for manual entry. For production, replace `runOCR()` in `src/core.js` with a server-side OCR/vision call.
- "Try the demo" loads example data.
