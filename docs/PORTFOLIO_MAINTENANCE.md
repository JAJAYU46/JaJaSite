# Maintaining JaJaSite

This portfolio extends Astro Casper. Articles stay in `src/content/posts/`, use `PostLayout.astro`, and render with Astro Content Collections. Standard project cards still use `PostCard.astro`. No additional frontend framework or runtime dependencies were added.

## Add or edit a project

Copy a project Markdown file to `src/content/posts/my-project.md`. Its filename becomes `/JaJaSite/my-project/`. Use a unique lowercase filename; do not use reserved route names such as `about`, `projects`, or `404`.

```yaml
---
title: My Project
description: A concise, factual summary.
date: 2026-11-08
dateVerified: false
author: jaja
projectCategory: robotics
tags: [robotics]
technologies: [C++, ROS 2]
order: 180
featured: false
showOnHome: false
draft: false
---

## Overview

Describe the problem and project context.

## My Contributions

Explain your individual responsibilities and distinguish team work.
```

Required Casper fields remain `title`, `date`, and `author`. The initial project dates are editorial placeholders for collection compatibility, **not verified project dates**. `dateVerified: false` hides them from the article and article SEO metadata. Once confirmed, update `date`, set `dateVerified: true`, and optionally add `dateLabel: "2025–2026"`. Feeds still use `date` as an editorial timestamp.

Add regular Markdown sections when useful: System Architecture, My Contributions, Technical Implementation, Challenges & Solutions, Results & Evaluation, and Additional Media / Resources. Smaller projects can omit sections. Use Markdown image syntax for diagrams, including SVG. Mermaid is not installed; export a diagram as SVG if needed. Only publish verified measurements with test conditions and disclosure permission.

## Categories, order, and homepage

- Set `projectCategory` to `robotics`, `software`, or `embedded`. Update `tags` to match for Casper tag archives. Category titles and their index order live in `src/data/portfolio.ts`.
- Smaller `order` numbers appear first in the project index and homepage standard cards.
- Set `featured: true` and `featuredOrder: 1`, `2`, or `3` to promote a project. Keep exactly three featured entries, each with a distinct order. Set `featured: false` to demote one before promoting its replacement. The homepage caps featured cards at three; the verification script flags fewer than three.
- Set `showOnHome: true` for a standard homepage card. Featured entries are excluded from the small grid. Change `homeProjectCount` in `src/data/portfolio.ts` to change its limit.
- Industrial Standards AI Agent and Mini Camera Drone are standard cards. Keep the drone frame, ESP32 camera, and circuit work together in `mini-camera-drone.md`.
- `draft: true` removes an article from routes, cards, related suggestions, and feeds. Original Casper examples remain as drafts for reference. Edit Markdown directly; the inherited `/admin/` CMS configuration is not configured for this portfolio and should not be used for publishing.

## Images and video

Most imported projects now use original external Drive thumbnail URLs directly. Keep the entire URL unchanged in `cover`, for example `cover: "https://drive.google.com/thumbnail?id=YOUR_FILE_ID"`. `getAssetUrl` leaves HTTPS URLs intact. No Astro remote-image optimization configuration is needed because these are ordinary responsive `<img>` elements. Verify sharing in a signed-out browser; an image failing here does not automatically mean that its Google Drive sharing is private.

`ProjectImage.astro` handles failed requests in cards, cover heroes, and galleries: it hides the broken image and displays a labeled neutral concept illustration. The original URL remains in frontmatter and in Resources. Do not replace inaccessible images with unrelated photos. Original Drive thumbnails may be only about 220 pixels; larger cards can therefore look soft even when the CSS is correct.

Place actual images under `public/assets/images/projects/`. Set `cover: assets/images/projects/your-actual-image.webp` and a descriptive `coverAlt`. Optionally set `coverPosition: "60% 40%"` to adjust the crop in featured cards, standard cards, and article heroes. Do not include `public/` or `/JaJaSite/` in frontmatter paths. Components apply the base URL automatically. Distinct SVG concept illustrations appear on cards without a cover; these are explicitly labeled, not project evidence. Articles without a video or cover begin with the breadcrumb and a compact title area.

For images inside Markdown, include the deployment base explicitly: `![Architecture description](/JaJaSite/assets/images/projects/architecture.svg)`. Update these Markdown links if the deployment base changes.

Set `youtubeUrl` to a YouTube watch/share URL or playlist URL. The article displays a responsive 16:9 privacy-enhanced iframe before the title, with lazy loading, no autoplay, and a YouTube fallback link. Remove the field to restore the normal image hero. `githubUrl` adds an optional source link. Do not guess repository URLs.

