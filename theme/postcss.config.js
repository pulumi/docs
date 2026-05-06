/**
 * PostCSS configuration used by webpack's postcss-loader when processing
 * the compiled SCSS output from sass-loader.
 */

const path = require("path");
const fs = require("fs");

// Walk a directory recursively and return all files matching a predicate.
function walkDir(dir, pred, out = []) {
    for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
        const full = path.join(dir, entry.name);
        if (entry.isDirectory()) walkDir(full, pred, out);
        else if (pred(entry.name)) out.push(full);
    }
    return out;
}

const scssDir = path.join(__dirname, "src/scss");

// @tailwindcss/postcss caches its output keyed on the mtimes of registered
// PostCSS dependency files. By default it only tracks the entry file (main.scss),
// so changes to imported SCSS partials go undetected and stale CSS is emitted.
// This plugin registers every SCSS partial as a dependency so Tailwind checks
// their mtimes and performs a full rebuild whenever any partial changes.
const registerScssDependencies = {
    postcssPlugin: "register-scss-dependencies",
    Once(root, { result }) {
        for (const file of walkDir(scssDir, (n) => n.endsWith(".scss"))) {
            result.messages.push({
                type: "dependency",
                plugin: "register-scss-dependencies",
                file,
                parent: result.opts.from,
            });
        }
    },
};

module.exports = {
    plugins: [
        registerScssDependencies,
        require("@tailwindcss/postcss"),
    ],
};
