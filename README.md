# Academic Website — Md Rayhanul Masud

This is a Jekyll site configured for GitHub Pages.

## Quick Deploy (GitHub Pages, user site)

1. Create a **public** repository named **`mrayhanulmasud.github.io`** on GitHub.
   - If your GitHub username is different, use `<USERNAME>.github.io` and update `url:` in `_config.yml`.
2. On your machine:
   ```bash
   git clone https://github.com/<USERNAME>/<USERNAME>.github.io
   cd <USERNAME>.github.io
   # copy all files from this folder into the repo (or unzip directly here)
   git add .
   git commit -m "Initial academic site"
   git push origin main
   ```
3. GitHub Pages will auto-build. Visit: `https://<USERNAME>.github.io` (first build may take ~1–2 minutes).

### Optional: Preview locally

```bash
# Requires Ruby
gem install bundler jekyll
bundle init
echo 'gem "jekyll"' >> Gemfile
bundle install
bundle exec jekyll serve --livereload
# Open http://127.0.0.1:4000
```

## Editing

- **News:** `_data/news.yml` (sorted newest → oldest automatically).
- **Publications:** `_data/publications.yml`
  - For **first-author** papers, include `first_author: true` and add `code_url:` and `poster_url:` where applicable.
- **Blog posts:** add Markdown files under `_posts/` with names like `YYYY-MM-DD-title.md`.
- **About/Home:** edit `index.md`.
- **Contact links:** update `_config.yml`.

## Structure

```
.
├── _config.yml
├── _data
│   ├── news.yml
│   └── publications.yml
├── _includes
│   └── publication.html
├── _posts
│   ├── 2025-08-17-hello-academic-web.md
│   └── 2025-08-17-repo-similarity-note.md
├── assets
│   └── css
│       └── custom.css
├── index.md
├── publications.md
├── news.md
├── blog.md
└── contact.md
```