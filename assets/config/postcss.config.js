/**
 * Configuration file for PostCSS. This is only used as part of the Hugo pipeline
 * build process for our Sass files, since we run the resulting CSS through PostCSS
 * at the end to do more transformations.
 */
module.exports = {
    plugins: [
        // TailwindCSS.
        require("tailwindcss")("./assets/config/tailwind.config.js"),

        // Apply vendor prefixes for CSS features that aren't fully supported yet.
        require("autoprefixer")({
            overrideBrowserslist: [
                "last 2 versions"
            ]
        }),

        // Use the following plugins when not building for "development":
        ...process.env.NODE_ENV !== "development" ? [
            // Remove unused CSS with Purgecss.
            require("@fullhuman/postcss-purgecss")({
                // These reference CSS classes.
                content: [
                    "./content/**/*.md",
                    "./layouts/**/*.html",
                    "./assets/js/search.js" // HTML is produced by this script which references some CSS classes.
                ],

                // HubSpot form classes.
                whitelistPatternsChildren: [/^hs/],

                // Tailwind uses colons.
                defaultExtractor: content => content.match(/[A-Za-z0-9-_:/]+/g) || []
            }),

            // Minify the CSS even further.
            require('cssnano')({
                preset: 'default',
            })
        ] : [],
    ]
};
