import * as uuid from "uuid";
import { GrowthBook } from "@growthbook/growthbook";

// Initialize GrowthBook
export const gb = new GrowthBook({
    apiHost: "https://cdn.growthbook.io",
    clientKey: (window as any).growthbook_sdk_key,
    decryptionKey: (window as any).growthbook_decrypt_key,
    enableDevMode: (window as any).growthbook_dev_mode,
});

gb.init({ streaming: true });

// Hook up GrowthBook to analytics when ready
(window as any).analytics.ready(function() {
    gb.setTrackingCallback((experiment, result) => {
        (window as any).analytics.track("Experiment Viewed", {
            experimentId: experiment.key,
            variationId: result.key,
        });
    });

    gb.setAttributes({
    // Set Anon/UserId for GB
    ...gb.getAttributes(),
        id: (window as any).analytics.user().anonymousId(),
        userId: (window as any).analytics.user().id(),
        url: (window as any).location.href,
        path: (window as any).location.pathname,
        query: (window as any).location.search,
        referrer: document.referrer,
        utmCampaign: getQueryVariable("utm_campaign"),
        utmSource: getQueryVariable("utm_source"),
        utmMedium: getQueryVariable("utm_medium"),
        utmTerm: getQueryVariable("utm_term"),
        utmContent: getQueryVariable("utm_content"),
    })
})
    

// Extracts a query string variable from the browser's location.
export function getQueryVariable(paramKey: string): string | null {
    const query = window.location.search.substring(1);
    const vars = query.split("&");

    let paramVal = null;
    vars.forEach(v => {
        const pair = v.split("=");
        if (pair[0] === paramKey) {
            paramVal = decodeURIComponent(pair[1].replace(/\+/g, "%20"));
        }
    });
    return paramVal;
}

export function getUUID() {
    return uuid.v4();
}

// waitForElementToExist waits for an element to exists on the DOM and timesout
// after a set amount of time.
export function waitForElementToExist(selector: string, timeout: number = 3000) {
    return new Promise((resolve, reject) => {
        const element = document.querySelector(selector);

        // If the element exists let's return it.
        if (element) {
            return resolve(element);
        }

        // Poll for the element to exist.
        const interval = setInterval(() => {
            const intervalElement = document.querySelector(selector);
            // If the element exists return it.
            if (intervalElement) {
                clearInterval(interval);
                return resolve(intervalElement);
            }
        }, 100);

        // Timeout the function and clear the interval.
        setTimeout(() => {
            clearInterval(interval);
            return reject(new Error(`The provided selector [${selector}] was not found on the DOM after ${timeout}ms.`));
        }, timeout);
    });
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

        // Poll for the property to exist.
        const interval = setInterval(() => {
            const intervalProperty = window[key];
            // If the property exists lets return it.
            if (intervalProperty) {
                clearInterval(interval);
                return resolve(intervalProperty);
            }
        }, 100);

        // Timeout the function and clear the interval.
        setTimeout(() => {
            clearInterval(interval);
            return reject(new Error(`The provided key [${key}] didn't propogate after ${timeout}ms.`));
        }, timeout);
    });
}

// parseUTMCookieString parses a UTM cookie string and returns an object of the values.
export function parseUTMCookieString(utmCookieString: string) {
    return (utmCookieString || "").split("|").reduce((obj, utm) => {
        const parts = utm.split("=");
        obj[parts[0]] = parts[1];
        return obj;
    }, {});
}

// parseCookie parses the document's cookie into an object.
export function parseCookie(): Record<string, string> {
    return document.cookie.split(";").reduce((obj, cookie) => {
        const index = cookie.indexOf("=");
        const key = cookie.substring(0, index).trim();
        const value = cookie.substring(index + 1).trim();
        obj[key] = value;
        return obj;
    }, {});
}
