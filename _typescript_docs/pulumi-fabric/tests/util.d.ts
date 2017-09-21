---
layout: typescript-reference
repo: pulumi-fabric
subpath: tests/util.d.ts
---
import { Computed } from "../index";
export declare type MochaFunc = (err: Error) => void;
export declare function asyncTest(test: () => Promise<void>): (func: MochaFunc) => void;
export declare function assertAsyncThrows(test: () => Promise<void>): Promise<void>;
export declare function computedToPromise<T>(computed: Computed<T>): Promise<T>;
