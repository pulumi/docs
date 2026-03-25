import com.pulumi.Context;
import com.pulumi.Pulumi;
import com.pulumi.core.Output;
import com.pulumi.awsx.ec2.Vpc;
import com.pulumi.eks.Cluster;
import com.pulumi.eks.ClusterArgs;
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
        // Create a VPC for our cluster.
        var vpc = new Vpc("vpc");

        // Create an EKS cluster inside of the VPC.
        var cluster = new Cluster("cluster", ClusterArgs.builder()
            .vpcId(vpc.vpcId())
            .publicSubnetIds(vpc.publicSubnetIds())
            .privateSubnetIds(vpc.privateSubnetIds())
            .nodeAssociatePublicIpAddress(false)
            .build());

        // Export the cluster's kubeconfig.
        ctx.export("kubeconfig", cluster.kubeconfig());
    }
}
