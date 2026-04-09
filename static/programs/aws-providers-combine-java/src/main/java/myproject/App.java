package myproject;

import com.pulumi.Pulumi;
import com.pulumi.awsx.ec2.Vpc;
import com.pulumi.awsx.ec2.VpcArgs;
import com.pulumi.awsx.ec2.inputs.NatGatewayConfigurationArgs;
import com.pulumi.awsx.ec2.enums.NatGatewayStrategy;
import com.pulumi.aws.s3.BucketV2;
import com.pulumi.awsnative.applicationsignals.ServiceLevelObjective;
import com.pulumi.awsnative.applicationsignals.ServiceLevelObjectiveArgs;
import com.pulumi.awsnative.applicationsignals.inputs.ServiceLevelObjectiveSliArgs;
import com.pulumi.awsnative.applicationsignals.inputs.ServiceLevelObjectiveSliMetricArgs;
import com.pulumi.awsnative.applicationsignals.inputs.ServiceLevelObjectiveGoalArgs;
import com.pulumi.awsnative.applicationsignals.inputs.ServiceLevelObjectiveIntervalArgs;
import com.pulumi.awsnative.applicationsignals.inputs.ServiceLevelObjectiveRollingIntervalArgs;
import com.pulumi.awsnative.applicationsignals.enums.ServiceLevelObjectiveSliMetricMetricType;
import com.pulumi.awsnative.applicationsignals.enums.ServiceLevelObjectiveSliComparisonOperator;
import com.pulumi.awsnative.applicationsignals.enums.ServiceLevelObjectiveDurationUnit;
import java.util.Map;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {

            // AWSx provides a VPC with well-architected defaults: subnets, route
            // tables, NAT gateways, and an internet gateway, all pre-configured.
            var vpc = new Vpc("main", VpcArgs.builder()
                .natGateways(NatGatewayConfigurationArgs.builder()
                    .strategy(NatGatewayStrategy.Single)
                    .build())
                .build());

            // The AWS provider manages the majority of resources.
            var bucket = new BucketV2("app-data");

            // The AWS Cloud Control provider is used for a resource available
            // through Cloud Control but not yet in the classic AWS provider.
            var slo = new ServiceLevelObjective("api-slo", ServiceLevelObjectiveArgs.builder()
                .name("api-availability-slo")
                .sli(ServiceLevelObjectiveSliArgs.builder()
                    .sliMetric(ServiceLevelObjectiveSliMetricArgs.builder()
                        .metricType(ServiceLevelObjectiveSliMetricMetricType.Availability)
                        .operationName("GET /api")
                        .keyAttributes(Map.of(
                            "Type", "Service",
                            "Name", "my-service",
                            "Environment", "production"))
                        .build())
                    .comparisonOperator(ServiceLevelObjectiveSliComparisonOperator.GreaterThanOrEqualTo)
                    .metricThreshold(99.0)
                    .build())
                .goal(ServiceLevelObjectiveGoalArgs.builder()
                    .attainmentGoal(99.0)
                    .warningThreshold(99.5)
                    .interval(ServiceLevelObjectiveIntervalArgs.builder()
                        .rollingInterval(ServiceLevelObjectiveRollingIntervalArgs.builder()
                            .durationUnit(ServiceLevelObjectiveDurationUnit.Day)
                            .duration(30)
                            .build())
                        .build())
                    .build())
                .build());

            ctx.export("vpcId", vpc.vpcId());
            ctx.export("bucketName", bucket.bucket());
            ctx.export("sloArn", slo.arn());
        });
    }
}