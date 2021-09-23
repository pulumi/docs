const fs = require("fs");
const glob = require("glob");

const original = glob.sync("public/css/bundle.*.css")[0];
fs.copyFileSync(original, `${original}.bak`);

module.exports = {
    content: [
        "public/**/*.html",
        "public/js/bundle.*.js",
    ],
    css: [
        original,
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

    // Overwrite the original.
    output: original,
};
