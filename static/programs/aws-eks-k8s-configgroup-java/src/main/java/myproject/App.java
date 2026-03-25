import com.pulumi.Context;
import com.pulumi.Pulumi;
import com.pulumi.core.Output;
import com.pulumi.eks.Cluster;
import com.pulumi.kubernetes.Provider;
import com.pulumi.kubernetes.ProviderArgs;
import com.pulumi.kubernetes.yaml.v2.ConfigGroup;
import com.pulumi.kubernetes.yaml.v2.ConfigGroupArgs;
import com.pulumi.resources.CustomResourceOptions;
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
        var cluster = new Cluster("cluster");

        var eksProvider = new Provider("eksProvider", ProviderArgs.builder()
            .kubeconfig(cluster.kubeconfigJson())
            .build());

        var guestbook = new ConfigGroup("guestbook", ConfigGroupArgs.builder()
            .files("yaml/*.yaml")
            .build(), CustomResourceOptions.builder()
                .provider(eksProvider)
                .build());

        ctx.export("kubeconfig", cluster.kubeconfig());
    }
}
