---
title: Module config
---

<a href="../index.html">@pulumi/aws</a> &gt; config

<h2 class="pdoc-module-header">Index</h2>

* <a href="#requireRegion">function requireRegion</a>
* <a href="#accessKey">let accessKey</a>
* <a href="#allowedAccountIds">let allowedAccountIds</a>
* <a href="#assumeRole">let assumeRole</a>
* <a href="#dynamodbEndpoint">let dynamodbEndpoint</a>
* <a href="#endpoints">let endpoints</a>
* <a href="#forbiddenAccountIds">let forbiddenAccountIds</a>
* <a href="#insecure">let insecure</a>
* <a href="#kinesisEndpoint">let kinesisEndpoint</a>
* <a href="#maxRetries">let maxRetries</a>
* <a href="#profile">let profile</a>
* <a href="#region">let region</a>
* <a href="#s3ForcePathStyle">let s3ForcePathStyle</a>
* <a href="#secretKey">let secretKey</a>
* <a href="#sharedCredentialsFile">let sharedCredentialsFile</a>
* <a href="#skipCredentialsValidation">let skipCredentialsValidation</a>
* <a href="#skipGetEc2Platforms">let skipGetEc2Platforms</a>
* <a href="#skipMetadataApiCheck">let skipMetadataApiCheck</a>
* <a href="#skipRegionValidation">let skipRegionValidation</a>
* <a href="#skipRequestingAccountId">let skipRequestingAccountId</a>
* <a href="#token">let token</a>

<a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/config/require.ts">config/require.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/config/vars.ts">config/vars.ts</a> 


<h2 class="pdoc-module-header" id="requireRegion">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/config/require.ts#L21">function requireRegion</a>
</h2>

```typescript
requireRegion(): Region
```


requireRegion fetches the AWS region, requiring that it exists; if it has not been configured, an error is thrown.

<h2 class="pdoc-module-header" id="accessKey">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/config/vars.ts#L14">let accessKey</a>
</h2>

```typescript
let accessKey: string | undefined =  __config.get("accessKey");
```


The access key for API operations. You can retrieve this from the 'Security & Credentials' section of the AWS console.

<h2 class="pdoc-module-header" id="allowedAccountIds">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/config/vars.ts#L15">let allowedAccountIds</a>
</h2>

```typescript
let allowedAccountIds: string[] | undefined =  __config.getObject<string[]>("allowedAccountIds");
```

<h2 class="pdoc-module-header" id="assumeRole">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/config/vars.ts#L16">let assumeRole</a>
</h2>

```typescript
let assumeRole: { ... } | undefined =  __config.getObject<{ externalId?: string, policy?: string, roleArn?: string, sessionName?: string }>("assumeRole");
```

<h2 class="pdoc-module-header" id="dynamodbEndpoint">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/config/vars.ts#L21">let dynamodbEndpoint</a>
</h2>

```typescript
let dynamodbEndpoint: string | undefined =  __config.get("dynamodbEndpoint");
```


Use this to override the default endpoint URL constructed from the `region`. It's typically used to connect to
dynamodb-local.

<h2 class="pdoc-module-header" id="endpoints">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/config/vars.ts#L22">let endpoints</a>
</h2>

```typescript
let endpoints: { ... }[] | undefined =  __config.getObject<{ acm?: string, apigateway?: string, autoscaling?: string, cloudformation?: string, cloudwatch?: string, cloudwatchevents?: string, cloudwatchlogs?: string, devicefarm?: string, dynamodb?: string, ec2?: string, ecr?: string, ecs?: string, efs?: string, elb?: string, es?: string, iam?: string, kinesis?: string, kms?: string, lambda?: string, r53?: string, rds?: string, s3?: string, sns?: string, sqs?: string, ssm?: string, sts?: string }[]>("endpoints");
```

<h2 class="pdoc-module-header" id="forbiddenAccountIds">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/config/vars.ts#L23">let forbiddenAccountIds</a>
</h2>

```typescript
let forbiddenAccountIds: string[] | undefined =  __config.getObject<string[]>("forbiddenAccountIds");
```

<h2 class="pdoc-module-header" id="insecure">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/config/vars.ts#L27">let insecure</a>
</h2>

```typescript
let insecure: boolean | undefined =  __config.getObject<boolean>("insecure");
```


Explicitly allow the provider to perform "insecure" SSL requests. If omitted,default value is `false`

<h2 class="pdoc-module-header" id="kinesisEndpoint">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/config/vars.ts#L32">let kinesisEndpoint</a>
</h2>

