const axios = require('axios');

// URL of the JSON file
const registrySearchIndexUrl = "https://www.pulumi.com/registry/search-index.json";
const docsSearchIndexUrl = "https://www.pulumi.com/search-index.json";
const indexSettingsUrl = "https://www.pulumi.com/search-index-settings.json";

// Configuration values required for updating the Algolia index.
const config = {
    appID: process.env.ALGOLIA_APP_ID,
    searchAPIKey: process.env.ALGOLIA_APP_SEARCH_KEY,
    adminAPIKey: process.env.ALGOLIA_APP_ADMIN_KEY,
    indexName: process.argv[2],
};

if (!config.appID || !config.searchAPIKey || !config.adminAPIKey || !config.indexName) {
    throw new Error(`Missing one or more required configuration values. (Provided keys: [${Object.keys(config)}])`);
}

async function publishIndex() {

    let registryIndex = [];
    let docsIndex = [];
    let indexSettings = [];

    async function fetchIndexFiles() {
        return Promise.all([
            axios.get(registrySearchIndexUrl)
                .then((response) => {
                    registryIndex = response.data;
                }),    
            axios.get(docsSearchIndexUrl)
                .then((response) => {
                    docsIndex = response.data;
                }),
            axios.get(indexSettingsUrl)
                .then((response) => {
                    indexSettings = response.data;
                })
            ]);
    }

    await fetchIndexFiles().catch((error) => {
        console.error("error retrieving index file:", error);
    });

    // De-dupe any registry objects that also may exist in the docs index.
    const filteredDocsObjects = docsIndex.filter(o => registryIndex.find(ro => ro.href === o.href) === undefined);

    // Combine search index objects from both docs and registry.
    let allObjects = [
        ...filteredDocsObjects,
        ...registryIndex,
    ];

    // Update the Algolia index, including all page objects and index settings (like searchable
    // attributes, custom ranking, synonyms, etc.).
    async function updateIndex(objects) {
        console.log("Updating search index...");

        try {
            console.log(` ↳ Replacing all records in the '${ config.indexName }' index...`);
            const result = await algoliaIndex.replaceAllObjects(objects, { safe: true });
            console.log(`   ↳ ${result.objectIDs.length} records updated.`);

            console.log(` ↳ Updating index settings...`)
            await algoliaIndex.setSettings(indexSettings);

            console.log(" ↳ Updating synonyms...")
            await algoliaIndex.saveSynonyms(indexSynonyms, { replaceExistingSynonyms: true });

            console.log(" ↳ Updating rules...")
            await algoliaIndex.replaceAllRules(indexRules);

            console.log(" ↳ Done. ✨\n");
        }
        catch (error) {
            console.error(error);
        }
    }

    await updateIndex(allObjects);
}

publishIndex();