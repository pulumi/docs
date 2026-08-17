import { Config } from "@stencil/core";
import { sass } from "@stencil/sass";

export const config: Config = {
    namespace: "pulumi-docs",
    enableCache: true,
    buildDist: true,
    outputTargets: [
        {
            type: "dist",
            dir: "./dist",
        },
        {
            type: "www",
            buildDir: "./build",
        },
    ],
    plugins: [sass()],
    testing: {
        browserArgs: ["--no-sandbox", "--disable-dev-shm-usage"],
        // uuid ships ESM-only (jest's CJS runtime can't parse it) and growthbook's
        // dom-mutator dependency needs a browser MutationObserver at import time; map
        // both to minimal stubs so suites that (transitively) import the store can run.
        moduleNameMapper: {
            "^uuid$": "<rootDir>/src/test-stubs/uuid.ts",
            "^@growthbook/growthbook$": "<rootDir>/src/test-stubs/growthbook.ts",
        },
    },
};
