---
user-invocable: false
description: Dependabot label taxonomy and risk classification
---

# Dependabot Labels

## Label Taxonomy

Parse these labels from PR data to determine risk level and handling approach:

### Risk Classification Labels

- `deps-risk-high` - High risk dependencies (runtime, bundling, core functionality)
- `deps-risk-medium` - Medium risk dependencies (build tools, dev dependencies with production impact)
- `deps-risk-low` - Low risk dependencies (dev-only tools, testing frameworks)
- `deps-risk-unknown` - Risk not yet classified

### Special Handling Labels

- `deps-security-patch` - Security vulnerability fix (always HIGH priority)
- `deps-lambda-edge-risk` - Affects Lambda@Edge bundling/runtime (ESM/CommonJS issues, webpack changes)
- `deps-bulk-update` - 10+ dependencies in single PR
- `deps-merge-after-test` - Requires testing before merge
- `deps-quarterly-review` - Part of quarterly batch update cycle

## Risk Classification Logic

Determine risk tier from labels:

1. **HIGH Risk**:
   - Has `deps-security-patch` label, OR
   - Has `deps-lambda-edge-risk` label, OR
   - Has `deps-risk-high` label

2. **MEDIUM Risk**:
   - Has `deps-risk-medium` label

3. **LOW Risk**:
   - Has `deps-risk-low` label

4. **UNKNOWN Risk**:
   - No risk label present, OR
   - Has `deps-risk-unknown` label

## Testing Checklists by Risk Tier

### HIGH Risk Testing

- Run `make serve-all` (full rebuild with asset pipeline)
- Test site search functionality
- Check browser console for errors (F12)
- Verify markdown rendering
- Test PR deployment: URL loads, Lambda@Edge errors via F12, search, navigation

### MEDIUM Risk Testing

- Run `make build`
- Check for build warnings
- If build tools affected: Verify PR deployment URL loads

### LOW Risk Testing

- Run `make lint`

## Quarterly Review Workflow

For PRs with `deps-quarterly-review` label:

### Batching Strategy

- Accumulate LOW/MEDIUM risk dependency updates
- Review and merge quarterly (every 3 months)
- Reduces testing overhead for low-impact changes
- Keeps dependencies reasonably current without constant churn

### Handling Options

1. **Approve for batch** - Add to quarterly batch (recommended)
2. **Merge now** - Urgent update needed before quarterly cycle
3. **Close with quarterly note** - Defer to next quarterly batch (duplicate or superseded)
4. **Investigate** - Need risk assessment before deciding

### Close Message for Quarterly Batching

When closing to batch with other quarterly updates:

```text
Closing to batch with other quarterly dependency updates. We'll merge accumulated quarterly updates together after comprehensive testing. This reduces testing overhead while keeping dependencies current.
```
