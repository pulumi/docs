package main

import (
	"github.com/pulumi/pulumi-awsx/sdk/v2/go/awsx/ecr"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		repository, err := ecr.NewRepository(ctx, "repository", &ecr.RepositoryArgs{
			ForceDelete: pulumi.Bool(true),
		})
		if err != nil {
			return err
		}

		_, err = ecr.NewImage(ctx, "image", &ecr.ImageArgs{
			RepositoryUrl: repository.Url,
			Context:       pulumi.String("./app"),
			Platform:      pulumi.String("linux/amd64"),
		})
		if err != nil {
			return err
		}

		ctx.Export("url", repository.Url)
		return nil
	})
}
