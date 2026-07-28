```
Previewing destroy (dev):

     Type                                        Name            Plan
 -   pulumi:pulumi:Stack                         quickstart-dev  delete
 -   └─ quickstart:index:KubernetesNginxService  my-nginx        delete
 -      ├─ kubernetes:core/v1:Service            nginx           delete
 -      └─ kubernetes:apps/v1:Deployment         nginx           delete

Outputs:
  - ip: "172.183.217.156"

Resources:
    - 4 to delete

Do you want to perform this destroy?  [Use arrows to move, type to filter]
> yes
  no
  details
```
