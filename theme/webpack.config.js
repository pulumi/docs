const fs = require("fs");
const path = require("path");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const TerserPlugin = require("terser-webpack-plugin");
const WebpackShellPluginNext = require("webpack-shell-plugin-next");

module.exports = function (env, argv = {}) {
    // `mode` is only populated when the caller passes `--mode`. `yarn run webpack --watch`
    // (invoked by `make serve-all` via theme/package.json's `start` script) does not, so
    // treat an unset mode as development.
    const isProd = argv.mode === "production";

    return {
        mode: isProd ? "production" : "development",
        entry: {
            "bundle": "./src/ts/main.ts",
            "marketing": "./src/ts/marketing.ts",
            "algolia": "./src/ts/algolia-entry.ts",
            "consent-manager": "./src/ts/consent-manager/index.ts",
            "header-nav": "./src/ts/header-nav.ts",
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
        // Webpack's default fs.watch-based watcher misses SCSS and TS edits in this
        // workspace — watchpack's kqueue watchers stay armed but never fire, so `make
        // serve-all` sits idle after a change. Polling is rock-solid and, at 300ms, fast
        // enough that rebuilds feel instant.
        watchOptions: {
            poll: 300,
            aggregateTimeout: 200,
            ignored: ["**/node_modules/**", "**/stencil/dist/**"],
        },
        // No cache: the default in-memory cache served stale CSS after SCSS partial
        // edits, and a persistent filesystem cache buys nothing here — prod runs in a
        // fresh CI container, dev recompiles are fast enough without it.
        cache: false,
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
                                    silenceDeprecations: ["import", "global-builtin"],
                                    loadPaths: [path.join(__dirname, "node_modules")],
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
                dev: !isProd,
                onBuildStart: {
                    blocking: true,
                    parallel: false,
                    scripts: ["yarn --cwd stencil run build"],
                },
            }),
            {
                apply(compiler) {
                    compiler.hooks.done.tap("JsManifestPlugin", stats => {
                        const manifest = {};
                        for (const [name, { assets }] of Object.entries(stats.toJson().entrypoints)) {
                            const jsFile = assets.find(a => a.name.endsWith(".js"));
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
            minimize: isProd,
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
            maxAssetSize: 5242880, // 5 MiB
            maxEntrypointSize: 5767168, // 5.5 MiB
            hints: "warning", // Keep as warnings to monitor growth
        },
    };
};
