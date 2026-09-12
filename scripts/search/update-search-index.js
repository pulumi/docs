const axios = require('axios');
const settings = require("./settings");
const { algoliasearch } = require("algoliasearch");

// URL of the JSON file
const registrySearchIndexUrl = "https://www.pulumi.com/registry/search-index.json";
const docsSearchIndexUrl = "https://www.pulumi.com/search-index.json";

// The Dev Center (tutorials, templates, community examples, glossary) ships from
// pulumi/marketing-web and publishes its own search index. Its records use a
// different shape than ours, so we normalize them before merging (see
// normalizeDevRecords). A fetch failure here is non-fatal: we log and continue
// with an empty set so a Dev Center outage never blocks the docs/registry index.
const devSearchIndexUrl = "https://www.pulumi.com/dev/search-index.json";

// Maps a Dev Center search record onto the docs/registry record shape. The Dev
// Center index carries a large `content` field, but `content` isn't a searchable
// attribute in our index (see settings.js), so we drop it here — that also keeps
// each record under Algolia's per-record size limit. Dev Center results match on
// title, blurb, and tags, like our blog and heading-level records.
function normalizeDevRecords(devIndex) {
    return devIndex
        .filter(o => o.objectID && o.href && o.title)
        .map(o => ({
            objectID: o.objectID,
            section: "Dev Center",
            title: o.title,
            h1: o.title,
            description: o.blurb || "",
            href: o.href,
            rank: o.featured ? 150 : 100,
            boosted: false,
            keywords: [].concat(o.tagLabels || [], o.languageLabels || []),
            tags: [].concat(o.tags || [], o.languages || [], o.clouds || []),
            ancestors: ["Dev Center", o.typeLabel].filter(Boolean),
        }));
}

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

async function publishIndex() {

    let registryIndex = [];
    let docsIndex = [];
    let devIndex = [];

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
        process.exit(1);
    });

    // Fetch the Dev Center index separately so a failure degrades gracefully
    // (empty results) rather than failing the whole publish.
    await axios.get(devSearchIndexUrl)
        .then((response) => {
            devIndex = normalizeDevRecords(response.data);
            console.log(`Fetched ${devIndex.length} Dev Center records.`);
        })
        .catch((error) => {
            console.error("error retrieving Dev Center index file (continuing without it):", error.message);
        });

    // De-dupe any registry objects that also may exist in the docs index.
    const filteredDocsObjects = docsIndex.filter(o => registryIndex.find(ro => ro.href === o.href) === undefined);

    // Combine search index objects from docs, registry, and the Dev Center.
    let allObjects = [
        ...filteredDocsObjects,
        ...registryIndex,
        ...devIndex,
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
            const result = await client.replaceAllObjects({
                indexName: config.indexName,
                objects: objects,
            });
            await client.waitForTask({
                indexName: config.indexName,
                taskID: result.taskID
            });
            console.log(`   ↳ ${objects.length} records updated.`);

            console.log(` ↳ Updating index settings...`)
            const settingsResult = await client.setSettings({
                indexName: config.indexName,
                indexSettings: indexSettings
            });
            await client.waitForTask({
                indexName: config.indexName,
                taskID: settingsResult.taskID
            });

            console.log(" ↳ Updating synonyms...")
            const synonymsResult = await client.saveSynonyms({
                indexName: config.indexName,
                synonymHits: indexSynonyms,
                forwardToReplicas: false,
                replaceExistingSynonyms: true
            });
            await client.waitForTask({
                indexName: config.indexName,
                taskID: synonymsResult.taskID
            });

            console.log(" ↳ Updating rules...")
            const rulesResult = await client.saveRules({
                indexName: config.indexName,
                rules: indexRules,
                forwardToReplicas: false,
                clearExistingRules: true
            });
            await client.waitForTask({
                indexName: config.indexName,
                taskID: rulesResult.taskID
            });

            console.log(" ↳ Done. ✨\n");
        }
        catch (error) {
            console.error(error);
        }
    }

    await updateIndex(allObjects);
}

publishIndex();