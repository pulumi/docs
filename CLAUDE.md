# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

> **Related documentation:**
> - [CONTRIBUTING.md](CONTRIBUTING.md) - Guide for contributing to Pulumi documentation
> - [STYLE-GUIDE.md](STYLE-GUIDE.md) - Comprehensive style and UX standards
> - [BLOGGING.md](BLOGGING.md) - Instructions for writing blog posts
> - [CODE-EXAMPLES.md](CODE-EXAMPLES.md) - Guidelines for creating code examples
> - [SEO.md](SEO.md) - Search engine optimization checklist

## Essential Commands

### Build and Development
- `make ensure`: Install dependencies and build assets
- `make build`: Build the site to ./public
- `make serve`: Run Hugo server locally at http://localhost:1313

### Validation
- `make lint`: Check Markdown and other files for correctness
- `make format`: Format all applicable files

### Testing
- `make test`: Run all example program tests
- `ONLY_TEST="example-name" make test-programs`: Run a specific test

### Content Creation
- `make new-blog-post`: Generate scaffold for a new blog post
- `make new-tutorial`: Create a new tutorial page
- `make new-example-program`: Generate a new multi-language code example

## Key Guidelines

For comprehensive guidelines, please refer to the specific documentation files linked above. Here are the most critical points:

- One h1 per page, use semantic line breaks
- Place tested code examples in /static/programs/
- Use descriptive link text (no "click here" or "here")
- Create redirects with Hugo aliases when changing URLs
- Follow language-specific conventions in [STYLE-GUIDE.md](STYLE-GUIDE.md)
- Test all code examples before submitting