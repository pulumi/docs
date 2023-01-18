import { Config } from "@stencil/core";
import { sass } from "@stencil/sass";

export const config: Config = {
    enableCache: true,
    buildDist: true,
    outputTargets: [
        {
            type: "dist-custom-elements-bundle",
            dir: "./dist",
        },
        {
            type: "www",
            buildDir: "./build",
        },
    ],
    plugins: [sass()],
};
