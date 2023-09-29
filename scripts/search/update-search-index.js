const axios = require('axios');
const settings = require("./settings");
const algoliasearch = require("algoliasearch");

// URL of the JSON file
const registrySearchIndexUrl = "https://www.pulumi.com/registry/search-index.json";
const docsSearchIndexUrl = "https://www.pulumi.com/search-index.json";

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

// Initialize the Algolia search client.
const client = algoliasearch(config.appID, config.adminAPIKey);
const algoliaIndex = client.initIndex(config.indexName);

async function publishIndex() {

    let registryIndex = [];
    let docsIndex = [];

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

    // Temporary hack: Remove any references to `azure-native-v1`. This line can be
    // removed once the azure-native-v1 package is removed from the Registry.
    // https://github.com/pulumi/registry/issues/2879
    allObjects = allObjects.filter(o => !o.href.includes("azure-native-v1"));

    // Gather up index settings, synonyms, and rules.
    const indexSettings = {
        searchableAttributes: settings.getSearchableAttributes(),
        attributesForFaceting: settings.getAttributesForFaceting(),
        attributesToHighlight: settings.getAttributesToHighlight(),
        customRanking: settings.getCustomRanking(),
        ignorePlurals: true,
    };

    const indexSynonyms = settings.getSynonyms();
    const indexRules = settings.getRules();

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