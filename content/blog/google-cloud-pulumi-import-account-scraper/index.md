---
title: "Google Cloud: Bulk Importing Resources into Pulumi"
date: 2023-03-16
meta_desc: "Learn how to bulk import your Google Cloud resources into Pulumi"
meta_image: "meta.png"
authors:
  - josh-kodroff
tags:
  - google-cloud
  - import
search:
  keywords:
    - importing
    - bulk
    - google
    - resources
    - cloud
    - import
    - learn
---

Point and click in the console is great when you're first starting out learning a new cloud or managed service, but it quickly becomes a hindrance when cloud infrastructure is widely adopted by an organization. The point at which the term "widely adopted" becomes applicable to your situation differs, but at some point in their careers, many infrastructure and platform engineers are faced with situations where a large number of critical infrastructure resources were created through "click ops" with no ability to track changes, reproduce environments consistently, and so on. When this happens (and it will probably happen to many of you), it's time to import those resources into infrastructure as code.

Fortunately, Pulumi has one of the smoothest and most powerful import processes of any IaC tool. In this post, we're going to show you how to automate the bulk importation of Google Cloud resources into Pulumi! This approach will also work on resources that were created by another IaC tool.

<!--more-->

In a previous post titled [Automating Pulumi Import with Manually Created Resources](../automating-pulumi-import-to-bring-manually-created-resources-into-iac), we covered the details of how `pulumi import` works and demonstrated a workflow of bulk importing resources from AWS. We won't repeat the details of how `pulumi import` works here, so please refer to "Automating Pulumi Import with Manually Created Resources" for those details.

## Writing an account scraper

