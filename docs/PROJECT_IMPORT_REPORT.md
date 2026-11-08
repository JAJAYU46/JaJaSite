# Project content import — November 8, 2026

## Outcome

- **16 existing Markdown articles updated; 1 existing FAST-LIVO2 article preserved byte-for-byte; 0 new project articles.**
- 17 independent project pages, organized as 6 robotics, 6 software/data, and 5 embedded/hardware projects.
- Exactly three Featured projects remain in the original order. Industrial Standards AI Agent and Mini Camera Drone remain standard cards.
- All 20 original Drive thumbnail URLs, 7 original YouTube URLs, and 8 original document URLs are preserved. The original website URL is included separately.
- The AI Agent report supplied two additional YouTube links, a project-files folder, a Colab notebook, and a proposal. Those report-discovered links are labeled separately; the demo is its hero video and the exhibition presentation remains in Resources. There are now **9 YouTube links and 6 video-first project pages**.
- Five drone records became four substantive article sections and one five-image set: a cover plus four gallery images.

The JSON was the primary structured import source; its original descriptions were checked against **MyWeb.xlsx → MyProject**. All 20 original title/description/image records matched the primary worksheet in the checked columns. The backup worksheet was not used. The original JSON is archived under `docs/sources/` for provenance; Markdown remains the only runtime project source.

## Inventory and unchanged routes

Every proposed source slug matched an existing project by title and topic. Existing slugs were preserved to avoid duplicate pages and broken links. All paths below are relative to `https://jajayu46.github.io`.

| Project | Existing project-detail route | Action |
|---|---|---|
| FAST-LIVO2 SLAM & Global Relocalization | `/JaJaSite/fast-livo2-slam-global-relocalization/` | Preserved |
| Autonomous Tomato Harvesting with Next-Best-View Planning | `/JaJaSite/autonomous-tomato-harvesting/` | Updated |
| Autonomous Navigation & Object Search | `/JaJaSite/autonomous-navigation-object-search/` | Updated |
| Scout Mini Library Navigation | `/JaJaSite/scout-mini-library-navigation/` | Updated |
| Robotic Arm Block Stacking | `/JaJaSite/robotic-arm-block-stacking/` | Updated |
| Field Robot Road Detection & Control | `/JaJaSite/field-robot-road-detection-control/` | Updated |
| Cinema Reservation System | `/JaJaSite/cinema-reservation-system/` | Updated |
| National Park Database Management System | `/JaJaSite/national-park-database/` | Updated |
| Blockchain-Based Vehicle Monitoring System | `/JaJaSite/blockchain-vehicle-monitoring/` | Updated |
| Industrial Standards AI Agent | `/JaJaSite/industrial-standards-ai-agent/` | Updated |
| Phone Price Prediction Model | `/JaJaSite/phone-price-prediction/` | Updated |
| JaJa's Original Website | `/JaJaSite/jaja-original-website/` | Updated |
| Mini Camera Drone Development | `/JaJaSite/mini-camera-drone/` | Updated; five source rows consolidated |
| Control Box Design & Fabrication | `/JaJaSite/control-box-design/` | Updated |
| Music-Reactive Lighting System | `/JaJaSite/music-reactive-lighting/` | Updated |
| Line-Following & Obstacle Avoidance Robot | `/JaJaSite/line-following-obstacle-avoidance/` | Updated |
| IR Sensor Counting & Container Positioning Prototype | `/JaJaSite/ir-counting-sorting/` | Title corrected; URL preserved |

`PROJECT_IMPORT_INVENTORY.json` records the source-to-existing-slug mapping, original titles, source worksheet rows, original URLs, and pre-import file hashes. `PROJECT_WORKSHEET_AUDIT.json` preserves only the relevant primary-sheet rows, not a workbook copy or backup-sheet substitution.

## External access: observed results and limits

Command-line anonymous HTTP checks first encountered a sandbox socket restriction and then a certificate-chain error in the network-enabled run. TLS verification was **not** disabled. `PROJECT_MEDIA_AUDIT.json` records these failed checks and must not be interpreted as evidence that the files are private or broken.

Browser checks provided stronger evidence: **all 16 supplied cover images rendered on the project index**, with nonzero natural dimensions and no fallback error state. The Google Drive PDF viewers displayed a Sign In link while exposing their report text, so those report checks did not require a Google login. These are observations from this browser session, not a guarantee that sharing settings or external availability will remain unchanged.

The original thumbnail URLs mostly return images whose longest edge is approximately **220 pixels**. The layout preserves aspect ratios and uses `object-fit: cover`; visible softness on large cards comes from the source resolution. No URL was rewritten to request a different size, and no remote project images were saved into the repository.

The four additional drone gallery URLs are preserved but were not confirmed in the browser: Google Docs navigation timed out, and subsequent browser control attempts also timed out. The final mobile layout and the corrected first-card CSS could not be visually rechecked after that interruption. The earlier project-index observation verified the 16 cover images; it does not prove the four gallery images are accessible. `PROJECT_MEDIA_AUDIT.json` records browser observations separately from command-line errors.

### Supporting document review

