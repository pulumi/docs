package myproject;

import com.pulumi.Context;
import com.pulumi.Pulumi;
import com.pulumi.kubernetes.helm.v3.Release;
import com.pulumi.kubernetes.helm.v3.ReleaseArgs;

public class App {
    public static void main(String[] args) {
        Pulumi.run(App::stack);
    }

    public static void stack(Context ctx) {
        var helm = new Release("helm", ReleaseArgs.builder()
            .chart("https://charts.bitnami.com/bitnami/wordpress-15.2.17.tgz")
            .build());

    }
}
