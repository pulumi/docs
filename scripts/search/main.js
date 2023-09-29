const fs = require("fs");
const page = require("./page");

// As part of the Hugo build, we generate a JSON file at /index.json containing a record for every
// page of the website. We use this file to generate primary search records for Algolia.
const pathToFullSiteJSON = "./public/index.json";
const hugoPageItems = JSON.parse(fs.readFileSync(pathToFullSiteJSON, "utf-8").toString());

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

// Temporary hack: Remove any references to `azure-native-v1`. This line can be
// removed once the azure-native-v1 package is removed from the Registry.
// https://github.com/pulumi/registry/issues/2879
allObjects = allObjects.filter(o => !o.href.includes("azure-native-v1"));

// Write the results, just so we have them.
console.log(" ↳ Writing results...");
fs.writeFileSync("./public/search-index.json", JSON.stringify(allObjects, null, 4));
console.log(" ↳ Done. ✨\n");
