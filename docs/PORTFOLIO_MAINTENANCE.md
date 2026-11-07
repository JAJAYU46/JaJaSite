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

Place actual images under `public/assets/images/projects/`. Set `cover: assets/images/projects/your-actual-image.webp` and a descriptive `coverAlt`. Do not include `public/` or `/JaJaSite/` in frontmatter paths. Components apply the base URL automatically. Abstract CSS illustrations appear on cards without a cover; these are explicitly labeled, not project evidence. Articles without a video or cover simply begin with the title.

For images inside Markdown, include the deployment base explicitly: `![Architecture description](/JaJaSite/assets/images/projects/architecture.svg)`. Update these Markdown links if the deployment base changes.

Set `youtubeUrl` to a YouTube watch/share URL or playlist URL. The article displays a responsive 16:9 privacy-enhanced iframe before the title, with lazy loading, no autoplay, and a YouTube fallback link. Remove the field to restore the normal image hero. `githubUrl` adds an optional source link. Do not guess repository URLs.

## Timeline, links, resume, and identity

Edit `timeline` in `src/data/portfolio.ts`; content is separate from the timeline component. Confirm all suggested dates before publication, including the NTU degree period and exchange dates.

The same file contains `portfolio.github`, `linkedin`, `resume`, `email`, and `homeProjectCount`. Empty LinkedIn and resume values render unavailable controls; empty email hides Contact. Set LinkedIn to the real HTTPS profile URL and email to an address without `mailto:`. Add the final U.S. application PDF under `public/assets/resume/`, then set `resume` to that **actual** local PDF path without `public/`. Resume links open a new tab. No old CV is reused.

Site title, description, favicon, and default Open Graph illustration are in `src/config.ts`. About content is `src/data/about.md`. Colors and responsive refinements are in `src/styles/portfolio.css`, layered after the original Casper styles.

## Preview, checks, and deployment

Use Node 24+ as required by `package.json` and the deployment workflow, with pnpm installed.

```sh
pnpm install
pnpm run dev
# Open http://localhost:4321/JaJaSite/

pnpm run build
pnpm exec tsc --noEmit
python scripts/verify_portfolio.py
pnpm run preview
```

The Python verification script uses only the standard library. Run after building to check generated links/assets, featured-card count, project routes, and video placement. `@astrojs/check` is not installed in this repository; `tsc` checks TypeScript files and the build compiles Astro templates. For full Astro diagnostics, install `@astrojs/check` deliberately and run `pnpm exec astro check`.

`astro.config.mjs` defaults to site `https://jajayu46.github.io` and base `/JaJaSite/`; the existing GitHub Actions workflow uses the same values. Only after reviewing the content and approving publication, push to this repository's `main` branch or manually trigger its existing Deploy workflow. A push to `main` deploys automatically. Enable GitHub Pages with GitHub Actions as its source if not already enabled. Expected address: `https://jajayu46.github.io/JaJaSite/`.

Do not modify or deploy the separate JaJaWebsite repository.

## Before public release

- Supply the missing design reference if closer visual matching is needed.
- Add authentic project images, architecture diagrams, code links, and verified individual contributions.
- Confirm timeline and project dates and complete the deliberately pending article sections.
- Supply LinkedIn, email, and the final resume PDF.
- Verify FAST-LIVO2 measurement context and permission before adding any performance numbers; none are currently published.
- Check YouTube playback on the public domain; network access, video-owner embed settings, and browser privacy settings can affect playback.
