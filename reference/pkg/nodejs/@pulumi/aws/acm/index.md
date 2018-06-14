---
title: Module acm
---

<a href="../index.html">@pulumi/aws</a> &gt; acm

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Certificate">class Certificate</a>
* <a href="#CertificateValidation">class CertificateValidation</a>
* <a href="#getCertificate">function getCertificate</a>
* <a href="#CertificateArgs">interface CertificateArgs</a>
* <a href="#CertificateState">interface CertificateState</a>
* <a href="#CertificateValidationArgs">interface CertificateValidationArgs</a>
* <a href="#CertificateValidationState">interface CertificateValidationState</a>
* <a href="#GetCertificateArgs">interface GetCertificateArgs</a>
* <a href="#GetCertificateResult">interface GetCertificateResult</a>

<a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acm/certificate.ts">acm/certificate.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acm/certificateValidation.ts">acm/certificateValidation.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acm/getCertificate.ts">acm/getCertificate.ts</a> 


<h2 class="pdoc-module-header" id="Certificate">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acm/certificate.ts#L22">class Certificate</a>
</h2>

The ACM certificate resource allows requesting and management of certificates
from the Amazon Certificate Manager.

It deals with requesting certificates and managing their attributes and life-cycle.
This resource does not deal with validation of a certificate but can provide inputs
for other resources implementing the validation. It does not wait for a certificate to be issued.
Use a [`aws_acm_certificate_validation`](acm_certificate_validation.html) resource for this.

Most commonly, this resource is used to together with [`aws_route53_record`](route53_record.html) and
[`aws_acm_certificate_validation`](acm_certificate_validation.html) to request a DNS validated certificate,
deploy the required validation records and wait for validation to complete.

Domain validation through E-Mail is also supported but should be avoided as it requires a manual step outside
of Terraform.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acm/certificate.ts#L62">constructor</a>
</h3>

```typescript
new Certificate(name: string, args: CertificateArgs, opts?: pulumi.ResourceOptions)
```


Create a Certificate resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acm/certificate.ts#L31">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: CertificateState): Certificate
```


Get an existing Certificate resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acm/certificate.ts#L38">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN of the certificate

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acm/certificate.ts#L42">property domainName</a>
</h3>

```typescript
public domainName: pulumi.Output<string>;
```


A domain name for which the certificate should be issued

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acm/certificate.ts#L46">property domainValidationOptions</a>
</h3>

```typescript
public domainValidationOptions: pulumi.Output<{ ... }[]>;
```


A list of attributes to feed into other resources to complete certificate validation. Can have more than one element, e.g. if SANs are defined. Only set if `DNS`-validation was used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acm/certificate.ts#L50">property subjectAlternativeNames</a>
</h3>

```typescript
public subjectAlternativeNames: pulumi.Output<string[] | undefined>;
```


A list of domains that should be SANs in the issued certificate

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acm/certificate.ts#L54">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... } | undefined>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acm/certificate.ts#L58">property validationEmails</a>
</h3>

```typescript
public validationEmails: pulumi.Output<string[]>;
```


A list of addresses that received a validation E-Mail. Only set if `EMAIL`-validation was used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acm/certificate.ts#L62">property validationMethod</a>
</h3>

```typescript
public validationMethod: pulumi.Output<string>;
```


Which method to use for validation. `DNS` or `EMAIL` are valid, `NONE` can be used for certificates that were imported into ACM and then into Terraform.

<h2 class="pdoc-module-header" id="CertificateValidation">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acm/certificateValidation.ts#L17">class CertificateValidation</a>
</h2>

This resource represents a successful validation of an ACM certificate in concert
with other resources.

Most commonly, this resource is used to together with [`aws_route53_record`](route53_record.html) and
[`aws_acm_certificate`](acm_certificate.html) to request a DNS validated certificate,
deploy the required validation records and wait for validation to complete.

~> **WARNING:** This resource implements a part of the validation workflow. It does not represent a real-world entity in AWS, therefore changing or deleting this resource on its own has no immediate effect.


<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acm/certificateValidation.ts#L37">constructor</a>
</h3>

```typescript
new CertificateValidation(name: string, args: CertificateValidationArgs, opts?: pulumi.ResourceOptions)
```


Create a CertificateValidation resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acm/certificateValidation.ts#L26">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: CertificateValidationState): CertificateValidation
```


Get an existing CertificateValidation resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acm/certificateValidation.ts#L33">property certificateArn</a>
</h3>

```typescript
public certificateArn: pulumi.Output<string>;
```


The ARN of the certificate that is being validated.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acm/certificateValidation.ts#L37">property validationRecordFqdns</a>
</h3>

```typescript
public validationRecordFqdns: pulumi.Output<string[] | undefined>;
```


List of FQDNs that implement the validation. Only valid for DNS validation method ACM certificates. If this is set, the resource can implement additional sanity checks and has an explicit dependency on the resource that is implementing the validation

<h2 class="pdoc-module-header" id="getCertificate">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acm/getCertificate.ts#L13">function getCertificate</a>
</h2>

```typescript
getCertificate(args: GetCertificateArgs): Promise<GetCertificateResult>
```


Use this data source to get the ARN of a certificate in AWS Certificate
Manager (ACM). The process of requesting and verifying a certificate in ACM
requires some manual steps, which means that Terraform cannot automate the
creation of ACM certificates. But using this data source, you can reference
them by domain without having to hard code the ARNs as input.

