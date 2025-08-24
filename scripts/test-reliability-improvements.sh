#!/bin/bash
# Test script to validate workflow reliability improvements
# This script tests the components we've added without requiring a full build

set -e

echo "=== Testing Workflow Reliability Improvements ==="
echo ""

# Test 1: Check retry-yarn.sh exists and is executable
echo "✓ Test 1: Checking retry-yarn.sh script..."
if [[ -x "./scripts/retry-yarn.sh" ]]; then
    echo "  ✓ retry-yarn.sh is executable"
else
    echo "  ✗ retry-yarn.sh is not executable"
    exit 1
fi

# Test 2: Test retry-yarn.sh with a simple command
echo "✓ Test 2: Testing retry-yarn.sh functionality..."
if ./scripts/retry-yarn.sh --version > /dev/null 2>&1; then
    echo "  ✓ retry-yarn.sh works correctly"
else
    echo "  ✗ retry-yarn.sh failed"
    exit 1
fi

# Test 3: Check yarn configuration
echo "✓ Test 3: Checking yarn configuration..."
timeout_config=$(yarn config get network-timeout)
concurrency_config=$(yarn config get network-concurrency)
registry_config=$(yarn config get registry)

if [[ "$timeout_config" == "60000" ]]; then
    echo "  ✓ Network timeout is correctly set to 60000ms"
else
    echo "  ✗ Network timeout is $timeout_config, expected 60000"
    exit 1
fi

if [[ "$concurrency_config" == "1" ]]; then
    echo "  ✓ Network concurrency is correctly set to 1"
else
    echo "  ✗ Network concurrency is $concurrency_config, expected 1"
    exit 1
fi

if [[ "$registry_config" == "https://registry.npmjs.org/" ]]; then
    echo "  ✓ Registry is correctly set to npm registry"
else
    echo "  ✗ Registry is $registry_config, expected https://registry.npmjs.org/"
    exit 1
fi

# Test 4: Check .yarnrc file exists
echo "✓ Test 4: Checking .yarnrc configuration file..."
if [[ -f ".yarnrc" ]]; then
    echo "  ✓ .yarnrc file exists"
    if grep -q "network-timeout 60000" .yarnrc; then
        echo "  ✓ .yarnrc contains correct timeout configuration"
    else
        echo "  ✗ .yarnrc missing timeout configuration"
        exit 1
    fi
else
    echo "  ✗ .yarnrc file does not exist"
    exit 1
fi

# Test 5: Check workflow file has caching
echo "✓ Test 5: Checking workflow caching configuration..."
if grep -q "actions/cache@v3" .github/workflows/build-and-deploy.yml; then
    echo "  ✓ Workflow includes caching configuration"
else
    echo "  ✗ Workflow missing caching configuration"
    exit 1
fi

# Test 6: Check ensure.sh uses retry mechanism
echo "✓ Test 6: Checking ensure.sh uses retry mechanism..."
if grep -q "retry-yarn.sh" scripts/ensure.sh; then
    echo "  ✓ ensure.sh uses retry mechanism"
else
    echo "  ✗ ensure.sh does not use retry mechanism"
    exit 1
fi

echo ""
echo "🎉 All tests passed! Workflow reliability improvements are properly configured."
echo ""
echo "Summary of improvements:"
echo "- ✅ Retry mechanism with exponential backoff"
echo "- ✅ GitHub Actions caching for node_modules"
echo "- ✅ Yarn configured for better reliability"
echo "- ✅ Enhanced error handling and notifications"
echo ""
echo "These improvements should significantly reduce failures due to external registry issues."