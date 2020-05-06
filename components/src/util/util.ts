


// Extracts a query string variable from the browser's location.
export function getQueryVariable(variable) {
    var query = window.location.search.substring(1);
    var vars = query.split("&");

    for (var i = 0; i < vars.length; i++) {
        var pair = vars[i].split("=");

        if (pair[0] === variable) {
            return decodeURIComponent(pair[1].replace(/\+/g, "%20"));
        }
    }
}