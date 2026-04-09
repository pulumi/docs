using Pulumi;
using System.Collections.Generic;
using Pulumi.Awsx.Ec2;
using Pulumi.Awsx.Ec2.Inputs;
using Aws = Pulumi.Aws;
using AwsNative = Pulumi.AwsNative;

return await Deployment.RunAsync(() =>
{
    // AWSx provides a VPC with well-architected defaults: subnets, route
    // tables, NAT gateways, and an internet gateway, all pre-configured.
    var vpc = new Vpc("main", new VpcArgs
    {
        NatGateways = new NatGatewayConfigurationArgs
        {
            Strategy = NatGatewayStrategy.Single,
        },
    });

    // The AWS provider manages the majority of resources.
    var bucket = new Aws.S3.BucketV2("app-data");

    // The AWS Cloud Control provider is used for a resource available
    // through Cloud Control but not yet in the classic AWS provider.
    var slo = new AwsNative.ApplicationSignals.ServiceLevelObjective("api-slo", new()
    {
        Name = "api-availability-slo",
        Sli = new AwsNative.ApplicationSignals.Inputs.ServiceLevelObjectiveSliArgs
        {
            SliMetric = new AwsNative.ApplicationSignals.Inputs.ServiceLevelObjectiveSliMetricArgs
            {
                MetricType = AwsNative.ApplicationSignals.ServiceLevelObjectiveSliMetricMetricType.Availability,
                OperationName = "GET /api",
                KeyAttributes =
                {
                    ["Type"] = "Service",
                    ["Name"] = "my-service",
                    ["Environment"] = "production",
                },
            },
            ComparisonOperator = AwsNative.ApplicationSignals.ServiceLevelObjectiveSliComparisonOperator.GreaterThanOrEqualTo,
            MetricThreshold = 99,
        },
        Goal = new AwsNative.ApplicationSignals.Inputs.ServiceLevelObjectiveGoalArgs
        {
            AttainmentGoal = 99,
            WarningThreshold = 99.5,
            Interval = new AwsNative.ApplicationSignals.Inputs.ServiceLevelObjectiveIntervalArgs
            {
                RollingInterval = new AwsNative.ApplicationSignals.Inputs.ServiceLevelObjectiveRollingIntervalArgs
                {
                    DurationUnit = AwsNative.ApplicationSignals.ServiceLevelObjectiveDurationUnit.Day,
                    Duration = 30,
                },
            },
        },
    });

    return new Dictionary<string, object?>
    {
        ["vpcId"] = vpc.VpcId,
        ["bucketName"] = bucket.Bucket,
        ["sloArn"] = slo.Arn,
    };
});