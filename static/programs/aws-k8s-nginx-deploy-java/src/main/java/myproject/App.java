package myproject;

import com.pulumi.Context;
import com.pulumi.Pulumi;
import com.pulumi.core.Output;
import com.pulumi.kubernetes.apps.v1.Deployment;
import com.pulumi.kubernetes.apps.v1.DeploymentArgs;
import com.pulumi.kubernetes.meta.v1.inputs.ObjectMetaArgs;
import com.pulumi.kubernetes.apps.v1.inputs.DeploymentSpecArgs;
import com.pulumi.kubernetes.meta.v1.inputs.LabelSelectorArgs;
import com.pulumi.kubernetes.core.v1.inputs.PodTemplateSpecArgs;
import com.pulumi.kubernetes.core.v1.inputs.ServicePortArgs;
import com.pulumi.kubernetes.core.v1.inputs.ContainerArgs;
import com.pulumi.kubernetes.core.v1.inputs.ContainerPortArgs;
import com.pulumi.kubernetes.core.v1.inputs.PodSpecArgs;
import com.pulumi.kubernetes.core.v1.Service;
import com.pulumi.kubernetes.core.v1.ServiceArgs;
import com.pulumi.kubernetes.core.v1.inputs.ServiceSpecArgs;
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
        // Create an NGINX Deployment and load balanced Service.
        var myDeployment = new Deployment("myDeployment", DeploymentArgs.builder()
            .metadata(ObjectMetaArgs.builder()
                .labels(Map.of("appClass", "my-deployment"))
                .build())
            .spec(DeploymentSpecArgs.builder()
                .replicas(2)
                .selector(LabelSelectorArgs.builder()
                    .matchLabels(Map.of("appClass", "my-deployment"))
                    .build())
                .template(PodTemplateSpecArgs.builder()
                    .metadata(ObjectMetaArgs.builder()
                        .labels(Map.of("appClass", "my-deployment"))
                        .build())
                    .spec(PodSpecArgs.builder()
                        .containers(ContainerArgs.builder()
                            .name("my-deployment")
                            .image("nginx")
                            .ports(ContainerPortArgs.builder()
                                .name("http")
                                .containerPort(80)
                                .build())
                            .build())
                        .build())
                    .build())
                .build())
            .build());

        var myService = new Service("myService", ServiceArgs.builder()
            .metadata(ObjectMetaArgs.builder()
                .labels(Map.of("appClass", "my-deployment"))
                .build())
            .spec(ServiceSpecArgs.builder()
                .type("LoadBalancer")
                .ports(ServicePortArgs.builder()
                    .port(80)
                    .targetPort("http")
                    .build())
                .selector(Map.of("appClass", "my-deployment"))
                .build())
            .build());

        // Export the URL for the load balanced service.
        ctx.export("url", myService.status().applyValue(status -> {
            return status
                .flatMap(s -> s.loadBalancer())
                .map(lb -> lb.ingress())
                .filter(ingress -> !ingress.isEmpty())
                .flatMap(ingress -> ingress.get(0).hostname())
                .orElse("");
        }));
    }
}
