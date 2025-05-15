package myproject;

import com.pulumi.Pulumi;
import com.pulumi.kubernetes.apps.v1.Deployment;
import com.pulumi.kubernetes.apps.v1.DeploymentArgs;
import com.pulumi.kubernetes.apps.v1.inputs.DeploymentSpecArgs;
import com.pulumi.kubernetes.core.v1.inputs.ContainerArgs;
import com.pulumi.kubernetes.core.v1.inputs.PodSpecArgs;
import com.pulumi.kubernetes.core.v1.inputs.PodTemplateSpecArgs;
import com.pulumi.kubernetes.meta.v1.inputs.LabelSelectorArgs;
import com.pulumi.kubernetes.meta.v1.inputs.ObjectMetaArgs;

import java.util.Map;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {
            var nginxDeployment = new Deployment("nginxDeployment", DeploymentArgs.builder()
                    .metadata(ObjectMetaArgs.builder()
                            .name("nginx-deployment")
                            .build())
                    .spec(DeploymentSpecArgs.builder()
                            .replicas(1)
                            .selector(LabelSelectorArgs.builder()
                                    .matchLabels(Map.of("app", "nginx"))
                                    .build())
                            .template(PodTemplateSpecArgs.builder()
                                    .metadata(ObjectMetaArgs.builder()
                                            .labels(Map.of("app", "nginx"))
                                            .build())
                                    .spec(PodSpecArgs.builder()
                                            .containers(ContainerArgs.builder()
                                                    .name("nginx")
                                                    .image("nginx:latest")
                                                    .build())
                                            .build())
                                    .build())
                            .build())
                    .build());
        });
    }
}
