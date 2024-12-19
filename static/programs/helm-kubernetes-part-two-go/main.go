package main

import (
	"context"

	helmv4 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/helm/v4"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi/internals"
	"k8s.io/apimachinery/pkg/apis/meta/v1/unstructured"
)

func main() {

	applyPatchForceAnnotation := func(ctx context.Context, rta *pulumi.XResourceTransformArgs) *pulumi.XResourceTransformResult {
		transform := func(applier interface{}) {
			o := rta.Props.ToMapOutputWithContext(ctx).ApplyT(applier)
			r, err := internals.UnsafeAwaitOutput(ctx, o)
			if err != nil {
				panic(err)
			}
			rta.Props = r.Value.(pulumi.Map)
		}

		switch rta.Type {
		case "kubernetes:helm.sh/v4:Chart":
			// Do nothing for Helm charts
		default:
			transform(func(obj map[string]any) pulumi.Map {
				// note: obj is an ordinary Unstructured object at this point.
				err := unstructured.SetNestedField(obj, "12345", "metadata", "annotations", "cost-center")
				if err != nil {
					return nil
				}
				return pulumi.ToMap(obj)
			})
		}
		return &pulumi.XResourceTransformResult{
			Props: rta.Props,
			Opts:  rta.Opts,
		}
	}

	pulumi.Run(func(ctx *pulumi.Context) error {
		_, err := helmv4.NewChart(ctx, "cert-manager", &helmv4.ChartArgs{
			Namespace: pulumi.String("cert-manager"),
			Chart:     pulumi.String("oci://registry-1.docker.io/bitnamicharts/cert-manager"),
			Version:   pulumi.String("1.3.1"),
		}, pulumi.Transforms([]pulumi.XResourceTransform{applyPatchForceAnnotation}))
		if err != nil {
			return err
		}
		return nil
	})
}
