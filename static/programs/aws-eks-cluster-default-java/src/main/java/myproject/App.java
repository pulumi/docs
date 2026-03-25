import com.pulumi.Context;
import com.pulumi.Pulumi;
import com.pulumi.core.Output;
import com.pulumi.eks.Cluster;
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
        // Create an EKS cluster with the default configuration.
        var cluster = new Cluster("cluster");

        // Export the cluster's kubeconfig.
        ctx.export("kubeconfig", cluster.kubeconfig());
    }
}
