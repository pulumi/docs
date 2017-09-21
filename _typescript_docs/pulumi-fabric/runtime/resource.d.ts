---
layout: typescript-reference
repo: pulumi-fabric
subpath: runtime/resource.d.ts
---
import { MaybeComputed } from "../computed";
import { Resource } from "../resource";
export declare function registerResource(res: Resource, t: string, name: string, props: {
    [key: string]: MaybeComputed<any> | undefined;
}): void;
export declare const unknownPropertyValue = "04da6b54-80e4-46f7-96ec-b56ff0331ba9";
export declare const specialSigKey = "4dabf18193072939515e22adb298388d";
export declare const specialAssetSig = "c44067f5952c0a294b673a41bacd8c17";
export declare const specialArchiveSig = "0def7320c3a5731c473e5ecbe6d01bc7";
