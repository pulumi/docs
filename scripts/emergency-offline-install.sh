#!/bin/bash
# Emergency fallback script for extreme registry outages
# This script tries to use only cached/offline dependencies

set -o errexit -o pipefail

echo "🚨 Emergency mode: Attempting to use only cached dependencies"
echo "This should only be used during widespread registry outages"

# Configure yarn for offline mode
yarn config set yarn-offline-mirror ./yarn-offline-cache
yarn config set yarn-offline-mirror-pruning true

# Try to install using only cache
echo "Attempting offline installation..."
if yarn install --offline --frozen-lockfile; then
    echo "✅ Offline installation successful"
    exit 0
else
    echo "❌ Offline installation failed"
    echo "📝 This likely means dependencies are not fully cached"
    echo "💡 Manual intervention required - check registry status or use pre-built container"
    exit 1
fi