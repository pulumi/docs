---
layout: typescript-reference
repo: pulumi-fabric
subpath: runtime/closure.d.ts
---
import { Computed } from "../computed";
export interface Closure {
    code: string;
    runtime: string;
    environment: Environment;
}
export declare type Environment = {
    [key: string]: EnvironmentEntry;
};
export interface EnvironmentEntry {
    json?: any;
    closure?: Closure;
    obj?: Environment;
    arr?: EnvironmentEntry[];
}
export declare function serializeClosure(func: Function): Computed<Closure>;
export interface AsyncClosure {
    code: string;
    runtime: string;
    environment: AsyncEnvironment;
}
export declare type AsyncEnvironment = {
    [key: string]: Promise<AsyncEnvironmentEntry>;
};
export interface AsyncEnvironmentEntry {
    json?: any;
    closure?: AsyncClosure;
    obj?: AsyncEnvironment;
    arr?: Promise<EnvironmentEntry>[];
}
