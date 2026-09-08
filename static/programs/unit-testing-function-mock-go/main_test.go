package main

import (
	"sync"
	"testing"

	"github.com/pulumi/pulumi/sdk/v3/go/common/resource"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/stretchr/testify/assert"
)

type mocks int

func (mocks) NewResource(args pulumi.MockResourceArgs) (string, resource.PropertyMap, error) {
	return args.Name + "_id", args.Inputs, nil
}

func (mocks) Call(args pulumi.MockCallArgs) (resource.PropertyMap, error) {
	if args.Token == "aws:ec2/getAmi:getAmi" {
		return resource.NewPropertyMapFromMap(map[string]interface{}{
			"id":           "ami-0eb1f3cdeeb8eed2a",
			"architecture": "x86_64",
		}), nil
	}
	return args.Args, nil
}

func TestInfrastructure(t *testing.T) {
	err := pulumi.RunErr(func(ctx *pulumi.Context) error {
		infra, err := createInfrastructure(ctx)
		assert.NoError(t, err)

		var wg sync.WaitGroup
		wg.Add(1)

		// The instance uses the AMI returned by the lookup.
		pulumi.All(infra.server.URN(), infra.server.Ami).ApplyT(func(all []interface{}) error {
			urn := all[0].(pulumi.URN)
			ami := all[1].(string)

			assert.Equalf(t, "ami-0eb1f3cdeeb8eed2a", ami, "unexpected AMI on server %v", urn)
			wg.Done()
			return nil
		})

		wg.Wait()
		return nil
	}, pulumi.WithMocks("project", "stack", mocks(0))) // Project and stack names; they show up in mocked URNs.
	assert.NoError(t, err)
}
