---
user-invocable: false
description: Image and diagram review criteria — alt text, file format, size, comparison screenshots, borders.
---

# Image Review

Applied to images and diagrams in user-facing content (docs, blogs, customer stories). Most checks are visual or filesystem-level; a few require running adjacent tooling.

---

## Alt text

- **Every image has alt text.** Markdown form: `![<alt>](<path>)`; HTML form: `<img alt="<alt>" ...>`. Missing alt text is an accessibility failure.
- **Alt text describes the image, not its filename or position.** Flag generic placeholders: "Screenshot", "Image", "Diagram", "image of <whatever>".
- **Decorative images use empty alt text** (`alt=""`) to signal "screen readers can skip this." Don't flag empty alt text on a decorative image.

(Note: `MD045` would handle missing-alt deterministically, but the markdownlint config currently has it disabled. Until that's enabled, this rule lives here.)

## File format and integrity

- **File format matches extension.** A WebP saved as `.png` renders broken in some preview environments. If the extension and apparent format disagree, flag and propose a rename or re-export. Verify via `file <path>` if uncertain.
- **No animated GIFs as `meta_image`.** Social previews fall back to the first frame, often the worst frame; use a static PNG/JPEG.

## Size limits

- **Animated GIFs:** max 1200px wide, max 3 MB. Beyond either limit, propose converting to MP4/WebM or trimming the GIF.
- **Static screenshots:** flag any single image >500 KB as a candidate for re-export at lower quality (lossy JPEG or PNG with reduced palette).
- **Bundle impact:** a PR adding multiple images >1 MB total is worth a flag — repeated retrieval costs add up across page loads.

## Screenshots

- **1px gray borders.** Screenshots without borders blend into the page background and can lose their edges. The `/add-borders` skill applies these in bulk; flag missing borders so the author knows to run it.
- **Comparison screenshots use side-by-side images of the same view.** Before/after pairs must show the same UI region, not different parts of the screen. If a "before" shows the dashboard and "after" shows a settings page, that's not a comparison — flag.
- **Current product UI.** Screenshots of stale product UI (old logos, old console layouts) hurt the post's credibility. Flag screenshots that visibly use deprecated UI elements.

## Diagrams

- **Mermaid preferred over ASCII art.** Per AGENTS.md. Hugo renders Mermaid natively via `layouts/_default/_markup/render-codeblock-mermaid.html`. ASCII diagrams in `<pre>` blocks should be flagged as "consider Mermaid" findings.
- **Diagram source over rasterized export.** When a diagram has source (Mermaid, draw.io, Excalidraw), prefer the source-rendered form over a PNG export. Source can be edited; PNGs require re-export to update.

## Do not flag

- **Image composition or visual design.** Colors, layout, typography, and aesthetic critique are out of scope. Flag *technical* issues (missing alt, wrong format, oversized file), not editorial design preferences.
- **Stock photography choice.** If the post uses a hero image, "you should use a different photo" is editorial. Flag a placeholder image that wasn't replaced; don't critique a real image.
- **Image redundancy.** "This screenshot doesn't add much" is editorial. Flag broken or stale screenshots, not whether the post needs them.
