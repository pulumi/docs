---
title: Kubernetes SDKs from the Pulumiverse
date: 2021-12-29T13:32:16Z
draft: false
meta_desc: In this article, we look at a new repository published on the Pulumiverse that delivers rich Kubernetes SDKs for popular CRDs.
meta_image: meta.png
authors: ["david-flanagan"]
tags: ["kubernetes"]
---

Pulumi provides an amazingly rich interface for developers and operators to define their Kubernetes workloads, providing typed access to recourses from the Kubernetes API and allowing our IDEs to provide code completion and refactoring opportunities through the native language plugins.

As great as that is, it's always gotten a little cumbersome when it comes to Custom Resource Definitions (CRDs), as the first option is to leverage the CustomResource escape-hatch that allows you to define any Kubernetes object you wish; however this does mean we lose the rich interface we've become accustomed to.

```typescript
new k8s.apiextensions.CustomResource('marvin-the-martian', {
    apiVersion: 'looneytunes.com/v1990',
    kind: 'LooneyTune',
    metadata: {
        name: 'Marvin the Martian',
        planet: 'mars'
    },
    spec: {
        armor: {
            style: 'hoplite',
            colors: ['green', 'red'],
        },
        phrases: [
            'Wheres the kaboom',
            'Oh, drat these computers. They’re so naughty and so complex. I could pinch them',
            'I do so enjoy observing the flora and fauna of that tiny planet',
            'Please, sir. Do not interrupt my chain of thought. I am a busy Martian',
            'Brace yourself for immediate disintegration'
        ]
    },
});
```

While this is a huge unblocker for working with Kubernetes, we can do better.

## crd2pulumi

Back in August, 2020, we published [crd2pulumi]({{< relref "/blog/introducing-crd2pulumi" >}}). `crd2pulumi` allows you to generate a Pulumi SDK for any Kubernetes Custom Resource. Now, when you want to start using cert-manager, Ambassador, Linkerd, or any other project within the Kubernetes and Cloud Native space; you can download the CRD YAML and run `crd2pulumi`, which will generate the SDK for whatever supported language you wish. Neat?

I've been using this approach for the past year and it's the easiest way to provide that rich interface to developers, but the repetition can become a little frustrating. For every new project that I was working on, I'd need to build out the same automation and there's also the maintenance burden of ensuring the SDK is up to date with the latest version deployed to the cluster.

Further more, these SDKs never change; if you generate a SDK for cert-manager and someone else does, supporting the same version - there's no difference in the code that is generated. Do we really need everyone to do this themselves?

Perhaps some further tooling is required.

## Kubernetes SDKs at Pulumiverse

I like solving problems like this. It's not technically challenging, the hard work is already done by the team supporting `crd2pulumi`. The problem we need to solve here is a quality of life / developer experience issue. How can we make this easier for developers to consume?

For us to make this easier, we have two issues:

1. How do we automate the generation of the SDKs, ensuring that the SDKs are always up to date?
2. Where do we publish them?

### Automation

GitHub Actions plays such a large role in our developer world these days, especially for open source projects. So it was an easy choice to make that any automation I build out for this will be built on top of GitHub Actions. Knowing that we want the SDKs to be up to date, we also know that this automation must run on a regular cadence. As such, the beginnnig of our GitHub Action can take some shape:

```yaml
name: Build SDKs

on:
  schedule:
    - cron: "10 3,15 * * *"
```

Here, we have our GitHub Action scheduled to run every day at 3:10am and 3:10pm.

Next, we need to know what to build. We don't want to build EVERY SDK that the project is aware of, so we need some code to look up GitHub Releases for some new tags. For this, we can drop to Python to do some quick lookups.

```python
from atoma import parse_atom_bytes
from datetime import datetime, timedelta, timezone
from json import dumps
from requests import get as httpget
from typing import List, Mapping, Optional
from yaml import safe_load, YAMLError
import sys


def has_been_updated(updated_at: Optional[datetime] = None) -> bool:
    if updated_at == None:
        return False
    hours_since: int = int(sys.argv[1]) if len(sys.argv) > 1 else 12

    return (datetime.now(timezone.utc) - updated_at) < timedelta(hours=hours_since)


def get_new_tags(repository: str) -> List[str]:
    response = httpget(f'https://{repository}/tags.atom')
    feed = parse_atom_bytes(response.content)

    return list(map(lambda entry: entry.title.value, filter(lambda entry: has_been_updated(entry.updated), feed.entries)))


with open("./sdks.yaml", "r") as stream:
    try:
        sdks: Mapping[str, str] = safe_load(stream)
    except YAMLError as exc:
        print(f"Error parsing SDK Yaml: {exc}")

sdks_to_build: List[str] = []
for name, repository in sdks.items():
    for tag in get_new_tags(repository):
        sdks_to_build.append(
            f'{name}|{repository}|{tag}')

print(dumps(sdks_to_build))
```

