const fs = require("fs");
const glob = require("glob");
const postcss = require("postcss");
const { purgeCSSPlugin } = require("@fullhuman/postcss-purgecss");
const cssnano = require("cssnano");

function minifyCSS(filePath, outputFilename) {
    const bundlePath = glob.sync(filePath)[0];

    // If there is no matching bundle then we will skip minifying things.
    if (bundlePath === undefined) {
        return Promise.resolve();
    }

    const css = fs.readFileSync(bundlePath);
    const outputPath = `public/css/${outputFilename}`;

    return postcss([

        // PurgeCSS removes unused CSS by analyzing the files of the built website.
        // https://purgecss.com/
        purgeCSSPlugin({
            content: [ "public/**/*.html", "public/js/bundle.*.js" ],
            // PurgeCSS looks through all the built files but, making an exception here
            // to skip the files in the azure-native-v2 package because it is causing
            // out of memory errors with all the new files added from the package. This
            // should not affect the minified bundle, since there isn't any new css being
            // used for this package that wouldn't already be in the bundle.
            skippedContentGlobs: [
                "public/registry/packages/azure-native-v1/**/*",
            ],
            css: [
                bundlePath,
            ],
            safelist: {
                deep: [
                    /^hs-/,
                    /^highlight$/,
                    /^pagination$/,
                    /^code-/,
                    /^copy-/,
                    /^carousel/,
                    /^st-/,
                    /^icon-/,
                    /^package-details/,
                    /^resources-properties/,
                    /^tabular/,
                    /^pulumi-/,
                ],
            },

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

        // Write to the output file with build ID in the name.
        fs.writeFileSync(outputPath, css);
        console.log(`Minified: ${outputPath}`);
    });
}

const cssBundleId = process.env.CSS_BUNDLE_ID;

if (!cssBundleId) {
    console.error("ERROR: CSS_BUNDLE_ID environment variable not set");
    process.exit(1);
}

// Ensure output directory exists
if (!fs.existsSync("public/css")) {
    fs.mkdirSync("public/css", { recursive: true });
}

Promise.all([
    minifyCSS("public/css/bundle.*.css", `bundle.${cssBundleId}.css`),
    minifyCSS("public/css/marketing.*.css", `marketing.${cssBundleId}.css`),
]).then(() => {
    console.log("CSS bundles minified successfully!");
    console.log(`  - bundle.${cssBundleId}.css`);
    console.log(`  - marketing.${cssBundleId}.css`);
});

// Exit non-zero when something goes wrong in the promise chain.
process.on("unhandledRejection", error => {
    throw new Error(error);
});
