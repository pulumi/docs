package main

import (
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/applicationsignals"
	"github.com/pulumi/pulumi-aws/sdk/v7/go/aws/s3"
	"github.com/pulumi/pulumi-awsx/sdk/v3/go/awsx/ec2"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {

		// AWSx provides a VPC with well-architected defaults: subnets, route
		// tables, NAT gateways, and an internet gateway, all pre-configured.
		vpc, err := ec2.NewVpc(ctx, "main", &ec2.VpcArgs{
			NatGateways: &ec2.NatGatewayConfigurationArgs{
				Strategy: ec2.NatGatewayStrategySingle,
			},
		})
		if err != nil {
			return err
		}

		// The AWS provider manages the majority of resources.
		bucket, err := s3.NewBucket(ctx, "app-data", nil)
		if err != nil {
			return err
		}

		// The AWS Cloud Control provider is used for a resource available
		// through Cloud Control but not yet in the classic AWS provider.
		slo, err := applicationsignals.NewServiceLevelObjective(ctx, "api-slo", &applicationsignals.ServiceLevelObjectiveArgs{
			Name: pulumi.String("api-availability-slo"),
			Sli: applicationsignals.ServiceLevelObjectiveSliArgs{
				SliMetric: applicationsignals.ServiceLevelObjectiveSliMetricArgs{
					MetricType:    applicationsignals.ServiceLevelObjectiveSliMetricMetricTypeAvailability,
					OperationName: pulumi.StringPtr("GET /api"),
					KeyAttributes: pulumi.StringMap{
						"Type":        pulumi.String("Service"),
						"Name":        pulumi.String("my-service"),
						"Environment": pulumi.String("production"),
					},
				},
				ComparisonOperator: applicationsignals.ServiceLevelObjectiveSliComparisonOperatorGreaterThanOrEqualTo,
				MetricThreshold:    pulumi.Float64(99),
			},
			Goal: &applicationsignals.ServiceLevelObjectiveGoalArgs{
				AttainmentGoal:   pulumi.Float64Ptr(99),
				WarningThreshold: pulumi.Float64Ptr(99.5),
				Interval: applicationsignals.ServiceLevelObjectiveIntervalArgs{
					RollingInterval: &applicationsignals.ServiceLevelObjectiveRollingIntervalArgs{
						DurationUnit: applicationsignals.ServiceLevelObjectiveDurationUnitDay,
						Duration:     pulumi.Int(30),
					},
				},
			},
		})
		if err != nil {
			return err
		}

		ctx.Export("vpcId", vpc.VpcId)
		ctx.Export("bucketName", bucket.Bucket)
		ctx.Export("sloArn", slo.Arn)

		return nil
	})
}
