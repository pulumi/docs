package myproject;

import com.pulumi.Context;
import com.pulumi.Pulumi;
import com.pulumi.core.Output;
import com.pulumi.aws.iam.Role;
import com.pulumi.aws.iam.RoleArgs;
import com.pulumi.aws.iam.InstanceProfile;
import com.pulumi.aws.iam.InstanceProfileArgs;
import com.pulumi.eks.Cluster;
import com.pulumi.eks.ClusterArgs;
import com.pulumi.eks.NodeGroupV2;
import com.pulumi.eks.NodeGroupV2Args;
import static com.pulumi.codegen.internal.Serialization.*;
import java.util.List;
import java.util.ArrayList;
import java.util.Map;
import java.io.File;
import java.nio.file.Files;
import java.nio.file.Paths;

public class App {
    public static void main(String[] args) {
        Pulumi.run(App::stack);
    }

    public static void stack(Context ctx) {
        final var managedPolicyArns = List.of(
            "arn:aws:iam::aws:policy/AmazonEKSWorkerNodePolicy",
            "arn:aws:iam::aws:policy/AmazonEKS_CNI_Policy",
            "arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly"
        );

        final var assumeRolePolicy = serializeJson(
            jsonObject(
                jsonProperty("Version", "2012-10-17"),
                jsonProperty("Statement", jsonArray(jsonObject(
                    jsonProperty("Action", "sts:AssumeRole"),
                    jsonProperty("Effect", "Allow"),
                    jsonProperty("Sid", null),
                    jsonProperty("Principal", jsonObject(
                        jsonProperty("Service", "ec2.amazonaws.com")
                    ))
                )))
            ));

        var role1 = new Role("role1", RoleArgs.builder()
            .assumeRolePolicy(assumeRolePolicy)
            .managedPolicyArns(managedPolicyArns)
            .build());

        var role2 = new Role("role2", RoleArgs.builder()
            .assumeRolePolicy(assumeRolePolicy)
            .managedPolicyArns(managedPolicyArns)
            .build());

        var instanceProfile1 = new InstanceProfile("instanceProfile1", InstanceProfileArgs.builder()
            .role(role1.name())
            .build());

        var instanceProfile2 = new InstanceProfile("instanceProfile2", InstanceProfileArgs.builder()
            .role(role2.name())
            .build());

        var cluster = new Cluster("cluster", ClusterArgs.builder()
            .skipDefaultNodeGroup(true)
            .instanceRoles(List.of(role1, role2))
            .build());

        var fixedNodeGroup = new NodeGroupV2("fixedNodeGroup", NodeGroupV2Args.builder()
            .cluster(cluster)
            .instanceType("t2.medium")
            .desiredCapacity(2)
            .minSize(1)
            .maxSize(3)
            .spotPrice("1")
            .labels(Map.of("ondemand", "true"))
            .instanceProfile(instanceProfile1)
            .build());

        var spotNodeGroup = new NodeGroupV2("spotNodeGroup", NodeGroupV2Args.builder()
            .cluster(cluster)
            .instanceType("t2.medium")
            .desiredCapacity(1)
            .minSize(1)
            .maxSize(2)
            .labels(Map.of("preemptible", "true"))
            .instanceProfile(instanceProfile2)
            .build());

        ctx.export("kubeconfig", cluster.kubeconfig());
    }
}
