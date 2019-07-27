"use strict";

importScripts("/js/lunr.min.js");

var index;

// Download the search index synchronously.
var req = new XMLHttpRequest();
req.open("GET", "/docs/search-index.json", false /* async */);
req.send();
if (req.readyState === req.DONE && req.status === 200) {
    var data = JSON.parse(req.responseText);
    index = lunr.Index.load(data);
} else {
    console.log("problem downloading search-index.json");
}

function search(query) {
    try {
        if (index && query.length) {
            var results = index.search(query);

            return results.map(function(result) {
                // Extract the url and title from the ref string (they're separated by "|").
                var i = result.ref.indexOf("|");
                if (i === -1) {
                    throw new Error("'|' not found in ref: " + result.ref);
                }
                var url = result.ref.substring(0, i);
                var title = result.ref.substring(i + 1);
                return { url: url, title: title };
            });
        }
    } catch (e) {
        console.log(e);
    }
    return [];
}

self.onmessage = function (message) {
    var type = message.data.type;
    var payload = message.data.payload;
    if (type === "search") {
        self.postMessage({ payload: { query: payload, results: search(payload) } });
    }
}
