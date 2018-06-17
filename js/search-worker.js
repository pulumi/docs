"use strict";

importScripts("/js/lunr.min.js");

var data = {};
var index;

// Download the search data synchronously.
var req = new XMLHttpRequest();
var async = false;
req.open("GET", "/search-data.json", async);
req.send();
if (req.readyState === req.DONE && req.status === 200) {
    data = JSON.parse(req.responseText);
    loadIndex();
} else {
    console.log("problem downloading search-data.json");
}

function loadIndex() {
    index = lunr(function() {
        this.ref("id");
        this.field("title", { boost: 10 });
        this.field("content");

        for (var key in data) {
            var item = data[key];
            if (item.title || item.content) {
                this.add({
                    id: key,
                    title: data[key].title,
                    content: data[key].content
                });
            }
        }
    });
}

function search(query) {
    try {
        if (index && query.length) {
            var results = index.search(query);

            return results.map(function(result) {
                return {
                    score: result.score,
                    url: result.ref,
                    title: data[result.ref].title
                };
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
