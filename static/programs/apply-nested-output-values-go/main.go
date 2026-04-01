package main

import (
	"github.com/pulumi/pulumi-aws/sdk/v7/go/aws/acm"
	"github.com/pulumi/pulumi-aws/sdk/v7/go/aws/route53"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		zone, err := route53.NewZone(ctx, "zone", &route53.ZoneArgs{
			Name: pulumi.String("example.com"),
		})
		if err != nil {
			return err
		}

		cert, err := acm.NewCertificate(ctx, "cert", &acm.CertificateArgs{
			DomainName:       pulumi.String("example.com"),
			ValidationMethod: pulumi.String("DNS"),
		})
		if err != nil {
			return err
		}

		// Using apply to access nested output values
		_, err = route53.NewRecord(ctx, "certValidationApply", &route53.RecordArgs{
			Name: cert.DomainValidationOptions.ApplyT(func(opts []acm.CertificateDomainValidationOption) string {
				return *opts[0].ResourceRecordName
			}).(pulumi.StringOutput),
			Type: cert.DomainValidationOptions.ApplyT(func(opts []acm.CertificateDomainValidationOption) string {
				return *opts[0].ResourceRecordType
			}).(pulumi.StringOutput),
			ZoneId: zone.ZoneId,
			Ttl:    pulumi.Int(60),
			Records: pulumi.StringArray{
				cert.DomainValidationOptions.ApplyT(func(opts []acm.CertificateDomainValidationOption) string {
					return *opts[0].ResourceRecordValue
				}).(pulumi.StringOutput),
			},
		})
		if err != nil {
			return err
		}

		// Using lifting to access nested output values
		_, err = route53.NewRecord(ctx, "certValidationLifting", &route53.RecordArgs{
			Name: cert.DomainValidationOptions.Index(pulumi.Int(0)).ResourceRecordName().Elem(),
			Type: cert.DomainValidationOptions.Index(pulumi.Int(0)).ResourceRecordType().Elem(),
			ZoneId: zone.ZoneId,
			Ttl:    pulumi.Int(60),
			Records: pulumi.StringArray{
				cert.DomainValidationOptions.Index(pulumi.Int(0)).ResourceRecordValue().Elem(),
			},
		})
		if err != nil {
			return err
		}

		return nil
	})
}
