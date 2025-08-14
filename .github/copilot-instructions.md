# Pulumi Documentation Website

Always follow these instructions first and only use additional search or context gathering if the information here is incomplete or found to be in error.

The Pulumi docs repository is a Hugo-based documentation website written in Markdown with Node.js tooling for asset building and automation. It includes extensive example programs that are automatically tested.

## Working Effectively

Bootstrap, build, and serve the repository:

- Install Hugo 0.126.0+: `wget https://github.com/gohugoio/hugo/releases/download/v0.126.0/hugo_extended_0.126.0_linux-amd64.tar.gz && tar -xzf hugo_extended_0.126.0_linux-amd64.tar.gz && sudo mv hugo /usr/local/bin/`
- Install dependencies: `CYPRESS_INSTALL_BINARY=0 PUPPETEER_SKIP_DOWNLOAD=1 make ensure` -- takes 2-3 minutes. NEVER CANCEL.
- Build CSS/JS assets: `make build-assets` -- takes 30 seconds. NEVER CANCEL.
- Build full site: `make build` -- takes 2-3 minutes. NEVER CANCEL. Set timeout to 300+ seconds.
- Serve development: `make serve` -- starts in 15 seconds on http://localhost:1313
- Serve built site: `make serve-static` -- starts immediately on http://localhost:8080

Run quality checks:
- Lint: `make lint` -- takes 10 seconds. Checks Markdown and code formatting.
- Format: `make format` -- takes 5 seconds. Auto-formats all code and Markdown.

## Validation

ALWAYS run through complete content editing workflows after making changes:
- Edit a Markdown file in `/content` 
- Run `make lint` and `make format` to ensure quality
- Run `make serve` and verify the page renders correctly at http://localhost:1313
- Test internal links and navigation work correctly

Example program testing:
- Test single program: `ONLY_TEST="program-name" ./scripts/programs/test.sh preview` -- takes 2+ minutes per program. NEVER CANCEL.
- Test all programs: `make test` -- takes 30+ minutes. NEVER CANCEL. Set timeout to 3600+ seconds.
- Many programs in `/static/programs` are skipped due to ignore rules in `scripts/programs/ignore.txt`

## Critical Build Requirements

Required tools and versions:
- Hugo 0.126.0+ (extended version required)
- Node.js 18+ (repo uses Node 18, supports Node 20)
- Yarn 1.x
- Go 1.20+ (for SDK documentation generation)
- Python 3.7+ (for SDK documentation generation)  
- .NET 6+ (for SDK documentation generation)
- Pulumi CLI (for SDK/CLI documentation generation)
- Pulumi ESC CLI (for ESC CLI documentation generation)

Network limitations in sandboxed environments:
- Cypress installation often fails - use `CYPRESS_INSTALL_BINARY=0` to skip
- Puppeteer installation often fails - use `PUPPETEER_SKIP_DOWNLOAD=1` to skip
- Pulumi plugin downloads may fail during example testing

## Repository Structure

Key directories:
- `/content` - All documentation content (Markdown files)
- `/static/programs` - Testable code examples in multiple languages
- `/layouts` - Hugo templates and shortcodes
- `/theme` - CSS/JS source files (built into `/assets`)
- `/scripts` - Build automation and utility scripts
- `/public` - Built website output
- `/static-prebuilt` - Pre-built SDK documentation
- `/infrastructure` - Pulumi deployment configuration

Important files:
- `Makefile` - Primary build automation interface
- `README.md` - Comprehensive setup and development guide
- `STYLE-GUIDE.md` - Content style guidelines
- `CODE-EXAMPLES.md` - Code example testing documentation
- `CONTRIBUTING.md` - Contribution guidelines

## Common Development Tasks

Content editing workflow:
1. `make ensure` (if dependencies changed)
2. Edit Markdown files in `/content`
3. `make serve` to preview changes
4. `make lint` and `make format` before committing
5. Test navigation and links manually

Code example workflow:
1. Add examples to `/static/programs/<name>-<language>/`
2. Use `{{< example-program path="name" >}}` shortcode in Markdown
3. Test with `ONLY_TEST="name-language" ./scripts/programs/test.sh preview`
4. Many examples are skipped - check `scripts/programs/ignore.txt`

Full site workflow:
1. `make ensure` -- installs dependencies
2. `make build` -- builds complete site to `/public`
3. `make serve-static` -- serves built site for testing
4. `make test` -- tests all example programs (very time-consuming)

## SDK and CLI Documentation Generation

Generate SDK docs (time-intensive):
- `make update-repos` -- clones package repositories into sibling directories
- `make generate` -- builds TypeScript, Python, and CLI docs. NEVER CANCEL. Takes 10+ minutes.

Generate specific docs:
- Node.js/Python SDK: `make generate` 
- .NET SDK: `dotnet tool install -g docfx && docfx build docfx/docfx.json`
- Pulumi CLI: `pulumi gen-markdown ./content/docs/cli/commands`
- ESC CLI: `esc gen-docs ./content/docs/esc-cli/commands`

## Content Guidelines

Follow established patterns:
- Use Hugo shortcodes for reusable content
- Internal links: `[Text]({{< relref "/path" >}})`
- Code examples go in `/static/programs` for testing
- First level headings use Title Case, others use sentence case
- Always add aliases for moved/renamed pages

## CI/CD Integration

GitHub Actions will:
- Run `make lint` and fail if issues found
- Build and deploy the site
- Test example programs daily
- Update search index automatically

Always run `make lint` and `make format` before committing to pass CI checks.

## Timing Expectations and Timeouts

Command timing (add 50% buffer for timeouts):
- `make ensure`: 2-3 minutes → Use 300+ second timeout
- `make build`: 2-3 minutes → Use 300+ second timeout  
- `make build-assets`: 30 seconds → Use 60+ second timeout
- `make serve`: 15 seconds to start → Use 30+ second timeout
- `make lint`: 10 seconds → Use 30+ second timeout
- `make format`: 5 seconds → Use 15+ second timeout
- `make test`: 30+ minutes → Use 3600+ second timeout. NEVER CANCEL.
- `make generate`: 10+ minutes → Use 1200+ second timeout. NEVER CANCEL.
- Single program test: 2+ minutes → Use 300+ second timeout

**CRITICAL: NEVER CANCEL long-running builds or tests. The full test suite can take 30+ minutes, and builds can take several minutes. Use appropriate timeouts and wait for completion.**