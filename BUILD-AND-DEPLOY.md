# Pulumi Docs: Build and Deployment Guide

This document provides comprehensive documentation of the entire build, test, deployment, and infrastructure system for the Pulumi documentation site.

## Table of Contents

1. [Overview](#overview)
2. [Architecture Overview](#architecture-overview)
3. [Local Development](#local-development)
4. [Build System](#build-system)
5. [GitHub Actions Workflows](#github-actions-workflows)
6. [Deployment Infrastructure](#deployment-infrastructure)
7. [Testing Strategy](#testing-strategy)
8. [Environment Management](#environment-management)
9. [Troubleshooting](#troubleshooting)
10. [Infrastructure Change Review](#infrastructure-change-review)
11. [Maintenance Tasks](#maintenance-tasks)
12. [Reference](#reference)

---

## Overview

### Purpose

This guide serves as the definitive reference for understanding and working with the Pulumi documentation site's build and deployment infrastructure. Whether you're a developer making changes, an operations engineer troubleshooting deployments, or a contributor adding content, this document will help you understand the complete lifecycle from source to production.

### Quick Reference

Common commands for daily development:

```bash
# Initial setup
make ensure                # Install all dependencies

# Local development
make serve                 # Start local server at http://localhost:1313
make serve-all            # Serve with asset rebuilding (webpack watch)

# Building
make build                # Full production build
make build-assets         # Build CSS/JS assets only

# Quality checks
make lint                 # Run linting checks
make format               # Format code with Prettier
make test                 # Run example program tests

# Cleanup
make clean                # Remove build artifacts and dependencies
```

### Key Concepts

- **Hugo**: Static site generator that transforms markdown content into HTML
- **Atomic Deployments**: Each deployment creates a new S3 bucket, enabling instant rollbacks
- **Bundle IDs**: Unique identifiers (git SHA or PR number) for cache busting assets
- **Ephemeral Buckets**: Temporary S3 buckets created for PR previews
- **CloudFront**: CDN that serves the production site globally
- **Pulumi ESC**: Environment, Secrets, and Config service for credential management
- **OIDC**: OpenID Connect authentication for AWS (no static credentials)

### Prerequisites

**Required Tools:**

- Node.js 24.x
- Hugo 0.154.5
- Yarn 1.22.x (not strictly enforced in CI)
- Go 1.25.x (for documentation generation)
- Python 3.9 (for testing workflows) and 3.13 (for SDK documentation generation)
- Pulumi CLI (for infrastructure deployments)

**Optional Tools:**

- AWS CLI (for debugging deployments)
- GitHub CLI (`gh`) (for PR operations)
- Docker (for dev container)

---

## Architecture Overview

### High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    Content Authors                               │
│                 (Markdown, Code Examples)                        │
└──────────────────────┬──────────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────────┐
│                   GitHub Repository                              │
│        (docs, blog, examples, static assets)                     │
└──────────────────────┬──────────────────────────────────────────┘
                       │
       ┌───────────────┴───────────────┐
       │                               │
       ▼                               ▼
┌──────────────┐              ┌──────────────┐
│  PR Build    │              │Master Build  │
│  (Testing)   │              │(Production)  │
└──────┬───────┘              └──────┬───────┘
       │                              │
       ▼                              ▼
┌──────────────────────────────────────────────────────────────┐
│                     Build Pipeline                            │
│  1. Asset Compilation (Webpack, Tailwind CSS)                │
│  2. Documentation Generation (TypeDoc, Sphinx, CLI)          │
│  3. Hugo Build (Markdown → HTML)                             │
│  4. CSS Optimization (PurgeCSS, CSSNano)                     │
│  5. Search Index Generation (Algolia)                        │
└──────────────────┬───────────────────────────────────────────┘
                   │
       ┌───────────┴────────────┐
       │                        │
       ▼                        ▼
┌──────────────┐        ┌──────────────┐
│  S3 Preview  │        │ S3 Production│
│    Bucket    │        │    Bucket    │
│(PR-specific) │        │ (versioned)  │
└──────────────┘        └──────┬───────┘
                               │
                               ▼
                       ┌───────────────┐
                       │  CloudFront   │
                       │  Distribution │
                       │ +Lambda@Edge  │
                       └───────┬───────┘
                               │
                               ▼
                       ┌───────────────┐
                       │  www.pulumi   │
                       │     .com      │
                       └───────────────┘
```

### Component Relationships

**Build System:**

- **Hugo**: Transforms content/ markdown into static HTML
- **Webpack**: Bundles TypeScript and CSS from theme/
- **TypeDoc**: Generates Node.js SDK documentation
- **Sphinx**: Generates Python SDK documentation
- **Pulumi CLI**: Generates CLI reference documentation

**Deployment Infrastructure:**

- **S3**: Origin buckets for static content
- **CloudFront**: Global CDN with caching
- **Lambda@Edge**: Request routing and redirects
- **Route53**: DNS management
- **Pulumi**: Infrastructure as Code for deployment

**CI/CD:**

- **GitHub Actions**: 25 workflows for build, test, deploy
- **Pulumi ESC**: Secrets and environment management
- **OIDC**: Secure AWS authentication without static keys

### Data Flow

```
Source Files → Asset Compilation → Hugo Build → Optimization → S3 Sync → CloudFront → Users
     │              │                   │            │            │
     │              │                   │            │            └─ Cache invalidation
     │              │                   │            └─ CSS minification, search indexing
     │              │                   └─ HTML generation, shortcode processing
     │              └─ JS bundling, CSS compilation
     └─ Markdown, images, code examples
```

### Multi-Repository Integration

The docs site integrates with several other Pulumi repositories:

- **pulumi/registry**: Package registry UI (external repository, served via CloudFront origin routing at /registry path)
- **pulumi/answers**: AI answers feature (embedded at /answers)
- **pulumi/pulumi-ai-app-infra**: AI application backend
- **pulumi/guides**: Interactive guides (embedded at /guides)

These are integrated via CloudFront origin routing and Pulumi stack references.

> **Note:** The registry is NOT part of the Hugo build. Only content/registry.md exists locally as a landing page. The actual registry application runs from a separate repository and is integrated via CloudFront origin routing.

---

## Local Development

### Environment Setup

#### Dev Container (Recommended)

The repository includes a dev container configuration with all required tools:

```bash
# Open in VS Code with Dev Containers extension
code .
# Select "Reopen in Container"
```

#### Manual Installation

**Install Required Tools:**

```bash
# Node.js 24 (via nvm)
nvm install 24
nvm use 24

# Yarn
npm install -g yarn@1.22

# Hugo 0.154.5
# macOS:
brew install hugo@0.154.5
# Linux: Download from https://github.com/gohugoio/hugo/releases/tag/v0.154.5

# Pulumi CLI
curl -fsSL https://get.pulumi.com | sh

# Go 1.25+
# macOS:
brew install go@1.25
# Linux: https://go.dev/doc/install

# Python 3.13+
# macOS:
brew install python@3.13
# Linux: Use your package manager
```

**Install Dependencies:**

```bash
make ensure
```

This will:

1. Run `clean.sh` to remove old artifacts
2. Install Node.js dependencies for root, theme, theme/stencil, and infrastructure
3. Build theme assets with webpack
4. Warn about expected TypeDoc peer dependency warnings (these are safe to ignore)

### Common Development Tasks

#### Starting the Local Server

```bash
# Basic dev server (fast, uses built assets)
make serve

# Dev server with asset rebuilding (watches for CSS/JS changes)
make serve-all

# Serve the built site (test production build locally)
make serve-static
```

The site will be available at <http://localhost:1313>.

> **Note:** The dev server uses `--buildDrafts` and `--buildFuture` flags, showing content not visible in production.

#### Building the Site

```bash
# Full production build
make build

# This runs:
# 1. make build-assets (webpack compilation)
# 2. build-site.sh (Hugo build + optimization)
```

Output directory: `public/`

#### Generating Documentation

```bash
# Generate all SDK and CLI documentation
make generate

# This runs:
# 1. run_typedoc.sh (Node.js API docs)
# 2. generate_python_docs.sh (Python API docs)
# 3. pulumi gen-markdown (CLI reference)
```

Generated docs go to `static-prebuilt/docs/reference/pkg/`

**Selective Generation:**

```bash
# TypeScript only
NOBUILD=true PKGS=pulumi ./scripts/run_typedoc.sh

# Skip rebuilds (faster)
NOBUILD=1 make generate
```

#### Linting and Formatting

```bash
# Run linting checks
make lint

# Auto-format code
make format

# Check for broken links
make check_links
```

#### Creating New Content

```bash
# New blog post
make new-blog-post

# New tutorial
make new-tutorial

# New example program
make new-example-program
```

### Directory Structure

```
./
├── content/              # All content (docs, blog, etc.)
│   ├── docs/            # Documentation
│   ├── blog/            # Blog posts
│   ├── registry.md      # Registry landing page (redirect)
│   └── ...
├── layouts/             # Hugo templates
├── data/                # YAML data files (menus, etc.)
├── theme/               # CSS/JS source code
│   ├── src/             # TypeScript and Sass source
│   ├── stencil/         # Web components
│   └── package.json     # Theme dependencies
├── assets/              # Compiled assets (generated)
│   ├── js/              # Compiled JavaScript
│   └── css/             # Compiled CSS
├── static/              # Static files (copied as-is)
├── static-prebuilt/     # Generated SDK documentation
│   └── docs/reference/pkg/
├── public/              # Final built site (generated)
├── scripts/             # Build and deployment scripts
├── infrastructure/      # Pulumi IaC for deployment
├── config/              # Hugo configuration
│   ├── _default/        # Base configuration
│   └── production/      # Production overrides
├── .github/workflows/   # GitHub Actions (25 workflows)
├── Makefile             # Build targets
└── BUILD-AND-DEPLOY.md  # This document
```

---

## Build System

### Makefile Targets

#### Core Build Targets

| Target | Description | Dependencies |
|--------|-------------|--------------|
| `default` / `all` | Runs complete build | banner, generate, build |
| `build` | Full site build | build-assets, build-site.sh |
| `build-assets` | Compile theme JS/CSS | yarn build in theme/ |
| `generate` | Generate SDK/CLI docs | TypeDoc, Sphinx, pulumi CLI |
| `serve` | Local dev server (port 1313) | serve.sh |
| `serve-all` | Dev server + asset watch | serve.sh + webpack watch |
| `serve-static` | Serve built public/ dir | http-server on port 8080 |

#### Setup & Cleanup

| Target | Description |
|--------|-------------|
| `ensure` | Install all dependencies |
| `clean` | Remove node_modules, public/, resources/ |
| `update-repos` | Sync external Pulumi repositories |

#### Testing & Validation

| Target | Description |
|--------|-------------|
| `lint` | Run markdown linting and Prettier checks |
| `format` | Auto-format with Prettier |
| `test` / `test-programs` | Run example program tests (preview mode) |
| `check_links` | Validate all links in production site |
| `check_search_urls` | Validate search index URLs |

#### CI/CD Targets

| Target | Description | Used By |
|--------|-------------|---------|
| `ci_push` | Production deployment workflow | build-and-deploy.yml |
| `ci_pull_request` | PR validation and preview | pull-request.yml |
| `ci_pull_request_closed` | Cleanup PR resources | pr-closed.yml |
| `ci_bucket_cleanup` | Remove old S3 buckets | bucket-cleanup.yml |
| `ci_update_search_index` | Update Algolia search | update-search-index.yml |

#### Content Creation

| Target | Description |
|--------|-------------|
| `new-blog-post` | Create new blog post |
| `new-tutorial` | Create new tutorial |
| `new-template` | Create new template |
| `new-example-program` | Create new example program |

### Build Scripts

All scripts are located in `scripts/`.

#### build-site.sh - Main Build Orchestrator

The primary build script that orchestrates the entire build process.

**What it does:**

1. Sets environment variables for bundle IDs:

   ```bash
   ASSET_BUNDLE_ID=${git-sha-short or pr-{num}-{sha}}
   CSS_BUNDLE_ID=${ASSET_BUNDLE_ID}
   ```

2. Exports asset paths for Hugo templates:

   ```bash
   REL_CSS_BUNDLE=/css/styles.${ASSET_BUNDLE_ID}.css
   REL_JS_BUNDLE=/js/bundle.min.${ASSET_BUNDLE_ID}.js
   ```

3. Copies prebuilt documentation:

   ```bash
   make copy_static_prebuilt
   ```

4. Runs Hugo build with optimization:

   ```bash
   hugo --minify --buildFuture --templateMetrics  # For preview/testing
   # Production omits --buildFuture
   ```

5. Generates search index data:

   ```bash
   node scripts/content/generate-docs-content.js
   ```

6. Minifies and optimizes CSS:

   ```bash
   yarn run minify-css
   ```

**Usage:**

```bash
# Production build
./scripts/build-site.sh

# Preview build (for PRs)
./scripts/build-site.sh preview
```

#### ensure.sh - Dependency Management

Installs and verifies all required dependencies.

**What it does:**

1. Checks for required tools:
   - Node.js 24.x
   - Hugo 0.154.5
   - Yarn 1.22.x

2. Installs dependencies for:
   - Root package.json
   - infrastructure/package.json
   - theme/package.json
   - theme/stencil/package.json

3. Warns about expected TypeDoc peer dependency conflicts (safe to ignore)

**Usage:**

```bash
make ensure
# or
./scripts/ensure.sh
```

#### serve.sh - Development Server

Starts the Hugo development server with live reload.

**What it does:**

1. Sets `ASSET_BUNDLE_ID` for development
2. Runs Hugo with:
   - `--renderToMemory`: No disk writes
   - `--disableFastRender`: Rebuild related content
   - `--buildDrafts`: Show draft content
   - `--buildFuture`: Show future-dated content (can be disabled with BUILD_FUTURE=false)
3. Connects to tf2pulumi conversion service
4. Uses Hugo's default binding (localhost:1313)

**Usage:**

```bash
make serve
# or
./scripts/serve.sh
```

#### ci-push.sh - Production Deployment

Complete production deployment pipeline.

**Steps:**

1. Build site: `./scripts/build-site.sh`
2. Sync to S3: `./scripts/sync-and-test-bucket.sh update`
3. Generate search index
4. Wait for in-progress operations: `node await-in-progress.js`
5. Pulumi infrastructure update: `./scripts/run-pulumi.sh`
6. Generate S3 redirects: `./scripts/make-s3-redirects.sh`

**Usage:**

```bash
make ci_push
# or
./scripts/ci-push.sh
```

#### ci-pull-request.sh - PR Preview Deployment

Builds and deploys PR preview environments.

**Steps:**

1. Check for AWS/Pulumi credentials (skip for forks)
2. Build site: `./scripts/build-site.sh preview`
3. Sync to preview bucket: `./scripts/sync-and-test-bucket.sh preview`
4. Generate search index for preview
5. Pulumi preview (non-destructive): `./scripts/run-pulumi.sh`
6. Generate S3 redirects

**Usage:**

```bash
make ci_pull_request
# or
./scripts/ci-pull-request.sh
```

#### sync-and-test-bucket.sh - S3 Deployment & Validation

Creates S3 bucket, syncs content, and validates deployment.

**What it does:**

1. **Creates S3 bucket** with atomic naming:

   ```
   www-{environment}-pulumi-docs-origin-{build-id}
   ```

2. **Configures bucket**:
   - Website hosting (index.html, 404.html)
   - Public access (ACL enabled)
   - CORS configuration

3. **Syncs content**:

   ```bash
   aws s3 sync public/ s3://{bucket}/ --delete
   ```

4. **Validates deployment**:
   - Checks for at least 1000 index.html files
   - Verifies bucket accessibility

5. **Generates metadata**:

   ```json
   {
     "bucket": "bucket-name",
     "commit": "git-sha"
   }
   ```

6. **Translates Hugo redirects** to S3 format

**Usage:**

```bash
# Production update
./scripts/sync-and-test-bucket.sh update

# PR preview
./scripts/sync-and-test-bucket.sh preview
```

### Asset Pipeline

The asset pipeline transforms source files into optimized bundles for production.

#### Webpack Configuration

Location: `theme/webpack.config.js`

**Entry Points:**

```javascript
{
  bundle: './src/ts/main.ts',      // Main site JavaScript
  marketing: './src/ts/marketing.ts' // Marketing pages
}
```

**Output:**

```
assets/js/bundle.js
assets/js/marketing.js
assets/css/bundle.css
assets/css/marketing.css
```

**Loaders:**

- TypeScript: `ts-loader`
- Sass: `sass-loader` → `css-loader`
- PostCSS: Tailwind CSS, Autoprefixer

**Plugins:**

- `MiniCssExtractPlugin`: Extract CSS to separate files
- `webpack.ProvidePlugin`: Make jQuery available globally

#### CSS Processing

Multi-stage CSS optimization pipeline:

1. **Tailwind CSS Compilation**
   - Processes utility classes
   - Applies theme configuration
   - Generates responsive variants

2. **PostCSS Processing**
   - Autoprefixer for browser compatibility
   - Custom PostCSS plugins

3. **PurgeCSS** (Production Only)
   - Scans: `public/**/*.html`, `public/js/bundle.*.js`
   - Removes unused CSS classes
   - Safelist patterns:
     - `hs-*` (HubSpot)
     - `highlight`, `code-*` (syntax highlighting)
     - `carousel`, `pagination` (UI components)
     - `st-*` (ShareThis)
     - `icon-*`, `pulumi-*` (custom icons)
   - Skips: `azure-native-v1/**/*` (prevents OOM)

4. **CSSNano Minification**
   - Removes whitespace and comments
   - Optimizes declarations
   - Merges rules

**Script:** `scripts/minify-css.js`

**Output:**

```
public/css/bundle.{CSS_BUNDLE_ID}.css
public/css/marketing.{CSS_BUNDLE_ID}.css
```

#### JavaScript Bundling

**Dependencies:**

- jQuery (provided globally)
- Stencil web components (separate build)
- Custom TypeScript modules

**Output:**

```
public/js/bundle.min.{ASSET_BUNDLE_ID}.js
public/js/marketing.min.{ASSET_BUNDLE_ID}.js
```

#### Asset Bundle IDs

Assets are versioned with bundle IDs for cache busting:

**Format:**

- Production: `{git-sha-short}` (e.g., `a1b2c3d`)
- PR Preview: `pr-{number}-{git-sha-short}` (e.g., `pr-123-a1b2c3d`)

**Environment Variables:**

```bash
ASSET_BUNDLE_ID=a1b2c3d
CSS_BUNDLE_ID=a1b2c3d
REL_CSS_BUNDLE=/css/styles.a1b2c3d.css
REL_JS_BUNDLE=/js/bundle.min.a1b2c3d.js
```

**Hugo Integration:**

Templates access bundle paths via:

```go-html-template
{{ getenv "REL_CSS_BUNDLE" }}
{{ getenv "REL_JS_BUNDLE" }}
```

This ensures every deployment has unique asset URLs, preventing cache issues.

### Hugo Build Process

#### Configuration Files

**Base Configuration:** `config/_default/config.yml`

Key settings:

```yaml
baseURL: https://www.pulumi.com/
timeout: 300000ms  # 300 seconds
enableGitInfo: true
enableRobotsTXT: true

markup:
  goldmark:
    renderer:
      unsafe: true  # Allow HTML in markdown
```

**Production Overrides:** `config/production/config.yml`

```yaml
baseURL: https://www.pulumi.com/
```

#### Environment-Specific Builds

**Development:**

```bash
hugo server --buildDrafts --buildFuture --renderToMemory
```

**Production:**

```bash
hugo --minify --templateMetrics  # Note: --buildFuture is omitted in production
```

**Preview (PRs):**

```bash
hugo --minify --buildFuture --baseURL={preview-url}
```

#### Template Execution

Hugo processes 46+ content directories:

- `/content/docs/` → Documentation
- `/content/blog/` → Blog posts
- `/content/templates/` → Templates
- `/content/product/` → Product pages

> **Note:** content/registry.md is a single landing page file, not a content directory. The full registry application is served from the separate pulumi/registry repository via CloudFront origin routing.

Templates are in `/layouts/` with various shortcodes for:

- Code examples
- Videos and images
- API references
- UI components

#### Content Generation

Hugo generates:

- HTML pages from markdown
- RSS feeds
- Sitemap.xml
- robots.txt
- Meta-refresh redirect pages (from aliases)

#### Minification

With `--minify` flag, Hugo minifies:

- HTML (remove whitespace, comments)
- CSS (via external process)
- JS (via external process)
- JSON
- XML (sitemap, RSS)

### Generated Documentation

The docs site includes auto-generated API reference documentation from multiple sources.

#### TypeDoc - Node.js API Documentation

**Script:** `scripts/run_typedoc.sh`

**Packages Generated:**

1. **pulumi** - Core Pulumi SDK
   - Source: pulumi/pulumi repository
   - Output: `static-prebuilt/docs/reference/pkg/nodejs/pulumi/`

2. **policy** - Pulumi Policy SDK
   - Source: pulumi/pulumi-policy repository
   - Output: `static-prebuilt/docs/reference/pkg/nodejs/pulumi/policy/`

3. **esc-sdk** - ESC SDK
   - Source: pulumi/esc-sdk repository
   - Output: `static-prebuilt/docs/reference/pkg/nodejs/pulumi/esc-sdk/`

**Configuration:**

- TypeDoc version: 0.28.15
- Plugin: `typedoc-plugin-script-inject` for custom scripting
- Format: HTML

**Usage:**

```bash
# Generate all packages
make generate

# Skip repository updates (faster)
NOBUILD=1 make generate

# Generate specific package only
PKGS=pulumi ./scripts/run_typedoc.sh
```

#### Sphinx - Python API Documentation

**Script:** `scripts/generate_python_docs.sh`

**Packages Generated:**

- pulumi
- pulumi_policy
- pulumi_terraform
- pulumi_esc_sdk

**Configuration:**

- Sphinx theme: ReadTheDocs
- Format: dirhtml
- Output: `static-prebuilt/docs/reference/pkg/python/`

**Usage:**

```bash
make generate
```

#### Pulumi CLI - Command Reference

**Command:** `pulumi gen-markdown`

Generates markdown documentation for all Pulumi CLI commands.

**Output:** `content/docs/cli/commands/`

**Format:**

```
pulumi.md
pulumi-cancel.md
pulumi-config.md
pulumi-destroy.md
...
```

**Automation:**

Updated automatically via `pulumi-cli.yml` workflow when new CLI versions are released.

#### ESC CLI - Command Reference

**Command:** `esc gen-docs`

Generates markdown documentation for ESC CLI commands.

**Output:** `content/docs/esc-cli/commands/`

**Automation:**

Updated automatically via `esc-cli.yml` workflow when new ESC versions are released.

---

## GitHub Actions Workflows

The repository uses 24 GitHub Actions workflows organized into categories. All workflows are in `.github/workflows/`.

### Production Deployment

#### build-and-deploy.yml

**Purpose:** Deploy the site to production (<www.pulumi.com>)

**Triggers:**

- Push to `master` branch
- Scheduled: Daily at 6 AM Eastern (7 AM during DST), noon Pacific (1 PM during DST)
- Manual: `workflow_dispatch`

**Environment:** Production (AWS Account: 388588623842)

**Jobs:**

1. **buildSite**
   - Checkout code
   - Fetch secrets from Pulumi ESC
   - Setup: Node.js 24, Go 1.25, Hugo 0.154.5
   - Configure AWS credentials via OIDC (role: ContinuousDelivery, 2-hour session)
   - Install Pulumi CLI
   - Run `make ci_push`:
     - Build site
     - Create S3 bucket with atomic naming
     - Sync content to S3
     - Run Cypress browser tests
     - Generate search index
     - Update CloudFront via Pulumi
     - Apply S3 redirects
   - Archive browser test videos and bucket metadata

2. **notify**
   - Sends Slack alert to `docs-ops` channel on failure

**Infrastructure Deployed:**

- S3 origin bucket (versioned by commit SHA)
- CloudFront distribution (updated to point to new bucket)
- Lambda@Edge functions
- Route53 records
- Response headers policies

**Typical Duration:** 8-12 minutes

#### testing-build-and-deploy.yml

**Purpose:** Deploy to testing environment (<www.pulumi-test.io>)

**Triggers:**

- Push to `master` branch
- Manual: `workflow_dispatch`

**Environment:** Testing (AWS Account: 571684982431)

**Differences from Production:**

- Deploys to separate AWS account
- Uses testing CloudFront distribution
- Sends failures to `docs-ops-test` Slack channel
- Parallel testing environment for validation

**Usage:** Test infrastructure changes before production deployment

### Pull Request Workflows

#### pull-request.yml

**Purpose:** Build and validate PRs, create preview environments

**Triggers:**

- Pull requests to `master` or `release/*` branches
- PR synchronize (new commits pushed)

**Environment:** Testing (AWS Account: 571684982431)

**Security:** Only runs deployment for PRs from the main repository (not forks)

**Jobs:**

1. **buildSite**
   - Check if PR is from fork (skip deployment if true)
   - Build site in preview mode
   - Create PR-specific S3 bucket:

     ```
     www-testing-pulumi-docs-origin-pr-{PR_NUMBER}-{SHA}
     ```

   - Sync built site to preview bucket
   - Run Cypress browser tests
   - Generate search index
   - Run Pulumi preview (non-destructive)
   - Post preview URL to PR comments:

     ```
     http://www-testing-pulumi-docs-origin-pr-123-abc1234.s3-website.us-west-2.amazonaws.com
     ```

   - Archive test results and metadata

2. **notify**
   - Slack alert on failure

**Preview Lifecycle:**

- Created on first PR commit
- Updated on subsequent commits
- Deleted when PR is closed

#### pr-closed.yml

**Purpose:** Clean up PR preview resources

**Triggers:**

- Pull request closed (merged or abandoned)

**Environment:** Testing

**Jobs:**

1. **do_cleanup**
   - Find all S3 buckets matching `*-pr-{PR_NUMBER}-*`
   - Delete buckets and all contents
   - Post cleanup notification to PR:

     ```
     Site previews for this pull request have been removed.
     ```

**Why It Matters:** Prevents accumulation of abandoned preview buckets, reducing AWS costs.

### Automated Documentation Generation

#### pulumi-cli.yml

**Purpose:** Auto-generate CLI documentation when Pulumi CLI is released

**Triggers:**

- Repository dispatch event from pulumi/pulumi repository
- Triggered automatically on Pulumi CLI release

**Jobs:**

1. **build-pulumi-cli-docs**
   - Checkout docs and pulumi repositories
   - Install: pulumictl, Pulumi CLI, Go, Hugo, Node, Python, .NET
   - Generate TypeScript SDK docs with TypeDoc
   - Generate Python SDK docs with Sphinx
   - Generate CLI command docs with `pulumi gen-markdown`
   - Update version files:
     - `static/latest-version`
     - `static/latest-dev-version`
   - Create feature branch: `pulumi/{run-id}-{run-number}`
   - Commit changes with bot credentials
   - Push branch

2. **pull-request**
   - Create PR with auto-merge label
   - Link to triggering pulumi/pulumi release
   - Auto-merge if tests pass

3. **notify**
   - Slack alert on failure

**Why It Matters:** Keeps CLI documentation synchronized with releases automatically.

#### esc-cli.yml

**Purpose:** Auto-generate ESC CLI documentation

**Triggers:**

- Repository dispatch from pulumi/esc repository
- Triggered on ESC CLI release

**Process:** Similar to pulumi-cli.yml but for ESC commands

**Output:**

- ESC CLI command documentation
- Updated `static/esc/latest-version`

#### customer-managed-deployment-agent-cli.yml

**Purpose:** Update CMDA CLI version

**Triggers:**

- Repository dispatch from CMDA repository

**Process:**

- Updates version file for customer-managed-deployment-agent
- Creates automated PR

### Scheduled Maintenance

#### scheduled-test.yml

**Purpose:** Run comprehensive tests on example programs

**Triggers:**

- Daily at 8:00 AM UTC
- Pull requests to master
- Manual: `workflow_dispatch`

**Platform:** Custom Pulumi runner (pulumi-service-ubuntu-24.04-4core)

**Setup:**

- Multi-language runtimes:
  - Go 1.25
  - Node.js 20
  - Python 3.9
  - .NET 8.0
  - Java 11
- Hugo 0.154.5
- Latest Pulumi CLI
- Kubernetes KinD cluster

**Cloud Authentication:**

- AWS via OIDC (gets credentials from Pulumi ESC)
- GCP via workload identity federation
- Azure credentials from ESC

**Tests:** Runs `make test` on ~425 example programs across:

- Languages: TypeScript, Python, Go, C#, Java, YAML
- Clouds: AWS, GCP, Azure, Kubernetes
- Scenarios: Simple deployments, complex architectures

**Notification:** Slack alert for scheduled failures only (not PRs)

**Typical Duration:** 2-2.5 hours (scheduled runs), 3-5 minutes (PR runs)

#### scheduled-upgrade-programs.yml

**Status:** ⚠️ Currently disabled due to disk space issues (see issue #17321)

**Purpose:** Keep example program dependencies up to date

**Triggers:**

- ~~Daily at 6:00 AM UTC~~ (schedule disabled)
- Manual: `workflow_dispatch` (but will likely fail without fixes)

**Jobs:**

- Upgrade Go module dependencies in example programs
- Run tests to verify upgrades work
- Create PR with branch `examples/upgrade`
- Uses PULUMI_BOT_TOKEN for authentication

**Why It Matters:** Prevents example programs from using outdated dependencies with security vulnerabilities.

**Note:** The workflow consistently fails due to GitHub Actions runner disk space exhaustion when testing 385+ example programs. The schedule has been disabled while we investigate proper fixes.

#### bucket-cleanup.yml

**Purpose:** Clean up old S3 buckets in production

**Triggers:**

- Daily at 3:00 PM UTC
- Manual: Not currently configured

**Environment:** Production (AWS Account: 388588623842)

**Jobs:**

- Run `make ci_bucket_cleanup`
- Identify buckets older than retention period
- Delete old origin buckets
- Clean up AWS Parameter Store records

**Retention Policy:** Configurable (typically 7-30 days)

#### bucket-cleanup-testing.yml

**Purpose:** Clean up old S3 buckets in testing

**Triggers:**

- Daily at 3:00 PM UTC
- Manual: `workflow_dispatch`

**Environment:** Testing (AWS Account: 571684982431)

**Process:** Same as production cleanup but for testing environment

### Quality Assurance

#### check-links.yml

**Purpose:** Verify all internal and external links

**Triggers:**

- Daily at 3:00 PM UTC
- Manual: `workflow_dispatch`

**Jobs:**

- Run `make check_links`
- Crawl production site (<www.pulumi.com>)
- Check all links (internal and external)
- Report broken links

**Output:** Slack notification with broken link report

#### check-search-urls.yml

**Purpose:** Validate search index integrity

**Triggers:**

- Daily at 3:00 PM UTC
- Manual: `workflow_dispatch`

**Jobs:**

- Run `make check_search_urls`
- Query Algolia search index
- Verify all indexed URLs are accessible
- Report missing or broken URLs

**Why It Matters:** Ensures search results don't link to 404 pages.

#### check-lighthouse.yml

**Purpose:** Monitor site performance and accessibility

**Triggers:**

- Daily at 3:00 PM UTC
- Manual: `workflow_dispatch`

**Pages Tested:**

- Homepage (<www.pulumi.com>)
- Product page
- Pricing page
- Get Started guide
- Documentation (concepts)
- Registry homepage
- Registry package page (AWS S3 bucket)

**Metrics:**

- Performance
- Accessibility
- Best Practices
- SEO

**Output:** Lighthouse scores and recommendations

### Utility Workflows

#### update-search-index.yml

**Purpose:** Update Algolia search index on demand

**Triggers:**

- Hourly (every 60 minutes)
- Manual: `workflow_dispatch`

**Environment:** Production

**Jobs:**

- Run `make ci_update_search_index`
- Extract content from built site
- Update Algolia indices
- Apply index settings and ranking rules

**Indices Updated:**

- pulumi (main documentation)
- blog posts
- registry packages

#### scheduled-upstream-sync.yaml

**Purpose:** Sync private fork with upstream

**Triggers:**

- Every 15 minutes
- Manual: `workflow_dispatch`

**Target:** Only runs on private fork repositories (not pulumi/docs)

**Jobs:**

- Sync latest commits from pulumi/docs to downstream fork
- Uses Fork-Sync-With-Upstream action
- Preserves private fork changes

**Why It Matters:** Keeps private documentation fork synchronized with public repository.

### Other Workflows

The repository includes 9 additional utility workflows for automation and project management:

**Automation and Auto-merge:**

- **automerge-workflow.yml**: Auto-merge approved PRs from trusted sources
- **auto-approve-for-auto-merge.yml**: Auto-approve PRs that meet auto-merge criteria (trusted bots, dependency updates)

**AI-Assisted Development:**

- **claude.yml**: AI-assisted code analysis and suggestions (triggered by @claude mentions in issues/PRs)
- **claude-code-review.yml**: AI-powered code review automation for pull requests

Both workflows include a permission check step that verifies the triggering user has write access to the repository before running Claude. Users without write access will see the workflow skip Claude execution.

**Project Management:**

- **add-triage-label.yml**: Automatically apply triage labels to new issues
- **add-to-project.yml**: Add issues and PRs to GitHub Projects for tracking

**Secret Management:**

- **export-repo-secrets.yml**: Export repository secrets for CI/CD consumption
- **export-secrets.yml**: General-purpose secrets export utility for workflows

**Development Versions:**

- **pulumi-cli-dev-version.yml**: Handle development and pre-release versions of Pulumi CLI documentation

These workflows support repository maintenance, automation, and developer experience but are not part of the core build and deployment pipeline documented in detail above.

### Workflow Summary Matrix

| Workflow | Trigger | Environment | Duration | Purpose |
|----------|---------|-------------|----------|---------|
| build-and-deploy | Push to master, Scheduled | Production | 8-12 min | Production deployment |
| testing-build-and-deploy | Push to master, Manual | Testing | 8-12 min | Testing deployment |
| pull-request | PRs to master | Testing | 10-15 min | PR validation & preview |
| pr-closed | PR closed | Testing | <1 min | Cleanup preview resources |
| pulumi-cli | Repository dispatch | N/A | 5-10 min | Auto-generate CLI docs |
| esc-cli | Repository dispatch | N/A | 3-5 min | Auto-generate ESC docs |
| scheduled-test | Daily 8 AM UTC, PRs | Testing | 2-2.5 hrs (scheduled), 3-5 min (PR) | Test example programs |
| scheduled-upgrade-programs | ~~Daily 6 AM UTC~~ (disabled) | N/A | N/A (fails) | Update dependencies |
| bucket-cleanup | Daily 3 PM UTC | Production | 2-5 min | Delete old buckets |
| bucket-cleanup-testing | Daily 3 PM UTC | Testing | 2-5 min | Delete old buckets |
| check-links | Daily 3 PM UTC | N/A | 5-10 min | Verify links |
| check-search-urls | Daily 3 PM UTC | N/A | 2-5 min | Validate search index |
| check-lighthouse | Daily 3 PM UTC | N/A | 3-8 min | Performance monitoring |
| update-search-index | Hourly | Production | 2-5 min | Update Algolia |

> **Note:** The table above shows the 14 core deployment and testing workflows. An additional 10 utility workflows (automation, AI review, project management, secret management, dev versions) are listed in the "Other Workflows" section, bringing the total to 24 workflows.

---

## Deployment Infrastructure

All deployment infrastructure is managed as code using Pulumi (TypeScript). Infrastructure code is in `infrastructure/`.

### Infrastructure as Code

**Primary File:** `infrastructure/index.ts`

**Pulumi Stack Configuration:**

- **Production:** `Pulumi.www-production.yaml`
- **Testing:** `Pulumi.www-testing.yaml`

**Stack References:**

The docs infrastructure integrates with other Pulumi projects via stack references:

```typescript
const registryStack = new pulumi.StackReference('pulumi/registry/production');
const answersStack = new pulumi.StackReference('pulumi/answers/production');
const aiAppStack = new pulumi.StackReference('pulumi/pulumi-ai-app-infra/prod');
const guidesStack = new pulumi.StackReference('pulumi/guides/production');
```

These provide outputs like domain names, ALB ARNs, and distribution IDs for integration.

#### How stack references work for origins

The docs CloudFront distribution uses StackReferences to dynamically configure origins from external stacks:

- **Registry**: Reads `cloudFrontDomain` from `pulumi/registry/{environment}`
- **Guides**: Reads `cloudFrontDomain` from `pulumi/guides/{environment}`
- **Answers**: Reads `cloudFrontDomain` from `pulumi/answers/{environment}`

**When external stacks are updated:**

1. External stack (for example, registry) deploys → creates new CloudFront distribution with new domain
2. Docs infrastructure automatically reads the updated output via StackReference on next deployment
3. Docs CloudFront distribution origins are updated with the new domain
4. CloudFront changes propagate globally (15-20 minutes)

**Important:** StackReferences always read the latest outputs from referenced stacks. No manual refresh is needed.

### AWS Resources

#### S3 Buckets

**Origin Bucket (Ephemeral):**

Created for each deployment with atomic naming:

```
www-{environment}-pulumi-docs-origin-{identifier}
```

Examples:

- Production: `www-production-pulumi-docs-origin-a1b2c3d4`
- Testing: `www-testing-pulumi-docs-origin-pr-123-abc1234`

**Configuration:**

- Website hosting enabled (index.html, 404.html)
- Public read access via ACL
- Object ownership: BucketOwnerPreferred
- Versioning: Disabled (ephemeral buckets)
- Lifecycle: Manual cleanup via bucket-cleanup workflows

**Uploads Bucket (Persistent):**

Stores user-uploaded assets and large files.

**Bundles Bucket (Temporary):**

Stores CSS/JS bundles during deployment.

**Fallback Bucket (Optional):**

Direct S3 website serving (not used in production).

**Logs Bucket:**

Stores CloudFront access logs.

Name: `{website-domain}-website-logs`
Format: Parquet
Delivery: CloudWatch Logs infrastructure v2

#### CloudFront Distribution

**Purpose:** Global CDN serving the production site

**Domain Aliases:**

- Production: <www.pulumi.com>
- Testing: <www.pulumi-test.io>

**SSL/TLS:**

- ACM Certificate (us-east-1)
- ARN from Pulumi config
- SNI-only (no dedicated IP)
- Minimum protocol: TLSv1.2_2021

**Origins:**

1. **Main Origin** - S3 website bucket
   - Path: /
   - Origin ID: S3-{bucket-name}
   - Custom origin (website endpoint, not S3 endpoint)

2. **Uploads Origin** - Uploads bucket
   - Path: /uploads
   - Origin ID: uploads-bucket

3. **Registry Origin** - From pulumi/registry stack
   - Path: /registry
   - ALB from stack reference

4. **Answers Origin** - From pulumi/answers stack
   - Path: /answers
   - ALB from stack reference

5. **AI App Origin** - From pulumi-ai-app-infra stack
   - Path: /ai, /pulumi-ai
   - Domain from stack reference

6. **Guides Origin** - From pulumi/guides stack
   - Path: /guides
   - ALB from stack reference

**Cache Behaviors:**

| Path Pattern | Origin | TTL | Notes |
|--------------|--------|-----|-------|
| Default | S3 Main | 5 min | General content |
| /css/*.css | S3 Main | 1 year | Versioned assets |
| /js/*.js | S3 Main | 1 year | Versioned assets |
| /registry/* | Registry | None | Dynamic content |
| /guides/* | Guides | None | Dynamic content |
| /ai/* | AI App | None | Dynamic content |
| /uploads/* | Uploads | 1 hour | User uploads |
| /fonts/* | S3 Main | 1 hour | Web fonts |
| /icons/* | S3 Main | 1 hour | Icons |
| /logos/* | S3 Main | 1 hour | Logos |
| *.woff,*.woff2 | S3 Main | 1 year | Font files |

**Compression:** Enabled (gzip, brotli)

**Price Class:** All (global distribution)

**Custom Error Responses:**

- 404 → 404.html

**Geo Restrictions:** None

#### Lambda@Edge Functions

**1. Edge Redirects**

**Event Type:** origin-request

**Purpose:** Handle cross-origin redirects at the edge

**Use Cases:**

- Redirect legacy URLs
- Handle cross-repository navigation
- Apply custom routing logic

**Configuration:**

```typescript
const edgeRedirects = new aws.lambda.Function("edge-redirects", {
    runtime: "nodejs22.x",
    handler: "index.handler",
    role: edgeRole.arn,
    code: new pulumi.asset.AssetArchive({
        "index.js": new pulumi.asset.StringAsset(redirectCode)
    })
});
```

**2. AI Answers Rewrites**

**Event Type:** origin-response

**Purpose:** Rewrite 404 responses to 410 (Gone) for unpublished AI answers

**Applied To:** `/ai/answers/*` paths

**Why:** Informs search engines that AI answers are intentionally unpublished

#### Route53 DNS

**Hosted Zone:** From config (<www.pulumi.com> or <www.pulumi-test.io>)

**A Record:**

```typescript
new aws.route53.Record("root-record", {
    zoneId: hostedZoneId,
    name: websiteDomain,
    type: "A",
    aliases: [{
        name: distribution.domainName,
        zoneId: distribution.hostedZoneId,
        evaluateTargetHealth: false
    }]
});
```

**AAAA Record:** IPv6 alias (same as A record)

### Atomic Deployment Process

The atomic deployment strategy ensures zero-downtime deployments with instant rollback capability.

**How It Works:**

1. **Build Phase**

   ```bash
   ./scripts/build-site.sh
   ```

   - Compile assets
   - Generate HTML
   - Optimize CSS
   - Create search index

2. **Create New Bucket**

   ```bash
   ./scripts/sync-and-test-bucket.sh update
   ```

   - Generate unique bucket name with commit SHA
   - Create S3 bucket
   - Configure website hosting
   - Enable public access

3. **Sync Content**

   ```bash
   aws s3 sync public/ s3://{bucket}/ --delete
   ```

   - Upload all files
   - Set content types
   - Apply cache headers

4. **Validate Deployment**

   ```bash
   # Check file count
   aws s3 ls s3://{bucket}/ --recursive | grep index.html | wc -l
   # Must meet minimum threshold (verify specific value in sync-and-test-bucket.sh)
   ```

5. **Run Tests**

   ```bash
   ./scripts/run-browser-tests.sh
   ```

   - Cypress smoke tests
   - Verify critical pages

6. **Update Infrastructure**

   ```bash
   ./scripts/run-pulumi.sh
   ```

   - Pulumi reads `origin-bucket-metadata.json`
   - Updates CloudFront origin to new bucket
   - Applies infrastructure changes

7. **Apply Redirects**

   ```bash
   ./scripts/make-s3-redirects.sh
   ```

   - Generate S3 redirect rules
   - Apply to bucket

8. **Clean Up Old Buckets** (Automated)
   - Scheduled cleanup workflow removes buckets older than retention period
   - Keeps recent buckets for potential rollback

**Benefits:**

- **Zero Downtime:** CloudFront continues serving old bucket until new one is ready
- **Instant Rollback:** Revert CloudFront origin to previous bucket (< 1 minute)
- **Validation:** Test new deployment before switching traffic
- **Immutable Deployments:** Each deployment is a complete snapshot
- **Debugging:** Old buckets remain available for comparison

**Rollback Procedures:**

Choose the appropriate method based on the situation:

**Method 1: Git Revert (Primary - Recommended)**

Use this when the issue is caused by recent code/content/configuration changes (most common scenario).

**Prerequisites:** GitHub write access

**Steps:**

```bash
# Find the problematic commit
git log --oneline -10

# Revert it
git revert {commit-sha}

# Push to master
git push origin master
```

The push automatically triggers build and deployment of the reverted code (~10-15 minutes).

**When to use:** Bad code changes, configuration errors, content issues
**Pros:** Simple, automatic, preserves git history, minimal access needed
**Cons:** Takes full build time (~10-15 min)

---

**Method 2: Pin to Previous Bucket (For Infrastructure Issues)**

Use this for faster rollback when the problem isn't in code (e.g., infrastructure issue, broken integration).

**Prerequisites:** Access to Pulumi Cloud (pulumi/docs organization)

**Steps:**

1. Find the previous bucket name:
   - Check GitHub Actions → Previous successful run → Artifacts → `origin-bucket-metadata.json`
   - Bucket format: `www-production-pulumi-docs-origin-{git-sha}`

2. Update Pulumi stack config:
   - Open <https://app.pulumi.com/pulumi/docs/www-production>
   - Go to Settings → Configuration
   - Set `originBucketNameOverride` to the previous bucket name
   - Save

3. Trigger deployment:
   - Go to GitHub → Actions → "Build and deploy" workflow
   - Click "Run workflow" → Select master branch → Run

CloudFront switches origins within 1-2 minutes (no rebuild required).

**When to use:** Infrastructure issues, external service problems, need fast rollback
**Pros:** Very fast (~1-2 min), no rebuild needed
**Cons:** Requires Pulumi Cloud access, doesn't fix code issues

**Important:** After the issue is resolved, clear the override to resume normal deployments:

```yaml
# In Pulumi Cloud console, set:
originBucketNameOverride: ""
```

---

**Method 3: Local Pulumi Execution (Advanced)**

For team members with complete local development environment.

**Prerequisites:**

- Pulumi CLI installed
- `PULUMI_ACCESS_TOKEN` environment variable set
- AWS CLI configured with SSO/OIDC
- Repository cloned locally

**Steps:**

```bash
# From repository root
cd infrastructure

# Select the production stack
pulumi stack select www-production

# List available buckets
aws s3 ls | grep pulumi-docs-origin | sort

# Pin to previous bucket
pulumi config set originBucketNameOverride {previous-bucket-name}

# Deploy (updates CloudFront only, no rebuild)
pulumi up

# Later: Clear override to resume normal deployments
pulumi config set originBucketNameOverride ""
pulumi up
```

**Rollback Time:** 1-2 minutes for CloudFront origin switch

### Redirect Management

The docs site uses three complementary redirect strategies.

#### 1. Hugo Aliases (Preferred for Doc Pages)

**When to Use:** Moving or renaming Hugo content files

**How It Works:**

Add `aliases` to frontmatter:

```yaml
---
title: New Page Title
aliases:
- /old/path/to/page/
- /another/old/path/
---
```

Hugo generates meta-refresh HTML pages at old paths:

```html
<!DOCTYPE html>
<html>
<head>
  <meta http-equiv="refresh" content="0; url=/new/path/">
  <meta name="robots" content="noindex">
</head>
</html>
```

**Verification:**

Use scripts in `scripts/alias-verification/`:

```bash
# After moving files
cd scripts/alias-verification
npm install
node verify-aliases.js
```

**Pros:**

- Automatic (Hugo handles it)
- Preserves SEO (meta-refresh + robots tag)
- No infrastructure changes needed

**Cons:**

- Not true 301 redirects (but search engines understand meta-refresh)
- Requires page to exist in Hugo content

#### 2. S3 Bucket Redirects (for Generated Content)

**When to Use:** Redirecting non-Hugo content (generated docs, CLI references)

**How It Works:**

Add redirect rules to text files in `scripts/redirects/`:

```
# scripts/redirects/neo-redirects.txt
source-path|destination-url
docs/old/path/index.html|/docs/new/path/
```

**Format:** `source-path|destination-url`

**Script:** `scripts/make-s3-redirects.sh`

**Process:**

1. Read redirect files from `scripts/redirects/*.txt`
2. Convert to S3 redirect rules
3. Apply to S3 bucket via website configuration

**S3 Redirect Rule:**

```xml
<RoutingRule>
  <Condition>
    <KeyPrefixEquals>docs/old/path/index.html</KeyPrefixEquals>
  </Condition>
  <Redirect>
    <HostName>www.pulumi.com</HostName>
    <ReplaceKeyWith>docs/new/path/</ReplaceKeyWith>
    <HttpRedirectCode>301</HttpRedirectCode>
  </Redirect>
</RoutingRule>
```

**Pros:**

- True 301 redirects
- Works for any path
- No Hugo involvement

**Cons:**

- Must be manually added to redirect files
- Deployed per bucket (atomic deployment limitation)

#### 3. Lambda@Edge Redirects (for Cross-Origin)

**When to Use:** Redirecting between different origins (docs → registry, etc.)

**How It Works:**

Lambda function intercepts requests at CloudFront edge:

```javascript
exports.handler = async (event) => {
    const request = event.Records[0].cf.request;

    if (request.uri.startsWith('/ai')) {
        return {
            status: '301',
            statusDescription: 'Moved Permanently',
            headers: {
                location: [{
                    key: 'Location',
                    value: '/answers'
                }]
            }
        };
    }

    return request;
};
```

**Deployment:** Managed in `infrastructure/index.ts`

**Pros:**

- Works across origins
- True 301 redirects
- Lowest latency (executes at edge)

**Cons:**

- Requires code deploy
- More complex to maintain

#### Redirect Strategy Decision Tree

```
Is the file managed by Hugo?
├─ Yes → Use Hugo aliases
└─ No → Is it same origin?
    ├─ Yes → Use S3 redirects
    └─ No → Use Lambda@Edge
```

### Security Headers

Production CloudFront distribution applies security headers via response headers policy:

```typescript
const securityHeaders = new aws.cloudfront.ResponseHeadersPolicy("security-headers", {
    securityHeadersConfig: {
        strictTransportSecurity: {
            accessControlMaxAgeSec: 31536000,
            includeSubdomains: true,
            override: true
        },
        frameOptions: {
            frameOption: "DENY",
            override: true
        },
        xssProtection: {
            modeBlock: true,
            protection: true,
            override: true
        },
        contentTypeOptions: {
            override: true
        },
        referrerPolicy: {
            referrerPolicy: "strict-origin-when-cross-origin",
            override: true
        }
    }
});
```

**Headers Applied:**

- `Strict-Transport-Security: max-age=31536000; includeSubDomains`
- `X-Frame-Options: DENY`
- `X-XSS-Protection: 1; mode=block`
- `X-Content-Type-Options: nosniff`
- `Referrer-Policy: strict-origin-when-cross-origin`

### Environment-Specific Configuration

#### Production (<www.pulumi.com>)

**File:** `Pulumi.www-production.yaml`

```yaml
config:
  aws:region: us-west-2
  www.pulumi.com:addSecurityHeaders: "true"
  www.pulumi.com:doEdgeRedirects: "true"
  www.pulumi.com:doAIAnswersRewrites: "true"
  www.pulumi.com:websiteDomain: www.pulumi.com
  www.pulumi.com:websiteLogsBucketName: www-prod.pulumi.com-website-logs
  www.pulumi.com:hostedZone: www.pulumi.com
  www.pulumi.com:registryStack: pulumi/registry/production
  www.pulumi.com:guidesStack: pulumi/guides/production
  www.pulumi.com:answersStack: pulumi/answers/production
  www.pulumi.com:cdnLogDeliverySourceName: CreatedByCloudFront-E3PRSXO1BZJEEY
  www.pulumi.com:enableDataWarehouseAccess: "true"
  www.pulumi.com:certificateArn: arn:aws:acm:us-east-1:388588623842:certificate/...
```

#### Testing (<www.pulumi-test.io>)

**File:** `Pulumi.www-testing.yaml`

```yaml
config:
  aws:region: us-west-2
  www.pulumi.com:addSecurityHeaders: "true"
  www.pulumi.com:doEdgeRedirects: "true"
  www.pulumi.com:doAIAnswersRewrites: "true"
  www.pulumi.com:websiteDomain: www.pulumi-test.io
  www.pulumi.com:websiteLogsBucketName: pulumi-test-io-website-logs
  www.pulumi.com:hostedZone: www.pulumi-test.io
  www.pulumi.com:registryStack: pulumi/registry/testing
  www.pulumi.com:guidesStack: pulumi/guides/testing
  www.pulumi.com:answersStack: pulumi/answers/testing
  www.pulumi.com:certificateArn: arn:aws:acm:us-east-1:571684982431:certificate/...
```

---

## Testing Strategy

The repository employs multiple testing strategies to ensure quality and reliability.

### Linting and Formatting

#### Markdown Linting

**Tool:** Custom markdown linter

**Configuration:** Cascading configuration using `.markdownlint-base.json` at the root and optional `.markdownlint.json` files in subdirectories.

**Rules Enforced:**

- Heading levels increment by one
- No trailing spaces
- Proper list formatting
- Code block language specification
- No bare URLs (must use markdown links)

**Usage:**

```bash
make lint
```

**Script:** `scripts/lint/lint-markdown.js`

#### Code Formatting

**Tool:** Prettier

**Scope:**

- Markdown files
- JavaScript/TypeScript
- JSON files
- YAML files

**Usage:**

```bash
# Check formatting
make lint

# Auto-fix
make format
```

**Configuration:** `.prettierrc.json`

**Version:** Prettier v2.8.8

**Why v2.x Instead of v3.x:**

We intentionally use Prettier v2.x instead of the newer v3.x due to significant performance regressions:

- **Prettier v2.x performance:** ~4 seconds for full repository lint
- **Prettier v3.x performance:** ~28 seconds for full repository lint (6x slower)
- **Root cause:** Prettier v3.x performs 45% more filesystem operations for config resolution, checking 33 .editorconfig files across node_modules directories

**Impact on Workflows:**

- **Local commits:** Fast (1-2 seconds) thanks to `lint-staged` checking only changed files
- **CI full lint:** Fast (~16 seconds total) thanks to v2.x performance
- **Git hooks:** Pre-commit hooks run `lint-staged` instead of full `make lint` for speed

**When to Upgrade:**

We will consider upgrading to Prettier v3.x when:

1. The Prettier team addresses the config resolution performance issues
2. Full repository linting with v3.x approaches v2.x performance (<10 seconds)
3. Benefits of v3.x features outweigh the performance cost

See [Prettier's CLI Performance Deep Dive](https://prettier.io/blog/2023/11/30/cli-deep-dive) for details on the performance characteristics.

#### Trailing Space Removal

Remove trailing spaces from files:

```bash
sed -i '' 's/[[:space:]]*$//' file1.md file2.md
```

### Browser Testing

#### Cypress Tests

**Location:** `cypress/integration/`

**Tests:**

- Smoke tests on deployed sites
- Critical path verification (homepage, docs, registry)
- Form submissions
- Search functionality
- Navigation menus

**Execution:**

```bash
# Local
npx cypress open

# CI
./scripts/run-browser-tests.sh
```

**CI Integration:**

Runs automatically in:

- `pull-request.yml` (PR builds)
- `build-and-deploy.yml` (production deployments)

**Artifacts:**

Video recordings archived in GitHub Actions artifacts on failure.

**Typical Duration:** 3-5 minutes

### Post-Deployment Health Checks

After Pulumi updates complete, automated health checks validate the deployed site using curl-based tests.

**Workflow:** `.github/workflows/post-deployment-health-check.yml`

**Implementation:** Inline bash script using curl (no external dependencies or repository checkout required)

**What it checks:**

- Core pages (homepage, docs, registry)
- SDK documentation endpoints (Node.js, Python, .NET, Java)
- High-traffic documentation pages
- Lambda@Edge redirect functionality

**When it runs:**

- Automatically after `build-and-deploy.yml` or `testing-build-and-deploy.yml` completes successfully
- Can be manually triggered via GitHub Actions UI
- Can be scheduled (add `schedule` trigger to workflow)

**On failure:**

- Dedicated Slack notification sent to #docs-ops (production) or #docs-ops-test (testing)
- Notification includes deployment info, commit SHA, and link to logs
- Health check workflow marked as failed in GitHub Actions
- Deployment workflow remains marked as successful (separation of concerns)

### Local testing

```bash
# Test individual endpoint
curl -s -o /dev/null -w "%{http_code}\n" -L https://www.pulumi.com/docs

# Test redirect
curl -s -o /dev/null -w "%{http_code}|%{redirect_url}\n" https://www.pulumi.com/docs/intro/cloud-providers/aws/
```

### Adding new checks

Edit `.github/workflows/post-deployment-health-check.yml` and add calls to:

- `check_endpoint` function for page availability checks (expects 200 status)
- `check_redirect` function for Lambda@Edge redirect tests (expects 301 with location match)

### Example Program Testing

**Purpose:** Validate that all code examples are functional

**Programs Tested:** ~425 programs in `/static/programs/`

**Languages:**

- TypeScript
- Python
- Go
- C# (.NET)
- Java
- YAML

**Cloud Providers:**

- AWS
- Google Cloud
- Azure
- Kubernetes
- Digital Ocean

**Test Script:** `scripts/programs/test.sh`

**Process:**

1. For each program directory:
   - Install dependencies
   - Run `pulumi preview` (verify no errors)
   - Check output for expected resources

2. Multi-cloud authentication:
   - AWS via OIDC
   - GCP via workload identity
   - Azure via service principal

**Usage:**

```bash
# Test all programs
make test

# Test specific program
ONLY_TEST="aws-s3-bucket-typescript" ./scripts/programs/test.sh
```

**CI Execution:**

- **scheduled-test.yml**: Daily at 8 AM UTC (full test suite)
- **pull-request.yml**: On PRs (quick validation with limited scope)

**Typical Duration (based on historical runs):** 2-2.5 hours (scheduled runs with full test suite), 3-5 minutes (PR runs with limited scope)

> **Note:** The repository contains ~425 program directories.

### Link Checking

**Purpose:** Prevent broken links in documentation

**Script:** `scripts/link-checker/check-links.sh`

**Process:**

1. Crawl production site (<www.pulumi.com>)
2. Check all links (internal and external)
3. Report:
   - 404 Not Found
   - Timeout
   - Invalid SSL

**Types of Links Checked:**

- Internal documentation links
- External reference links
- Images and assets
- Anchors (# fragments)

**Usage:**

```bash
make check_links
```

**CI Execution:** Daily at 3 PM UTC via `check-links.yml`

**Output:** Report posted to Slack

### Search Validation

**Purpose:** Ensure search index integrity

**Script:** `scripts/search/check-urls.sh`

**Process:**

1. Query Algolia search index
2. Extract all indexed URLs
3. Verify each URL is accessible (HTTP 200)
4. Report broken URLs

**Why It Matters:** Prevents search results from linking to 404 pages, which hurts user experience and SEO.

**Usage:**

```bash
make check_search_urls
```

**CI Execution:** Daily at 3 PM UTC via `check-search-urls.yml`

### Performance Monitoring

**Tool:** Lighthouse CI

**Pages Monitored:**

- Homepage (<www.pulumi.com>)
- Product page (/product/)
- Pricing (/pricing/)
- Get Started (/docs/get-started/)
- Documentation concepts (/docs/intro/concepts/resources/)
- Registry (/registry/)
- Registry package (/registry/packages/aws/api-docs/s3/bucket/)

**Metrics:**

- **Performance:** Page load speed, time to interactive
- **Accessibility:** WCAG compliance, ARIA labels
- **Best Practices:** HTTPS, console errors, security
- **SEO:** Meta tags, structured data, indexability

**Thresholds:**

Configurable in Lighthouse CI configuration. Typical thresholds:

- Performance: > 90
- Accessibility: > 95
- Best Practices: > 95
- SEO: > 95

**Usage:**

```bash
# Local
npm install -g @lhci/cli
lhci autorun
```

**CI Execution:** Daily at 3 PM UTC via `check-lighthouse.yml`

**Output:** Lighthouse reports with scores and recommendations

---

## Environment Management

The Pulumi docs infrastructure operates across multiple environments for different purposes.

### Production Environment

**Domain:** <www.pulumi.com>

**AWS Account:** 388588623842

**Region:** us-west-2

**Pulumi Stack:** `www-production`

**CloudFront Distribution:** E3PRSXO1BZJEEY

**Deployment Triggers:**

- Push to `master` branch
- Scheduled: Daily at 6 AM Eastern (7 AM during DST), noon Pacific (1 PM during DST)
- Manual via workflow_dispatch

**S3 Bucket Pattern:**

```
www-production-pulumi-docs-origin-{git-sha}
```

**Search Index:** Production Algolia index (appId: OCCYMHQD)

**Logs:** CloudWatch Logs, S3 logs bucket

**Access:**

- Developers: Via Pulumi organization
- CI/CD: Via OIDC role `arn:aws:iam::388588623842:role/ContinuousDelivery`

### Testing Environment

**Domain:** <www.pulumi-test.io>

**AWS Account:** 571684982431

**Region:** us-west-2

**Pulumi Stack:** `www-testing`

**Purpose:**

- Validate infrastructure changes before production
- Parallel testing environment
- PR preview deployments

**Deployment Triggers:**

- Push to `master` branch
- Manual via workflow_dispatch

**S3 Bucket Pattern:**

```
www-testing-pulumi-docs-origin-{identifier}
```

**Differences from Production:**

- Separate AWS account
- Separate CloudFront distribution
- Separate search indices
- Less restrictive security policies (for testing)
- Slack alerts go to `docs-ops` channel (same as production)

### PR Preview Environments

**Purpose:** Per-PR preview sites for reviewing changes

**AWS Account:** 571684982431 (Testing)

**URL Pattern:**

```
http://www-testing-pulumi-docs-origin-pr-{PR_NUMBER}-{SHA}.s3-website.us-west-2.amazonaws.com
```

**Lifecycle:**

1. **Created:** On first PR commit
2. **Updated:** On subsequent commits
3. **Deleted:** When PR is closed

**Characteristics:**

- Direct S3 website hosting (no CloudFront)
- Ephemeral (deleted after PR closes)
- No custom domain
- Limited search indexing

**Bucket Naming:**

```
www-testing-pulumi-docs-origin-pr-123-abc1234
```

**Cleanup:** Automated via `pr-closed.yml` workflow

### Dev Stacks

**Purpose:** Personal development and testing stacks

**Who Can Use:** Pulumi organization members

**Naming:** `dev-{username}`

**Usage:**

```bash
# Create dev stack
pulumi stack init dev-myname

# Deploy
pulumi up

# Destroy
pulumi destroy
```

**Benefits:**

- Test infrastructure changes without affecting production or testing
- Personal sandbox environment
- Full CloudFront distribution (not just S3)

**Costs:** Developer is responsible for cleaning up

### Environment Variables

Critical environment variables used across all environments:

#### Build Variables

| Variable | Purpose | Example |
|----------|---------|---------|
| `ASSET_BUNDLE_ID` | Asset versioning | `abc1234` or `pr-123-abc1234` |
| `CSS_BUNDLE_ID` | CSS versioning | Same as ASSET_BUNDLE_ID |
| `REL_CSS_BUNDLE` | CSS path for Hugo | `/css/styles.abc1234.css` |
| `REL_JS_BUNDLE` | JS path for Hugo | `/js/bundle.min.abc1234.js` |
| `HUGO_BASEURL` | Site base URL | `https://www.pulumi.com/` |
| `DEPLOYMENT_ENVIRONMENT` | Environment name | `production` or `testing` |
| `NODE_OPTIONS` | Node.js memory | `--max_old_space_size=8192` |

#### AWS Variables

| Variable | Purpose | Source |
|----------|---------|--------|
| `AWS_REGION` | AWS region | Pulumi config |
| `AWS_ACCESS_KEY_ID` | AWS credentials | OIDC (temporary) |
| `AWS_SECRET_ACCESS_KEY` | AWS credentials | OIDC (temporary) |
| `AWS_SESSION_TOKEN` | AWS credentials | OIDC (temporary) |
| `CDN_PULUMI_URN` | CloudFront URN | Pulumi stack output |

#### Pulumi Variables

| Variable | Purpose | Source |
|----------|---------|--------|
| `PULUMI_ACCESS_TOKEN` | Pulumi API access | Pulumi ESC |
| `PULUMI_STACK_NAME` | Current stack | Workflow config |
| `PULUMI_CONFIG_PASSPHRASE` | Stack encryption | Not used (ESC) |

#### External Service Variables

| Variable | Purpose | Source |
|----------|---------|--------|
| `ALGOLIA_APP_ID` | Search app ID | Pulumi ESC |
| `ALGOLIA_APP_ADMIN_KEY` | Search admin key | Pulumi ESC |
| `SENTRY_AUTH_TOKEN` | Error monitoring | Pulumi ESC |
| `SLACK_WEBHOOK_URL` | Notifications | Pulumi ESC |
| `GITHUB_TOKEN` | GitHub API | GitHub Actions |

#### Feature Flags

| Variable | Purpose | Values |
|----------|---------|--------|
| `NOBUILD` | Skip repo rebuilds | `1` or unset |
| `ONLY_TEST` | Test single program | Program name |

### Pulumi ESC Integration

**What is Pulumi ESC?**

Pulumi ESC (Environments, Secrets, and Configuration) is a centralized secrets and config management service.

**Why Use It?**

- No static credentials in GitHub
- OIDC authentication for AWS
- Dynamic credential generation
- Audit logging
- Centralized secret rotation

**GitHub Actions Integration:**

```yaml
- uses: pulumi/esc-action@v1
  with:
    organization: pulumi
    environment: github-secrets/pulumi-docs
  env:
    PULUMI_ACCESS_TOKEN: ${{ secrets.PULUMI_ACCESS_TOKEN }}
```

**What It Provides:**

All secrets and config for:

- AWS credentials (via OIDC)
- Pulumi tokens
- Algolia keys
- Sentry tokens
- Slack webhooks
- GCP credentials
- Azure credentials

**No Hardcoded Secrets:** All sensitive values retrieved dynamically at runtime.

---

## Troubleshooting

Common issues and their solutions.

### Build Issues

#### Hugo Version Mismatch

**Symptom:** Build fails with Hugo errors

**Solution:**

```bash
# Check Hugo version
hugo version

# Should be: hugo v0.154.5

# Update if different
# macOS:
brew upgrade hugo

# Verify in workflows that Hugo version matches
grep "hugo-version" .github/workflows/*.yml
```

> **Note:** Hugo version must match **exactly** across all workflows. Version mismatches cause template compatibility issues.

#### Node.js Memory Issues

**Symptom:** Build fails with "JavaScript heap out of memory"

**Solution:**

```bash
# Increase Node.js memory
export NODE_OPTIONS="--max_old_space_size=8192"

# Or in package.json scripts:
"build": "NODE_OPTIONS='--max_old_space_size=8192' webpack"
```

#### Dependency Installation Failures

**Symptom:** `make ensure` fails with peer dependency errors

**Solution:**

TypeDoc peer dependency warnings are expected and safe to ignore:

```
npm WARN ERESOLVE overriding peer dependency
npm WARN While resolving: typedoc-plugin-script-inject@2.0.0
```

Real errors look different (missing packages, network timeouts). If you see those:

```bash
# Clear cache and retry
make clean
yarn cache clean
make ensure
```

#### Asset Compilation Errors

**Symptom:** Webpack build fails

**Solution:**

```bash
# Check theme dependencies
cd theme
yarn install

# Rebuild assets
yarn run build

# Check for TypeScript errors
yarn run tsc --noEmit
```

#### Missing Environment Variables

**Symptom:** Build fails with "undefined environment variable"

**Solution:**

Check that required variables are set:

```bash
# For local builds
export ASSET_BUNDLE_ID=$(git rev-parse --short HEAD)
export CSS_BUNDLE_ID=$ASSET_BUNDLE_ID

# For CI/CD, check Pulumi ESC configuration
pulumi config -s www-production
```

### Deployment Issues

#### S3 Bucket Creation Failures

**Symptom:** "Bucket already exists" or permission errors

**Cause:** Bucket name collision or insufficient permissions

**Solution:**

```bash
# Check if bucket exists
aws s3 ls | grep pulumi-docs-origin

# If exists from failed deployment, delete it
aws s3 rb s3://{bucket-name} --force

# Check AWS credentials
aws sts get-caller-identity

# Should show role: ContinuousDelivery
```

#### CloudFront Cache Issues

**Symptom:** Changes not visible on production site

**Cause:** CloudFront cache serving old content

**Solution:**

```bash
# Create cache invalidation
aws cloudfront create-invalidation \
  --distribution-id E3PRSXO1BZJEEY \
  --paths "/*"

# Check invalidation status
aws cloudfront get-invalidation \
  --distribution-id E3PRSXO1BZJEEY \
  --id {invalidation-id}
```

> **Note:** Invalidations take 5-15 minutes to propagate globally.

#### Lambda@Edge Propagation Delays

**Symptom:** Edge functions not executing after deployment

**Cause:** Lambda@Edge replication to edge locations takes time

**Timeline:**

- Code update: Immediate
- Replication to edges: 5-30 minutes
- Full propagation: Up to 1 hour

**Verification:**

```bash
# Check function version
aws lambda get-function \
  --function-name edge-redirects \
  --region us-east-1

# Lambda@Edge must be in us-east-1
```

**Solution:** Wait for propagation or test from different edge location.

#### Pulumi State Conflicts

**Symptom:** "Another update is currently in progress"

**Cause:** Concurrent Pulumi operations or orphaned locks

**Solution:**

```bash
# Check for in-progress operations
pulumi stack -s www-production

# Cancel orphaned updates (if safe)
pulumi cancel -s www-production

# If persistent, check Pulumi service console
# https://app.pulumi.com/pulumi/docs/www-production
```

#### Search Index Update Failures

**Symptom:** Search returns old results

**Cause:** Algolia indexing failed or timed out

**Solution:**

```bash
# Manual index update
make ci_update_search_index

# Check Algolia dashboard
# https://www.algolia.com/apps/OCCYMHQD/

# Verify index settings
node scripts/search/check-settings.js
```

### Test Failures

#### Example Program Test Failures

**Symptom:** `make test` fails for specific programs

**Debug:**

```bash
# Run single test with verbose output
ONLY_TEST="aws-s3-bucket-typescript" \
PULUMI_VERBOSE_LOGGING=true \
./scripts/programs/test.sh

# Check for common issues:
# - Missing cloud credentials
# - Outdated dependencies
# - API changes

# Update dependencies
cd static/programs/aws-s3-bucket-typescript
npm update
```

#### Cypress Browser Test Failures

**Symptom:** Browser tests fail in CI but pass locally

**Common Causes:**

- Timing issues (page not loaded)
- Environment differences (URLs, auth)
- Flaky tests (random failures)

**Debug:**

```bash
# View video artifacts in GitHub Actions
# Artifacts > browser-test-videos.zip

# Run locally with same baseURL
CYPRESS_BASE_URL=http://bucket.s3-website.amazonaws.com \
npx cypress run
```

**Fix:**

```javascript
// Add explicit waits
cy.get('.element').should('be.visible');
cy.wait('@apiCall');

// Increase timeout
cy.get('.element', { timeout: 10000 });
```

#### Link Checking Failures

**Symptom:** `make check_links` reports broken links

**Triage:**

1. **Internal links:** Usually due to moved/deleted pages
   - Check if file was moved → add alias
   - Check if intentionally deleted → update linking pages

2. **External links:** May be temporary outages
   - Verify in browser
   - Check if domain changed
   - Consider link rot (archive.org)

3. **Anchors:** Fragment not found
   - Verify heading exists
   - Check for typos in anchor
   - Hugo auto-generates slugs (spaces → hyphens, lowercase)

**Fix:**

```bash
# Find pages linking to broken URL
grep -r "broken-url" content/

# Update or remove links
```

#### Lighthouse Performance Failures

**Symptom:** Performance score drops below threshold

**Common Causes:**

- Large images not optimized
- JavaScript bundle size increased
- Render-blocking resources
- Third-party scripts

**Debug:**

```bash
# Run Lighthouse locally
npx @lhci/cli@latest autorun --url=https://www.pulumi.com

# Analyze bundle size
cd theme
yarn run webpack-bundle-analyzer

# Check image sizes
find static/images -type f -size +500k
```

**Fix:**

- Optimize images (compress, WebP format)
- Code split large bundles
- Lazy load images
- Defer non-critical JavaScript

### Debug Commands

#### Check Site Health

```bash
# Verify site is accessible
curl -I https://www.pulumi.com

# Check specific page
curl -I https://www.pulumi.com/docs/

# Check S3 bucket
aws s3 ls s3://www-production-pulumi-docs-origin-abc1234/

# Test S3 website directly
curl -I http://www-production-pulumi-docs-origin-abc1234.s3-website.us-west-2.amazonaws.com
```

#### Check CloudFront

```bash
# Get distribution details
aws cloudfront get-distribution --id E3PRSXO1BZJEEY

# List cache behaviors
aws cloudfront get-distribution-config --id E3PRSXO1BZJEEY \
  | jq '.DistributionConfig.CacheBehaviors'

# Check origin configuration
aws cloudfront get-distribution-config --id E3PRSXO1BZJEEY \
  | jq '.DistributionConfig.Origins'
```

#### Check Pulumi Stack

```bash
# View stack outputs
pulumi stack output -s www-production

# View configuration
pulumi config -s www-production

# View recent updates
pulumi stack history -s www-production

# View resources
pulumi stack -s www-production
```

#### Check Logs

**GitHub Actions Logs:**

- Navigate to Actions tab
- Select workflow run
- View job logs

**CloudWatch Logs:**

```bash
# Lambda@Edge logs are in region where function executed
# Check multiple regions

aws logs tail /aws/lambda/us-east-1.edge-redirects --follow
```

**S3 Access Logs:**

```bash
# Download logs
aws s3 sync s3://www-prod.pulumi.com-website-logs/ ./logs/

# Analyze with AWS Athena (if configured)
```

---

## Infrastructure Change Review

When reviewing infrastructure changes (`infrastructure/`, `package.json`, webpack config, Lambda@Edge, CloudFront), identify potential risks that require human attention. This section provides guidance on common issues to flag during review.

### Key Risk Areas

**Lambda@Edge Bundling Issues:**

Lambda@Edge failures are often caused by bundling problems that aren't caught until runtime:

- **ESM/CommonJS incompatibility**: ESM-only packages (e.g., `url-pattern` >=7.0.0) break if webpack is misconfigured
- **Webpack config changes**: Changes to `output.module` or `experiments.outputModule` can break bundling
- **Dynamic imports**: `import()` statements may not work in Lambda@Edge runtime
- **Bundle size**: Lambda@Edge has strict limits (1MB compressed, 50MB uncompressed)

**What to flag in reviews:**

- Dependency updates that affect webpack, babel, or bundlers (especially major versions)
- Changes to webpack configuration files
- New dependencies in `package.json` used by Lambda@Edge code
- Changes to `infrastructure/index.ts` (Lambda@Edge function code)

**CloudFront Distribution Changes:**

- **Redirect logic**: Changes to redirect handling may break existing URLs
- **Cache behavior**: Modified cache settings require invalidation
- **Lambda associations**: Changes to CloudFront-Lambda event types must be coordinated

**Deployment Risks:**

- **High risk** (affects all users immediately): Lambda@Edge, CloudFront, DNS changes
- **Medium risk** (affects next deployment): Build system, dependency updates
- **Low risk** (limited scope): Documentation, scripts

**Dependency Updates:**

Large batches of dependency updates (especially Dependabot PRs with 20+ updates) increase risk:

- Flag webpack/bundler updates for testing against Lambda@Edge bundling
- Flag major version bumps for changelog review
- Suggest splitting build tool updates into separate PRs

### Testing & Validation

**For human reviewers to verify:**

- Changes tested on pulumi-test.io staging environment
- Lambda@Edge execution tested manually (not just deployment)
- Critical pages return expected status codes (not 503/500)
- CloudWatch logs checked for Lambda@Edge errors (logs appear in edge regions)

### Resources

- Lambda@Edge limits: <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-requirements-limits.html>
- Lambda@Edge code: `infrastructure/index.ts`
- CloudWatch logs: Edge regions (not us-east-1)

---

## Maintenance Tasks

Regular maintenance tasks to keep the infrastructure healthy and cost-effective.

### Bucket Cleanup

#### Automated Cleanup

**Workflows:**

- `bucket-cleanup.yml` (production)
- `bucket-cleanup-testing.yml` (testing)

**Schedule:** Daily at 3:00 PM UTC

**Process:**

1. List all origin buckets
2. Identify buckets older than retention period (typically 7 days)
3. Delete old buckets and contents
4. Clean up metadata in AWS Parameter Store
5. Report cleanup results

**Retention Policy:**

Retains 10 buckets beyond the currently deployed bucket (count-based, not time-based).

Configured in `scripts/list-recent-buckets.sh`:

```bash
buckets_to_retain=10
```

**Why It Matters:** Old buckets accumulate quickly (1 per deployment), costing money and cluttering AWS console.

#### Manual Cleanup

**List recent buckets:**

```bash
./scripts/list-recent-buckets.sh

# Output:
# www-production-pulumi-docs-origin-abc1234 (2 days old)
# www-production-pulumi-docs-origin-def5678 (5 days old)
# www-production-pulumi-docs-origin-ghi9012 (10 days old) ← Cleanup candidate
```

**Delete specific bucket:**

```bash
# Delete bucket and contents
aws s3 rb s3://bucket-name --force

# Verify deletion
aws s3 ls | grep bucket-name
```

**Bulk cleanup:**

```bash
# Delete all buckets older than 30 days
./scripts/ci-bucket-cleanup.sh --days 30
```

### Dependency Updates

#### Node.js Dependencies

**Locations:**

- Root `package.json`
- `theme/package.json`
- `theme/stencil/package.json`
- `infrastructure/package.json`

**Update Process:**

```bash
# Check for outdated packages
yarn outdated

# Update all dependencies
yarn upgrade

# Update specific package
yarn upgrade package-name

# Run tests
make test

# Commit changes
git add package.json yarn.lock
git commit -m "Update Node.js dependencies"
```

**Automation:** Dependabot creates PRs for dependency updates weekly.

#### Hugo Version Updates

> **Warning:** Hugo updates require changes in **multiple locations**.

**Files to Update:**

1. `.github/workflows/build-and-deploy.yml`
2. `.github/workflows/testing-build-and-deploy.yml`
3. `.github/workflows/pull-request.yml`
4. `.github/workflows/pulumi-cli.yml`
5. `.github/workflows/scheduled-test.yml`
6. `scripts/ensure.sh`
7. Dev container configuration (if applicable)

**Process:**

```bash
# Update Hugo version in all workflow files
find .github/workflows -name "*.yml" -exec sed -i 's/hugo-version: 0.154.5/hugo-version: 0.155.0/g' {} +

# Update ensure.sh
sed -i 's/0.154.5/0.155.0/g' scripts/ensure.sh

# Test locally
make clean
make ensure
make build

# Test in PR before merging
```

#### SDK Documentation Tools

**TypeDoc:**

```bash
# Check current version
npm list typedoc

# Update
yarn add --dev typedoc@latest typedoc-plugin-script-inject@latest

# Regenerate docs
make generate
```

**Sphinx:**

```bash
# Update in Python requirements
# (typically handled in scripts/generate_python_docs.sh)

# Test generation
./scripts/generate_python_docs.sh
```

#### GitHub Actions Versions

Dependabot automatically updates GitHub Actions versions. Review and merge Dependabot PRs regularly.

**Current Action Versions (as of January 2026):**

| Action | Version | Purpose |
|--------|---------|---------|
| `actions/checkout` | v4 | Repository checkout |
| `actions/setup-node` | v6 | Node.js environment setup |
| `actions/setup-go` | v5 | Go environment setup |
| `actions/setup-python` | v5 | Python environment setup |
| `actions/setup-dotnet` | v4 | .NET environment setup |
| `actions/setup-java` | v3 | Java environment setup |
| `actions/upload-artifact` | v4 | Artifact upload |
| `actions/create-github-app-token` | v2 | GitHub App token generation |
| `aws-actions/configure-aws-credentials` | v4 | AWS credential configuration |
| `google-github-actions/auth` | v2 | Google Cloud authentication |
| `peaceiris/actions-hugo` | v2 | Hugo installation |
| `pulumi/actions` | v4 | Pulumi CLI installation |
| `pulumi/esc-action` | v1 | Pulumi ESC integration |
| `pulumi/action-install-pulumi-cli` | v1.0.1 | Legacy action used in the CLI release workflow; `pulumi/actions` should be used everywhere else |
| `jaxxstorm/action-install-gh-release` | v2.1.0 | Install tools from GitHub releases |
| `treosh/lighthouse-ci-action` | v12 | Lighthouse CI integration |
| `hmarr/auto-approve-action` | v4 | Automated PR approval |
| `repo-sync/pull-request` | v2 | Pull request creation |
| `helm/kind-action` | v1 | Kubernetes KinD cluster setup |

**Recent Major Version Updates:**

- **setup-node v4 → v6**: Updated Node.js setup action with improved caching and performance
- **jaxxstorm/action-install-gh-release v1 → v2**: Enhanced GitHub release installation with better error handling
- **create-github-app-token v1 → v2**: Updated GitHub App token generation with security improvements

**Example Update:**

```yaml
# Before
- uses: actions/setup-node@v4

# After (Dependabot PR)
- uses: actions/setup-node@v6
```

## Dependency management

This section provides comprehensive guidance for triaging and managing Dependabot pull requests in this repository.

### Dependabot configuration

**Schedule:** Monthly updates (first Monday at 09:00 UTC)

**Ecosystems:**

- npm (root, theme, stencil, infrastructure)
- GitHub Actions
- pip (Python dependencies)

**Grouping Strategy:** Ultra-aggressive single catch-all group per ecosystem

- Root: `all-dependencies` group captures all npm packages
- Theme: `all-dependencies` group captures all theme packages
- Stencil: `all-dependencies` group captures all stencil packages
- Infrastructure: `all-dependencies` group captures all infrastructure packages
- GitHub Actions: `all-actions` group captures all action updates

**Expected Volume:** 5 grouped PRs per month + security patches as needed

**PR Limits:** 1 PR per ecosystem (prevents flooding)

**Major Version Updates:** Blocked for non-security updates via wildcard ignore rules

**Security Updates:** Arrive immediately regardless of schedule (Dependabot auto-override)

### Automated risk labeling

All Dependabot PRs automatically receive:

**Dependabot-applied labels:**

- `dependencies` - Standard label applied by Dependabot

**Auto-applied labels (via label-dependabot.yml workflow):**

**Risk Tier Labels:**

- `deps-risk-high` - Runtime/browser/parser dependencies
- `deps-risk-medium` - Build tools/infrastructure dependencies
- `deps-risk-low` - Dev tools only

**Action Labels:**

- `deps-merge-after-test` - Test locally, then merge (HIGH risk or security patches)
- `deps-security-patch` - Security update, merge immediately after testing
- `deps-quarterly-review` - Close for batch review in quarterly cycle (MEDIUM/LOW risk)

**Special Flags:**

- `deps-lambda-edge-risk` - Webpack/bundler/AWS SDK updates (see Infrastructure Change Review)
- `deps-bulk-update` - 10+ dependencies in single PR

### Dependency risk tiers

#### HIGH RISK - Runtime/browser/parser dependencies

**Characteristics:**

- Execute in browser or server runtime
- Parse user content or external data
- Directly affect site functionality and user experience

**Packages:**

- **Search:** `@algolia/*`, `algoliasearch`, `search-insights`
- **A/B Testing:** `@growthbook/*`
- **Content Parsing:** `marked`, `markdown-it`, `js-yaml`, `cheerio`, `gray-matter`
- **Browser APIs:** `clipboard-polyfill`
- **Web Components:** `@stencil/*`, `swiper`
- **Utilities:** `uuid`

**Triage Action:** `deps-merge-after-test`

**Testing Checklist:**

1. Run `make serve-all` and verify site loads
1. Test search functionality (Algolia integration)
1. Check browser console for errors
1. Verify markdown rendering on multiple pages
1. Test interactive components (code copy, tabs, etc.)
1. Check A/B testing integration (GrowthBook)

#### MEDIUM RISK - Build tools/infrastructure dependencies

**Characteristics:**

- Affect build process and bundling
- Infrastructure as code dependencies
- Lambda@Edge function dependencies (special attention required)

**Packages:**

- **Webpack Ecosystem:** `webpack*`, `*-loader`, `*-webpack-plugin*`
- **CSS Processing:** `postcss*`, `sass*`, `cssnano`, `autoprefixer`, `@fullhuman/postcss-purgecss`, `tailwindcss`
- **TypeScript:** `typescript`
- **Pulumi:** `@pulumi/*`
- **AWS SDK:** `@aws-sdk/*` (Lambda@Edge risk)

**Triage Action:** `deps-quarterly-review` (unless security patch)

**Special Considerations:**

- **Lambda@Edge Risk:** Webpack, bundlers, and AWS SDK updates affect Lambda@Edge function size. See [Infrastructure Change Review](#infrastructure-change-review) section for deployment risks and 1MB compressed size limit.
- **Build Performance:** CSS/PostCSS updates can affect build times
- **TypeScript:** Breaking changes may require code updates

**Quarterly Review Process:**

1. Batch all MEDIUM-risk PRs from the quarter
1. Test webpack/bundler updates first (Lambda@Edge size check)
1. Test CSS processing updates second (build time check)
1. Test TypeScript updates last (compilation check)
1. Merge in order of successful testing

#### LOW RISK - Dev tools only

**Characteristics:**

- Testing and development tools
- Code quality and formatting tools
- Documentation generation tools
- Local development servers

**Packages:**

- **Testing:** `cypress`, `jest*`, `puppeteer`
- **Build Optimization:** `workbox-build`
- **Code Quality:** `prettier`, `eslint*`, `markdownlint`, `husky`, `lint-staged`
- **Dev Servers:** `http-server`, `concurrently`
- **Documentation:** `typedoc`

**Triage Action:** `deps-quarterly-review`

**Quarterly Review Process:**

1. Batch all LOW-risk PRs from the quarter
1. Quick smoke test: `make test && make lint`
1. Merge all if tests pass
1. If failures, debug individually

### Monthly triage workflow

On the first Monday of each month, Dependabot generates exactly 5 grouped PRs (one per ecosystem). Follow this workflow:

**Step 1: Check Labels (30 seconds per PR)**

- Look at auto-applied risk tier and action labels
- No need to read PR bodies initially—labels tell you everything

**Step 2: Security Patches (Immediate)**

- PRs with `deps-security-patch` label: Test and merge immediately
- Run testing checklist for applicable risk tier
- Merge within 24 hours

**Step 3: HIGH Risk Runtime Dependencies (Same Day)**

- PRs with `deps-risk-high` + `deps-merge-after-test` labels
- Run HIGH risk testing checklist (see above)
- Merge if tests pass, or debug and fix issues

**Step 4: MEDIUM/LOW Risk Dependencies (Defer)**

- PRs with `deps-quarterly-review` label
- Close with comment: "Deferring to quarterly review cycle. Will batch with other MEDIUM/LOW-risk updates."
- Do not merge monthly—wait for quarterly batch

**Step 5: Lambda@Edge Risk Flag (Extra Attention)**

- PRs with `deps-lambda-edge-risk` label
- Cross-reference [Infrastructure Change Review](#infrastructure-change-review) section
- Check Lambda@Edge function size after webpack/bundler updates
- Verify CloudFront deployment succeeds in testing environment

**Expected Monthly Time:** 5-10 minutes for triage + 20-30 minutes for HIGH-risk testing

### Quarterly review cycle

**Schedule:** January, April, July, October (first week)

**Process:**

1. Review all closed PRs from past 3 months with `deps-quarterly-review` label
1. Check if newer versions are available (Dependabot may have newer PRs open)
1. Create consolidated testing branch with all MEDIUM/LOW updates
1. Run full test suite: `make test && make lint && make build`
1. Test Lambda@Edge function size for webpack/bundler updates
1. Merge if all tests pass
1. If failures, debug individually and merge successful updates only

**Expected Quarterly Time:** 1-2 hours for batch testing and merging

### Security patch handling

**Override Rule:** Security patches bypass all other processes

**Arrival:** Immediately when vulnerability discovered (ignores monthly schedule)

**Labels:** Auto-labeled with `deps-security-patch` + applicable risk tier

**Workflow:**

1. Dependabot opens PR immediately (any time of month)
1. Auto-labeling workflow adds `deps-security-patch` + risk tier
1. Test using checklist for applicable risk tier
1. Merge within 24 hours regardless of risk tier
1. Deploy to production immediately

**Example:** CVE in `marked` (HIGH risk parser)

- PR arrives immediately
- Labels: `deps-security-patch`, `deps-risk-high`, `deps-merge-after-test`
- Run HIGH risk testing checklist
- Merge and deploy within 24 hours

### Bulk updates (10+ dependencies)

**Label:** `deps-bulk-update`

**Risk:** Higher chance of conflicts or breaking changes

**Process:**

1. Review PR carefully—don't rely solely on automated labels
1. Check for major version updates within the bulk (may be hidden)
1. Test more thoroughly than single-dependency updates
1. Consider splitting into smaller batches if failures occur

**Testing:**

1. Full test suite: `make test && make lint`
1. Local build: `make serve-all`
1. Visual regression testing on key pages
1. Extended soak testing (leave `make serve-all` running for 30 minutes)

### Cross-references

**Lambda@Edge Deployment Risks:**

- See [Infrastructure Change Review](#infrastructure-change-review) section
- Webpack, bundlers, and AWS SDK updates affect Lambda@Edge function size
- 1MB compressed size limit—test after bundler updates

**Infrastructure Changes:**

- Pulumi infrastructure updates (`@pulumi/*`, `@aws-sdk/*`)
- See [Infrastructure Change Review](#infrastructure-change-review) for deployment process

### Known exceptions

**Prettier v3.x:**

- Ignored in root and theme `dependabot.yml`
- Reason: Performance regression (5-10x slower than v2.x)
- Revisit: When performance regression is fixed upstream

**Tailwindcss Major Versions:**

- Ignored in root and theme `dependabot.yml`
- Reason: Breaking changes require manual migration
- Revisit: During planned design system updates

**pulumi/action-install-pulumi-cli:**

- Ignored in `dependabot.yml` GitHub Actions section
- Reason: v2+ has circular dependency on `versions.json` which the CLI release workflow creates
- Current version: v1.0.1 (downloads directly from GitHub releases)
- Usage: `.github/workflows/pulumi-cli.yml` only; `pulumi/actions` should be used elsewhere
- Revisit: When action is fixed to support direct GitHub release downloads without `versions.json`

**Major Versions (Wildcard):**

- Ignored across all ecosystems via wildcard rule
- Reason: Breaking changes require manual review and testing
- Exception: Security patches override this rule

### Search Index Management

#### Algolia Configuration

**Settings File:** `scripts/search/settings.js`

**Configuration:**

- Searchable attributes
- Ranking rules
- Custom ranking
- Facets
- Synonyms

**Update Settings:**

```bash
# Apply settings
node scripts/search/apply-settings.js

# Verify settings
node scripts/search/check-settings.js
```

#### Index Update

**Manual Reindexing:**

```bash
# Update all indices
make ci_update_search_index

# Update specific index
ALGOLIA_INDEX=pulumi node scripts/search/update-index.js
```

**Automated Updates:**

- **Hourly:** Via `update-search-index.yml`
- **On Deploy:** Via `ci-push.sh` and `ci-pull-request.sh`

#### Search Ranking Rules

Priority order for search results:

1. Exact match
2. Page title match
3. Heading match
4. Content match
5. Custom ranking:
   - Documentation > Blog > Registry
   - Newer content ranked higher

**Modify Ranking:**

Edit `scripts/search/settings.js`:

```javascript
ranking: [
  'typo',
  'geo',
  'words',
  'filters',
  'proximity',
  'attribute',
  'exact',
  'custom'
],
customRanking: [
  'desc(date)',
  'desc(weight)'
]
```

### Performance Optimization

#### CSS Bundle Size Monitoring

**Check Current Size:**

```bash
# Build site
make build

# Check CSS sizes
ls -lh public/css/

# Target: < 200KB per bundle
```

**Optimization Techniques:**

1. **PurgeCSS Configuration**
   - Review safelist patterns
   - Remove unused components
   - Optimize Tailwind config

2. **Reduce Tailwind Variants**

   ```javascript
   // theme/tailwind.config.js
   module.exports = {
     variants: {
       extend: {
         // Only enable variants you use
         backgroundColor: ['hover'],
         textColor: ['hover'],
       }
     }
   }
   ```

3. **Code Splitting**
   - Separate critical CSS
   - Load non-critical CSS async

#### JavaScript Bundle Optimization

**Analyze Bundle:**

```bash
cd theme
npx webpack-bundle-analyzer dist/stats.json
```

**Optimization Techniques:**

1. **Code Splitting**

   ```javascript
   // Dynamic imports
   const module = await import('./heavy-module');
   ```

2. **Tree Shaking**
   - Use ES modules
   - Avoid default exports

3. **Lazy Loading**

   ```javascript
   // Load on interaction
   button.addEventListener('click', async () => {
     const module = await import('./feature');
   });
   ```

#### Image Optimization

**Check Large Images:**

```bash
find static -type f \( -name "*.png" -o -name "*.jpg" \) -size +500k

# Optimize with ImageOptim, TinyPNG, or similar
```

**Best Practices:**

- Use WebP format with fallback
- Provide multiple sizes (srcset)
- Lazy load images below fold
- Use SVG for icons and logos

#### CloudFront Cache Strategies

**Cache Headers:**

```yaml
# Long cache for versioned assets
/css/*.css: 1 year
/js/*.js: 1 year

# Short cache for HTML
/*.html: 5 minutes

# No cache for dynamic content
/registry/*: no cache
```

**Optimization:**

1. **Increase TTL for static assets**
   - Versioned assets can cache forever
   - Use bundle IDs for cache busting

2. **Cache Patterns**

   ```typescript
   // infrastructure/index.ts
   cacheBehaviors: [{
     pathPattern: "/images/*",
     targetOriginId: s3Origin.id,
     minTtl: 3600,
     defaultTtl: 86400,
     maxTtl: 31536000
   }]
   ```

3. **Compression**
   - Enable gzip and brotli
   - Reduces transfer size by 70-80%

### Security Updates

#### Dependabot Configuration

**File:** `.github/dependabot.yml`

```yaml
version: 2
updates:
  - package-ecosystem: npm
    directory: "/"
    schedule:
      interval: weekly
    open-pull-requests-limit: 10

  - package-ecosystem: github-actions
    directory: "/"
    schedule:
      interval: weekly
```

**Process:**

1. Dependabot creates PR with dependency update
2. CI runs tests automatically
3. Review changes
4. Merge if tests pass

#### Secret Rotation

**Pulumi ESC Secrets:**

All secrets managed via Pulumi ESC with automatic rotation capabilities.

**To Rotate:**

1. Update secret in Pulumi ESC console
2. No code changes needed
3. Next deployment uses new secret

**Secrets to Rotate Regularly:**

- Pulumi tokens
- AWS IAM roles (refresh OIDC trust)
- Algolia keys
- Slack webhooks
- Sentry tokens

#### IAM Role Reviews

**Check Role Permissions:**

```bash
# Production role
aws iam get-role --role-name ContinuousDelivery --profile production

# Testing role
aws iam get-role --role-name ContinuousDelivery --profile testing
```

**Principle of Least Privilege:**

Regularly review and remove unnecessary permissions:

```json
{
  "Effect": "Allow",
  "Action": [
    "s3:CreateBucket",
    "s3:DeleteBucket",
    "s3:GetObject",
    "s3:PutObject",
    "s3:DeleteObject"
  ],
  "Resource": "arn:aws:s3:::www-*-pulumi-docs-origin-*"
}
```

#### OIDC Token Management

**GitHub OIDC Configuration:**

Trust relationship between GitHub and AWS allows temporary credentials:

```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Principal": {
      "Federated": "arn:aws:iam::388588623842:oidc-provider/token.actions.githubusercontent.com"
    },
    "Action": "sts:AssumeRoleWithWebIdentity",
    "Condition": {
      "StringEquals": {
        "token.actions.githubusercontent.com:aud": "sts.amazonaws.com",
        "token.actions.githubusercontent.com:sub": "repo:pulumi/docs:ref:refs/heads/master"
      }
    }
  }]
}
```

**Benefits:**

- No long-lived credentials
- Automatic expiration (2 hours)
- Audit trail in CloudTrail
- Scoped to specific workflows

**Verify OIDC Config:**

```bash
aws iam get-role --role-name ContinuousDelivery \
  | jq '.Role.AssumeRolePolicyDocument'
```

---

## Reference

### Key Scripts Reference

Complete reference of all build and deployment scripts.

| Script | Location | Purpose | Usage |
|--------|----------|---------|-------|
| **build-site.sh** | scripts/ | Main build orchestrator | `./scripts/build-site.sh [preview]` |
| **ensure.sh** | scripts/ | Install dependencies | `./scripts/ensure.sh` |
| **serve.sh** | scripts/ | Local dev server | `./scripts/serve.sh` |
| **clean.sh** | scripts/ | Remove build artifacts | `./scripts/clean.sh` |
| **ci-push.sh** | scripts/ | Production deployment | `./scripts/ci-push.sh` |
| **ci-pull-request.sh** | scripts/ | PR deployment | `./scripts/ci-pull-request.sh` |
| **sync-and-test-bucket.sh** | scripts/ | S3 sync and validation | `./scripts/sync-and-test-bucket.sh update` |
| **run-pulumi.sh** | scripts/ | Pulumi deployment | `./scripts/run-pulumi.sh` |
| **make-s3-redirects.sh** | scripts/ | Apply S3 redirects | `./scripts/make-s3-redirects.sh` |
| **generate-search-index.sh** | scripts/ | Update search index | `./scripts/generate-search-index.sh` |
| **run_typedoc.sh** | scripts/ | Generate Node.js docs | `./scripts/run_typedoc.sh` |
| **generate_python_docs.sh** | scripts/ | Generate Python docs | `./scripts/generate_python_docs.sh` |
| **run-browser-tests.sh** | scripts/ | Run Cypress tests | `./scripts/run-browser-tests.sh` |
| **check-links.sh** | scripts/link-checker/ | Verify links | `./scripts/link-checker/check-links.sh` |
| **check-urls.sh** | scripts/search/ | Validate search index | `./scripts/search/check-urls.sh` |
| **minify-css.js** | scripts/ | Optimize CSS | `node scripts/minify-css.js` |
| **generate-docs-content.js** | scripts/content/ | Generate search data | `node scripts/content/generate-docs-content.js` |
| **list-recent-buckets.sh** | scripts/ | List S3 buckets | `./scripts/list-recent-buckets.sh` |
| **ci-bucket-cleanup.sh** | scripts/ | Delete old buckets | `./scripts/ci-bucket-cleanup.sh --days 30` |
| **common.sh** | scripts/ | Shared utilities | Sourced by other scripts |

### Critical Environment Variables

| Variable | Purpose | Example | Set By |
|----------|---------|---------|--------|
| **ASSET_BUNDLE_ID** | Asset versioning | `abc1234` or `pr-123-abc1234` | build-site.sh |
| **CSS_BUNDLE_ID** | CSS versioning | Same as ASSET_BUNDLE_ID | build-site.sh |
| **REL_CSS_BUNDLE** | CSS path (Hugo) | `/css/styles.abc1234.css` | build-site.sh |
| **REL_JS_BUNDLE** | JS path (Hugo) | `/js/bundle.min.abc1234.js` | build-site.sh |
| **HUGO_BASEURL** | Site base URL | `https://www.pulumi.com/` | Workflow |
| **DEPLOYMENT_ENVIRONMENT** | Environment | `production` or `testing` | Workflow |
| **NODE_OPTIONS** | Node.js memory | `--max_old_space_size=8192` | Workflow |
| **AWS_REGION** | AWS region | `us-west-2` | Pulumi config |
| **CDN_PULUMI_URN** | CloudFront URN | `urn:pulumi:www-production::...` | Pulumi stack |
| **PULUMI_ACCESS_TOKEN** | Pulumi API | `pul-...` | Pulumi ESC |
| **PULUMI_STACK_NAME** | Stack name | `www-production` | Workflow |
| **ALGOLIA_APP_ID** | Search app | `OCCYMHQD` | Pulumi ESC |
| **ALGOLIA_APP_ADMIN_KEY** | Search admin key | (secret) | Pulumi ESC |
| **SENTRY_AUTH_TOKEN** | Error monitoring | (secret) | Pulumi ESC |
| **SLACK_WEBHOOK_URL** | Notifications | (secret) | Pulumi ESC |
| **GITHUB_TOKEN** | GitHub API | (auto) | GitHub Actions |
| **NOBUILD** | Skip rebuilds | `1` | User |
| **ONLY_TEST** | Test single program | `aws-s3-typescript` | User |
| **GOGC** | Go GC tuning | `3` | Workflow |

### AWS Resource Naming Conventions

| Resource Type | Naming Pattern | Example |
|---------------|----------------|---------|
| **S3 Origin Bucket** | `www-{env}-pulumi-docs-origin-{id}` | `www-production-pulumi-docs-origin-abc1234` |
| **S3 Preview Bucket** | `www-testing-pulumi-docs-origin-pr-{num}-{sha}` | `www-testing-pulumi-docs-origin-pr-123-abc1234` |
| **S3 Logs Bucket** | `{domain}-website-logs` | `www-prod.pulumi.com-website-logs` |
| **CloudFront Distribution** | Manual (persistent) | `E3PRSXO1BZJEEY` |
| **Lambda@Edge Function** | `edge-{purpose}` | `edge-redirects` |
| **IAM Role** | `ContinuousDelivery` | `ContinuousDelivery` |
| **Pulumi Stack** | `www-{environment}` | `www-production` |

### Port and URL Reference

| Service | URL/Port | Purpose |
|---------|----------|---------|
| **Local Dev Server** | <http://localhost:1313> | Hugo development server |
| **Static Server** | <http://localhost:8080> | Serve built public/ directory |
| **Production** | <https://www.pulumi.com> | Production site |
| **Testing** | <https://www.pulumi-test.io> | Testing environment |
| **PR Preview** | http://{bucket}.s3-website.{region}.amazonaws.com | PR preview sites |
| **Pulumi Console** | <https://app.pulumi.com> | Pulumi service |
| **Algolia Dashboard** | <https://www.algolia.com/apps/OCCYMHQD> | Search management |
| **GitHub Actions** | <https://github.com/pulumi/docs/actions> | CI/CD workflows |

### Related Documentation

| Document | Location | Purpose |
|----------|----------|---------|
| **README.md** | / | Getting started guide |
| **CONTRIBUTING.md** | / | Contribution guidelines |
| **BLOGGING.md** | / | Blog post creation |
| **STYLE-GUIDE.md** | / | Content style guide |
| **AGENTS.md** | / | AI agent guidelines |
| **CODE-EXAMPLES.md** | / | Example program guide |
| **SEO.md** | / | Search optimization |
| **SCHEMA.md** | / | Data schemas |
| **infrastructure/README.md** | infrastructure/ | Infrastructure details |
| **Pulumi Docs** | <https://www.pulumi.com/docs/> | Pulumi documentation |
| **Hugo Docs** | <https://gohugo.io/documentation/> | Hugo reference |
| **AWS CloudFront** | <https://docs.aws.amazon.com/cloudfront/> | CloudFront documentation |
| **GitHub Actions** | <https://docs.github.com/actions> | Workflow documentation |
| **Algolia Docs** | <https://www.algolia.com/doc/> | Search documentation |

### External Dependencies

| Dependency | Version | Purpose |
|------------|---------|---------|
| **Node.js** | 24.x | Runtime for build tools |
| **Hugo** | 0.154.5 | Static site generator |
| **Yarn** | 1.22.x | Package manager |
| **Go** | 1.25+ | Doc generation |
| **Python** | 3.13+ | Doc generation |
| **Pulumi CLI** | Latest | Infrastructure deployment |
| **TypeDoc** | 0.28.15 | Node.js doc generation |
| **Sphinx** | Latest | Python doc generation |
| **Webpack** | 5.x | Asset bundling |
| **Tailwind CSS** | 3.x | CSS framework |
| **PostCSS** | 8.x | CSS processing |
| **Cypress** | Latest | Browser testing |
| **AWS CLI** | 2.x | AWS operations |
| **GitHub CLI (gh)** | Latest | GitHub operations |

---

## Frequently Asked Questions

### How do I roll back a bad deployment?

The atomic deployment strategy makes rollbacks easy. Choose the method based on the situation:

**Most Common: Git Revert (10-15 min)**

```bash
git revert {problematic-commit-sha}
git push origin master
# Auto-triggers full rebuild and deployment
```

**Faster: Pin to Previous Bucket (1-2 min)**

For infrastructure issues or when git revert isn't suitable:

1. Find previous bucket (check GitHub Actions artifacts: `origin-bucket-metadata.json`)
2. Update config in Pulumi Cloud console:
   - <https://app.pulumi.com/pulumi/docs/www-production>
   - Settings → Configuration → Set `originBucketNameOverride`
3. Trigger "Build and deploy" workflow in GitHub Actions

CloudFront switches origins within 1-2 minutes (no rebuild).

**See [Rollback Procedures](#rollback-procedures) for detailed instructions on all methods.**

### How long do PR preview environments stay active?

PR preview environments persist until the PR is closed. They are automatically cleaned up by the `pr-closed.yml` workflow.

### Can I test infrastructure changes without affecting production?

Yes! Use the testing environment or create a personal dev stack:

```bash
# Testing environment (shared)
# Push to master, manually trigger testing-build-and-deploy.yml

# Personal dev stack
cd infrastructure
pulumi stack init dev-myname
pulumi up
```

### What happens if a build fails in production?

- CloudFront continues serving the previous deployment
- No downtime occurs
- Slack alert sent to `docs-ops` channel
- Failed build artifacts retained for debugging

### How do I add a new redirect?

It depends on the scenario:

1. **Moved Hugo content:** Add alias to frontmatter
2. **Generated content:** Add to `scripts/redirects/*.txt`
3. **Cross-origin:** Update Lambda@Edge function in `infrastructure/index.ts`

See [Redirect Management](#redirect-management) for details.

### Why are there so many S3 buckets?

Each deployment creates a new bucket for atomic deployments. Old buckets are automatically cleaned up after 7 days by the `bucket-cleanup.yml` workflow.

### How do I update the Hugo version?

Update in **all** workflow files and `scripts/ensure.sh`. See [Hugo Version Updates](#hugo-version-updates).

### What is Pulumi ESC and why do we use it?

Pulumi ESC (Environments, Secrets, and Config) manages all secrets and credentials. It provides:

- No static credentials in GitHub
- OIDC-based AWS authentication
- Centralized secret management
- Audit logging

### Can I run the full build locally?

Yes:

```bash
make clean
make ensure
make generate  # Optional, takes ~10 minutes
make build
make serve-static
```

The site will be available at <http://localhost:8080>.

### What access do I need to perform a rollback?

**For Git Revert (Method 1 - Most Common):**

- Write access to GitHub repository (to push reverts to master)
- That's it! No additional credentials needed

**For Bucket Pinning (Method 2 - Fast Rollback):**

- Access to Pulumi Cloud organization (`pulumi/docs` stack)
- Permission to trigger GitHub Actions workflows

**For Local Execution (Method 3 - Advanced):**

- All of the above, plus:
- Pulumi CLI installed locally
- `PULUMI_ACCESS_TOKEN` environment variable
- AWS CLI configured (SSO/OIDC)
- Local development environment setup

**Don't have access?** Contact your team admin or use Method 1 (git revert) which requires minimal permissions.

### Rollback Troubleshooting

**Issue: "Cannot access Pulumi stack"**

- Verify you're logged into Pulumi Cloud (<https://app.pulumi.com>)
- Check you have access to the `pulumi` organization
- Verify stack name: `pulumi/docs/www-production`
- Contact team admin for access if needed

**Issue: "AWS credentials not configured" (Local execution)**

- Configure AWS CLI with SSO: `aws sso login --profile production`
- Or use Pulumi ESC: Credentials are automatically provided in GitHub Actions
- Check your AWS profile is set: `export AWS_PROFILE=production`

**Issue: "Bucket not found"**

- Verify bucket name format: `www-production-pulumi-docs-origin-{git-sha-short}`
- Check bucket wasn't cleaned up (retention is 10 buckets beyond current)
- Older buckets may have been deleted by automated cleanup workflow
- Find bucket name in GitHub Actions artifacts: `origin-bucket-metadata.json`

**Issue: "Git revert creates conflicts"**

- If automatic revert fails, manually revert changes:

  ```bash
  git revert {commit-sha} --no-commit
  # Resolve conflicts manually
  git add .
  git commit
  git push origin master
  ```

**Issue: "Rollback didn't fix the problem"**

- Verify you reverted/pinned to a known-good deployment
- Check GitHub Actions history for last successful deployment
- Issue might be in external service (check Algolia, CloudFront, Lambda@Edge)
- Consider rolling back further if problem persists

### How do I debug a failed workflow?

1. Navigate to GitHub Actions tab
2. Select the failed workflow run
3. Expand failed job steps
4. Download artifacts (browser-test-videos, bucket-metadata)
5. Check Slack notifications for summary

For deployments, also check:

- AWS CloudWatch Logs
- S3 bucket contents
- CloudFront distribution status
- Pulumi stack history

---