This Python will loop through our configured SDKs, loaded from a YAML document, and reach out to the atom feed that GitHub provides for every public repository. This allows us to quickly loop over the tags/releases and find any published within the last window. We don't need to do anything else besides print this to the terminal and allow GitHub Actions to store the output for use in our build matrix.

```yaml
jobs:
  find_new_tags:
    runs-on: ubuntu-latest
    steps:
      - ... random boring steps

      - id: find_new_tags
        run: echo "::set-output name=sdk_versions::$(poetry run python ./bin/find-new-tags.py ${{ github.event.inputs.since_hours }})"

    outputs:
      sdk_versions: ${{ steps.find_new_tags.outputs.sdk_versions }}

build_nodejs_sdk:
    needs: find_new_tags
    runs-on: ubuntu-latest
    strategy:
      matrix:
        version: ${{ fromJson(needs.find_new_tags.outputs.sdk_versions) }}
```

Once our Python script has run and the output stored, we're using a helper function from GitHub called `fromJson` to use the output as a dynamic input to their matrix build system. We'll get exactly one job for every new tag that we've found.

The job to generate the SDK and publish it to npm looks like this:

```yaml
- name: crd2pulumi-generate-sdk
  run: |
    IFS='|' read -r -a build_parts <<< "${{ matrix.version }}"
    mkdir -p ./_output
    curl -fsSL -o crd.yaml https://doc.crds.dev/raw/${build_parts[1]}@${build_parts[2]}
    crd2pulumi --nodejsName ${build_parts[0]} --nodejsPath ./_output ./crd.yaml --force
    # Fix Package Name
    sed -ie "s#@pulumi/${build_parts[0]}#@pulumiverse/${build_parts[0]}#g" ./_output/package.json
    # Fix Package Version
    sed -ie "s#\"version\": \"\"#\"version\": \"${build_parts[2]}\"#g" ./_output/package.json
- run: npm publish --access=public
  working-directory: ./_output
  env:
    NODE_AUTH_TOKEN: ${{ secrets.NPM_TOKEN }}
```

Like I said earlier, the hard work was already done; we just needed to glue some automation together to improve the DX.

### Publishing

Now that we have this system in place to regularly check and build new SDKs, we needed a home for them to live. Recently, some amazing Pulumi community members, worked together on a new GitHub initiative, with Pulumi support, called Pulumiverse. Pulumiverse aims to be a community lead and governed initiative to provide new abstractions and libraries for consumers of Pulumi to use and make their lives easier. This is the perfect place for these SDKs to live.

You can checkout the [repository today](https://github.com/pulumiverse/kubernetes-sdks).

### SDKs

Currently, the automation publishes NodeJS SDKs (JavaScript and TypeScript) to npm, but plans to add Python will be executed very soon. We're also looking to publish packages for dotNet, but research is still underway.

I don't expect to publish packages for Go ... sadly, because Go modules use GitHub for fetching source code - we'd need to publish generated code to the repository and I'm not entirely keen on that approach. I could possibly be persuaded, but I'd love some suggestions for alternate ways to resolve this.

We currently provide SDKs for:

- argocd
- cert-managaer
- crossplane
- knative
- redpanda

Need more? No problem! Open a pull request adding a SINGLE LINE to `sdks.yaml` and the SDK will be available shortly.

Nice.

### Prior Art

While writing this article, I discovered an [old repository](https://github.com/pulumi/pulumi-kubernetes-crds) within the Pulumi organization that actually did something similar to this last year 😮 It's not automated like this new initiative, but it was great to find that previous attempts to improve the developer experience for Kubernetes teams using Pulumi. Mad props to Paul Stack and Albert Zhong.

So that's it! Thanks for reading. We hope you find this useful and we encourage you to join us and help by adding your favourite Kubernetes SDKs to the automation.

We'll see you in 2022, have a great New Year. 🎉
