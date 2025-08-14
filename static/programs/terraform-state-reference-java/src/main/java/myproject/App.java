package myproject;

import com.pulumi.Pulumi;
import com.pulumi.terraform.state.inputs.GetLocalReferenceArgs;
import com.pulumi.terraform.state.StateFunctions;
import com.pulumi.eks.Cluster;
import com.pulumi.eks.ClusterArgs;

import java.util.List;
import java.util.stream.Collectors;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {
            var tfState = StateFunctions.getLocalReference(GetLocalReferenceArgs.builder()
                    .path("../terraform/terraform.tfstate")
                    .build());

            var vpcId = tfState.applyValue(state -> (String) state.outputs().get("vpc_id"));

            var publicSubnetIds = tfState.applyValue(state -> {
                @SuppressWarnings("unchecked")
                List<Object> ids = (List<Object>) state.outputs().get("public_subnet_ids");
                return ids.stream()
                        .map(id -> (String) id)
                        .collect(Collectors.toList());
            });

            var privateSubnetIds = tfState.applyValue(state -> {
                @SuppressWarnings("unchecked")
                List<Object> ids = (List<Object>) state.outputs().get("private_subnet_ids");
                return ids.stream()
                        .map(id -> (String) id)
                        .collect(Collectors.toList());
            });

            var cluster = new Cluster("my-cluster", ClusterArgs.builder()
                    .vpcId(vpcId)
                    .publicSubnetIds(publicSubnetIds)
                    .privateSubnetIds(privateSubnetIds)
                    .build());
        });
    }
}
