package main

import (
	"sample-components-go/staticpagecomponent"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		page, err := staticpagecomponent.NewStaticPage(ctx, "my-static-page", &staticpagecomponent.StaticPageArgs{
			IndexContent: pulumi.String("<h1>I love Pulumi!</h1>"),
		})
		if err != nil {
			return err
		}

		url := page.Endpoint.ApplyT(func(endpoint string) string {
			return "http://" + endpoint
		}).(pulumi.StringOutput)

		ctx.Export("websiteURL", url)
		return nil
	})
}
