const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const TerserPlugin = require("terser-webpack-plugin");
const WebpackShellPluginNext = require("webpack-shell-plugin-next");
const webpack = require("webpack");

module.exports = function (env, { mode }) {
    return {
        mode: mode || "development",
        entry: {
            bundle: "./src/ts/main.ts",
            marketing: "./src/ts/marketing.ts",
        },
        output: {
            filename: "[name].js",
            chunkFilename: "chunk-[id].js",
            path: `${process.cwd()}/../assets/js`,
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
                                },
                            },
                        },
                    ],
                },
            ],
        },
        plugins: [
            new MiniCssExtractPlugin({
                filename: "../css/[name].css",
            }),
            new webpack.optimize.LimitChunkCountPlugin({
                maxChunks: 1,
            }),
            new WebpackShellPluginNext({
                onBuildStart: {
                    blocking: true,
                    parallel: false,
                    scripts: ["yarn --cwd stencil run build"],
                },
            }),
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
    };
};
