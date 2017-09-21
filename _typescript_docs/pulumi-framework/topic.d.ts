---
layout: typescript-reference
repo: pulumi-framework
subpath: topic.d.ts
---
export declare class Topic<T> implements Stream<T> {
    private name;
    private topic;
    publish: (item: T) => Promise<void>;
    constructor(name: string);
    subscribe(name: string, shandler: (item: T) => Promise<void>): void;
}
export interface Stream<T> {
    subscribe(name: string, handler: (item: T) => Promise<void>): void;
}
