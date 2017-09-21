---
layout: typescript-reference
repo: pulumi-fabric
subpath: resource.d.ts
---
import { Computed, MaybeComputed } from "./computed";
export declare type ID = string;
export declare type URN = string;
export declare abstract class Resource {
    readonly id: Computed<ID>;
    readonly urn: Computed<URN>;
    constructor(t: string, name: string, props: {
        [key: string]: MaybeComputed<any> | undefined;
    });
}
