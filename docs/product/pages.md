# Host the R2R animated explainer with GitHub Pages

**Current state:** This deployment workflow was prepared in [PR #2](https://github.com/kingwangking/r2r/pull/2). **No public GitHub Pages URL is claimed active** until GitHub confirms a completed deployment. The stable `v0.1.0` GitHub Release is unrelated to Pages and remains unchanged.

## What is actually published?

- **Single source of truth:** [`docs/product/landing.html`](landing.html), a self-contained HTML file with inline CSS/JS; no hosted build system, backend or external script needed.
- **GitHub Pages entry:** the [Pages Actions workflow](../../.github/workflows/pages.yml) copies that file to `_site/index.html` and deploys only from `main`.
- **PR preview:** the existing [candidate workflow](../../.github/workflows/skill-candidate.yml) uses Chrome to render desktop/mobile screenshots, checks JavaScript and exports a static site preview artifact. It **does not publish PR code** as a live site.
- **Production security:** `contents: read` for build; Pages deploy receives `pages: write` and `id-token: write`, with the `github-pages` environment and a single serialized deployment group.

## How to enable the real site

1. In [repository Settings → Pages](https://github.com/kingwangking/r2r/settings/pages), set **Build and deployment → Source → GitHub Actions**. The current connector does not expose this administrative setting.
2. Review and merge PR #2 into `main` when approved. The Pages workflow is added by that PR and will run on the first matching `main` push. If Pages settings are enabled only after the merge, manually run **R2R visual site (GitHub Pages)** once under GitHub Actions.
3. Open the workflow run and verify its **Deploy approved standalone site** step shows success.
4. Only then use the hosted site at the URL reported by the deployment. Expected standard GitHub Pages project URL: `https://kingwangking.github.io/r2r/` (do **not** claim this URL is live before verification).
5. Replace the [temporary HTMLPreview link in README](../../README.md) with the verified first-party Pages URL; update GitHub About homepage if desired.

## What will be tested

Already in PR: HTML structure, JS syntax, actual Chrome desktop/mobile rendering, two-stage animation reaching READY, mobile accessibility check and source/package checks.

Still NOT_RUN until the actual GitHub Pages workflow succeeds: real Pages deployment and public HTTP request against the final hosted URL. Full manual browser and coding-agent adoption feedback is separate from release/hosting smoke tests.

## Official guidance

[Configure a GitHub Pages publishing source](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site) · [GitHub Pages custom Actions workflows](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages).
