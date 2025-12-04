# Jovnat — Local Preview

This is a small static landing page (HTML + CSS) for a bakery-style project. The repository contains:

- `index.html` — main page
- `style.css` — styles
- `images/` — local SVG placeholder images used by the page
- `serve.ps1` — PowerShell script to preview the site locally

How to preview (PowerShell):

```powershell
Set-Location 'c:\Users\dehoo\Desktop\PROJECTS\jovnat'
# If you have Python installed
python -m http.server 8000
# or use the included serve script
./serve.ps1
```

Open http://localhost:8000 in your browser.

Replace the placeholder `images/*.svg` files with your real optimized WebP/JPG images and update the `<picture>` elements in `index.html` if you want to provide multiple source formats.
