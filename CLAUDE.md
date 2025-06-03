# CLAUDE.md - Guide for Working in this Repository

** IMPORTANT **
- Read `@STYLE-GUIDE.md` for styling information.
- Do not change the package manager to pnpm in `package.json`.
- Any new files must end with a newline.


This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Build/Test/Lint Commands
- Build site: `make build`
- Serve locally: `make serve` or `make serve-all` (with asset rebuilding)
- Lint code: `make lint`
- Format code: `make format`
- Run tests: `make test`
- Test specific programs: `ONLY_TEST="program-name" ./scripts/programs/test.sh`

## Code Style Guidelines
- **Markdown**: Use one line per paragraph or semantic line breaks (see STYLE-GUIDE.md)
- **Headings**: First level (H1) uses title case, all other headings use sentence case
- **Links**: Use Hugo's `relref` shortcode for internal links: `[Text]({{< relref "/path" >}})`
- **Code Examples**: Place in `/static/programs` directory with language suffix naming convention
- **TypeScript/JavaScript**: Follow tsconfig.json settings - no comments unless requested
- **File Structure**: Follow existing conventions for placement of new content
- **Includes**: Use Hugo shortcodes for shared content across articles
- **Naming**: Use lowercase for non-proper nouns (e.g., "stack" not "Stack" in text)

