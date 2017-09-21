---
layout: typescript-reference
repo: pulumi-fabric
subpath: asset/asset.d.ts
---
import { Computed, MaybeComputed } from "../computed";
export declare abstract class Asset {
}
export declare class FileAsset extends Asset {
    readonly path: Computed<string>;
    constructor(path: MaybeComputed<string>);
}
export declare class StringAsset extends Asset {
    readonly text: Computed<string>;
    constructor(text: MaybeComputed<string>);
}
export declare class RemoteAsset extends Asset {
    readonly uri: Computed<string>;
    constructor(uri: MaybeComputed<string>);
}
