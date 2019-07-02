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

        // Minify the CSS even further. (It works!)
        require('cssnano')({
            preset: 'default',
        })
    ]
};
