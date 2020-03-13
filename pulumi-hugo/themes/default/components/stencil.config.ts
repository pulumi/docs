import { Config } from "@stencil/core";
import { sass } from "@stencil/sass";

export const config: Config = {
    namespace: "components",
    enableCache: false,
    devServer: {
        openBrowser: false,
    },
    outputTargets: [
        {
            // Allows for more isolated development and testing.
            type: "www",
            serviceWorker: null,
        },
        {
            type: "dist",

            // Publish the bundle to the Hugo site's static directory. Note that this runs in both
            // dev and production modes.
            buildDir: "../../static/js/",
        },
    ],
    plugins: [
        sass(),
    ],
};
