# `/event-meta-image` eval

A headless LLM eval for the `/event-meta-image` skill. It runs the skill non-interactively
(`claude -p`) across a set of fixtures on one or more models, then asserts on the **artifacts the
model produced** — the `config.json` it wrote and the five PNGs it rendered — never on prose. This
catches a model that ignores the skill's defaults (adding a button it shouldn't, dropping a speaker,
producing wrong sizes) and tells you the cheapest model that runs the skill correctly.

## Run it

```bash
# Core fixtures on the default target model (opus):
node .claude/commands/event-meta-image/eval/run.mjs

# Full cost spread — prints a cheapest-passing table:
node .claude/commands/event-meta-image/eval/run.mjs --models haiku,sonnet,opus,fable

# One fixture, deterministic core only, keep outputs to eyeball:
node .claude/commands/event-meta-image/eval/run.mjs --fixture button-requested --keep
```

Flags: `--models <csv>` (aliases `haiku,sonnet,opus,fable`), `--fixture <id>`, `--no-web` (skip
live-web fixtures), `--web-strict` (let web fixtures gate the exit code), `--keep` (leave the
`.context/event-images/eval/<id>/` output dirs in place). Override the CLI binary with
`CLAUDE_BIN`. Runs are sequential; each takes ~1–5 min per fixture depending on the model and
whether it hits the web.

Exit code is non-zero if any **core** fixture fails for any tested model — suitable for CI.

## Fixtures (`fixtures.json`)

All fixtures run in **standalone** mode with an explicit output dir, so the eval never mutates
`content/events/`.

- **Core** (`web:false`) — resolve entirely from local files / the bundled logo cache, so they're
  deterministic and gate pass/fail: basic card (button off, Pulumi only), two local presenters,
  an explicitly-requested Register button (button on), and a cached-partner logo (Microsoft).
- **Web** (`web:true`) — exercise live `WebSearch`/`WebFetch` sourcing. They run and report
  separately and gate only under `--web-strict`, because search results and headshot availability
  shift over time. `partner-logo-web` (NVIDIA) forces a real logo fetch — `forceMissLogo` deletes
  the cache entry before **and** after the run so it always fetches fresh and leaves the committed
  cache clean. `external-presenter-web` (a headshot search) is `soft:true` — auth-gated headshots
  are inherently flaky, so it only checks the byline name and never gates.

## What each run asserts

Per fixture, against the model-written `config.json` + rendered PNGs:

- `config.json` was written to the output dir and parses.
- `showButton` matches the expectation (this is the button-regression guard).
- `speakers.length` matches; `logos` contain the expected substrings; the byline contains the
  expected names.
- **Five card PNGs**, one per expected size — verified by reading each PNG's `IHDR` width/height,
  so it's filename-agnostic (`1200x628`, `628x628`, `1200x675`, `1080x1080`, `540x960`). Only
  card-sized PNGs are counted; a fetched source photo the skill saves into the same folder (e.g. a
  downloaded headshot) is a non-card size and is ignored, not counted as a sixth card.
- The config **re-renders with no unresolved assets** — the harness runs
  `scripts/meta-images/render-event.mjs` once on the model's config and fails on any
  `could not resolve` warning.
- **The partner logo is actually visible** — for any fixture with a non-Pulumi logo, the harness
  decodes that re-render and counts "ink" pixels in the partner-logo band of the card. A logo that
  *resolves* can still be *invisible* (a white / dark-mode asset on the near-white `#f5f5ff` card);
  resolution alone isn't enough. Calibrated on real runs: visible logos land ~3,100–5,600 ink,
  an invisible one lands 0; the threshold is 400. This is the check that catches a cheap model
  fetching an off-brand dark-mode logo.

## Reading the cost table

The summary sorts models with all core fixtures passing first, then by measured run cost (the real
`total_cost_usd` from each `claude -p` run), and names the cheapest passing model. Output pricing
(the driver of cost) is `haiku $5 < sonnet $15 < opus $25 < fable $50` per 1M tokens — so "lowest
cost that works" is a direct read-off. (Fable is the most capable *and* most expensive model, not a
cheap one; the reported failure that motivated this eval was Fable ignoring a default, which is
exactly what these assertions catch.)