<h2 class="pdoc-module-header" id="CertificateArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acm/certificate.ts#L140">interface CertificateArgs</a>
</h2>

The set of arguments for constructing a Certificate resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acm/certificate.ts#L144">property domainName</a>
</h3>

```typescript
domainName: pulumi.Input<string>;
```


A domain name for which the certificate should be issued

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acm/certificate.ts#L148">property subjectAlternativeNames</a>
</h3>

```typescript
subjectAlternativeNames?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of domains that should be SANs in the issued certificate

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acm/certificate.ts#L152">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acm/certificate.ts#L156">property validationMethod</a>
</h3>

```typescript
validationMethod: pulumi.Input<string>;
```


Which method to use for validation. `DNS` or `EMAIL` are valid, `NONE` can be used for certificates that were imported into ACM and then into Terraform.

<h2 class="pdoc-module-header" id="CertificateState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acm/certificate.ts#L106">interface CertificateState</a>
</h2>

Input properties used for looking up and filtering Certificate resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acm/certificate.ts#L110">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN of the certificate

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acm/certificate.ts#L114">property domainName</a>
</h3>

```typescript
domainName?: pulumi.Input<string>;
```


A domain name for which the certificate should be issued

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acm/certificate.ts#L118">property domainValidationOptions</a>
</h3>

```typescript
domainValidationOptions?: pulumi.Input<{ ... }[]>;
```


A list of attributes to feed into other resources to complete certificate validation. Can have more than one element, e.g. if SANs are defined. Only set if `DNS`-validation was used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acm/certificate.ts#L122">property subjectAlternativeNames</a>
</h3>

```typescript
subjectAlternativeNames?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of domains that should be SANs in the issued certificate

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acm/certificate.ts#L126">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acm/certificate.ts#L130">property validationEmails</a>
</h3>

```typescript
validationEmails?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of addresses that received a validation E-Mail. Only set if `EMAIL`-validation was used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acm/certificate.ts#L134">property validationMethod</a>
</h3>

```typescript
validationMethod?: pulumi.Input<string>;
```


Which method to use for validation. `DNS` or `EMAIL` are valid, `NONE` can be used for certificates that were imported into ACM and then into Terraform.

<h2 class="pdoc-module-header" id="CertificateValidationArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acm/certificateValidation.ts#L82">interface CertificateValidationArgs</a>
</h2>

The set of arguments for constructing a CertificateValidation resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acm/certificateValidation.ts#L86">property certificateArn</a>
</h3>

```typescript
certificateArn: pulumi.Input<string>;
```


The ARN of the certificate that is being validated.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acm/certificateValidation.ts#L90">property validationRecordFqdns</a>
</h3>

```typescript
validationRecordFqdns?: pulumi.Input<pulumi.Input<string>[]>;
```


List of FQDNs that implement the validation. Only valid for DNS validation method ACM certificates. If this is set, the resource can implement additional sanity checks and has an explicit dependency on the resource that is implementing the validation

<h2 class="pdoc-module-header" id="CertificateValidationState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acm/certificateValidation.ts#L68">interface CertificateValidationState</a>
</h2>

Input properties used for looking up and filtering CertificateValidation resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acm/certificateValidation.ts#L72">property certificateArn</a>
</h3>

```typescript
certificateArn?: pulumi.Input<string>;
```


The ARN of the certificate that is being validated.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acm/certificateValidation.ts#L76">property validationRecordFqdns</a>
</h3>

```typescript
validationRecordFqdns?: pulumi.Input<pulumi.Input<string>[]>;
```


List of FQDNs that implement the validation. Only valid for DNS validation method ACM certificates. If this is set, the resource can implement additional sanity checks and has an explicit dependency on the resource that is implementing the validation

<h2 class="pdoc-module-header" id="GetCertificateArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acm/getCertificate.ts#L25">interface GetCertificateArgs</a>
</h2>

A collection of arguments for invoking getCertificate.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acm/getCertificate.ts#L29">property domain</a>
</h3>

```typescript
domain: pulumi.Input<string>;
```


The domain of the certificate to look up. If no certificate is found with this name, an error will be returned.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acm/getCertificate.ts#L33">property mostRecent</a>
</h3>

```typescript
mostRecent?: pulumi.Input<boolean>;
```


If set to true, it sorts the certificates matched by previous criteria by the NotBefore field, returning only the most recent one. If set to false, it returns an error if more than one certificate is found. Defaults to false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acm/getCertificate.ts#L39">property statuses</a>
</h3>

```typescript
statuses?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of statuses on which to filter the returned list. Valid values are `PENDING_VALIDATION`, `ISSUED`,
`INACTIVE`, `EXPIRED`, `VALIDATION_TIMED_OUT`, `REVOKED` and `FAILED`. If no value is specified, only certificates in the `ISSUED` state
are returned.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acm/getCertificate.ts#L43">property types</a>
</h3>

```typescript
types?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of types on which to filter the returned list. Valid values are `AMAZON_ISSUED` and `IMPORTED`.

<h2 class="pdoc-module-header" id="GetCertificateResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acm/getCertificate.ts#L49">interface GetCertificateResult</a>
</h2>

A collection of values returned by getCertificate.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/acm/getCertificate.ts#L53">property arn</a>
</h3>

```typescript
arn: string;
```


Set to the ARN of the found certificate, suitable for referencing in other resources that support ACM certificates.

