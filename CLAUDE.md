# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Build and Serve
- `make build`: Build the entire website to ./public
- `make serve`: Run Hugo server locally at http://localhost:1313
- `make ensure`: Install dependencies and build assets

## Lint and Format
- `make lint`: Run linting on Markdown and other files
- `make format`: Format all applicable files

## Testing
- `make test`: Run all tests
- `make test-programs`: Test programs in static/programs
- `ONLY_TEST="example-name" make test-programs`: Run a specific test

## Style Guidelines
- Formatting: 4-space indent (2 for YAML), 180 char line width, double quotes
- Markdown: One h1 per page, semantic line breaks, sentence case headings
- Language: Use inclusive terminology, avoid directional language
- Content: Lead with engaging content, use headings/lists, include visuals
- SEO: Titles under 60 chars, meta descriptions 50-160 chars, PNG meta images
- Links: Use descriptive link text, no "click here" or "here" phrases
- Naming: Clear, descriptive variable/function names