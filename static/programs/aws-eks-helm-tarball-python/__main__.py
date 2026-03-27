import pulumi_kubernetes as kubernetes

helm = kubernetes.helm.v3.Release("helm", chart="https://charts.bitnami.com/bitnami/wordpress-15.2.17.tgz")
