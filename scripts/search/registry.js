const { Octokit } = require("@octokit/rest");
const yaml = require("js-yaml");
const fetch = require("node-fetch");
const fs = require("fs");
const path = require("path");
const page = require("./page");

module.exports = {

    // Fetch a set of objects representing all Registry resources.
    getObjects(pathToRegistryJSON, hugoPageItems) {
        const registryPackageNames = fs.readdirSync(pathToRegistryJSON);
        const registryItems = [];

        registryPackageNames
            .map(providerJSON => {
                const providerName = providerJSON.replace(".json", "");
                const providerResults = [];

                // API docs JSON doesn't contain proper provider/package names, so we obtain those
                // from the Hugo-generated set.
                const providerTitle = hugoPageItems.find(o => {
                    return o.href === `/registry/packages/${providerName}/`;
                }).title;

                // Read the API docs JSON file.
                const providerItems = JSON.parse(
                    fs.readFileSync(path.join(pathToRegistryJSON, providerJSON), "utf8").toString(),
                );

                // For every resource in that file, generate an individual search record, including
                // tokens as keywords to make them easier to find by copy/paste.
                function getMember(itemPath, item) {

                    // Some of the items in our registry nav files contain trailing slashes, which
                    // don't play nicely with the string concatenation we do to build up our search
                    // URLs. So we strip them out to avoid ending up with doubles (and thus 404s).
                    item.link = item.link.replace(/\/+$/, "");

                    providerResults.push({
                        title: `${item.name} (${itemPath.concat(item.name).join(".")})`,
                        description: `API documentation for the ${item.name} ${item.type} of the ${providerTitle} provider, including examples, input and output properties, lookup functions, and supporting types.`,
                        type: item.type,
                        href: `/registry/packages/${providerName}/api-docs/${itemPath.concat(item.link).slice(1).join("/").toLowerCase()}/`,
                        keywords: [
                            item.name,
                            itemPath.concat(item.name).slice(1).join(" ").toLowerCase(),
                            itemPath.concat(item.name).join("."),
                            itemPath.concat(item.name).join(":"),
                            itemPath.concat(item.name).join(" "),
                            `${providerTitle} ${item.name}`
                        ],
                        ancestors: [ "Registry", providerTitle, "API Docs" ],
                    });

                    if (item.children) {
                        item.children.map(child => {
                            getMember([...itemPath, item.name], child);
                        });
                    }
                }

                providerItems.forEach(item => {
                    getMember([ providerName ], item);
                });

                return {
                    name: providerName,
                    items: providerResults,
                };
            })
            .forEach(member => {
                registryItems.push(...member.items);
            });

            return registryItems.map(item => {
                return {
                    objectID: page.getObjectID(item),
                    title: item.title,
                    description: item.description,
                    section: "Registry",
                    href: item.href,
                    rank: page.getRank(item),
                    keywords: item.keywords,
                    ancestors: item.ancestors,
                };
            });
    },

    async getSnapshot() {
        const auth = process.env.GITHUB_TOKEN;
        const octokit = new Octokit({ auth });

        const pulumiRegistryRepo = {
            owner: "pulumi",
            repo: "registry",
            ref: "master",
        };

        function fromBase64(s) {
            return Buffer.from(s, "base64").toString().trim();
        }

        const packages = await octokit.rest.repos.getContent({
            ...pulumiRegistryRepo,
            path: "/themes/default/data/registry/packages",
        });

        const packageSummaries = await Promise.all(
            packages.data.map(async package => {

                const result = await octokit.rest.repos.getContent({
                    ...pulumiRegistryRepo,
                    path: package.path,
                });

                const packageYaml = yaml.load(fromBase64(result.data.content));
                const packageRepoURL = new URL(packageYaml.repo_url);
                const [ _, packageOwner, packageRepo ] = packageRepoURL.pathname.split("/");
                const packageSchemaPath = packageYaml.schema_file_path;
                const packageVersion = packageYaml.version;
                const packageTitle = packageYaml.title;

                return {
                    title: packageTitle,
                    repoURL: packageRepoURL.toString(),
                    owner: packageOwner,
                    repo: packageRepo,
                    path: packageSchemaPath,
                    ref: packageVersion,
                };
            }),
        );

        console.log(`\nProcessing ${packageSummaries.length} registry packages...`);
        const results = {};

        for await (const summary of packageSummaries) {
            const fileType = path.extname(summary.path).replace(".", "");

            // Fetch content of the the schema file.
            const result = await octokit.rest.repos.getContent({
                owner: summary.owner,
                repo: summary.repo,
                path: summary.path,
                ref: summary.ref,
            });

            // Try to decode the content. Large files won't be included, so if that's the case,
            // fetch the file from the download URL instead.
            let content = fromBase64(result.data.content);

            if (!content) {
                let response = await fetch(result.data.download_url);
                content = await response.buffer();
            }

            let package;

            switch(fileType) {
                case "yaml":
                case "yml":
                    package = yaml.load(content);
                    break;
                case "json":
                    package = JSON.parse(content);
                    break;
            }

            if (package) {
                const props = {};

                for (let prop of [ "resources", "types" ]) {
                    props[prop] = Object.keys(package[prop] || {})
                        .map(key => {
                            return {
                                type: key,
                                inputs: Object.keys((package[prop][key] || {}).inputProperties || {}),
                                outputs: Object.keys((package[prop][key] || {}).properties || {}),
                            };
                        });
                }

                results[package.name] = {
                    title: summary.title,
                    version: summary.ref,
                    ...props,
                };

                console.log(` ↳ ${summary.title} (${package.name}) ✓`);
            }
        }

        console.log(" ↳ Done. ✨\n");
        return results;
    },

    async getPropertiesObjects() {
        const snapshot = await this.getSnapshot();
        return this.toPropertiesObjects(snapshot);
    },

    typeToRegistryPath(type) {
        const parts = this.typeToParts(type);
        const optionalModulePath = parts.modules.length > 0 ? parts.modules.join("/") + "/" : "";
        return `/registry/packages/${parts.provider}/api-docs/${optionalModulePath}${parts.name.toLowerCase()}/`;
    },

    typeToParts(type) {
        const outerSegments = type.split(":");
        const [ one, two, three ] = outerSegments;

        const parts = {
            provider: one,
            name: three,
        };

        // Modules is the stuff in the middle.
        const innerSegments = two.split("/");

        // azure-justrun:index:containerapp
        // /registry/packages/azure-justrun/api-docs/containerapp/
        if ((innerSegments.length === 1 || innerSegments.length === 2) && innerSegments[0] === "index") {
            return {
                ...parts,
                modules: [],
            };
        }

        // aws:s3/bucket:Bucket
        // /registry/packages/aws/api-docs/s3/bucket/
        if (innerSegments[1] && innerSegments[1].toLowerCase() === parts.name.toLowerCase()) {
            return {
                ...parts,
                modules: [
                    innerSegments[0],
                ],
            };
        }

        // kubernetes:admissionregistration.k8s.io/v1alpha1:ValidatingAdmissionPolicyBinding
        // /registry/packages/kubernetes/api-docs/admissionregistration/v1alpha1/validatingadmissionpolicybinding/
        const dotSegments = innerSegments[0].split(".");
        if (dotSegments.length > 0) {
            return {
                ...parts,
                modules: [
                    dotSegments[0],
                    innerSegments[1],
                ],
            };
        }
    },

    typeToSimplifiedType(type) {
        const parts = this.typeToParts(type);
        return [ parts.provider, parts.modules[0], parts.name ].filter(p => !!p).join(".");
    },

    toPropertiesObjects(snapshot) {
        const packageNames = Object.keys(snapshot);
        const objects = [];

        packageNames.forEach(packageName => {
            const package = snapshot[packageName];

            package.resources.forEach(resource => {
                try {
                    const href = `${this.typeToRegistryPath(resource.type)}#properties`;
                    const simplifiedType = this.typeToSimplifiedType(resource.type);
                    const parts = this.typeToParts(resource.type);

                    // For every resource, push a link to the inputs and outputs headings, using property lists as keywords.
                    objects.push({
                        objectID: page.getObjectID({ href }),
                        title: `${parts.name} (${simplifiedType}) properties`,
                        description: `${resource.inputs.join(", ")}`,
                        href,
                        section: "Registry",
                        keywords: [
                            ...(new Set([ ...resource.inputs, ...resource.outputs ])),
                            resource.type,
                        ],
                        ancestors: [
                            "Registry",
                            package.title,
                            "API Docs",
                        ],
                    });

                } catch (err) {
                    console.error(err);
                    console.log(`Failed on on ${resource.type}.`);
                }
            });
        });

        return objects;
    },
};
