// Identifies signed-in Pulumi Cloud users to the Intercom Messenger with a
// backend-signed Messenger Security JWT fetched from app.pulumi.com. Rides the
// consent-managed Segment lifecycle (analytics.ready, same as the head
// partial's ad pixel): anonymous or non-consented visitors cost zero requests.
// Segment boots the widget as usual — this attaches (or clears) verified
// identity and drops Segment's stale persisted user.

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
// Segment's persisted user outlives the console session, and its device-mode
// Intercom destination pushes the stale id into the Messenger unsigned,
// colliding with JWT-verified identities ("User ID mismatch" errors).
const SEGMENT_USER_ID_KEY = "ajs_user_id";
// ajs_anonymous_id is deliberately absent: pre-signup tracking depends on it.
const SEGMENT_USER_KEYS = [SEGMENT_USER_ID_KEY, "ajs_user_traits"];

type IntercomFn = (command: string, arg?: unknown) => void;

// The analytics.js global is untyped; cross the `any` boundary in one place.
function segmentAnalytics(): { ready?(cb: () => void): void; user?(): { id(value: string | null): void } } | undefined {
    return (window as any).analytics;
}

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

function cookieValue(name: string): string | null {
    for (const entry of document.cookie.split(";")) {
        const idx = entry.indexOf("=");
        if (idx !== -1 && entry.slice(0, idx).trim() === name) {
            try {
                return decodeURIComponent(entry.slice(idx + 1).trim());
            } catch (e) {
                return null;
            }
        }
    }
    return null;
}

// Mirrors theme/stencil/src/store/reducers/user.ts's getUserInfoCookie —
// keep the parsing logic in sync.
function hintUserId(): string | null {
    const raw = cookieValue(HINT_COOKIE);
    if (raw === null) {
        return null;
    }
    try {
        const parsed = JSON.parse(raw.replace(/^j:/, "")) as { userId?: string };
        return typeof parsed.userId === "string" && parsed.userId ? parsed.userId : null;
    } catch (e) {
        return null;
    }
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

// A shutdown earlier in this page view unloaded the messenger, so "update" has
// nothing left to attach to — Intercom needs a fresh boot to start the next
// session.
function identify(intercom: IntercomFn, jwt: string, userId: string, bootAppId?: string): void {
    if (bootAppId) {
        intercom("boot", { app_id: bootAppId, intercom_user_jwt: jwt });
    } else {
        intercom("update", { intercom_user_jwt: jwt });
    }
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

// analytics.js persists each value in localStorage with an apex-domain cookie
// mirror, and reads localStorage first; mirror that read order here.
function segmentValue(key: string): string | null {
    let raw: string | null = null;
    try {
        raw = localStorage.getItem(key);
    } catch (e) {
        // Storage unavailable: the cookie fallback below still applies.
    }
    return raw !== null ? raw : cookieValue(key);
}

// Gate on the id key only: a traits-only identify (the consent manager's
// destinationTrackingPreferences) persists ajs_user_traits for visitors who
// never signed in, and there's no id to collide without ajs_user_id.
function hasSegmentUser(): boolean {
    return segmentValue(SEGMENT_USER_ID_KEY) !== null;
}

// analytics.js persists values JSON-encoded; tolerate bare strings too.
function decodeSegmentValue(raw: string): string | null {
    try {
        const parsed = JSON.parse(raw) as unknown;
        return typeof parsed === "string" && parsed ? parsed : null;
    } catch (e) {
        return raw ? raw : null;
    }
}

function segmentUserId(): string | null {
    const raw = segmentValue(SEGMENT_USER_ID_KEY);
    return raw === null ? null : decodeSegmentValue(raw);
}

function segmentUserIsStale(): boolean {
    const sessionUserId = hintUserId();
    if (!sessionUserId) {
        return hasSegmentUser();
    }
    // An account switch rewrites the apex cookie but not this origin's
    // localStorage copy, which analytics.js reads first.
    const segmentId = segmentUserId();
    return segmentId !== null && segmentId !== sessionUserId;
}

// Deletion only takes with a matching domain attribute, so expire both the
// host-only and the apex-domain variant (Segment writes the latter).
function expireCookie(name: string): void {
    const expired = name + "=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/";
    document.cookie = expired;
    const labels = location.hostname.split(".");
    if (labels.length > 1) {
        document.cookie = expired + "; domain=." + labels.slice(-2).join(".");
    }
}

function clearSegmentUser(): void {
    // An already-loaded analytics.js (the 401 path) holds the user in memory,
    // and its stores persist id(null) as a literal "null" — reset first so the
    // storage clear below removes that write too.
    try {
        const analytics = segmentAnalytics();
        if (analytics && typeof analytics.user === "function") {
            analytics.user().id(null);
        }
    } catch (e) {
        // Best effort: the storage clear below is the real cleanup.
    }
    for (const key of SEGMENT_USER_KEYS) {
        try {
            localStorage.removeItem(key);
        } catch (e) {
            // Storage unavailable: the cookie expiry below still applies.
        }
        expireCookie(key);
    }
}

function signedOutCleanup(intercom: IntercomFn): void {
    const wasIdentified = identifiedUser() !== null;
    clearCaches();
    // The 401 is the staleness proof here; the hint cookie may still match.
    if (hasSegmentUser()) {
        clearSegmentUser();
    }
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
    let switched = false;
    if (previouslyIdentified && previouslyIdentified.userId !== userId) {
        // A different Pulumi Cloud user is now encoded in the hint cookie
        // (shared/kiosk machine, or an account switch that never left the
        // hint cookie absent during a page load here). Shut down the stale
        // identity — and drop any cached JWT for the old user — before
        // attaching the new one, so the Messenger never mixes conversation
        // histories across accounts.
        clearCaches();
        intercom("shutdown");
        switched = true;
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
            return resp.json() as Promise<{ appId?: string; userJwt?: string; expiresAt?: number }>;
        })
        .then(body => {
            if (body && body.userJwt) {
                if (body.expiresAt) {
                    cacheJwt(body.userJwt, body.expiresAt, userId);
                }
                identify(intercom, body.userJwt, userId, switched ? body.appId : undefined);
            }
        })
        .catch(() => {
            // Network failure: stay anonymous, no user-visible error.
        });
}

// Runs at module evaluation, before the consent manager loads analytics.js —
// the stale user is gone before Segment's Intercom destination can push it.
if (segmentUserIsStale()) {
    clearSegmentUser();
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
    if (typeof (window as { Intercom?: unknown }).Intercom !== "function") {
        return;
    }
    ran = true;
    // Intercom's loader replaces window.Intercom (pre-boot queue stub -> real
    // widget) moments after boot, discarding the stub's queue as it goes. A
    // reference captured before that swap is dead by the time the awaited
    // settings fetch resolves, and calling it throws, so resolve the global on
    // every call rather than holding one.
    run((cmd, arg) => (window as unknown as { Intercom: IntercomFn }).Intercom(cmd, arg));
}

const analytics = segmentAnalytics();
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
