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
            homepage: "./src/ts/homepage.ts",
            algolia: "./src/ts/algolia-entry.ts",
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
                        fs.writeFileSync(path.join(outDir, "js_manifest.json"), JSON.stringify(manifest, null, 2) + "\n");
                    });
                },
            },
        ],
        optimization: {
            minimize: true,
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
