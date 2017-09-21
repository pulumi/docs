---
layout: typescript-reference
repo: pulumi-aws
subpath: opsworks/application.d.ts
---
import * as fabric from "@pulumi/pulumi-fabric";
export declare class Application extends fabric.Resource {
    readonly appSource: fabric.Computed<{
        password?: string;
        revision?: string;
        sshKey?: string;
        type: string;
        url?: string;
        username?: string;
    }[]>;
    readonly autoBundleOnDeploy?: fabric.Computed<string>;
    readonly awsFlowRubySettings?: fabric.Computed<string>;
    readonly dataSourceArn?: fabric.Computed<string>;
    readonly dataSourceDatabaseName?: fabric.Computed<string>;
    readonly dataSourceType?: fabric.Computed<string>;
    readonly description?: fabric.Computed<string>;
    readonly documentRoot?: fabric.Computed<string>;
    readonly domains?: fabric.Computed<string[]>;
    readonly enableSsl?: fabric.Computed<boolean>;
    readonly environment?: fabric.Computed<{
        key: string;
        secure?: boolean;
        value: string;
    }[]>;
    readonly applicationId: fabric.Computed<string>;
    readonly name: fabric.Computed<string>;
    readonly railsEnv?: fabric.Computed<string>;
    readonly shortName: fabric.Computed<string>;
    readonly sslConfiguration?: fabric.Computed<{
        certificate: string;
        chain?: string;
        privateKey: string;
    }[]>;
    readonly stackId: fabric.Computed<string>;
    readonly type: fabric.Computed<string>;
    constructor(urnName: string, args: ApplicationArgs);
}
export interface ApplicationArgs {
    readonly appSource?: fabric.MaybeComputed<{
        password?: fabric.MaybeComputed<string>;
        revision?: fabric.MaybeComputed<string>;
        sshKey?: fabric.MaybeComputed<string>;
        type: fabric.MaybeComputed<string>;
        url?: fabric.MaybeComputed<string>;
        username?: fabric.MaybeComputed<string>;
    }>[];
    readonly autoBundleOnDeploy?: fabric.MaybeComputed<string>;
    readonly awsFlowRubySettings?: fabric.MaybeComputed<string>;
    readonly dataSourceArn?: fabric.MaybeComputed<string>;
    readonly dataSourceDatabaseName?: fabric.MaybeComputed<string>;
    readonly dataSourceType?: fabric.MaybeComputed<string>;
    readonly description?: fabric.MaybeComputed<string>;
    readonly documentRoot?: fabric.MaybeComputed<string>;
    readonly domains?: fabric.MaybeComputed<fabric.MaybeComputed<string>>[];
    readonly enableSsl?: fabric.MaybeComputed<boolean>;
    readonly environment?: fabric.MaybeComputed<{
        key: fabric.MaybeComputed<string>;
        secure?: fabric.MaybeComputed<boolean>;
        value: fabric.MaybeComputed<string>;
    }>[];
    readonly name?: fabric.MaybeComputed<string>;
    readonly railsEnv?: fabric.MaybeComputed<string>;
    readonly shortName?: fabric.MaybeComputed<string>;
    readonly sslConfiguration?: fabric.MaybeComputed<{
        certificate: fabric.MaybeComputed<string>;
        chain?: fabric.MaybeComputed<string>;
        privateKey: fabric.MaybeComputed<string>;
    }>[];
    readonly stackId: fabric.MaybeComputed<string>;
    readonly type: fabric.MaybeComputed<string>;
}
