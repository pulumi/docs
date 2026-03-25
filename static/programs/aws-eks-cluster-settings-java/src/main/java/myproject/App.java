import com.pulumi.Context;
import com.pulumi.Pulumi;
import com.pulumi.core.Output;
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
        // Create an EKS cluster with a modified configuration.
        var cluster = new Cluster("cluster", ClusterArgs.builder()
            .desiredCapacity(5)
            .minSize(3)
            .maxSize(5)
            .enabledClusterLogTypes(
                "api",
                "audit",
                "authenticator")
            .build());

        // Export the cluster's kubeconfig.
        ctx.export("kubeconfig", cluster.kubeconfig());
    }
}
