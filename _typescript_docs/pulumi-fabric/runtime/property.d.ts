---
layout: typescript-reference
repo: pulumi-fabric
subpath: runtime/property.d.ts
---
import { Computed, MaybeComputed } from "../computed";
export declare function isInsideMapValueCallback(): boolean;
export declare class Property<T> implements Computed<T> {
    readonly inputPromise: Promise<T | undefined>;
    readonly outputPromise: Promise<T | undefined>;
    private input;
    private output;
    private resolveInput;
    private resolveOutput;
    constructor(value: MaybeComputed<T> | undefined, setInput: boolean, setOutput: boolean);
    private static resolveTo<T>(p, value, setInput, setOutput);
    mapValue<U>(callback: (v: T) => MaybeComputed<U>): Computed<U>;
    done(dryRun: boolean): void;
    awaitingInput(): boolean;
    awaitingOutput(): boolean;
    setInput(value: T | undefined): void;
    setOutput(value: T | undefined, isFinal: boolean, skipIfAlready: boolean): void;
    toString(): string;
}
