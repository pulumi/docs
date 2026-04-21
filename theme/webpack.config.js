const fs = require("fs");
const path = require("path");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const TerserPlugin = require("terser-webpack-plugin");
const WebpackShellPluginNext = require("webpack-shell-plugin-next");

module.exports = function (env, { mode }) {
    return {
        mode: mode || "development",
        entry: {
            bundle: "./src/ts/main.ts",
            marketing: "./src/ts/marketing.ts",
            "marketing-homepage": "./src/ts/marketingHomepage.ts",
            algolia: "./src/ts/algolia-entry.ts",
            "consent-manager": "./src/ts/consent-manager/index.ts",
        },
        output: {
            filename: "[name].[contenthash:8].js",
            chunkFilename: "chunk-[contenthash:8].js",
            path: `${process.cwd()}/../static/js`,
            publicPath: "/js/",
        },
        resolve: {
            extensions: [".ts", ".js"],
            modules: ["src", "node_modules"],
        },
        devServer: {
            writeToDisk: true,
        },
        // Disable webpack's module cache in development. When enabled (the default),
        // changes to SCSS partials imported from main.scss/_marketing.scss don't
        // invalidate the extracted CSS module — webpack rebuilds the JS stub but
        // serves stale CSS from cache until the watcher is restarted. See the
        // output of `make serve-all` showing "cached modules ... 766 KiB (css/mini-extract)"
        // after a partial change. Disabling the cache in dev mode forces sass-loader
        // to re-run on every rebuild. Production builds are unaffected.
        cache: mode === "production",
        module: {
            rules: [
                {
                    test: /\.ts$/i,
                    use: [
                        {
                            loader: "ts-loader",
                            options: {
                                transpileOnly: true,
                            },
                        },
                    ],
                    exclude: /node_modules/,
                },
                {
                    test: /\.s[ac]ss$/i,
                    use: [
                        MiniCssExtractPlugin.loader,
                        {
                            loader: "css-loader",
                            options: {
                                sourceMap: false,
                                url: false,
                            },
                        },
                        {
                            loader: "postcss-loader",
                        },
                        {
                            loader: "sass-loader",
                            options: {
                                sourceMap: false,
                                sassOptions: {
                                    outputStyle: "compressed",
                                    quietDeps: true,
                                    silenceDeprecations: ['import', 'global-builtin'],
                                },
                            },
                        },
                    ],
                },
            ],
        },
        plugins: [
            new MiniCssExtractPlugin({
                filename: "../../assets/css/[name].css",
            }),
            new WebpackShellPluginNext({
                // dev: true clears the script list after the first run, so stencil is not
                // rebuilt on every webpack recompilation — only on startup. Stencil component
                // edits are picked up by stencil's own --watch process, which runs alongside
                // webpack via theme/package.json's `start` script (used by `make serve-all`).
                // Has no effect on production builds (single compilation).
                dev: mode !== "production",
                onBuildStart: {
                    blocking: true,
                    parallel: false,
                    scripts: ["yarn --cwd stencil run build"],
                },
            }),
            {
                apply(compiler) {
                    compiler.hooks.done.tap("JsManifestPlugin", (stats) => {
                        const manifest = {};
                        for (const [name, { assets }] of Object.entries(stats.toJson().entrypoints)) {
                            const jsFile = assets.find((a) => a.name.endsWith(".js"));
                            if (jsFile) manifest[name] = jsFile.name;
                        }
                        const outDir = path.resolve(compiler.outputPath, "../../data");
                        fs.mkdirSync(outDir, { recursive: true });
                        const manifestPath = path.join(outDir, "js_manifest.json");
                        const newContent = JSON.stringify(manifest, null, 2) + "\n";
                        // Only write if changed — avoids a spurious Hugo reload on CSS-only rebuilds.
                        const existing = fs.existsSync(manifestPath) ? fs.readFileSync(manifestPath, "utf8") : "";
                        if (newContent !== existing) {
                            fs.writeFileSync(manifestPath, newContent);
                        }
                    });
                },
            },
        ],
        optimization: {
            minimize: mode === "production",
            minimizer: [
                new TerserPlugin({
                    terserOptions: {
                        format: {
                            comments: false,
                        },
                    },
                    extractComments: false,
                }),
            ],
        },
        performance: {
            // Increase thresholds to accommodate TailwindCSS utility classes
            // bundle.css is ~4.21 MiB due to comprehensive utility generation
            maxAssetSize: 5242880,        // 5 MiB
            maxEntrypointSize: 5767168,   // 5.5 MiB
            hints: 'warning',              // Keep as warnings to monitor growth
        },
    };
};
