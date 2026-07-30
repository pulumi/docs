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
// expiresAt (unix seconds). Both the cache and the "already identified"
// marker also carry the userId encoded in the hint cookie at the time they
// were written, so a cache/identification left behind by a previous Pulumi
// Cloud user (shared machine, account switch) is never reused for a
// different signed-in user.
interface CachedJwt {
    jwt: string;
    expiresAtMs: number;
    userId: string;
}

interface IdentifiedUser {
    userId: string;
}

// Mirrors theme/stencil/src/store/reducers/user.ts's getUserInfoCookie —
// keep the parsing logic in sync.
function hintUserId(): string | null {
    for (const entry of document.cookie.split(";")) {
        const idx = entry.indexOf("=");
        if (idx === -1) {
            continue;
        }
        if (entry.slice(0, idx).trim() !== HINT_COOKIE) {
            continue;
        }
        try {
            const parsed = JSON.parse(decodeURIComponent(entry.slice(idx + 1).trim()).replace(/^j:/, "")) as {
                userId?: string;
            };
            return typeof parsed.userId === "string" && parsed.userId ? parsed.userId : null;
        } catch (e) {
            return null;
        }
    }
    return null;
}

function identifiedUser(): IdentifiedUser | null {
    try {
        const raw = localStorage.getItem(IDENTIFIED_KEY);
        if (raw) {
            const parsed = JSON.parse(raw) as IdentifiedUser;
            if (parsed.userId) {
                return parsed;
            }
        }
    } catch (e) {
        // Storage unavailable or stale shape: treat as not identified.
    }
    return null;
}

function identify(intercom: IntercomFn, jwt: string, userId: string): void {
    intercom("update", { intercom_user_jwt: jwt });
    try {
        localStorage.setItem(IDENTIFIED_KEY, JSON.stringify({ userId }));
    } catch (e) {
        // Storage unavailable: identity still attaches for this page view.
    }
}

function clearCaches(): void {
    try {
        localStorage.removeItem(IDENTIFIED_KEY);
        sessionStorage.removeItem(JWT_CACHE_KEY);
    } catch (e) {
        // Storage unavailable: nothing to clean up.
    }
}

function signedOutCleanup(intercom: IntercomFn): void {
    const wasIdentified = identifiedUser() !== null;
    clearCaches();
    if (wasIdentified) {
        intercom("shutdown");
    }
}

function cachedJwt(userId: string): string | null {
    try {
        const raw = sessionStorage.getItem(JWT_CACHE_KEY);
        if (raw) {
            const cached = JSON.parse(raw) as CachedJwt;
            if (cached.jwt && cached.userId === userId && cached.expiresAtMs - Date.now() > REFRESH_HEADROOM_MS) {
                return cached.jwt;
            }
        }
    } catch (e) {
        // Storage unavailable or stale cache shape: fall through to a fresh fetch.
    }
    return null;
}

function cacheJwt(jwt: string, expiresAtSec: number, userId: string): void {
    try {
        const cached: CachedJwt = { jwt, expiresAtMs: expiresAtSec * 1000, userId };
        sessionStorage.setItem(JWT_CACHE_KEY, JSON.stringify(cached));
    } catch (e) {
        // Storage unavailable: skip caching, identify anyway.
    }
}

function run(intercom: IntercomFn): void {
    // The hint cookie only decides whether to attempt the fetch; the 401
    // below is the authoritative signed-out signal.
    const userId = hintUserId();
    if (!userId) {
        signedOutCleanup(intercom);
        return;
    }

    const previouslyIdentified = identifiedUser();
    if (previouslyIdentified && previouslyIdentified.userId !== userId) {
        // A different Pulumi Cloud user is now encoded in the hint cookie
        // (shared/kiosk machine, or an account switch that never left the
        // hint cookie absent during a page load here). Shut down the stale
        // identity — and drop any cached JWT for the old user — before
        // attaching the new one, so the Messenger never mixes conversation
        // histories across accounts.
        clearCaches();
        intercom("shutdown");
    }

    const jwt = cachedJwt(userId);
    if (jwt) {
        identify(intercom, jwt, userId);
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
                    cacheJwt(body.userJwt, body.expiresAt, userId);
                }
                identify(intercom, body.userJwt, userId);
            }
        })
        .catch(() => {
            // Network failure: stay anonymous, no user-visible error.
        });
}

// analytics.ready fires only after the consent-managed Segment load completes
// (see conditionallyLoadAnalytics), which is already deferred to browser idle —
// same fail-closed rendezvous the head partial's ad pixel uses. But ready()
// never fires if any device-mode destination throws during init, so a slow
// bounded poll for the widget backstops it. The fallback is just as
// fail-closed: window.Intercom only exists when the consented Segment load
// booted the destination.
const POLL_INTERVAL_MS = 5 * 1000;
const POLL_MAX_ATTEMPTS = 12;

let ran = false;
function tryRun(): void {
    if (ran) {
        return;
    }
    const intercom = (window as { Intercom?: unknown }).Intercom;
    if (typeof intercom === "function") {
        ran = true;
        run(intercom as IntercomFn);
    }
}

const analytics = (window as any).analytics;
if (analytics && typeof analytics.ready === "function") {
    analytics.ready(tryRun);
}

let pollAttempts = 0;
const poll = setInterval(() => {
    pollAttempts++;
    tryRun();
    if (ran || pollAttempts >= POLL_MAX_ATTEMPTS) {
        clearInterval(poll);
    }
}, POLL_INTERVAL_MS);
