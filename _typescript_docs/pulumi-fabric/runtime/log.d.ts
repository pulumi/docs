---
layout: typescript-reference
repo: pulumi-fabric
subpath: runtime/log.d.ts
---
export declare class Log {
    private static errcnt;
    private static lastLog;
    static hasErrors(): boolean;
    static debug(msg: string): void;
    static info(msg: string): void;
    static warn(msg: string): void;
    static error(msg: string): void;
    private static log(engine, sev, msg);
}
