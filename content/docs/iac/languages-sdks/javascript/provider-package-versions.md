---
title_tag: "Provider package version management in components"
meta_desc: Learn how to manage provider package versions when building Pulumi components in TypeScript and JavaScript.
title: Provider package version management
h1: Provider package version management in components
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        parent: iac-languages-javascript
        weight: 10
---

When building component packages in TypeScript or JavaScript, it's important to understand how package managers handle provider package versions. Some package management systems allow for different versions of a package to be installed concurrently. You can include a package as a direct dependency in your project, and another dependency could depend on the same package but with a different version.

## Version conflicts with provider packages

Suppose we are building a component package where you use `@pulumi/random`, major version 3. In our `package.json` file for the component package, you have this:

```json
{
  "name": "components",
  "version": "1.0.0",
  ...
  "dependencies": {
    ...
    "@pulumi/random": "^3",
    ...
  },
  ...
}
```

In a project where you consume this component library, you can add more `random` resources, but now using major v4:

```json
{
  "name": "components-consume",
  ...
  "dependencies": {
    ...
    "@pulumi/random": "^4",
    "components": "^1",
    ...
  },
  ...
}
```

In the situation where you mix major versions, the specification `^3` excludes major version `4`. If we check on our dependency graph, we see two versions included:

```sh
$ npm why @pulumi/random
@pulumi/random@v4.14.0
node_modules/@pulumi/random
  @pulumi/random@"^4.14.0" from the root project

@pulumi/random@v3.2.0 extraneous
  @pulumi/random@"^3" from components@1.0.0
    components@1.0.0
```

When you use a Pulumi Node.js SDK for a provider, Pulumi will always use the plugin binary of the same version. By having multiple versions of an SDK in our dependency graph, you will see multiple versions of the default provider in your Pulumi state file as a result. The child `random` resources of components from your library will be provisioned with plugin binary v3, while the top level `random` resources will use v4.

A similar situation would happen if you would pin the component library and the consuming project to explicit but different versions. For instance, using `"4.11.0"` in the component library and `"4.14.0"` in the consuming project would result in 2 default providers with exactly these versions.

## Recommended approach

If you only want single version of the package and default provider, we suggest to use the caret style notation in your component package. Use `^`, followed by the minimum version of the dependency, and use a compatible version in your consuming project for your components to work correctly.

For instance, if `@pulumi/random` v4.8.2 contained a fix you rely on, use this in your library `package.json`:

```json
{
  "name": "components",
  "version": "1.0.0",
  ...
  "dependencies": {
    ...
    "@pulumi/random": "^4.8.2",
    ...
  },
  ...
}
```

When you use a version of `@pulumi/random` in your consuming project which is too old, npm will warn you that you need to upgrade.
