const fs = require("fs");
const page = require("./page");
const algoliasearch = require("algoliasearch");

// As part of the Hugo build, we generate a JSON file at /index.json containing a record for every
// page of the website. We use this file to generate primary search records for Algolia.
const pathToFullSiteJSON = "./public/index.json";
const hugoPageItems = JSON.parse(fs.readFileSync(pathToFullSiteJSON, "utf-8").toString());

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

// Generate a list of primary page objects. This list contains one record for every page of the site.
console.log("\nBuilding search index...");
console.log(" ↳ Building primary page objects...");
const primaryPageObjects = page.getPrimaryObjects(hugoPageItems);

// Generate a list of secondary objects. This list contains additional records for things like H2
// headings and other DOM-resident content that we can't get as easily by other means.
console.log(" ↳ Building secondary page objects...");
const secondaryPageObjects = page.getSecondaryObjects(primaryPageObjects);

// Stitch these lists together into one tidy bundle.
let allObjects = [
    ...primaryPageObjects,
    ...secondaryPageObjects,
];

// Generate array of objects related to docs. The primary objects are included here instead of the filtered objects,
// since these will be filtered by the job that stiches the registry and docs objects together.
let docsObjects = [
    ...primaryPageObjects,
    ...secondaryPageObjects,
]

// Temporary hack: Remove any references to `azure-native-v1`. This line can be
// removed once the azure-native-v1 package is removed from the Registry.
// https://github.com/pulumi/registry/issues/2879
allObjects = allObjects.filter(o => !o.href.includes("azure-native-v1"));

// Write the results, just so we have them.
console.log(" ↳ Writing results...");
fs.writeFileSync("./public/search-index.json", JSON.stringify(allObjects, null, 4));
console.log(" ↳ Done. ✨\n");

// Update the Algolia index, including all page objects and index settings (like searchable
// attributes, custom ranking, synonyms, etc.).
async function updateIndex(objects) {
    console.log("Updating search index...");

    try {
        console.log(` ↳ Replacing all records in the '${ config.indexName }' index...`);
        const result = await algoliaIndex.replaceAllObjects(objects, { safe: true });
        console.log(`   ↳ ${result.objectIDs.length} records updated.`);
        console.log(" ↳ Done. ✨\n");
    }
    catch (error) {
        console.error(error);
    }
}

updateIndex(allObjects);
