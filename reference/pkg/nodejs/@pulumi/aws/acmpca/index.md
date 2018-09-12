---
title: Module acmpca
---

<a href="../index.html">@pulumi/aws</a> &gt; acmpca

<h2 class="pdoc-module-header">Index</h2>

* <a href="#CertificateAuthority">class CertificateAuthority</a>
* <a href="#getCertificateAuthority">function getCertificateAuthority</a>
* <a href="#CertificateAuthorityArgs">interface CertificateAuthorityArgs</a>
* <a href="#CertificateAuthorityState">interface CertificateAuthorityState</a>
* <a href="#GetCertificateAuthorityArgs">interface GetCertificateAuthorityArgs</a>
* <a href="#GetCertificateAuthorityResult">interface GetCertificateAuthorityResult</a>

<a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acmpca/certificateAuthority.ts">acmpca/certificateAuthority.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acmpca/getCertificateAuthority.ts">acmpca/getCertificateAuthority.ts</a> 


<h2 class="pdoc-module-header" id="CertificateAuthority">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acmpca/certificateAuthority.ts#L14">class CertificateAuthority</a>
</h2>

Provides a resource to manage AWS Certificate Manager Private Certificate Authorities (ACM PCA Certificate Authorities).

~> **NOTE:** Creating this resource will leave the certificate authority in a `PENDING_CERTIFICATE` status, which means it cannot yet issue certificates. To complete this setup, you must fully sign the certificate authority CSR available in the `certificate_signing_request` attribute and import the signed certificate outside of Terraform. Terraform can support another resource to manage that workflow automatically in the future.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acmpca/certificateAuthority.ts#L78">constructor</a>
</h3>

```typescript
new CertificateAuthority(name: string, args: CertificateAuthorityArgs, opts?: pulumi.CustomResourceOptions)
```


Create a CertificateAuthority resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acmpca/certificateAuthority.ts#L23">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: CertificateAuthorityState): CertificateAuthority
```


Get an existing CertificateAuthority resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acmpca/certificateAuthority.ts#L30">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


Amazon Resource Name (ARN) of the certificate authority.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acmpca/certificateAuthority.ts#L34">property certificate</a>
</h3>

```typescript
public certificate: pulumi.Output<string>;
```


Base64-encoded certificate authority (CA) certificate. Only available after the certificate authority certificate has been imported.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acmpca/certificateAuthority.ts#L38">property certificateAuthorityConfiguration</a>
</h3>

```typescript
public certificateAuthorityConfiguration: pulumi.Output<{ ... }>;
```


Nested argument containing algorithms and certificate subject information. Defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acmpca/certificateAuthority.ts#L42">property certificateChain</a>
</h3>

```typescript
public certificateChain: pulumi.Output<string>;
```


Base64-encoded certificate chain that includes any intermediate certificates and chains up to root on-premises certificate that you used to sign your private CA certificate. The chain does not include your private CA certificate. Only available after the certificate authority certificate has been imported.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acmpca/certificateAuthority.ts#L46">property certificateSigningRequest</a>
</h3>

```typescript
public certificateSigningRequest: pulumi.Output<string>;
```


The base64 PEM-encoded certificate signing request (CSR) for your private CA certificate.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acmpca/certificateAuthority.ts#L50">property enabled</a>
</h3>

```typescript
public enabled: pulumi.Output<boolean | undefined>;
```


Boolean value that specifies whether certificate revocation lists (CRLs) are enabled. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acmpca/certificateAuthority.ts#L54">property notAfter</a>
</h3>

```typescript
public notAfter: pulumi.Output<string>;
```


Date and time after which the certificate authority is not valid. Only available after the certificate authority certificate has been imported.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acmpca/certificateAuthority.ts#L58">property notBefore</a>
</h3>

```typescript
public notBefore: pulumi.Output<string>;
```


Date and time before which the certificate authority is not valid. Only available after the certificate authority certificate has been imported.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acmpca/certificateAuthority.ts#L62">property revocationConfiguration</a>
</h3>

```typescript
public revocationConfiguration: pulumi.Output<{ ... } | undefined>;
```


Nested argument containing revocation configuration. Defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acmpca/certificateAuthority.ts#L66">property serial</a>
</h3>

```typescript
public serial: pulumi.Output<string>;
```


Serial number of the certificate authority. Only available after the certificate authority certificate has been imported.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acmpca/certificateAuthority.ts#L70">property status</a>
</h3>

```typescript
public status: pulumi.Output<string>;
```


Status of the certificate authority.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acmpca/certificateAuthority.ts#L74">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<Tags | undefined>;
```


