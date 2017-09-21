---
layout: typescript-reference
repo: pulumi-aws
subpath: dynamodb/table.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class Table extends fabric.Resource {
    readonly arn: fabric.Computed<string>;
    readonly attribute: fabric.Computed<{
        name: string;
        type: string;
    }[]>;
    readonly globalSecondaryIndex?: fabric.Computed<{
        hashKey: string;
        name: string;
        nonKeyAttributes?: string[];
        projectionType: string;
        rangeKey?: string;
        readCapacity: number;
        writeCapacity: number;
    }[]>;
    readonly hashKey: fabric.Computed<string>;
    readonly localSecondaryIndex?: fabric.Computed<{
        name: string;
        nonKeyAttributes?: string[];
        projectionType: string;
        rangeKey: string;
    }[]>;
    readonly name: fabric.Computed<string>;
    readonly rangeKey?: fabric.Computed<string>;
    readonly readCapacity: fabric.Computed<number>;
    readonly streamArn: fabric.Computed<string>;
    readonly streamEnabled: fabric.Computed<boolean>;
    readonly streamLabel: fabric.Computed<string>;
    readonly streamViewType: fabric.Computed<string>;
    readonly tags?: fabric.Computed<{
        [key: string]: any;
    }>;
    readonly ttl?: fabric.Computed<{
        attributeName: string;
        enabled: boolean;
    }[]>;
    readonly writeCapacity: fabric.Computed<number>;
    constructor(urnName: string, args: TableArgs);
}
export interface TableArgs {
    readonly attribute: fabric.MaybeComputed<{
        name: fabric.MaybeComputed<string>;
        type: fabric.MaybeComputed<string>;
    }>[];
    readonly globalSecondaryIndex?: fabric.MaybeComputed<{
        hashKey: fabric.MaybeComputed<string>;
        name: fabric.MaybeComputed<string>;
        nonKeyAttributes?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
        projectionType: fabric.MaybeComputed<string>;
        rangeKey?: fabric.MaybeComputed<string>;
        readCapacity: fabric.MaybeComputed<number>;
        writeCapacity: fabric.MaybeComputed<number>;
    }>[];
    readonly hashKey: fabric.MaybeComputed<string>;
    readonly localSecondaryIndex?: fabric.MaybeComputed<{
        name: fabric.MaybeComputed<string>;
        nonKeyAttributes?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
        projectionType: fabric.MaybeComputed<string>;
        rangeKey: fabric.MaybeComputed<string>;
    }>[];
    readonly name?: fabric.MaybeComputed<string>;
    readonly rangeKey?: fabric.MaybeComputed<string>;
    readonly readCapacity: fabric.MaybeComputed<number>;
    readonly streamEnabled?: fabric.MaybeComputed<boolean>;
    readonly streamViewType?: fabric.MaybeComputed<string>;
    readonly tags?: fabric.MaybeComputed<{
        [key: string]: any;
    }>;
    readonly ttl?: fabric.MaybeComputed<{
        attributeName: fabric.MaybeComputed<string>;
        enabled: fabric.MaybeComputed<boolean>;
    }>[];
    readonly writeCapacity: fabric.MaybeComputed<number>;
}
