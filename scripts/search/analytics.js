const fs = require("fs");
const path = require("path");
const crypto = require("crypto");
const algoliasearch = require("algoliasearch");
const fetch = require("node-fetch");
const qs = require("qs");

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

// https://www.algolia.com/doc/api-reference/api-methods/get-logs/
async function getRecentQueries() {

    const result = await client.getLogs({
        type: "query",
        length: 100,
    });

    return result.logs
        .filter(item => {
            try {
                JSON.parse(item.query_body)
                return true;
            } catch (err) {
                return false;
            }
        })
        .map(item => JSON.parse(item.query_body))
        .filter(queryBody => queryBody && queryBody.requests && queryBody.requests[1])
        .map(queryBody => queryBody.requests[1])
        .map(queryBody => queryBody.query);
}

async function get(path, options) {
    const result = await fetch(`https://analytics.algolia.com/2/${ path }?${ qs.stringify({ ...options, index: config.indexName }) }`, {
        method: "GET",
        headers: {
            "X-Algolia-API-Key": config.adminAPIKey,
            "X-Algolia-Application-Id":  config.appID,
        },
    });

    const data = await result.json();
    return data;
}

async function getEverything() {
    await Promise.all(
        [
            getRecentQueries(),
            get("/searches", { limit: 1000 }),
            get("/searches/count"),
            get("/searches/noResults", { limit: 200 }),
            get("/searches/noClicks", { limit: 200 }),
            get("/searches/noResultRate"),
            get("/searches/noClickRate"),
            get("/hits"),
            get("/users/count"),
            get("/filters"),
        ]
    )
    .then(([
            recentQueries,
            searches,
            searchesCount,
            searchesNoResults,
            searchesNoClicks,
            searchesNoResultRate,
            searchesNoClickRate,
            hits,
            usersCount,
            filters,
        ]) => {

        const everything = {
            timestamp: Date.now(),
            recentQueries,
            searches,
            searchesCount,
            searchesNoResults,
            searchesNoClicks,
            searchesNoResultRate,
            searchesNoClickRate,
            hits,
            usersCount,
            filters,
        };

        fs.writeFileSync("./search-analytics.json", JSON.stringify(everything, null, 4), "utf-8");
    });
}

getEverything();
