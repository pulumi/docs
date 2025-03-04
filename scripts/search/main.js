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

// Incorporate any additional objects. This list is provided as a hand-crafted list for now, because pragmatism,
// but it should probably be pulled out into a proper module at some point.
const additionalObjects = [
    {
        "section": "Docs",
        "title": "Pulumi Node.js SDK Documentation",
        "description": "Documentation for the Pulumi Node.js SDK.",
        "href": "/docs/reference/pkg/nodejs/pulumi/pulumi/",
        "keywords": [
            "@pulumi/pulumi",
            "javascript sdk",
            "typescript sdk",
            "nodejs sdk",
            "node sdk",
            "sdk",
        ],
        "ancestors": [
            "Docs",
            "Languages & SDKs",
            "TypeScript (Node.js)"
        ],
    },
    {
        "section": "Docs",
        "title": "Pulumi Python SDK Documentation",
        "description": "Documentation for the Pulumi Python SDK.",
        "href": "/docs/reference/pkg/python/pulumi/",
        "keywords": [
            "pulumi_pulumi",
            "python sdk",
            "sdk",
        ],
        "ancestors": [
            "Docs",
            "Languages & SDKs",
            "Python"
        ],
    },
    {
        "section": "Docs",
        "title": "Pulumi Go SDK Documentation",
        "description": "Documentation for the Pulumi Go SDK.",
        "href": "https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi",
        "rank": 860, // The default ranking for docs. (See rank.js.)
        "keywords": [
            "go sdk",
            "golang sdk",
            "sdk",
        ],
        "ancestors": [
            "Docs",
            "Languages & SDKs",
            "Go"
        ],
    },
    {

        "section": "Docs",
        "title": "Pulumi .NET SDK Documentation (C#, VB, F#)",
        "description": "Documentation for the Pulumi .NET SDK.",
        "href": "/docs/reference/pkg/dotnet/Pulumi/Pulumi.html",
        "keywords": [
            "Pulumi.Pulumi",
            ".net sdk",
            "c# sdk",
            "vb sdk",
            "f# sdk",
            "sdk"
        ],
        "ancestors": [
            "Docs",
            "Languages & SDKs",
            ".NET (C#, VB, F#)"
        ],
    },
].map(item => {
    return {
        "objectID": page.getObjectID({ href: item.href }),
        ...item,
    };
});

// Stitch these lists together into one tidy bundle.
let allObjects = [
    ...primaryPageObjects,
    ...secondaryPageObjects,
    ...additionalObjects,
];

// Temporary hack: Remove any references to `azure-native-v1`. This line can be
// removed once the azure-native-v1 package is removed from the Registry.
// https://github.com/pulumi/registry/issues/2879
allObjects = allObjects.filter(o => !o.href.includes("azure-native-v1"));

// Write the results, just so we have them.
console.log(" ↳ Writing results...");
fs.writeFileSync("./public/search-index.json", JSON.stringify(allObjects, null, 4));
console.log(" ↳ Done. ✨\n");
