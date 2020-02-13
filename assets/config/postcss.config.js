/**
 * Configuration file for PostCSS. This is only used as part of the Hugo pipeline
 * build process for our Sass files, since we run the resulting CSS through PostCSS
 * at the end to do more transformations.
 */
module.exports = {
    plugins: [
        // TailwindCSS
        require("tailwindcss")("./assets/config/tailwind.config.js"),

        // Apply vendor prefixes for CSS features that aren't
        // fully supported yet.
        require("autoprefixer")({
            overrideBrowserslist: [
                "last 2 versions"
            ]
        }),

        // PurgeCSS to remove unused classes for better page speed.
        require("@fullhuman/postcss-purgecss")({
            // Specify the paths to all of the template files in your project
            content: [ "./layouts/**/*.html" ],
            // Whitelist HubSpot specific classes so they don't get removed.
            whitelist: ["supported-cicd-platforms", ":not"],
            whitelistPatterns: [/^fa-/, /^hs-/, /^highlight$/, /^pagination$/, /^code-/,  /^copy-/],
            whitelistPatternsChildren: [/^hs-/, /^highlight$/, /^pagination$/, /^code-/,  /^copy-/],
            // Extract the default tailwind classes.
            defaultExtractor: content => content.match(/[\w-/:]+(?<!:)/g) || [],
        }),

        // Minify the CSS even further. (It works!)
        require('cssnano')({
            preset: 'default',
        })
    ]
};
