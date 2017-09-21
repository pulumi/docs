---
layout: typescript-reference
repo: pulumi-fabric
subpath: config.d.ts
---
export declare class Config {
    readonly name: string;
    constructor(name: string);
    get(key: string): string | undefined;
    getBoolean(key: string): boolean | undefined;
    getNumber(key: string): number | undefined;
    getObject<T>(key: string): T | undefined;
    require(key: string): string;
    requireBoolean(key: string): boolean;
    requireNumber(key: string): number;
    requireObject<T>(key: string): T;
    private fullKey(key);
}