| Project | Original document | Relevant content actually read |
|---|---|---|
| Tomato NBV | [Full report](https://drive.google.com/file/d/1fQugP5H3UlYT9QG-rZcHBkgtyob6sIOC/view?usp=sharing) | Cover, abstract/contents, methodology on pp. 7–10; node roles, YOLOv8/DeepSORT, RANSAC/ICP, OctoMap/SDF |
| Scout Mini | [Full report](https://drive.google.com/file/d/19wtMZeI3QJxFg0ZKVo2OYzOaOm2WOCfG/view?usp=drive_link) | pp. 1–3; Scout adoption, ROS/Gazebo workflow, team size, internal evaluation limits |
| Block stacking | [Report](https://drive.google.com/file/d/1PDHNC-LprKW0frabGmJ4Pirf39SuaQLV/view?usp=drive_link) | pp. 1–3; OpenCV contours, orientation, fixed-height camera calibration, grasping challenges |
| Vehicle monitoring | [Report](https://drive.google.com/file/d/1wRC-P0oy873NkSm0TEB4VckjptFcTR2g/view?usp=drive_link) | Cover/contents and pp. 14–18; team context, sensor module, IOTA upload and AES modules |
| National parks | [Report](https://drive.google.com/file/d/18CwpuQ_oQD54med0io9_ULwXcvUZKFRK/view?usp=drive_link) | pp. 1–3; purpose, E-R schema, eight listed tables including a junction table |
| Industrial standards AI | [Report](https://drive.google.com/file/d/1UCBANRYIlkimmNB1PdLxv-PzzwGbCck9/view?usp=drive_link) | pp. 1–2; Gradio, embedding/agent models, table-processing/RAG workflow, original resource links |
| Phone prices | [Report](https://drive.google.com/file/d/1rfT6JBAptdvk5ejfXbNdD88YO85FM_8C/view?usp=drive_link) | pp. 1–4 and 9–13; dataset features and brand-comparison model/interface |
| Music-reactive lights | [Google Doc](https://docs.google.com/document/d/1ac-VghLU4rsU2PAV6SmzS6wFQxBruPph0U-tRhLg4Hg/edit?usp=sharing) | Browser navigation timed out. **Document body not read**; article uses the primary worksheet descriptions. |

These were targeted excerpt reviews, not full technical audits of the reports. New report-discovered links are preserved but are not all independently tested for playback, execution, or access. A working YouTube embed URL is not proof of video playback.

## Missing media and review items

1. **FAST-LIVO2:** no supplied real image, video, or new report. Its original article, concept diagram, and neutral card fallback remain unchanged. No benchmark was added.
2. **National parks schema count:** the primary record says seven entities; the report enumerates eight tables, including `park_species`. This may be a distinction between domain entities and a junction table. Both originals remain in the provenance files; the public summary avoids an unresolved count. Please confirm the intended terminology.
3. **Gradio:** initially present only in the structured summary, then independently confirmed on pp. 1–2 of the AI Agent report. The public technology tag was restored after that review.
4. **IR project:** the old placeholder title implied sorting. The primary record supports counting and container positioning; the title and article were corrected while retaining the established URL.
5. **Scout report title:** “Temi, Temi, Take Me!” is not a different project. The report explicitly explains the switch from planned Temi hardware to Scout Mini; the source record and report agree on the deployed platform.
6. **Block-stacking camera:** the source lists a depth camera, while the reviewed report describes image-coordinate calibration at a fixed grasp height. The article preserves that distinction and does not claim a full depth-reconstruction pipeline.
7. **Dates and results:** editorial placeholder frontmatter dates remain hidden through `dateVerified: false`. The NBV report cover supplies a research period, but no unrequested date change was made. Existing disclosure restrictions on FAST-LIVO2 still apply. The line-following class ranking is explicitly supported by its source record; no other performance numbers were invented.
8. **Music document and old-site availability:** the music document body was not reviewed. The old website URL is preserved as a resource; command-line and web-tool failures do not establish whether it is currently reachable in a normal browser.

Projects without a supplied source YouTube video are FAST-LIVO2, the original website, control box, vehicle monitoring, national parks, phone prices, music-reactive lights, field robot, IR counter, mini drone, and line-following robot. AI Agent gained a real demo from its linked report. Missing videos are not replaced with fake players; projects use their source covers where available.

## Files and maintenance

- Updated the 16 matching files under `src/content/posts/`.
- Extended the existing collection with optional `youtubeLabel`, `resources`, and `gallery` fields.
- Added `ProjectImage.astro` for shared, event-driven image-error handling and `ProjectResources.astro` for resource links and optional galleries.
- Reused PostCard, FeaturedProjectCard, PostLayout, the YouTube helper, and existing styles. A narrowly scoped Casper selector fix prevents real covers from reactivating the template's oversized first-card layout in the small grid.
- Preserved navigation, routes, categories, timeline, About page, the three diagonal cards, Astro configuration, dependency files, and deployment workflow.

See `PORTFOLIO_MAINTENANCE.md` for adding a Markdown project, replacing an external cover URL, changing a YouTube URL, and adding report/gallery links. The archived source JSON is not imported by the website.

## Verification

Run from the project root:

```sh
pnpm run build
pnpm exec tsc --noEmit
python scripts/verify_portfolio.py
python scripts/verify_project_import.py
```

The import check verifies 17 unique project routes, category counts 6/6/5, featured order, preservation of all original URLs, safe resource links, drone consolidation, 6 video-first articles, and a byte-for-byte unchanged FAST-LIVO2 source file. External-resource availability is reported separately from these local checks.

No images were downloaded into the repository. No source files outside JaJaSite were modified. No push or deployment was performed, and the old JaJaWebsite repository was not changed.
