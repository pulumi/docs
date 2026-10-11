import { TrackingPreferences } from "./types";

const COOKIE_NAME = "tracking-preferences";
const COOKIE_EXPIRY_DAYS = 365;

function getTopDomain(): string {
    const parts = window.location.hostname.split(".");
    if (parts.length <= 1) return "";
    for (let i = parts.length - 2; i >= 0; i--) {
        const domain = "." + parts.slice(i).join(".");
        document.cookie = `__tld__=1;domain=${domain};path=/;SameSite=Lax;Secure`;
        if (document.cookie.indexOf("__tld__") >= 0) {
            document.cookie = `__tld__=;domain=${domain};path=/;expires=Thu, 01 Jan 1970 00:00:00 GMT;SameSite=Lax;Secure`;
            return domain;
        }
    }
    return "";
}

export function getPreferences(): { destinationPreferences?: Record<string, boolean>; customPreferences?: Record<string, boolean | null> } {
    try {
        const cookies = document.cookie.split("; ");
        for (const cookie of cookies) {
            const [name, ...rest] = cookie.split("=");
            if (name === COOKIE_NAME) {
                const value = decodeURIComponent(rest.join("="));
                const parsed: TrackingPreferences = JSON.parse(value);
                return {
                    destinationPreferences: parsed.destinations,
                    customPreferences: parsed.custom,
                };
            }
        }
    } catch {}
    return {};
}

export function savePreferences(
    destinationPreferences: Record<string, boolean>,
    customPreferences?: Record<string, boolean | null>,
): void {
    const domain = getTopDomain();
    const data: TrackingPreferences = {
        version: 1,
        destinations: destinationPreferences,
        custom: customPreferences,
    };
    const expires = new Date();
    expires.setDate(expires.getDate() + COOKIE_EXPIRY_DAYS);
    let cookieStr = `${COOKIE_NAME}=${encodeURIComponent(JSON.stringify(data))}`;
    cookieStr += `;expires=${expires.toUTCString()}`;
    cookieStr += ";path=/";
    if (domain) {
        cookieStr += `;domain=${domain}`;
    }
    cookieStr += ";SameSite=Lax;Secure";
    document.cookie = cookieStr;
}
