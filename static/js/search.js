"use strict";

(function () {
    var searchBox = document.getElementById("search-box");
    var spinner = document.getElementById("spinner");
    var searchResultsContainer = document.getElementById("search-results-container");

    // Use a worker to download and setup the index in the background.
    var worker = new Worker("/js/search-worker.js");
    worker.onmessage = function (message) {
        var payload = message.data.payload;
        displaySearchResults(payload.results);
    };

    // Extract the query from the browser's URL.
    var query = getQueryVariable("q");
    if (query) {
        // Set the search-box's value to the query.
        searchBox.value = query;
        // Update the page title to include the query.
        document.title = query + " - Pulumi";
        // Kick-off the search by sending a message to the worker.
        worker.postMessage({ type: "search", payload: query });
    } else {
        // If no query, display empty results.
        displaySearchResults([]);
    }

    // Extracts a query string variable from the browser's location.
    function getQueryVariable(variable) {
        var query = window.location.search.substring(1);
        var vars = query.split("&");

        for (var i = 0; i < vars.length; i++) {
            var pair = vars[i].split("=");

            if (pair[0] === variable) {
                return decodeURIComponent(pair[1].replace(/\+/g, "%20"));
            }
        }
    }

    // Display the results of the search.
    function displaySearchResults(results) {
        // Hide the spinner.
        spinner.style.display = "none";

        if (results.length) {
            // Group the results by category.
            var categoryMap = {};
            for (var i = 0; i < results.length; i++) {
                var result = results[i];
                var categoryName = getCategoryName(result.url);
                var category = categoryMap[categoryName] = categoryMap[categoryName] || [];
                prepareResult(result, categoryName);
                category.push(result);
            }

            // Build up the HTML to display.
            var appendString = "";
            for (var i = 0; i < categories.length; i++) {
                var categoryName = categories[i].name;
                var category = categoryMap[categoryName];
                if (category && category.length > 0) {
                    appendString += buildCategoryString(categoryName, category);
                }
            }
            searchResultsContainer.innerHTML = appendString;
        } else {
            searchResultsContainer.innerHTML = "<p>No results found.</p>";
        }
    }

    var defaultCategory = "Other";
    var categories = [
        {
            name: "APIs",
            predicate: function (url) {
                return url.startsWith("/reference/pkg/");
            }
        },
        {
            name: "CLI",
            predicate: function (url) {
                return url.startsWith("/reference/cli/") || url === "/reference/commands/";
            }
        },
        {
            name: "Tutorials",
            predicate: function (url) {
                return url.startsWith("/quickstart/");
            }
        },
        {
            name: defaultCategory,
            predicate: function (url) {
                return true;
            }
        },
    ];

    function getCategoryName(url) {
        for (var i = 0; i < categories.length; i++) {
            var category = categories[i];
            if (category.predicate(url)) {
                return category.name;
            }
        }
        return defaultCategory;
    }

    function prepareResult(result, categoryName) {
        switch (categoryName) {
            case "APIs":
                if (result.title.startsWith("Module ")) {
                    result.display = result.title.substring("Module ".length);
                    result.type = "module";
                    return;
                } else if (result.title.startsWith("Package ")) {
                    result.display = result.title.substring("Package ".length);
                    result.type = "package";
                    return;
                }
                break;

            case "CLI":
                if (result.title.length === 0 && result.url.startsWith("/reference/cli/")) {
                    var regex = /\/reference\/cli\/([a-z_]+)/gm;
                    var match = regex.exec(result.url)
                    if (match !== null) {
                        result.display = match[1].replace(/_/g, " ");
                        return;
                    }
                }
                break;
        }

        result.display = result.title || result.url;
    }

    function buildCategoryString(categoryName, category) {
        var appendString = "<div class='search-results'><h3>" + categoryName + " (" + category.length + ")</h3>";

        // Display the top 5 results first.
        appendString += "<ul>";
        var topResults = category.splice(0, 5);
        for (var i = 0; i < topResults.length; i++) {
            var item = topResults[i];
            var prefix = getPrefix(item, categoryName);
            appendString += "<li class='top'><a href='" + item.url + "'>" + prefix + item.display + "</a>";
        }
        appendString += "</ul>";

        // Now display any remaining results, sorted alphabetically.
        if (category.length > 0) {
            category.sort(function (l, r) {
                return l.display.toUpperCase() > r.display.toUpperCase() ? 1 : -1;
            });
            appendString += "<ul>";
            for (var i = 0; i < category.length; i++) {
                var item = category[i];
                var prefix = getPrefix(item, categoryName);
                appendString += "<li><a href='" + item.url + "'>" + prefix + item.display + "</a>";
            }
            appendString += "</ul>";
        }

        appendString += "</div>";
        return appendString;
    }

    function getPrefix(result, categoryName) {
        if (result.type) {
            switch (result.type) {
                case "module":
                    return "<span class='symbol module'></span>";
                case "package":
                    return "<span class='symbol package'></span>"
            }
        }

        return "";
    }
})();
