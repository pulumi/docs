---
layout: typescript-reference
repo: pulumi-fabric
subpath: runtime/langhost.d.ts
---
export declare function serveLanguageHost(monitor: string, engine: string | undefined): {
    server: any;
    port: number;
};
