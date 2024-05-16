package main

import (
	"github.com/pulumi/pulumi-aws/sdk/v6/go/aws/acm"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		_, err := acm.NewCertificate(ctx, "cert", &acm.CertificateArgs{
			DomainName:       pulumi.String("example.com"),
			ValidationMethod: pulumi.String("DNS"),
		})
		if err != nil {
			return err
		}
		return nil
	})
}