Specifies a key-value map of user-defined tags that are attached to the certificate authority.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acmpca/certificateAuthority.ts#L78">property type</a>
</h3>

```typescript
public type: pulumi.Output<string | undefined>;
```


The type of the certificate authority. Currently, this must be `SUBORDINATE`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="getCertificateAuthority">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acmpca/getCertificateAuthority.ts#L10">function getCertificateAuthority</a>
</h2>

```typescript
getCertificateAuthority(args: GetCertificateAuthorityArgs, opts?: pulumi.InvokeOptions): Promise<GetCertificateAuthorityResult>
```


Get information on a AWS Certificate Manager Private Certificate Authority (ACM PCA Certificate Authority).

<h2 class="pdoc-module-header" id="CertificateAuthorityArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acmpca/certificateAuthority.ts#L189">interface CertificateAuthorityArgs</a>
</h2>

The set of arguments for constructing a CertificateAuthority resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acmpca/certificateAuthority.ts#L193">property certificateAuthorityConfiguration</a>
</h3>

```typescript
certificateAuthorityConfiguration: pulumi.Input<{ ... }>;
```


Nested argument containing algorithms and certificate subject information. Defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acmpca/certificateAuthority.ts#L197">property enabled</a>
</h3>

```typescript
enabled?: pulumi.Input<boolean>;
```


Boolean value that specifies whether certificate revocation lists (CRLs) are enabled. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acmpca/certificateAuthority.ts#L201">property revocationConfiguration</a>
</h3>

```typescript
revocationConfiguration?: pulumi.Input<{ ... }>;
```


Nested argument containing revocation configuration. Defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acmpca/certificateAuthority.ts#L205">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


Specifies a key-value map of user-defined tags that are attached to the certificate authority.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acmpca/certificateAuthority.ts#L209">property type</a>
</h3>

```typescript
type?: pulumi.Input<string>;
```


The type of the certificate authority. Currently, this must be `SUBORDINATE`.

<h2 class="pdoc-module-header" id="CertificateAuthorityState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acmpca/certificateAuthority.ts#L131">interface CertificateAuthorityState</a>
</h2>

Input properties used for looking up and filtering CertificateAuthority resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acmpca/certificateAuthority.ts#L135">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


Amazon Resource Name (ARN) of the certificate authority.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acmpca/certificateAuthority.ts#L139">property certificate</a>
</h3>

```typescript
certificate?: pulumi.Input<string>;
```


Base64-encoded certificate authority (CA) certificate. Only available after the certificate authority certificate has been imported.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acmpca/certificateAuthority.ts#L143">property certificateAuthorityConfiguration</a>
</h3>

```typescript
certificateAuthorityConfiguration?: pulumi.Input<{ ... }>;
```


Nested argument containing algorithms and certificate subject information. Defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acmpca/certificateAuthority.ts#L147">property certificateChain</a>
</h3>

```typescript
certificateChain?: pulumi.Input<string>;
```


Base64-encoded certificate chain that includes any intermediate certificates and chains up to root on-premises certificate that you used to sign your private CA certificate. The chain does not include your private CA certificate. Only available after the certificate authority certificate has been imported.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acmpca/certificateAuthority.ts#L151">property certificateSigningRequest</a>
</h3>

```typescript
certificateSigningRequest?: pulumi.Input<string>;
```


The base64 PEM-encoded certificate signing request (CSR) for your private CA certificate.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acmpca/certificateAuthority.ts#L155">property enabled</a>
</h3>

```typescript
enabled?: pulumi.Input<boolean>;
```


Boolean value that specifies whether certificate revocation lists (CRLs) are enabled. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acmpca/certificateAuthority.ts#L159">property notAfter</a>
</h3>

```typescript
notAfter?: pulumi.Input<string>;
```


Date and time after which the certificate authority is not valid. Only available after the certificate authority certificate has been imported.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acmpca/certificateAuthority.ts#L163">property notBefore</a>
</h3>

```typescript
notBefore?: pulumi.Input<string>;
```


Date and time before which the certificate authority is not valid. Only available after the certificate authority certificate has been imported.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acmpca/certificateAuthority.ts#L167">property revocationConfiguration</a>
</h3>

```typescript
revocationConfiguration?: pulumi.Input<{ ... }>;
```


