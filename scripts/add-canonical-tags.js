#!/usr/bin/env node

const fs = require('fs');
const path = require('path');
const glob = require('glob');

const STATIC_PREBUILT_DIR = path.join(__dirname, '../static-prebuilt');
const BASE_URL = 'https://www.pulumi.com';

function addCanonicalTag(filePath) {
    let content = fs.readFileSync(filePath, 'utf8');

    const relativePath = path.relative(STATIC_PREBUILT_DIR, filePath);
    let canonicalPath = '/' + relativePath.replace(/\\/g, '/');

    canonicalPath = canonicalPath.replace(/\/index\.html$/, '/');

    const canonicalUrl = BASE_URL + canonicalPath;
    const canonicalTag = `<link rel="canonical" href="${canonicalUrl}"/>`;

    const existingCanonicalRegex = /<link\s+rel="canonical"\s+href="([^"]+)"\s*\/?>/i;
    const match = content.match(existingCanonicalRegex);

    if (match) {
        const existingUrl = match[1];
        if (existingUrl === canonicalUrl) {
            console.log(`Skipping ${filePath} - already has correct canonical tag`);
            return;
        }
        if (existingUrl.startsWith('http://') || existingUrl.startsWith('https://')) {
            console.log(`Skipping ${filePath} - already has absolute canonical URL: ${existingUrl}`);
            return;
        }
        content = content.replace(existingCanonicalRegex, canonicalTag);
        fs.writeFileSync(filePath, content, 'utf8');
        console.log(`Updated relative canonical to absolute in ${filePath}: ${existingUrl} -> ${canonicalUrl}`);
        return;
    }

    const headCloseIndex = content.indexOf('</head>');
    if (headCloseIndex === -1) {
        console.warn(`Warning: No </head> tag found in ${filePath}`);
        return;
    }

    const newContent = content.slice(0, headCloseIndex) +
                      canonicalTag +
                      content.slice(headCloseIndex);

    fs.writeFileSync(filePath, newContent, 'utf8');
    console.log(`Added canonical tag to ${filePath}: ${canonicalUrl}`);
}

function processDirectory(pattern) {
    const files = glob.sync(pattern, {
        cwd: STATIC_PREBUILT_DIR,
        absolute: true
    });

    console.log(`Found ${files.length} HTML files to process`);

    files.forEach(file => {
        try {
            addCanonicalTag(file);
        } catch (error) {
            console.error(`Error processing ${file}:`, error.message);
        }
    });
}

console.log('Adding canonical tags to static HTML files...');
processDirectory('docs/reference/pkg/**/*.html');
console.log('Done!');
