const fs = require("fs");
const glob = require("glob");
const postcss = require("postcss");
const purgecss = require("@fullhuman/postcss-purgecss");
const cssnano = require("cssnano");

const bundlePath = glob.sync("public/css/bundle.*.css")[0];
const css = fs.readFileSync(bundlePath);

postcss([

    // PurgeCSS removes unused CSS by analyzing the files of the built website.
    // https://purgecss.com/
    purgecss({
        content: [
            "public/**/*.html",
            "public/js/bundle.*.js",
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
        // Ex. https://tailwindcss.com/docs/controlling-file-size/#writing-purgeable-html
        defaultExtractor: content => content.match(/[\w-/:]*[\w-/:]/g) || [],
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
.process(css, { from: bundlePath, to: bundlePath })
.then(result => {
    const css = result.css;

    // Make sure there's at least some valid-looking CSS in the result.
    if (!css || !css.match(/html|body/)) {
        throw new Error(`Unexpected PostCSS result: ${css}`);
    }

    // Write the result back to the file.
    fs.writeFileSync(bundlePath, css);
});

// Exit non-zero when something goes wrong in the promise chain.
process.on("unhandledRejection", error => {
    throw new Error(error);
});
