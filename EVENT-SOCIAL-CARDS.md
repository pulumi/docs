# Event social cards (OpenGraph / meta images)

When someone shares an event page (a workshop, webinar, or talk under `content/events/<slug>/index.md`) on X, LinkedIn, or Slack, the image they see is its social card: the `og:image` and `twitter:image`.

You usually don't have to make one. The site generates it automatically at build time from the event's frontmatter. This guide covers when that automatic card is enough and when to make your own.

> This is about the workshop and webinar event bundles under `content/events/`. It doesn't cover the widget-based marketing landing pages (`layout: template-page`, like `content/kubecon/`), which have their own [event landing page guide](./EVENT-PAGE-TEMPLATE-GUIDE.md).

## Quick decision guide

Find your situation:

| Your situation | What to do |
|---|---|
| An internal event (Pulumi hosts only), and you just need the shared image to look good | Nothing. The build generates it from frontmatter. |
| You want the extra social sizes (portrait, tall, or square-large) | Run [the render script](#extra-sizes-without-ai). It reads the same frontmatter, so you don't need the skill. |
| An external co-host whose photo is in `presenters` | Nothing needed for the photo, though the card won't show their company logo. Add the logo with the skill. |
| You want the co-host's company logo on the card | Use the [`/event-meta-image` skill](#custom-cards-with-the-event-meta-image-skill). |

## What the build generates automatically

At build time, `scripts/generate-meta-images.mjs` renders each event two cards from frontmatter: a landscape card at 1200×628 and a square one at 628×628. It reads the `title`, the `event_type` (shown as the overline), and each photo under `presenters`, then wires the cards to the page's meta tags for you. You don't set `meta_image` yourself.

The generated cards are ephemeral. For an event at `content/events/<slug>/index.md`, they land at:

```text
assets/images/generated/events/<slug>/index.png         # landscape, 1200×628
assets/images/generated/events/<slug>/index.square.png  # square, 628×628
```

That directory is gitignored and rebuilt on every build, so you never commit or edit these files directly. To change a card, change the frontmatter and rebuild.

For a typical Pulumi-hosted event, that's all you need. Fill in `title`, `event_type`, and the `presenters` (each with a `photo`), and you get a good landscape and square card.

## The external-host gap

If your event has an external co-host, add them to `presenters` with a `photo`, and their headshot shows up on the automatic card. That covers most cases.

The one thing the automatic card can't do is show the co-host's company logo, since it always renders the Pulumi logo on its own. When you want a "Pulumi + Acme" lockup, you'll need a [custom card](#custom-cards-with-the-event-meta-image-skill).

## Extra sizes without AI

Beyond the landscape and square cards, the renderer also supports portrait (540×960), tall (1200×675), and square-large (1080×1080) for manual posting. To render all five straight from frontmatter, with the same look as the automatic card, run:

```bash
node scripts/meta-images/render-event-cards.mjs <slug-or-path> [--out <dir>]
```

Pass an event slug, which resolves to `content/events/<slug>/index.md`, or a path to the `index.md`. Without `--out`, the script writes the five images into the event bundle. With `--out <dir>`, it writes them to a folder you choose (for example, a scratch directory) and leaves the bundle untouched. It never modifies frontmatter.

## Custom cards with the /event-meta-image skill

Some cards need judgment a script can't apply: a partner or company logo, a co-presenter who isn't in frontmatter, or a headshot you have to find on the web. For those, use the `/event-meta-image` skill in Claude Code or another agent. It adds the logos and people, renders all five sizes into the event bundle, and sets `meta_image` and `meta_image_square` so the custom card overrides the automatic one. The agent-facing details live in [the skill itself](./.claude/commands/event-meta-image/SKILL.md).

To run it without answering prompts, pass `--yes` (or its alias `--non-interactive`), as in `/event-meta-image <slug> --yes`. The skill then fills in sensible defaults and asks nothing. It still searches for the people and logos it can infer from the event, and skips anything it can't resolve rather than stopping to ask.

### Which model to run it with

For an event whose assets are all local, such as Pulumi hosts with presenter photos already in frontmatter, any model runs the skill well, including the least expensive, Claude Haiku. Sourcing a company logo or headshot from the web is the one step where a smaller model can pick a poor asset, like a white or dark-mode logo that's invisible on the near-white card. For those runs, use Claude Sonnet or larger. The skill's eval, under `.claude/commands/event-meta-image/eval/`, is where this was measured.

## Overriding manually

If you'd rather supply your own image, set `meta_image` in the event's frontmatter, or commit the PNGs the skill produced. Either one overrides the automatic card for that page.
