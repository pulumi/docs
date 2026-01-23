#!/usr/bin/env node

/**
 * Post-install patch for @stencil/redux
 *
 * The @stencil/redux v0.2.0 package is deprecated and unmaintained. Its
 * collection manifest references a global script that doesn't have the
 * required default export, causing build warnings in Stencil v4.
 *
 * This script removes the global script reference from the collection
 * manifest to eliminate the warnings while preserving functionality.
 */

const fs = require('fs');
const path = require('path');

const manifestPath = path.join(
    __dirname,
    '../node_modules/@stencil/redux/dist/collection/collection-manifest.json'
);

try {
    // Check if file exists
    if (!fs.existsSync(manifestPath)) {
        console.log('⚠️  @stencil/redux collection manifest not found, skipping patch');
        process.exit(0);
    }

    // Read the manifest
    const manifest = JSON.parse(fs.readFileSync(manifestPath, 'utf8'));

    // Check if global script reference exists
    if (!manifest.global) {
        console.log('✓ @stencil/redux already patched');
        process.exit(0);
    }

    // Remove the global script reference
    delete manifest.global;

    // Write back the patched manifest
    fs.writeFileSync(manifestPath, JSON.stringify(manifest, null, 2) + '\n');

    console.log('✓ Patched @stencil/redux collection manifest (removed global script reference)');
} catch (error) {
    console.error('❌ Failed to patch @stencil/redux:', error.message);
    // Don't fail the install if patching fails
    process.exit(0);
}
