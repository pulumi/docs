---
layout: typescript-reference
repo: pulumi-fabric
subpath: asset/archive.d.ts
---
import { Computed, MaybeComputed } from "../computed";
import { Asset } from "./asset";
export declare abstract class Archive {
}
export declare type AssetMap = {
    [name: string]: Asset;
};
export declare class AssetArchive extends Archive {
    readonly assets: Computed<AssetMap>;
    constructor(assets: MaybeComputed<AssetMap>);
}
export declare class FileArchive extends Archive {
    readonly path: Computed<string>;
    constructor(path: MaybeComputed<string>);
}
export declare class RemoteArchive extends Archive {
    readonly uri: Computed<string>;
    constructor(uri: MaybeComputed<string>);
}
