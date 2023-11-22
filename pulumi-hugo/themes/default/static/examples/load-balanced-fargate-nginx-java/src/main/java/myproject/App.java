package myproject;

import com.pulumi.Context;
import com.pulumi.Pulumi;
import com.pulumi.core.Output;
import com.pulumi.awsx.ecr.Repository;
import com.pulumi.awsx.ecr.RepositoryArgs;
import com.pulumi.aws.ecs.Cluster;
import com.pulumi.awsx.lb.ApplicationLoadBalancer;
import com.pulumi.awsx.ecs.FargateService;
import com.pulumi.awsx.ecs.FargateServiceArgs;
import com.pulumi.awsx.ecs.inputs.FargateServiceTaskDefinitionArgs;
import com.pulumi.awsx.ecs.inputs.TaskDefinitionContainerDefinitionArgs;
import com.pulumi.awsx.ecs.inputs.TaskDefinitionPortMappingArgs;

public class App {
    public static void main(String[] args) {
        Pulumi.run(App::stack);
    }

    public static void stack(Context ctx) {
        var repository = new Repository("repository", RepositoryArgs.builder()
            .forceDelete(true)
            .build());

        var cluster = new Cluster("cluster");
        var lb = new ApplicationLoadBalancer("lb");

        var service = new FargateService("service", FargateServiceArgs.builder()
            .cluster(cluster.arn())
            .assignPublicIp(true)
            .taskDefinitionArgs(FargateServiceTaskDefinitionArgs.builder()
                .container(TaskDefinitionContainerDefinitionArgs.builder()
                    .name("my-service")
                    .image("nginx:latest")
                    .cpu(128)
                    .memory(512)
                    .essential(true)
                    .portMappings(TaskDefinitionPortMappingArgs.builder()
                        .containerPort(80)
                        .targetGroup(lb.defaultTargetGroup())
                        .build())
                    .build())
                .build())
            .build());

        ctx.export("url", Output.format("http://%s", lb.loadBalancer().applyValue(loadBalancer -> loadBalancer.dnsName())));
    }
}