In our AWS account scraper, we took the approach of querying each resource type using [boto3](https://pypi.org/project/boto3/), the AWS Python SDK. In contrast, Google Cloud has a tool called [Config Connector](https://cloud.google.com/config-connector/docs/overview) that allows us to query all resources in a Google Cloud project with a single command, and without needing to write the code to query each resource type via the Google Cloud SDK.

Our process for importing from Google Cloud has the following steps:

1. Query resources using Config Connector and output them to a YAML file.
1. In a Python script, take the Config Connector YAML output and transform it into JSON suitable for a bulk `pulumi import` operation.
1. Run the `pulumi import` command and place the generated code in our Pulumi program.

### Config Connector

Config Connector is designed to manage Google Cloud resources represented as Kubernetes Custom Resource Definitions (CRDs). We will not be using this capability of Config Connector, but if you are interested in managing Pulumi stacks as CRDs in a GitOps workflow, check out the [Pulumi Kubernetes Operator](https://www.pulumi.com/docs/iac/packages-and-automation/continuous-delivery/pulumi-kubernetes-operator/). Instead, we'll use Config Connector's [bulk export](https://cloud.google.com/config-connector/docs/how-to/import-export/bulk-export#exporting_an_inventory_with_config-connector) capability to query our Google Cloud environment for resources and output them as Kubernetes manifests, then transform those Kubernetes manifests into JSON suitable for a bulk `pulumi import` operation via a script written in Python.

First, we need to install the `config-connector` CLI per the instructions [in the Config Connector docs](https://cloud.google.com/config-connector/docs/how-to/import-export/overview#installing-config-connector). Then, to generate our Kubernetes manifests, we run the following command:

```bash
config-connector bulk-export --project <YOUR PROJECT ID> --output bulk-export.yaml --iam-format policymember --on-error continue
```

This command will generate a YAML file with a series of Kubernetes manifests like the following:

```yaml
---
apiVersion: artifactregistry.cnrm.cloud.google.com/v1beta1
kind: ArtifactRegistryRepository
metadata:
  annotations:
    cnrm.cloud.google.com/project-id: my-google-cloud-project
  labels:
    goog-managed-by: cloudfunctions
  name: gcf-artifacts
spec:
  description: This repository is created and used by Cloud Functions for storing
    function docker images.
  format: DOCKER
  location: europe-west1
  resourceID: gcf-artifacts
---
apiVersion: compute.cnrm.cloud.google.com/v1beta1
kind: ComputeDisk
metadata:
  labels:
    goog-gke-volume: ""
  name: gke-helloworld-2a71d4f-pvc-1e6aa931-d742-437e-a52b-413999ace2be
spec:
  description: '{"kubernetes.io/created-for/pv/name":"pvc-1e6aa931-d742-437e-a52b-413999ace2be","kubernetes.io/created-for/pvc/name":"wpdev-wordpress","kubernetes.io/created-for/pvc/namespace":"default"}'
  location: us-central1-a
  physicalBlockSizeBytes: 4096
  projectRef:
    external: my-google-cloud-project
  resourceID: gke-helloworld-2a71d4f-pvc-1e6aa931-d742-437e-a52b-413999ace2be
  size: 10
  type: pd-standard
---
# etc...
```

Now that we have a single file containing all of our Google Cloud resources, we can take this file as input for Python script.

### Mapping from Kubernetes manifests to `pulumi import` JSON

We need to write some code in order to convert the Kubernetes manifests generated by Config Connector into a JSON format suitable for `pulumi import`. For detailed information on bulk import in Pulumi and all supported fields, see [Bulk Import Operations](https://www.pulumi.com/docs/iac/adopting-pulumi/import/#bulk-import-operations) in the Pulumi docs.

In order for a resource to be imported, three fields are required:

1. `type`, which indicates the Pulumi resource type, e.g. `gcp:compute/network:Network`.
1. `name`, which, when combined with `type`, uniquely identifies the resource within the Pulumi program. In the following example, the Pulumi name is `my-network`:

    ```typescript
    const network = new gcp.compute.Network("my-network");
    ```

1. `id`, which informs the `pulumi import` command how to query the Google Cloud API for the existing resource for its attributes and output the generated code with all attributes filled in. IDs for import vary by the type of resource, although in Google Cloud, they often follow a predictable pattern which we'll discuss in further detail soon. The format of a resource's ID can be found in the [Pulumi Registry](https://www.pulumi.com/registry/) in the Import section of the resource's API page ([example](https://www.pulumi.com/registry/packages/gcp/api-docs/compute/network/#import)).

In order to get the `type`, we need to translate the Kubernetes `kind` to a Pulumi type. We can accomplish this by keeping a straightforward mapping in a Python `dict`:

```python
resource_type_mappings = {
    'ArtifactRegistryRepository': {
        'pulumi_type': 'gcp:artifactregistry/repository:Repository'
    },
    'ComputeDisk': {
        'pulumi_type': 'gcp:compute/disk:Disk',
    },
    'ComputeFirewall': {
        'pulumi_type': 'gcp:compute/firewall:Firewall'
    },
    # etc.
```

Obtaining the `name` is simple - virtually all of the Kubernetes manifests in our sample data contained a unique or near-unique identifier under `k8s_resource['metadata']['name']`. Occasionally, we saw naming collisions that cause errors, for example where a compute instance (VM) and its main disk resource shared the same name. At the time of writing, the `pulumi import` command requires that names be unique within the context of a bulk import. However, this is not a requirement when authoring Pulumi programs - the combination of (name, type) must be unique. In these cases, we simply ensured a unique name by appending `-1` to the resource name. This isn't the most elegant solution, but it works well enough when collisions are relatively infrequent:

```python
def ensure_unique_name(pulumi_resource):
    """Ensures that each resource has a unique name. `pulumi import` will fail
    if multiple resources have the same name due to
    https://github.com/pulumi/pulumi/issues/6032"""

    for resource in resources:
        if 'name' in resource and 'name' in pulumi_resource and resource['name'] == pulumi_resource['name']:
            pulumi_resource['name'] += "-1"
            return
```

Finally, we need to map the `id` value. In many cases, the Google Cloud resource ID is in the form `{{region}}/{{location}}/{{resource ID}}`, and can be mapped from fields that are consistent in the Kubernetes manifest:

```python
def get_default_id(k8s_resource):
    """Returns the most common form of an ID of a Google Cloud resource, adding
    region and zone if they can be determined"""
    id = ""

    if 'region' in k8s_resource['spec']:
        id += f"{k8s_resource['spec']['region']}/"

    if 'location' in k8s_resource['spec']:
        id += f"{k8s_resource['spec']['location']}/"

    id += k8s_resource['spec']['resourceID']

    return id
```

For any resource types that do not fit this pattern, we'll need to do some additional work.

### Mapping resources with custom ID requirements

If the Kubernetes manifest for our resource does not follow the standard pattern, we'll need to write a custom function to get the ID. One example of resources that do not follow the standard pattern are compute instances and compute instance groups, which store the project ID in a different key:

```yaml
apiVersion: compute.cnrm.cloud.google.com/v1beta1
kind: ComputeInstance
metadata:
  annotations:
    cnrm.cloud.google.com/project-id: my-project-id
# ...
```

Therefore, we need to write a custom function to handle grabbing the IDs from these types:

```python
def get_compute_instance_id(k8s_resource):
    return f"{k8s_resource['metadata']['annotations']['cnrm.cloud.google.com/project-id']}/{k8s_resource['spec']['zone']}/{k8s_resource['metadata']['name']}"
```

And then map our custom function to the appropriate typed in our type mappings dict:

```python
resource_type_mappings = {
    # ...
    'ComputeInstance': {
        'pulumi_type': 'gcp:compute/instance:Instance',
        'get_id': get_compute_instance_id,
    },
    'ComputeInstanceGroup': {
        'pulumi_type': 'gcp:compute/instanceGroup:InstanceGroup',
        'get_id': get_compute_instance_id,
    },
    # ...
}
```

[The full code](https://github.com/pulumi/pulumi-import-google-cloud-account-scraper) also contains some additional mapping and processing for Google Cloud IAM resources, but it follows the same basic patterns as the mapping for other types.

## Importing to Pulumi

Now that we have our conversion script written, we can run it with the following command:

```bash
python3 main.py -i sample-output.yaml -o pulumi-import.json -p <your-project-id>
```

The command will generate output like the following:

```json
{
  "resources": [
    {
      "type": "gcp:artifactregistry/repository:Repository",
      "name": "gcf-artifacts",
      "id": "europe-west1/gcf-artifacts"
    },
    {
      "type": "gcp:compute/disk:Disk",
      "name": "gke-helloworld-2a71d4f-pvc-1e6aa931-d742-437e-a52b-413999ace2be",
      "id": "us-central1-a/gke-helloworld-2a71d4f-pvc-1e6aa931-d742-437e-a52b-413999ace2be"
    },
// ...
```

Once we're in our Pulumi program's root, we can instruct `pulumi import` to do a bulk import and output the generated code to a file in the language of our program (this example includes TypeScript output, but `pulumi import` will automatically generate code in the correct language for your project).

```bash
pulumi import -f ../config-connector-transform/pulumi-import.json -y -s dev -o index.ts
```

And we can see that in our Pulumi program, all the attributes of our imported resources are present, which means no further actions are (typically - see note below for known exceptions) necessary! We are ready to manage our critical infrastructure as code from now on!

```typescript
const gcf_artifacts = new gcp.artifactregistry.Repository("gcf-artifacts", {
    description: "This repository is created and used by Cloud Functions for storing function docker images.",
    format: "DOCKER",
    labels: {
        "goog-managed-by": "cloudfunctions",
    },
    location: "europe-west1",
    project: "your-project-id",
    repositoryId: "gcf-artifacts",
});

const gke_helloworld_2a71d4f_pvc_1e6aa931_d742_437e_a52b_413999ace2be = new gcp.compute.Disk("gke-helloworld-2a71d4f-pvc-1e6aa931-d742-437e-a52b-413999ace2be", {
    description: "{\"kubernetes.io/created-for/pv/name\":\"pvc-1e6aa931-d742-437e-a52b-413999ace2be\",\"kubernetes.io/created-for/pvc/name\":\"wpdev-wordpress\",\"kubernetes.io/created-for/pvc/namespace\":\"default\"}",
    labels: {
        "goog-gke-volume": "",
    },
    name: "gke-helloworld-2a71d4f-pvc-1e6aa931-d742-437e-a52b-413999ace2be",
    physicalBlockSizeBytes: 4096,
    project: "your-project-id",
    size: 10,
    zone: "us-central1-a",
});
```

{{% notes %}}
You may need to massage some of the generated output for any `*IAMPolicy` resources because deleted principals cannot be contained in IAM policies due to a limitation of the Google Classic provider, but they are still contained in the generated code returned by `pulumi import`, which in turn comes from the Google API.
{{% /notes %}}

## Next Steps

Now that we have our Google Cloud resources under Pulumi management, we might want to consider some additional steps to build upon our IaC solution:

* **Set up a CI/CD pipeline:** By adding our Pulumi code to a delivery pipeline, we can help ensure that all infrastructure changes go through an automated process. Pulumi has helpful integrations and documentation for many popular tools. See [Continuous Delivery](/docs/iac/packages-and-automation/continuous-delivery/) in the Pulumi docs for more information.

* **Add policy as code:** By adding policy as code to our IaC pipeline, we can ensure that our infrastructure is in compliance with any security or regulatory requirements before it’s ever provisioned in the cloud, as well as checks on any existing Pulumi resources. For more information on Pulumi’s policy as code capabilities, see [CrossGuard (Policy as Code)](/docs/using-pulumi/crossguard/) in the Pulumi docs.

## Conclusion

We’ve shown how the Google Cloud account scraper combined with `pulumi import` enables organizations to quickly get all of their Google Cloud resources under management with Pulumi. Managing cloud resources with Pulumi allows organizations to utilize modern, automated, code-centric approach, and `pulumi import` makes adopting Pulumi as painless as possible, even when critical resources have been created via point and click in the console!

If you use the Google Cloud account scraper and find something you need is not supported, please [submit an issue](https://github.com/pulumi/pulumi-import-google-cloud-account-scraper/issues), or better yet, submit a pull request!
