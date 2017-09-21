---
layout: typescript-reference
repo: pulumi-fabric
subpath: computed.d.ts
---
export interface Computed<T> {
    mapValue<U>(callback: (v: T) => MaybeComputed<U>): Computed<U>;
}
export declare type MaybeComputed<T> = T | Computed<T> | Promise<T>;
