---
layout: typescript-reference
repo: pulumi-framework
subpath: api.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export interface Request {
    body: any;
    method: string;
    params: {
        [param: string]: string;
    };
    headers: {
        [header: string]: string;
    };
    query: {
        [query: string]: string;
    };
    path: string;
}
export interface Response {
    status(code: number): Response;
    setHeader(name: string, value: string): Response;
    write(data: string): Response;
    end(data?: string): void;
    json(obj: any): void;
}
export declare type RouteHandler = (req: Request, res: Response, next: () => void) => void;
export declare class HttpAPI {
    url?: fabric.Computed<string>;
    private api;
    private deployment;
    private swaggerSpec;
    private apiName;
    private lambdas;
    private bucket;
    constructor(apiName: string);
    staticFile(path: string, filePath: string, contentType?: string): void;
    private routeLambda(method, path, func);
    private routePrepare(method, path);
    route(method: string, path: string, middleware: RouteHandler[], handler: RouteHandler): void;
    get(path: string, middleware: RouteHandler[], handler: RouteHandler): void;
    put(path: string, middleware: RouteHandler[], handler: RouteHandler): void;
    post(path: string, middleware: RouteHandler[], handler: RouteHandler): void;
    delete(path: string, middleware: RouteHandler[], handler: RouteHandler): void;
    options(path: string, middleware: RouteHandler[], handler: RouteHandler): void;
    all(path: string, middleware: RouteHandler[], handler: RouteHandler): void;
    publish(): fabric.Computed<string>;
    private attachCustomDomain(domain);
}
export interface Domain {
    domainName: string;
    certificateBody: string;
    certificatePrivateKey: string;
    certificateChain: string;
}
