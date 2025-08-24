# Workflow Reliability Improvements

This document describes improvements made to the `build-and-deploy.yml` workflow to address intermittent failures caused by external package registry issues.

## Problem

The workflow was experiencing intermittent failures during the dependency installation phase with errors like:
- `Error: https://registry.yarnpkg.com/package-name: Request failed "500 Internal Server Error"`
- These failures were external infrastructure issues, not code problems
- Different packages failed at different times, indicating registry availability issues

## Implemented Solutions

### 1. Retry Mechanism (`scripts/retry-yarn.sh`)

A new script that wraps yarn commands with retry logic:
- **3 retry attempts** with exponential backoff
- **Base delay of 10 seconds**, doubling each attempt (with jitter)
- **Network timeout of 60 seconds** for yarn operations
- **Reduced concurrency** (network-concurrency 1) for reliability

### 2. Dependency Caching

Added GitHub Actions cache for node_modules:
- Caches all node_modules directories (root, infrastructure, theme, theme/stencil)
- Caches yarn cache directory
- Uses yarn.lock files as cache key
- Reduces dependency on external registries for subsequent runs

### 3. Yarn Configuration

Pre-configures yarn for reliability:
- Sets appropriate network timeouts
- Reduces network concurrency
- Explicitly sets npm registry

### 4. Improved Error Handling

Enhanced the workflow to:
- Provide better logging during dependency installation
- Update notification messages to hint at potential registry issues
- Framework for distinguishing infrastructure vs code failures

## Usage

The improvements are transparent to normal workflow operation. The retry mechanism automatically activates when yarn commands encounter network errors.

## Monitoring

To monitor the effectiveness:
1. Check workflow run logs for retry attempts
2. Monitor frequency of "yarn registry failure" patterns in notifications
3. Observe cache hit rates in workflow logs

## Manual Retry

If a workflow fails due to registry issues, simply re-run the workflow. The retry mechanism and caching should resolve most transient issues.