/**
 * Configuration file for PostCSS. This is only used as part of the Hugo pipeline
 * build process for our Sass files, since we run the resulting CSS through PostCSS
 * at the end to do more transformations.
 */

// Note whether we're in "production" mode, so we can avoid doing post-processing and
// optimization during development.
const isProduction = process.env.NODE_ENV === "production";

module.exports = {
    plugins: [
        // TailwindCSS
        require("tailwindcss")("./assets/config/tailwind.config.js"),

        // Apply vendor prefixes for CSS features that aren't
        // fully supported yet.
        isProduction ? require("autoprefixer")({
            overrideBrowserslist: [
                "last 2 versions"
            ]
        }) : null,

        // Remove whitespace, comments and other safe things.
        // https://cssnano.co/guides/getting-started/
        isProduction ? require("cssnano")({
            preset: [
                "default",
                {
                    discardComments: {
                        removeAll: true,
                    },
                },
            ],
        }) : null,

        // Use PurgeCSS to remove unused classes for better page speed.
        // Docs: https://purgecss.com/plugins/postcss.html
        isProduction ? require("@fullhuman/postcss-purgecss")({
            // Specify the paths to all of the template files in your project
            content: [
                // All layout files.
                "./layouts/**/*.html",

                // Some of our scripts reference CSS classes.
                "./assets/js/**/*.js",

                // Look for CSS classes in our Markdown content. We use `glob` explicitly here so we can ignore the
                // files for the API docs in ./content/docs/reference/pkg/**/* because it includes a large number of
                // files that significantly impacts build time (~25 seconds vs. many minutes). Instead, we'll only look
                // for CSS classes in a subset of packages for NodeJS and Python, which should be representative of all
                // the other packages.
                ...require("glob").sync("./content/**/*.md", { ignore: "./content/docs/reference/pkg/**/*" }),
                "./content/docs/reference/pkg/nodejs/pulumi/aws/**/*.md",
                "./content/docs/reference/pkg/python/pulumi/**/*.md",
            ],

            // Whitelist specific classes that were being removed.
            whitelist: ["supported-cicd-platforms", ":not", ":target", "md:max-w-lg", "blink", "typing", "char"],

            // Whitelist custom parent selectors and their children.
            whitelistPatterns: [/^fa-/, /^hs-/, /^highlight$/, /^pagination$/, /^code-/, /^copy-/, /^carousel/],
            whitelistPatternsChildren: [/^hs-/, /^highlight$/, /^pagination$/, /^code-/, /^copy-/, /^carousel/],

            // We need to extract the Tailwind screen size selectors (e.g. sm, md, lg)
            // so that we do not strip them out. As long as a class name appears in the HTML
            // in its entirety, PurgeCSS will not remove it.
            // Ex. https://tailwindcss.com/docs/controlling-file-size/#writing-purgeable-html
            defaultExtractor: content => content.match(/[\w-/:]*[\w-/:]/g) || [],
        }) : null,
    ],
};
