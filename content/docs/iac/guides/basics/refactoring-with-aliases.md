---
title_tag: "Refactoring with Aliases"
meta_desc: Learn how to refactor Pulumi infrastructure code using the aliases property to reorganize resources without recreating them.
title: Refactoring with Aliases
h1: Refactoring with Aliases
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        parent: iac-guides-basics
        identifier: iac-guides-basics-refactoring-aliases
        weight: 4
---

As your infrastructure evolves, you may need to reorganize your Pulumi code - renaming resources, establishing parent-child relationships, or extracting common patterns into reusable components. The `aliases` property enables you to refactor your infrastructure code while preserving existing cloud resources.

This guide demonstrates how to use `aliases` to refactor infrastructure code through a practical example that evolves from simple resources to a well-organized component structure.

## Understanding aliases

When you refactor Pulumi code by renaming resources or changing their parent-child relationships, Pulumi needs to know that resources in your new code correspond to resources in your existing state. Without this information, Pulumi would attempt to create new resources and delete the old ones.

The [`aliases`](/docs/concepts/resources#aliases) property tells Pulumi that a resource in your updated code is the same as a resource from a previous state, even if its name or location in the resource hierarchy has changed.

## Example: refactoring customer infrastructure

This example demonstrates a test-driven development cycle applied to infrastructure code. You'll start with simple resources and progressively refactor them into a clean, hierarchical structure without disrupting deployed infrastructure.

### Starting point

Begin with an empty Pulumi project:

```typescript
import * as pulumi from "@pulumi/pulumi";

const config = new pulumi.Config('gitlab')
```

Running `pulumi up` creates an empty stack with no resources.

### Adding a git repository

Add a GitLab repository for your first customer:

```typescript
const config = new pulumi.Config('gitlab')

const gitlabNamespace = config.getNumber('namespace')

const firstCustomer = new gitlab.Project("FirstCustomer",
    {
        name: "first-customer",
        description: "First Customer code",
        namespaceId: gitlabNamespace,
        visibilityLevel: "private",
        defaultBranch: "master",
        pipelinesEnabled: true,
        issuesEnabled: false,
        wikiEnabled: false,
        snippetsEnabled: false,
        containerRegistryEnabled: false,
        mergeRequestsEnabled: false,
        mergeMethod: "ff",
        onlyAllowMergeIfPipelineSucceeds: true,
        sharedRunnersEnabled: true
    }
)
```

After running `pulumi up`, the GitLab project is created and appears as a child of your stack in the Pulumi Console.

### Adding cloud infrastructure

For your second customer, add a GitLab repository plus Google Cloud infrastructure:

```typescript
const secondCustomer = new gitlab.Project("SecondCustomer",
    {
        name: "second-customer",
        description: "Second Customer code",
        // ... same properties as firstCustomer
    }
)

const secondCustomerProject = new gcp.organizations.Project("SecondCustomer",
    {
        projectId: 'second-customer',
        name: 'Second Customer Infrastructure'
    }
)

const serviceAccountSecondCustomer = new gcp.serviceAccount.Account("ServiceAccountSecondCustomer",
    {
        accountId: 'secondcustomer',
        displayName: 'Service Account for Second Customer project',
        project: secondCustomerProject.projectId
    }
);

const serviceAccountSecondCustomerKey = new gcp.serviceAccount.Key("ServiceAccountSecondCustomerKey",
    {
        serviceAccountId: serviceAccountSecondCustomer.email
    }
);

const secondCustomerGitlabCIVariable = new gitlab.ProjectVariable("SecondCustomerGCPAccess",
    {
        project: secondCustomer.id,
        variableType: 'file',
        key: "GOOGLE_APPLICATION_CREDENTIALS",
        value: serviceAccountSecondCustomerKey.privateKey.apply(value =>
            Buffer.from(value, 'base64').toString('utf-8')
        ),
        protected: true,
        environmentScope: "*"
    }
)
```

At this point, all resources are direct children of the stack. While functional, this flat structure makes it difficult to visualize which resources belong together.

### Establishing resource relationships

The resources you created have natural parent-child relationships:

- A service account key belongs to a service account
- A GitLab CI variable belongs to a GitLab project

To express these relationships in Pulumi's state, use the `parent` property from [`CustomResourceOptions`](/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions):

```typescript
const serviceAccountSecondCustomerKey = new gcp.serviceAccount.Key("ServiceAccountSecondCustomerKey",
    {
        serviceAccountId: serviceAccountSecondCustomer.email
    },
    {
        parent: serviceAccountSecondCustomer
    }
);
```

If you run `pulumi preview`, Pulumi wants to replace the key because it expects to find it as a child of the service account, but in your current state, it's a child of the stack.

This is where `aliases` comes in. Add an alias that points to the resource's current location:

```typescript
const serviceAccountSecondCustomerKey = new gcp.serviceAccount.Key("ServiceAccountSecondCustomerKey",
    {
        serviceAccountId: serviceAccountSecondCustomer.email
    },
    {
        parent: serviceAccountSecondCustomer,
        aliases: [
            { parent: pulumi.rootStackResource }
        ]
    }
);
```

The `aliases` property tells Pulumi: "This resource currently exists as a child of the root stack. Use that existing resource instead of creating a new one."

Apply the same pattern to the GitLab CI variable:

```typescript
const secondCustomerGitlabCIVariable = new gitlab.ProjectVariable("SecondCustomerGCPAccess",
    {
        project: secondCustomer.id,
        variableType: 'file',
        key: "GOOGLE_APPLICATION_CREDENTIALS",
        value: serviceAccountSecondCustomerKey.privateKey.apply(value =>
            Buffer.from(value, 'base64').toString('utf-8')
        ),
        protected: true,
        environmentScope: "*"
    },
    {
        parent: secondCustomer,
        aliases: [
            { parent: pulumi.rootStackResource }
        ]
    }
)
```

Now when you run `pulumi up`, no cloud resources are modified - Pulumi simply updates the parent-child relationships in its state. The Pulumi Console now displays a clearer hierarchy showing which resources belong together.

### Extracting a reusable component

With two customers sharing similar code, it's time to eliminate duplication by creating a reusable component. Create a custom `ComponentResource`:

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as gcp from "@pulumi/gcp";
import * as gitlab from "@pulumi/gitlab";

export interface ProjectArgs {
    // The name of the customer, e.g. "First Customer"
    customer: pulumi.Input<string>;
    // Whether to create Google Cloud infrastructure for this customer
    needsGoogleInfra: boolean;
    // Namespace in GitLab to create the repositories in
    gitlabNamespace?: pulumi.Input<number> | undefined
}

// Pulumi custom resource representing a customer project
export class Project extends pulumi.ComponentResource {
    constructor(name: string, args: ProjectArgs, opts: pulumi.CustomResourceOptions = {}) {
        super('customer:Project', name, {}, opts);

        const customerId = name.replace(/([a-zA-Z])(?=[A-Z])/g, '$1-').toLowerCase();
        const serviceId = name.replace(/([a-zA-Z])(?=[A-Z])/g, '$1').toLowerCase();

        const gitlabProject = new gitlab.Project(name,
            {
                name: customerId,
                description: pulumi.interpolate`${args.customer} code`,
                namespaceId: args.gitlabNamespace,
                visibilityLevel: "private",
                defaultBranch: "master",
                pipelinesEnabled: true,
                issuesEnabled: false,
                wikiEnabled: false,
                snippetsEnabled: false,
                containerRegistryEnabled: false,
                mergeRequestsEnabled: false,
                mergeMethod: "ff",
                onlyAllowMergeIfPipelineSucceeds: true,
                sharedRunnersEnabled: true
            }
        )

        if (args.needsGoogleInfra) {
            const gcpProject = new gcp.organizations.Project(name,
                {
                    projectId: customerId,
                    name: pulumi.interpolate`${args.customer} Infrastructure`
                }
            )

            const serviceAccount = new gcp.serviceAccount.Account(`ServiceAccount${name}`,
                {
                    accountId: serviceId,
                    displayName: pulumi.interpolate`Service Account for ${args.customer} project`,
                    project: gcpProject.projectId
                }
            );

            const serviceAccountKey = new gcp.serviceAccount.Key(`ServiceAccount${name}Key`,
                {
                    serviceAccountId: serviceAccount.email
                }
            );

            const gitlabCIVariable = new gitlab.ProjectVariable(`${name}GCPAccess`,
                {
                    project: gitlabProject.id,
                    variableType: 'file',
                    key: "GOOGLE_APPLICATION_CREDENTIALS",
                    value: serviceAccountKey.privateKey.apply(value =>
                        Buffer.from(value, 'base64').toString('utf-8')
                    ),
                    protected: true,
                    environmentScope: "*"
                }
            )
        }
    }
}
```

Now you can use this component for both customers:

```typescript
const firstCustomer = new customer.Project("FirstCustomer",
    {
        customer: 'First Customer',
        needsGoogleInfra: false,
        gitlabNamespace: gitlabNamespace
    }
)

const secondCustomerProject = new customer.Project('SecondCustomer',
    {
        customer: 'Second Customer',
        needsGoogleInfra: true,
        gitlabNamespace: gitlabNamespace
    }
)
```

When you run `pulumi up`, Pulumi creates two `customer:Project` component resources in your state. However, the child resources (GitLab projects, Google Cloud projects, etc.) still appear as children of the stack rather than the components.

### Organizing resources under components

To complete the refactoring, make the child resources parents of their respective component instances. Inside the `Project` constructor, add the `parent` option to each child resource, using `this` to reference the component instance:

```typescript
export class Project extends pulumi.ComponentResource {
    constructor(name: string, args: ProjectArgs, opts: pulumi.CustomResourceOptions = {}) {
        super('customer:Project', name, {}, opts);

        const customerId = name.replace(/([a-zA-Z])(?=[A-Z])/g, '$1-').toLowerCase();
        const serviceId = name.replace(/([a-zA-Z])(?=[A-Z])/g, '$1').toLowerCase();

        const gitlabProject = new gitlab.Project(name,
            {
                name: customerId,
                description: pulumi.interpolate`${args.customer} code`,
                namespaceId: args.gitlabNamespace,
                visibilityLevel: "private",
                defaultBranch: "master",
                pipelinesEnabled: true,
                issuesEnabled: false,
                wikiEnabled: false,
                snippetsEnabled: false,
                containerRegistryEnabled: false,
                mergeRequestsEnabled: false,
                mergeMethod: "ff",
                onlyAllowMergeIfPipelineSucceeds: true,
                sharedRunnersEnabled: true
            },
            {
                parent: this,
                aliases: [
                    { parent: pulumi.rootStackResource }
                ]
            }
        )

        if (args.needsGoogleInfra) {
            const gcpProject = new gcp.organizations.Project(name,
                {
                    projectId: customerId,
                    name: pulumi.interpolate`${args.customer} Infrastructure`
                },
                {
                    parent: this,
                    aliases: [
                        { parent: pulumi.rootStackResource }
                    ]
                }
            )

            const serviceAccount = new gcp.serviceAccount.Account(`ServiceAccount${name}`,
                {
                    accountId: serviceId,
                    displayName: pulumi.interpolate`Service Account for ${args.customer} project`,
                    project: gcpProject.projectId
                },
                {
                    parent: gcpProject,
                    aliases: [
                        { parent: pulumi.rootStackResource }
                    ]
                }
            );

            const serviceAccountKey = new gcp.serviceAccount.Key(`ServiceAccount${name}Key`,
                {
                    serviceAccountId: serviceAccount.email
                },
                {
                    parent: serviceAccount,
                    aliases: [
                        { parent: serviceAccountSecondCustomer }
                    ]
                }
            );

            const gitlabCIVariable = new gitlab.ProjectVariable(`${name}GCPAccess`,
                {
                    project: gitlabProject.id,
                    variableType: 'file',
                    key: "GOOGLE_APPLICATION_CREDENTIALS",
                    value: serviceAccountKey.privateKey.apply(value =>
                        Buffer.from(value, 'base64').toString('utf-8')
                    ),
                    protected: true,
                    environmentScope: "*"
                },
                {
                    parent: gitlabProject,
                    aliases: [
                        { parent: pulumi.rootStackResource }
                    ]
                }
            )
        }
    }
}
```

After running `pulumi up`, the Pulumi Console displays a clear hierarchy:

- Two customer project components
- Each component contains its child resources
- The second customer's Google Cloud project contains a service account
- The service account contains a key

Anyone viewing this resource graph can immediately understand:

- Your infrastructure has 2 customer projects
- One customer only has a GitLab repository
- The other customer also has Google Cloud infrastructure
- When Google Cloud infrastructure exists, it includes a project, service account, key, and GitLab CI variable

## Alias patterns

The `aliases` property accepts an array of alias objects. Each alias can specify:

- `{ name: "OldResourceName" }` - The resource had a different name
- `{ parent: oldParentResource }` - The resource had a different parent
- `{ name: "OldResourceName", parent: oldParentResource }` - Both the name and parent were different

**Important:** Providing separate entries for name and parent is different from providing a single entry with both:

```typescript
// These are NOT equivalent:
aliases: [
    { name: "OldName" },
    { parent: oldParent }
]

aliases: [
    { name: "OldName", parent: oldParent }
]
```

The first form tells Pulumi: "This resource either had a different name OR a different parent." The second form tells Pulumi: "This resource had both a different name AND a different parent at the same time."

Additionally, note that `name` values in aliases cannot be `Input`s - they must be resolvable at preview time, similar to the resource name itself.

## Next steps

- Learn more about [resource options](/docs/concepts/resources/options/) including parent, aliases, and more
- Explore [component resources](/docs/concepts/resources/components/) for building reusable abstractions
- See how to [organize projects and stacks](/docs/iac/guides/basics/organizing-projects-stacks/) for large-scale infrastructure
