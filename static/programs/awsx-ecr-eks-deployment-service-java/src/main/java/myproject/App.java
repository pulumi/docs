package myproject;

import com.pulumi.Context;
import com.pulumi.Pulumi;
import com.pulumi.core.Output;
import com.pulumi.awsx.ecr.Repository;
import com.pulumi.awsx.ecr.RepositoryArgs;
import com.pulumi.awsx.ecr.Image;
import com.pulumi.awsx.ecr.ImageArgs;
import com.pulumi.eks.Cluster;
import com.pulumi.kubernetes.Provider;
import com.pulumi.kubernetes.ProviderArgs;
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
import com.pulumi.resources.CustomResourceOptions;
import java.util.Map;

public class App {
    public static void main(String[] args) {
        Pulumi.run(App::stack);
    }

    public static void stack(Context ctx) {
        final var appName = "my-app";

        var repository = new Repository("repository", RepositoryArgs.builder()
            .forceDelete(true)
            .build());

        var image = new Image("image", ImageArgs.builder()
            .repositoryUrl(repository.url())
            .context("./app")
            .platform("linux/amd64")
            .build());

        var cluster = new Cluster("cluster");

        var clusterProvider = new Provider("clusterProvider", ProviderArgs.builder()
            .kubeconfig(cluster.kubeconfigJson())
            .enableServerSideApply(true)
            .build());

        var deployment = new Deployment("deployment", DeploymentArgs.builder()
            .metadata(ObjectMetaArgs.builder()
                .labels(Map.of("appClass", appName))
                .build())
            .spec(DeploymentSpecArgs.builder()
                .replicas(2)
                .selector(LabelSelectorArgs.builder()
                    .matchLabels(Map.of("appClass", appName))
                    .build())
                .template(PodTemplateSpecArgs.builder()
                    .metadata(ObjectMetaArgs.builder()
                        .labels(Map.of("appClass", appName))
                        .build())
                    .spec(PodSpecArgs.builder()
                        .containers(ContainerArgs.builder()
                            .name(appName)
                            .image(image.imageUri())
                            .ports(ContainerPortArgs.builder()
                                .name("http")
                                .containerPort(80)
                                .build())
                            .build())
                        .build())
                    .build())
                .build())
            .build(), CustomResourceOptions.builder()
                .provider(clusterProvider)
                .build());

        var service = new Service("service", ServiceArgs.builder()
            .metadata(ObjectMetaArgs.builder()
                .labels(Map.of("appClass", appName))
                .build())
            .spec(ServiceSpecArgs.builder()
                .type("LoadBalancer")
                .selector(Map.of("appClass", appName))
                .ports(ServicePortArgs.builder()
                    .port(80)
                    .targetPort("http")
                    .build())
                .build())
            .build(), CustomResourceOptions.builder()
                .provider(clusterProvider)
                .build());

        ctx.export("url", Output.format("http://%s", service.status().applyValue(status -> {
            return status.get().loadBalancer().get().ingress().get(0).hostname().get();
        })));
    }
}
