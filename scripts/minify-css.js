const fs = require("fs");
const glob = require("glob");
const postcss = require("postcss");
const { purgeCSSPlugin } = require("@fullhuman/postcss-purgecss");
const cssnano = require("cssnano");

// Shared safelist patterns for classes that are dynamically generated or injected at runtime.
const sharedSafelist = [
    /^hs-/,
    /^highlight$/,
    /^pagination$/,
    /^code-/,
    /^copy-/,
    /^carousel/,
    /^st-/,
    /^pulumi-/,
];

// Per-bundle PurgeCSS configuration.
const bundles = [
    {
        name: "bundle",
        input: "public/css/bundle.*.css",
        content: ["public/**/*.html", "public/js/bundle.*.js", "public/js/algolia.*.js"],
        safelist: [
            ...sharedSafelist,
            /^icon-/,
            /^package-details/,
            /^resources-properties/,
            /^tabular/,
        ],
        // Skip azure-native-v1 because it causes out-of-memory errors during
        // PurgeCSS content scanning. No unique CSS classes originate from it.
        skippedContentGlobs: ["public/registry/packages/azure-native-v1/**/*"],
    },
    {
        name: "marketing",
        input: "public/css/marketing.*.css",
        content: ["public/**/*.html", "public/js/bundle.*.js"],
        safelist: [...sharedSafelist],
    },
    {
        // Homepage-specific marketing CSS: same source as marketing but purged
        // against only the homepage HTML for a smaller bundle. The webpack entry
        // produces assets/css/marketing-homepage.css for Hugo dev mode.
        name: "marketing-homepage",
        input: "public/css/marketing.*.css",
        content: ["public/index.html", "public/js/bundle.*.js"],
        safelist: [...sharedSafelist],
    },
    {
        name: "homepage",
        input: "public/css/homepage.*.css",
        content: ["public/index.html", "public/js/bundle.*.js"],
        safelist: [...sharedSafelist],
    },
];

function minifyCSS(config) {
    const bundlePath = glob.sync(config.input)[0];

    if (bundlePath === undefined) {
        return Promise.resolve();
    }

    const css = fs.readFileSync(bundlePath);
    const outputPath = `public/css/${config.name}.${cssBundleId}.css`;

    // PurgeCSS removes unused CSS by analyzing the built site files.
    // https://purgecss.com/
    return postcss([
        purgeCSSPlugin({
            content: config.content,
            skippedContentGlobs: config.skippedContentGlobs || [],
            css: [bundlePath],
            safelist: { deep: config.safelist },

            // We need to extract the Tailwind screen size selectors (e.g. sm, md, lg)
            // so that we do not strip them out. As long as a class name appears in the HTML
            // in its entirety, PurgeCSS will not remove it.
            // Ex. https://tailwindcss.com/docs/optimizing-for-production#writing-purgeable-html
            defaultExtractor: content => content.match(/[\w-/.:]+(?<!:)/g) || [],
        }),

        // CSSNano minifies our rendered CSS by removing whitespace, comments, etc.
        // https://cssnano.co/
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
