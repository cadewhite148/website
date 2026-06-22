# Personal academic website

Built with [Quarto](https://quarto.org), hosted on GitHub Pages.

## One-time setup

1. Install Quarto: https://quarto.org/docs/get-started/
2. Create a repo named `USERNAME.github.io` (replace USERNAME with your
   GitHub username) and push this project to it.
3. In the repo on GitHub: **Settings → Pages → Build and deployment →
   Source → GitHub Actions**.
4. Find-and-replace every `USERNAME`, `you@oregonstate.edu`, `[Last Name]`,
   and `TBD` placeholder across the project.

## Local preview

```bash
quarto preview
```

Live-reloads in your browser as you edit `.qmd` files.

## Deploy

Push to `main`. The GitHub Action in `.github/workflows/publish.yml` renders
and publishes automatically. First deploy takes a couple minutes.

## Add your files

Drop these into `papers/`:
- `cv.pdf`
- `jmp.pdf`
- `jmp-slides.pdf`

Replace `assets/headshot-placeholder.png` with a real headshot when ready
(keep the same filename, or update the path in `index.qmd`).

## Custom domain (optional, later)

Buy a domain, add a `CNAME` file containing the domain, and configure DNS.
Quarto + Pages handle the rest.

## Structure

```
_quarto.yml        site config, nav, theme
index.qmd          landing page
research.qmd       JMP + working papers
teaching.qmd       courses
cv.qmd             embedded CV
css/custom.scss    styling
assets/            images
papers/            PDFs (CV, JMP, slides)
```
