import pulumi
import pulumi_aws as aws
import pulumi_aws_native as awsnative
import pulumi_awsx as awsx

# AWSx provides a VPC with well-architected defaults: subnets, route
# tables, NAT gateways, and an internet gateway, all pre-configured.
vpc = awsx.ec2.Vpc("main", nat_gateways=awsx.ec2.VpcNatGatewayArgs(
    strategy=awsx.ec2.NatGatewayStrategy.SINGLE,
))

# The AWS provider manages the majority of resources.
bucket = aws.s3.BucketV2("app-data")

# The AWS Cloud Control provider is used for a resource available
# through Cloud Control but not yet in the classic AWS provider.
slo = awsnative.applicationsignals.ServiceLevelObjective("api-slo",
    name="api-availability-slo",
    sli=awsnative.applicationsignals.ServiceLevelObjectiveSliArgs(
        sli_metric=awsnative.applicationsignals.ServiceLevelObjectiveSliMetricArgs(
            metric_type=awsnative.applicationsignals.ServiceLevelObjectiveSliMetricMetricType.AVAILABILITY,
            operation_name="GET /api",
            key_attributes={
                "Type": "Service",
                "Name": "my-service",
                "Environment": "production",
            },
        ),
        comparison_operator=awsnative.applicationsignals.ServiceLevelObjectiveSliComparisonOperator.GREATER_THAN_OR_EQUAL_TO,
        metric_threshold=99,
    ),
    goal=awsnative.applicationsignals.ServiceLevelObjectiveGoalArgs(
        attainment_goal=99,
        warning_threshold=99.5,
        interval=awsnative.applicationsignals.ServiceLevelObjectiveIntervalArgs(
            rolling_interval=awsnative.applicationsignals.ServiceLevelObjectiveRollingIntervalArgs(
                duration_unit=awsnative.applicationsignals.ServiceLevelObjectiveDurationUnit.DAY,
                duration=30,
            ),
        ),
    ),
)

pulumi.export("vpcId", vpc.vpc_id)
pulumi.export("bucketName", bucket.bucket)
pulumi.export("sloArn", slo.arn)