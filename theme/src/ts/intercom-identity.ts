// Identifies signed-in Pulumi Cloud users to the Intercom Messenger with a
// backend-signed Messenger Security JWT fetched from app.pulumi.com. Rides the
// consent-managed Segment lifecycle (analytics.ready, same as the head
// partial's ad pixel): anonymous or non-consented visitors cost zero requests.
// Segment boots the widget as usual — this only attaches (or clears) verified
// identity.

// Local docs dev (make serve) pairs with a local console (devtool.py start);
// everywhere else the console lives at app.pulumi.com.
const APP_HOST = location.hostname === "localhost" ? "http://localhost:3000" : "https://app.pulumi.com";
const SETTINGS_PATH = "/intercom/web-settings";
// Also parsed by layouts/partials/head.html (is-signed-in class) and
// theme/stencil/src/store/reducers/user.ts — keep the three in sync.
const HINT_COOKIE = "pulumi_web_user_info";
const JWT_CACHE_KEY = "pulumi_intercom_jwt";
const IDENTIFIED_KEY = "pulumi_intercom_identified";
const REFRESH_HEADROOM_MS = 5 * 60 * 1000;

type IntercomFn = (command: string, arg?: unknown) => void;

// The JWT is opaque to this module; freshness comes from the endpoint's
// expiresAt (unix seconds), stored alongside the token.
interface CachedJwt {
    jwt: string;
    expiresAtMs: number;
}

function hasHintCookie(): boolean {
    return document.cookie.split(";").some(c => c.trim().indexOf(`${HINT_COOKIE}=`) === 0);
}

function identify(intercom: IntercomFn, jwt: string): void {
    intercom("update", { intercom_user_jwt: jwt });
    try {
        localStorage.setItem(IDENTIFIED_KEY, "1");
    } catch (e) {
        // Storage unavailable: identity still attaches for this page view.
    }
}

function signedOutCleanup(intercom: IntercomFn): void {
    let wasIdentified = false;
    try {
        wasIdentified = localStorage.getItem(IDENTIFIED_KEY) === "1";
        localStorage.removeItem(IDENTIFIED_KEY);
        sessionStorage.removeItem(JWT_CACHE_KEY);
    } catch (e) {
        // Storage unavailable: nothing to clean up.
    }
    if (wasIdentified) {
        intercom("shutdown");
    }
}

function cachedJwt(): string | null {
    try {
        const raw = sessionStorage.getItem(JWT_CACHE_KEY);
        if (raw) {
            const cached = JSON.parse(raw) as CachedJwt;
            if (cached.jwt && cached.expiresAtMs - Date.now() > REFRESH_HEADROOM_MS) {
                return cached.jwt;
            }
        }
    } catch (e) {
        // Storage unavailable or stale cache shape: fall through to a fresh fetch.
    }
    return null;
}

function cacheJwt(jwt: string, expiresAtSec: number): void {
    try {
        const cached: CachedJwt = { jwt, expiresAtMs: expiresAtSec * 1000 };
        sessionStorage.setItem(JWT_CACHE_KEY, JSON.stringify(cached));
    } catch (e) {
        // Storage unavailable: skip caching, identify anyway.
    }
}

function run(intercom: IntercomFn): void {
    // The hint cookie only decides whether to attempt the fetch; the 401
    // below is the authoritative signed-out signal.
    if (!hasHintCookie()) {
        signedOutCleanup(intercom);
        return;
    }

    const jwt = cachedJwt();
    if (jwt) {
        identify(intercom, jwt);
        return;
    }

    fetch(APP_HOST + SETTINGS_PATH, { credentials: "include" })
        .then(resp => {
            if (resp.status === 401) {
                signedOutCleanup(intercom);
                return null;
            }
            if (!resp.ok) {
                return null; // Not configured / upstream issue: stay anonymous.
            }
            return resp.json() as Promise<{ userJwt?: string; expiresAt?: number }>;
        })
        .then(body => {
            if (body && body.userJwt) {
                if (body.expiresAt) {
                    cacheJwt(body.userJwt, body.expiresAt);
                }
                identify(intercom, body.userJwt);
            }
        })
        .catch(() => {
            // Network failure: stay anonymous, no user-visible error.
        });
}

// analytics.ready fires only after the consent-managed Segment load completes
// (see conditionallyLoadAnalytics), which is already deferred to browser idle —
// same fail-closed rendezvous the head partial's ad pixel uses. Intercom can
// still be absent (destination disabled or not consented): one direct check,
// no polling.
const analytics = window.analytics;
if (analytics && typeof analytics.ready === "function") {
    analytics.ready(() => {
        const intercom = (window as { Intercom?: unknown }).Intercom;
        if (typeof intercom === "function") {
            run(intercom as IntercomFn);
        }
    });
}
