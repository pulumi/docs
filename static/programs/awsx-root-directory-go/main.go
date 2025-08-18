package main

import (
	"os"
	"path/filepath"

	"github.com/pulumi/pulumi-awsx/sdk/v2/go/awsx/ecr"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		root := ctx.RootDirectory()
		cwd, err := os.Getwd()
		if err != nil {
			return err
		}
		path := filepath.Join(root, "app")
		path, err = filepath.Rel(cwd, path)
		if err != nil {
			return err
		}

		repository, err := ecr.NewRepository(ctx, "repository", &ecr.RepositoryArgs{
			ForceDelete: pulumi.Bool(true),
		})
		if err != nil {
			return err
		}

		_, err = ecr.NewImage(ctx, "image", &ecr.ImageArgs{
			RepositoryUrl: repository.Url,
			Context:       pulumi.String(path),
			Platform:      pulumi.String("linux/amd64"),
		})
		if err != nil {
			return err
		}

		ctx.Export("url", repository.Url)
		return nil
	})
}