Optional `youtubeLabel` distinguishes a demonstration from a presentation, such as `youtubeLabel: "ACPA11 research presentation"`. Keep additional videos and all reports in `resources`; links open in a new tab with `noopener noreferrer`.

```yaml
resources:
  - label: Full Project Report
    url: https://drive.google.com/file/d/YOUR_FILE_ID/view
  - label: Explanatory Presentation
    url: https://youtu.be/YOUR_ACTUAL_VIDEO_ID
gallery:
  - url: https://drive.google.com/thumbnail?id=YOUR_ADDITIONAL_IMAGE_ID
    alt: A factual description of the project image
    caption: Optional context and contribution credit
```

`resources` and `gallery` default to empty lists, and `youtubeLabel` is optional. Empty sections are omitted. Gallery images use the same responsive error handling as covers. Keep each original URL in one canonical Markdown article; the five drone records belong in `mini-camera-drone.md` with individual/team credit in the appropriate subsections.

The import inventory, source comparison, access limitations, and unchanged route list are in `PROJECT_IMPORT_REPORT.md`. `docs/sources/JaJaSite_project_source_data.json` is an archived reference, not a live database. Edit Markdown for future updates; do not rerun a migration over newer manual writing.

## Timeline, links, resume, and identity

Edit `timeline` in `src/data/portfolio.ts`; content is separate from the timeline component. Confirm all suggested dates before publication, including the NTU degree period and exchange dates.

The same file contains `portfolio.github`, `linkedin`, `resume`, `email`, and `homeProjectCount`. Empty LinkedIn and resume values render unavailable controls; empty email hides Contact. Set LinkedIn to the real HTTPS profile URL and email to an address without `mailto:`. Add the final U.S. application PDF under `public/assets/resume/`, then set `resume` to that **actual** local PDF path without `public/`. Resume links open a new tab. No old CV is reused.

Site title, description, favicon, and default Open Graph illustration are in `src/config.ts`. About content is `src/data/about.md`. Colors and responsive refinements are in `src/styles/portfolio.css`, layered after the original Casper styles.

The original decorative glacier is `public/assets/images/glacier-landscape.svg`, shared by `GlacierArtwork.astro`. `OceanWaves.astro` supplies the wave layers. Timeline icon names in `src/data/portfolio.ts` map to the inline SVGs in `PortfolioIcon.astro`; changing an icon does not change milestone text or dates.

Article H2 headings receive automatic CSS section numbers and dividers; keep writing normal Markdown headings. The FAST-LIVO2 conceptual flow is an editable SVG referenced only by its own Markdown article, with a caption clarifying that it is not a verified dependency graph. Replace it with a verified diagram when available.

For confirmed measurements only, Markdown can include a `<div class="metric-highlights">` containing `<div class="metric-card"><strong>Verified value</strong><p>Metric name, test conditions, and source.</p></div>` blocks. The layout never generates metric values. No performance numbers have been added during the visual refinement.

## Preview, checks, and deployment

Use Node 24+ as required by `package.json` and the deployment workflow, with pnpm installed.

```sh
pnpm install
pnpm run dev
# Open http://localhost:4321/JaJaSite/

pnpm run build
pnpm exec tsc --noEmit
python scripts/verify_portfolio.py
python scripts/verify_project_import.py
pnpm run preview
```

The Python verification script uses only the standard library. Run after building to check generated links/assets, featured-card count, project routes, and video placement. `@astrojs/check` is not installed in this repository; `tsc` checks TypeScript files and the build compiles Astro templates. For full Astro diagnostics, install `@astrojs/check` deliberately and run `pnpm exec astro check`.

`astro.config.mjs` defaults to site `https://jajayu46.github.io` and base `/JaJaSite/`; the existing GitHub Actions workflow uses the same values. Only after reviewing the content and approving publication, push to this repository's `main` branch or manually trigger its existing Deploy workflow. A push to `main` deploys automatically. Enable GitHub Pages with GitHub Actions as its source if not already enabled. Expected address: `https://jajayu46.github.io/JaJaSite/`.

Do not modify or deploy the separate JaJaWebsite repository.

## Before public release

- The supplied composite design reference guides the glacier artwork, diagonal featured cards, and article hierarchy. Authentic project media is still needed to complete the image-driven design.
- Add authentic project images, architecture diagrams, code links, and verified individual contributions.
- Confirm timeline and project dates and complete the deliberately pending article sections.
- Supply LinkedIn, email, and the final resume PDF.
- Verify FAST-LIVO2 measurement context and permission before adding any performance numbers; none are currently published.
- Check YouTube playback on the public domain; network access, video-owner embed settings, and browser privacy settings can affect playback.
