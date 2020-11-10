import * as uuid from "uuid";

// Extracts a query string variable from the browser's location.
export function getQueryVariable(paramKey) :string {
    const query = window.location.search.substring(1);
    const vars = query.split("&");

    let paramVal = null
    vars.forEach( v => {
        const pair = v.split("=");
        if (pair[0] === paramKey) {
            paramVal = decodeURIComponent(pair[1].replace(/\+/g, "%20"));
        }
    })
    return paramVal;
}

export function getUUID() {
    return uuid.v4();
}

// waitForWindowPropertyToExist waits for a property to exist on the global window
// variable.
export function waitForWindowPropertyToExist(key: string, timeout: number = 3000) {
    return new Promise((resolve, reject) => {
        const property = window[key];

        // If the property exists lets return it.
        if (property) {
            return resolve(property);
        }

        // Poll for the element to exist.
        const interval = setInterval(() => {
            const intervalProperty = window[key];
            // If the element exists lets return it.
            if (intervalProperty) {
                clearInterval(interval);
                return resolve(intervalProperty);
            }
        }, 50);

        // Timeout the function and clear the interval.
        setTimeout(() => {
            clearInterval(interval);
            return reject(new Error(`The provided key [${key}] didn't propogate after ${timeout}ms.`));
        }, timeout);
    });
}
