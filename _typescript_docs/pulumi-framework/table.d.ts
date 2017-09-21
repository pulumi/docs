---
layout: typescript-reference
repo: pulumi-framework
subpath: table.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export interface TableOptions {
    readCapacity?: number;
    writeCapacity?: number;
}
export declare class Table {
    private table;
    private readonly readCapacity;
    private readonly writeCapacity;
    tableName: fabric.Computed<string>;
    readonly primaryKey: string;
    readonly primaryKeyType: string;
    get: (query: Object) => Promise<any>;
    insert: (item: Object) => Promise<void>;
    scan: () => Promise<any[]>;
    delete: (query: Object) => Promise<void>;
    update: (query: Object, updates: Object) => Promise<void>;
    constructor(name: string, primaryKey?: string, primaryKeyType?: "S" | "N" | "B", opts?: TableOptions);
}