```typescript
let kinesisEndpoint: string | undefined =  __config.get("kinesisEndpoint");
```


Use this to override the default endpoint URL constructed from the `region`. It's typically used to connect to
kinesalite.

<h2 class="pdoc-module-header" id="maxRetries">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/config/vars.ts#L36">let maxRetries</a>
</h2>

```typescript
let maxRetries: number | undefined =  __config.getObject<number>("maxRetries");
```


The maximum number of times an AWS API request is being executed. If the API request still fails, an error is thrown.

<h2 class="pdoc-module-header" id="profile">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/config/vars.ts#L40">let profile</a>
</h2>

```typescript
let profile: string | undefined =  __config.get("profile");
```


The profile for API operations. If not set, the default profile created with `aws configure` will be used.

<h2 class="pdoc-module-header" id="region">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/config/vars.ts#L44">let region</a>
</h2>

```typescript
let region: Region =  <any>utilities.requireWithDefault(() => __config.require("region"), utilities.getEnv("AWS_REGION", "AWS_DEFAULT_REGION"));
```


The region where AWS operations will take place. Examples are us-east-1, us-west-2, etc.

<h2 class="pdoc-module-header" id="s3ForcePathStyle">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/config/vars.ts#L50">let s3ForcePathStyle</a>
</h2>

```typescript
let s3ForcePathStyle: boolean | undefined =  __config.getObject<boolean>("s3ForcePathStyle");
```


Set this to true to force the request to use path-style addressing, i.e., http://s3.amazonaws.com/BUCKET/KEY. By
default, the S3 client will use virtual hosted bucket addressing when possible (http://BUCKET.s3.amazonaws.com/KEY).
Specific to the Amazon S3 service.

<h2 class="pdoc-module-header" id="secretKey">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/config/vars.ts#L54">let secretKey</a>
</h2>

```typescript
let secretKey: string | undefined =  __config.get("secretKey");
```


The secret key for API operations. You can retrieve this from the 'Security & Credentials' section of the AWS console.

<h2 class="pdoc-module-header" id="sharedCredentialsFile">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/config/vars.ts#L58">let sharedCredentialsFile</a>
</h2>

```typescript
let sharedCredentialsFile: string | undefined =  __config.get("sharedCredentialsFile");
```


The path to the shared credentials file. If not set this defaults to ~/.aws/credentials.

<h2 class="pdoc-module-header" id="skipCredentialsValidation">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/config/vars.ts#L63">let skipCredentialsValidation</a>
</h2>

```typescript
let skipCredentialsValidation: boolean | undefined =  __config.getObject<boolean>("skipCredentialsValidation");
```


Skip the credentials validation via STS API. Used for AWS API implementations that do not have STS
available/implemented.

<h2 class="pdoc-module-header" id="skipGetEc2Platforms">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/config/vars.ts#L67">let skipGetEc2Platforms</a>
</h2>

```typescript
let skipGetEc2Platforms: boolean | undefined =  __config.getObject<boolean>("skipGetEc2Platforms");
```


Skip getting the supported EC2 platforms. Used by users that don't have ec2:DescribeAccountAttributes permissions.

<h2 class="pdoc-module-header" id="skipMetadataApiCheck">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/config/vars.ts#L68">let skipMetadataApiCheck</a>
</h2>

```typescript
let skipMetadataApiCheck: boolean | undefined =  __config.getObject<boolean>("skipMetadataApiCheck");
```

<h2 class="pdoc-module-header" id="skipRegionValidation">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/config/vars.ts#L73">let skipRegionValidation</a>
</h2>

```typescript
let skipRegionValidation: boolean | undefined =  __config.getObject<boolean>("skipRegionValidation");
```


Skip static validation of region name. Used by users of alternative AWS-like APIs or users w/ access to regions that are
not public (yet).

<h2 class="pdoc-module-header" id="skipRequestingAccountId">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/config/vars.ts#L77">let skipRequestingAccountId</a>
</h2>

```typescript
let skipRequestingAccountId: boolean | undefined =  __config.getObject<boolean>("skipRequestingAccountId");
```


Skip requesting the account ID. Used for AWS API implementations that do not have IAM/STS API and/or metadata API.

<h2 class="pdoc-module-header" id="token">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/config/vars.ts#L81">let token</a>
</h2>

```typescript
let token: string | undefined =  __config.get("token");
```


session token. A session token is only required if you are using temporary security credentials.

