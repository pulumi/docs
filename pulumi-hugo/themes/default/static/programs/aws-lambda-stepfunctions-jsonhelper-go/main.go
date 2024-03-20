/*
The Pulumi Go SDK does not currently support serializing or deserializing maps with unknown values.
It is tracked [here](https://github.com/pulumi/pulumi/issues/12460).

The following is a simplified example of using `pulumi.JSONMarshal` in Go.
*/

package main

import (
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/sfn"
	"github.com/pulumi/pulumi-aws/sdk/v4/go/aws/iam"
	"github.com/pulumi/pulumi-aws/sdk/v4/go/aws/lambda"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		pulumi.JSONMarshal(pulumi.ToMapOutput(map[string]pulumi.Output{
			"bool": pulumi.ToOutput(true),
			"int":  pulumi.ToOutput(1),
			"str":  pulumi.ToOutput("hello"),
			"arr": pulumi.ToArrayOutput([]pulumi.Output{
				pulumi.ToOutput(false),
				pulumi.ToOutput(1.0),
				pulumi.ToOutput(""),
				pulumi.ToMapOutput(map[string]pulumi.Output{
					"key": pulumi.ToOutput("value"),
				}),
			}),
			"map": pulumi.ToMapOutput(map[string]pulumi.Output{
				"key": pulumi.ToOutput("value"),
			}),
			// The following functionality is currently unsupported as myResource
			// is an unknown value.
			"unknown": myResource.ApplyT(func(res interface{}) (interface{}, error) {
				return "Hello World!", nil
			}),
		}))
		return nil
	})
}
