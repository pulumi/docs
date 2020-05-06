
// Extracts a query string variable from the browser's location.
export function getQueryVariable(paramKey) :string {
    const query = window.location.search.substring(1);
    const vars = query.split("&");

    vars.forEach( v => {
        const pair = v.split("=");
        if (pair[0] === paramKey) {
            return decodeURIComponent(pair[1].replace(/\+/g, "%20"));
        }
    })

    return null;
}
