const fs = require("fs");
const path = require("path");
const crypto = require("crypto");
const page = require("./page");
const registry = require("./registry");
const settings = require("./settings");
const algoliasearch = require("algoliasearch");

// As part of the Hugo build, we generate a JSON file at /index.json containing a record for every
// page of the website. We use this file to generate primary search records for Algolia.
const pathToFullSiteJSON = "./public/index.json";
const hugoPageItems = JSON.parse(fs.readFileSync(pathToFullSiteJSON, "utf-8").toString());

// As part of the Registry build, we also generate a collection of JSON files that we use to power
// the API docs navigation. We use this file here as well to add resource listings, etc., to the
// index to make them more findable by their type names and the like.
const pathToRegistryPackagesJSON = "./public/registry/packages/navs";

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

async function generateIndexData() {

    // Generate a list of primary page objects. This list contains one record for every page of the site.
    console.log("\nBuilding search index...");
    console.log(" ↳ Building primary page objects...");
    const primaryPageObjects = page.getPrimaryObjects(hugoPageItems);

    // Generate a list of secondary objects. This list contains additional records for things like H2
    // headings and other DOM-resident content that we can't get as easily by other means.
    console.log(" ↳ Building secondary page objects...");
    const secondaryPageObjects = page.getSecondaryObjects(primaryPageObjects);

    // Generate a list of all Registry items -- modules, resources, functions, etc.
    console.log(" ↳ Building Registry resource objects...");
    const registryObjects = registry.getObjects(pathToRegistryPackagesJSON, hugoPageItems);

    // Remove any objects from primaryPageObjects that also exist in registryObjects (to de-dupe).
    const filteredPageObjects = primaryPageObjects.filter(o => registryObjects.find(ro => ro.href === o.href) === undefined);

    // Generate a full snapshot of the Registry, including all packages, resources, and supporting types.
    const resourcePropertiesObjects = await registry.getPropertiesObjects();

    // Stitch these lists together into one tidy bundle.
    const indexObjects = [
        ...filteredPageObjects,
        ...secondaryPageObjects,
        ...registryObjects,
        ...resourcePropertiesObjects,
    ];

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

    // Write the results, just so we have them.
    console.log("Writing results...");
    fs.writeFileSync("./public/search-index.json", JSON.stringify(indexObjects, null, 4));
    fs.writeFileSync("./public/search-index-settings.json", JSON.stringify({ indexSettings, indexSynonyms, indexRules }, null, 4));
    fs.writeFileSync(`./public/search-registry-snapshot.json`, JSON.stringify(resourcePropertiesObjects, null, 4));
    console.log(" ↳ Done. ✨");

    return {
        indexObjects,
        indexSettings,
        indexSynonyms,
        indexRules,
    };
}

// Update the Algolia index, including all page objects and index settings (like searchable
// attributes, custom ranking, synonyms, etc.).
async function updateIndex({ indexObjects, indexSettings, indexSynonyms, indexRules }) {
    console.log("\nUpdating search index...");

    try {
        console.log(` ↳ Replacing all records in the '${ config.indexName }' index...`);
        const result = await algoliaIndex.replaceAllObjects(indexObjects, { safe: true });
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

generateIndexData()
    .then(async results => await updateIndex(results));
