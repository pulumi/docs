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
    }
};
