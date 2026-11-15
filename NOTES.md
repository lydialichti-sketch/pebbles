# How this repo fits together

- `claude-version.html` is the source of the app. It is also published as a Claude artifact, where it syncs through Claude.
- `index.html` is the web app for GitHub Pages. Build it from the source with `python3 build-web.py` after any change, and commit both files.
- Icons and `manifest.webmanifest` make it work as a home-screen app. The `?v=2` tags in index.html force phones to reload the icon; bump them if the icon changes.
- Outside Claude, data lives in each person's browser (localStorage key `pebbles-data`). Settings → Move my data copies it out and brings it in.
