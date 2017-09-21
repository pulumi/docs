---
layout: typescript-reference
repo: pulumi-fabric
subpath: runtime/settings.d.ts
---
export declare function errorString(err: Error): string;
export declare let dryRun: boolean;
export declare function hasMonitor(): boolean;
export declare function isDryRun(): boolean;
export declare function getMonitor(): Object | undefined;
export declare function getEngine(): Object | undefined;
export declare function configure(m: Object | undefined, e: Object | undefined, dr: boolean): void;
export declare function disconnect(): void;
export declare function rpcKeepAlive(): () => void;
