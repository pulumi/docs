package main

import (
	"fmt"

	"github.com/pulumi/pulumi-aws-apigateway/sdk/v2/go/apigateway"
	"github.com/pulumi/pulumi-aws/sdk/v6/go/aws"
	"github.com/pulumi/pulumi-aws/sdk/v6/go/aws/acm"
	awsapigateway "github.com/pulumi/pulumi-aws/sdk/v6/go/aws/apigateway"
	"github.com/pulumi/pulumi-aws/sdk/v6/go/aws/route53"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {

		hostedZone := "example.com"
		domainName := fmt.Sprintf("myapp.%s", hostedZone)

		zone := route53.LookupZoneOutput(ctx, route53.LookupZoneOutputArgs{
			Name: pulumi.StringPtr(hostedZone),
		})

		usEast1, err := aws.NewProvider(ctx, "us-east-1", &aws.ProviderArgs{
			Region: pulumi.StringPtr("us-east-1"),
		})
		if err != nil {
			return err
		}

		certificate, err := acm.NewCertificate(ctx, "certificate", &acm.CertificateArgs{
			DomainName:       pulumi.String(domainName),
			ValidationMethod: pulumi.String("DNS"),
		}, pulumi.Provider(usEast1))
		if err != nil {
			return err
		}

		validationOption := certificate.DomainValidationOptions.Index(pulumi.Int(0))
		validationRecord, err := route53.NewRecord(ctx, "certificate-validation-record", &route53.RecordArgs{
			Name: validationOption.ResourceRecordName().Elem(),
			Type: validationOption.ResourceRecordType().Elem(),
			Records: pulumi.StringArray{
				validationOption.ResourceRecordValue().Elem(),
			},
			ZoneId: zone.ZoneId(),
			Ttl:    pulumi.Int(60),
		})
		if err != nil {
			return err
		}

		validation, err := acm.NewCertificateValidation(ctx, "certificate-validation", &acm.CertificateValidationArgs{
			CertificateArn: certificate.Arn,
			ValidationRecordFqdns: pulumi.StringArray{
				validationRecord.Fqdn,
			},
		}, pulumi.Provider(usEast1))
		if err != nil {
			return err
		}

		methodGET := apigateway.MethodGET
		api, err := apigateway.NewRestAPI(ctx, "api", &apigateway.RestAPIArgs{
			Routes: []apigateway.RouteArgs{
				{
					Path:      "/",
					Method:    &methodGET,
					LocalPath: pulumi.StringRef("www"),
				},
			},
		})
		if err != nil {
			return err
		}

		gatewayDomainName, err := awsapigateway.NewDomainName(ctx, "gateway-domain-name", &awsapigateway.DomainNameArgs{
			CertificateArn: certificate.Arn,
			DomainName:     pulumi.String(domainName),
		}, pulumi.DependsOn([]pulumi.Resource{validation}))
		if err != nil {
			return err
		}

		_, err = route53.NewRecord(ctx, "gateway-dns-record", &route53.RecordArgs{
			ZoneId: zone.ZoneId(),
			Type:   pulumi.String("A"),
			Name:   pulumi.String(domainName),
			Aliases: route53.RecordAliasArray{
				route53.RecordAliasArgs{
					Name:                 gatewayDomainName.CloudfrontDomainName,
					ZoneId:               gatewayDomainName.CloudfrontZoneId,
					EvaluateTargetHealth: pulumi.Bool(false),
				},
			},
		})
		if err != nil {
			return err
		}

		apiID := api.Api.ApplyT(func(api *awsapigateway.RestApi) pulumi.StringOutput {
			return api.ID().ToStringOutput()
		})

		basePathMapping, err := awsapigateway.NewBasePathMapping(ctx, "gateway-path-mapping", &awsapigateway.BasePathMappingArgs{
			RestApi:    apiID,
			StageName:  api.Stage.StageName(),
			DomainName: gatewayDomainName.DomainName,
		})
		if err != nil {
			return err
		}

		ctx.Export("url", pulumi.Sprintf("http://%s", basePathMapping.DomainName))
		return nil
	})
}