Nested argument containing revocation configuration. Defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acmpca/certificateAuthority.ts#L171">property serial</a>
</h3>

```typescript
serial?: pulumi.Input<string>;
```


Serial number of the certificate authority. Only available after the certificate authority certificate has been imported.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acmpca/certificateAuthority.ts#L175">property status</a>
</h3>

```typescript
status?: pulumi.Input<string>;
```


Status of the certificate authority.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acmpca/certificateAuthority.ts#L179">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


Specifies a key-value map of user-defined tags that are attached to the certificate authority.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acmpca/certificateAuthority.ts#L183">property type</a>
</h3>

```typescript
type?: pulumi.Input<string>;
```


The type of the certificate authority. Currently, this must be `SUBORDINATE`.

<h2 class="pdoc-module-header" id="GetCertificateAuthorityArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acmpca/getCertificateAuthority.ts#L21">interface GetCertificateAuthorityArgs</a>
</h2>

A collection of arguments for invoking getCertificateAuthority.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acmpca/getCertificateAuthority.ts#L25">property arn</a>
</h3>

```typescript
arn: string;
```


Amazon Resource Name (ARN) of the certificate authority.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acmpca/getCertificateAuthority.ts#L26">property revocationConfigurations</a>
</h3>

```typescript
revocationConfigurations?: { ... }[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acmpca/getCertificateAuthority.ts#L27">property tags</a>
</h3>

```typescript
tags?: { ... };
```

<h2 class="pdoc-module-header" id="GetCertificateAuthorityResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acmpca/getCertificateAuthority.ts#L33">interface GetCertificateAuthorityResult</a>
</h2>

A collection of values returned by getCertificateAuthority.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acmpca/getCertificateAuthority.ts#L37">property certificate</a>
</h3>

```typescript
certificate: string;
```


Base64-encoded certificate authority (CA) certificate. Only available after the certificate authority certificate has been imported.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acmpca/getCertificateAuthority.ts#L41">property certificateChain</a>
</h3>

```typescript
certificateChain: string;
```


Base64-encoded certificate chain that includes any intermediate certificates and chains up to root on-premises certificate that you used to sign your private CA certificate. The chain does not include your private CA certificate. Only available after the certificate authority certificate has been imported.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acmpca/getCertificateAuthority.ts#L45">property certificateSigningRequest</a>
</h3>

```typescript
certificateSigningRequest: string;
```


The base64 PEM-encoded certificate signing request (CSR) for your private CA certificate.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acmpca/getCertificateAuthority.ts#L82">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acmpca/getCertificateAuthority.ts#L49">property notAfter</a>
</h3>

```typescript
notAfter: string;
```


Date and time after which the certificate authority is not valid. Only available after the certificate authority certificate has been imported.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acmpca/getCertificateAuthority.ts#L53">property notBefore</a>
</h3>

```typescript
notBefore: string;
```


Date and time before which the certificate authority is not valid. Only available after the certificate authority certificate has been imported.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acmpca/getCertificateAuthority.ts#L62">property revocationConfigurations</a>
</h3>

```typescript
revocationConfigurations: { ... }[];
```


Nested attribute containing revocation configuration.
* `revocation_configuration.0.crl_configuration` - Nested attribute containing configuration of the certificate revocation list (CRL), if any, maintained by the certificate authority.
* `revocation_configuration.0.crl_configuration.0.custom_cname` - Name inserted into the certificate CRL Distribution Points extension that enables the use of an alias for the CRL distribution point.
* `revocation_configuration.0.crl_configuration.0.enabled` - Boolean value that specifies whether certificate revocation lists (CRLs) are enabled.
* `revocation_configuration.0.crl_configuration.0.expiration_in_days` - Number of days until a certificate expires.
* `revocation_configuration.0.crl_configuration.0.s3_bucket_name` - Name of the S3 bucket that contains the CRL.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acmpca/getCertificateAuthority.ts#L66">property serial</a>
</h3>

```typescript
serial: string;
```


Serial number of the certificate authority. Only available after the certificate authority certificate has been imported.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acmpca/getCertificateAuthority.ts#L70">property status</a>
</h3>

```typescript
status: string;
```


Status of the certificate authority.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acmpca/getCertificateAuthority.ts#L74">property tags</a>
</h3>

```typescript
tags: { ... };
```


Specifies a key-value map of user-defined tags that are attached to the certificate authority.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acmpca/getCertificateAuthority.ts#L78">property type</a>
</h3>

```typescript
type: string;
```


The type of the certificate authority.

