const fs = require("fs");
const glob = require("glob");
const postcss = require("postcss");
const cssnano = require("cssnano");

// Per-bundle minification configuration.
//
// Tailwind v4 emits its variants using native CSS nesting (e.g. `.hover\:bg-gray-100
// { &:hover { ... } }`), which PurgeCSS's selector matcher does not understand —
// running PurgeCSS over Tailwind v4 output silently drops every hover, focus,
// focus-visible, group-hover, space-y/x, and many responsive utility rules. Tailwind
// v4 already content-scans @source paths and only emits classes it finds, so PurgeCSS
// is both redundant and destructive here. We keep cssnano for minification only.
const bundles = [
    {
        name: "bundle",
        input: "public/css/bundle.*.css",
    },
    {
        name: "marketing",
        input: "public/css/marketing.*.css",
    },
];

function minifyCSS(config) {
    const bundlePath = glob.sync(config.input)[0];

    if (bundlePath === undefined) {
        return Promise.resolve();
    }

    const css = fs.readFileSync(bundlePath);
    const outputPath = `public/css/${config.name}.${cssBundleId}.css`;

    return postcss([
        cssnano({
            preset: [
                "default",
                {
                    discardComments: {
                        removeAll: true,
                    },
                },
            ],
        }),
    ])
    .process(css, { from: bundlePath, to: outputPath })
    .then(result => {
        const css = result.css;

        // Make sure there's at least some valid-looking CSS in the result.
        if (!css || !css.match(/html|body/)) {
            throw new Error(`Unexpected PostCSS result: ${css}`);
        }

        fs.writeFileSync(outputPath, css);
        console.log(`Minified: ${outputPath}`);
    });
}

const cssBundleId = process.env.CSS_BUNDLE_ID;

if (!cssBundleId) {
    console.error("ERROR: CSS_BUNDLE_ID environment variable not set");
    process.exit(1);
}

if (!fs.existsSync("public/css")) {
    fs.mkdirSync("public/css", { recursive: true });
}

Promise.all(bundles.map(b => minifyCSS(b))).then(() => {
    console.log("CSS bundles minified successfully!");
    bundles.forEach(b => console.log(`  - ${b.name}.${cssBundleId}.css`));
});

// Exit non-zero when something goes wrong in the promise chain.
process.on("unhandledRejection", error => {
    throw new Error(error);
});
