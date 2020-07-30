// Copyright 2016-2020, Pulumi Corporation.  All rights reserved.

var fs = require("fs");
var path = require("path");
var glob = require("glob");

// The path to the Hugo build.
const webContentsRootPath = process.argv[2];

// The domain to redirect to, if any.
const redirectDomain = process.argv[3];

if (!webContentsRootPath) {
    console.log("Usage: translate-redirects.js [path-to-website-build] [optional-redirect-domain]");
    console.log(`       translate-redirects.js "./public" "www-yourname.pulumi-dev.io"`);
    process.exit(1);
}

// translateRedirect fixes up the redirect, if needed.
// If the redirect is already prefixed with "https://" or "http://", it is returned unmodified.
// If the redirect starts with "/", it is translated to an `https://${redirectDomain}${redirect}`.
// Otherwise, an Error is thrown.
function translateRedirect(filePath, redirect) {
    // If the redirect already has the https or http protocol specified, return it.
    if (redirect.startsWith("https://") || redirect.startsWith("http://")) {
        return redirect;
    }

    // If the redirect starts with "/", and a redirectDomain has been provided, prefix the
    // redirect with that domain. Otherwise, just return the redirect, as it's relative to
    // the current bucket.
    if (redirect.startsWith("/")) {
        if (redirectDomain) {
            return `https://${redirectDomain}${redirect}`;
        }
        return redirect;
    }

    // Otherwise, it's not in a format that we expect so throw an error.
    throw new Error(`The redirect "${redirect}" in "${filePath}" is not in an expected format.`);
}

// Returns the redirect URL if filePath is an HTML file that contains a meta refresh tag, otherwise undefined.
function getMetaRefreshRedirect(filePath) {
    // Only .html files contain meta refresh redirects.
    if (path.extname(filePath) !== ".html") {
        return undefined;
    }

    // Extract the redirect from the content of the file.
    const text = fs.readFileSync(filePath, "utf8");
    const regex = /<meta\s+?http-equiv=refresh\s+?content="0;\s+?url=(.*?)"/gmi;
    const match = regex.exec(text);

    if (match && match.length === 2) {
        const redirect = match[1];
        if (!redirect || redirect.length === 0) {
            throw new Error(`Meta refresh tag found in "${filePath}" but the redirect URL was empty.`);
        }
        return redirect;
    }

    return match && match.length === 2 ? match[1] : undefined;
}

// For each Hugo-generated redirect, write the relative path and destination URL
// to a text file to be processed later in the sync step.
const redirectPaths = new Map();
glob.sync(`${webContentsRootPath}/**/*.html`).map(filePath => {
    const relativeFilePath = filePath.replace(webContentsRootPath + "/", "");
    const redirect = getMetaRefreshRedirect(filePath);

    if (redirect) {
        redirectPaths.set(relativeFilePath, translateRedirect(filePath, redirect));
    }
});

// Write the file, overwriting the existing file if present.
fs.writeFileSync(
    `${webContentsRootPath}/redirects.txt`,
    Array.from(redirectPaths, ([k, v]) => `${k}|${v}`).join("\n") + "\n",
);
