```
Do you want to perform this destroy? yes
Destroying (dev)

     Type                                        Name            Status
 -   pulumi:pulumi:Stack                         quickstart-dev  deleted (0.08s)
 -   └─ quickstart:index:KubernetesNginxService  my-nginx        deleted (0.08s)
 -      ├─ kubernetes:core/v1:Service            nginx           deleted (16s)
 -      └─ kubernetes:apps/v1:Deployment         nginx           deleted (0.59s)

Outputs:
  - ip: "172.183.217.156"

Resources:
    - 4 deleted

Duration: 18s
```
