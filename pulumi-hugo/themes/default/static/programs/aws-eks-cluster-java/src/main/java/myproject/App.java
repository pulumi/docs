package myproject;

import com.pulumi.Pulumi;
import com.pulumi.awsx.ec2.Vpc;
import com.pulumi.awsx.ec2.VpcArgs;
import com.pulumi.eks.Cluster;
import com.pulumi.eks.ClusterArgs;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {
            // Create a VPC for the Kubernetes cluster
            var vpc = new Vpc("eks-vpc", VpcArgs.builder()
                .enableDnsHostnames(true)
                .cidrBlock("10.0.0.0/16")
                .build());

            // Create the EKS Cluster
            var cluster = new Cluster("eks-cluster", ClusterArgs.builder()
                .vpcId(vpc.vpcId())
                .instanceType("t3.medium")
                .desiredCapacity(3)
                .minSize(3)
                .maxSize(6)
                .build());

            // Export the cluster's kubeconfig
            ctx.export("kubeconfig", cluster.kubeconfig());
        });
    }
}
