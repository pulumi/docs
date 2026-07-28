// Identifies signed-in Pulumi Cloud users to the Intercom Messenger with a
// backend-signed Messenger Security JWT fetched from app.pulumi.com. Runs at
// browser idle on every page load; anonymous visitors are untouched. Segment
// boots the widget as usual — this only attaches (or clears) verified identity.

// Local docs dev (make serve) pairs with a local console (devtool.py start);
// everywhere else the console lives at app.pulumi.com.
const APP_HOST = location.hostname === "localhost" ? "http://localhost:3000" : "https://app.pulumi.com";
const SETTINGS_PATH = "/intercom/web-settings";
const HINT_COOKIE = "pulumi_web_user_info";
const JWT_CACHE_KEY = "pulumi_intercom_jwt";
const IDENTIFIED_KEY = "pulumi_intercom_identified";
const EXP_HEADROOM_MS = 5 * 60 * 1000;
const INTERCOM_WAIT_MS = 250;
const INTERCOM_WAIT_TRIES = 80; // ~20s total

type IntercomFn = (command: string, arg?: unknown) => void;

function getIntercom(): IntercomFn | undefined {
    const intercom = (window as { Intercom?: unknown }).Intercom;
    return typeof intercom === "function" ? (intercom as IntercomFn) : undefined;
}

function hasHintCookie(): boolean {
    return document.cookie.split(";").some(c => c.trim().indexOf(`${HINT_COOKIE}=`) === 0);
}

function jwtExpMs(jwt: string): number {
    try {
        const payload = jwt.split(".")[1].replace(/-/g, "+").replace(/_/g, "/");
        return (JSON.parse(atob(payload)) as { exp: number }).exp * 1000;
    } catch (e) {
        return 0;
    }
}

function withIntercom(fn: (intercom: IntercomFn) => void, tries: number): void {
    const intercom = getIntercom();
    if (intercom) {
        fn(intercom);
        return;
    }
    if (tries <= 0) {
        return;
    }
    setTimeout(() => withIntercom(fn, tries - 1), INTERCOM_WAIT_MS);
}

function identify(jwt: string): void {
    withIntercom(intercom => {
        intercom("update", { intercom_user_jwt: jwt });
        try {
            localStorage.setItem(IDENTIFIED_KEY, "1");
        } catch (e) {
            // Storage unavailable: identity still attaches for this page view.
        }
    }, INTERCOM_WAIT_TRIES);
}

function signedOutCleanup(): void {
    let wasIdentified = false;
    try {
        wasIdentified = localStorage.getItem(IDENTIFIED_KEY) === "1";
        localStorage.removeItem(IDENTIFIED_KEY);
        sessionStorage.removeItem(JWT_CACHE_KEY);
    } catch (e) {
        // Storage unavailable: nothing to clean up.
    }
    if (wasIdentified) {
        withIntercom(intercom => intercom("shutdown"), INTERCOM_WAIT_TRIES);
    }
}

function cachedJwt(): string | null {
    try {
        const jwt = sessionStorage.getItem(JWT_CACHE_KEY);
        if (jwt && jwtExpMs(jwt) - Date.now() > EXP_HEADROOM_MS) {
            return jwt;
        }
    } catch (e) {
        // Storage unavailable: fall through to a fresh fetch.
    }
    return null;
}

function run(): void {
    // The hint cookie only decides whether to attempt the fetch; the 401
    // below is the authoritative signed-out signal.
    if (!hasHintCookie()) {
        signedOutCleanup();
        return;
    }

    const jwt = cachedJwt();
    if (jwt) {
        identify(jwt);
        return;
    }

    fetch(APP_HOST + SETTINGS_PATH, { credentials: "include" })
        .then(resp => {
            if (resp.status === 401) {
                signedOutCleanup();
                return null;
            }
            if (!resp.ok) {
                return null; // Not configured / upstream issue: stay anonymous.
            }
            return resp.json() as Promise<{ userJwt?: string }>;
        })
        .then(body => {
            if (body && body.userJwt) {
                try {
                    sessionStorage.setItem(JWT_CACHE_KEY, body.userJwt);
                } catch (e) {
                    // Storage unavailable: skip caching, identify anyway.
                }
                identify(body.userJwt);
            }
        })
        .catch(() => {
            // Network failure: stay anonymous, no user-visible error.
        });
}

if ("requestIdleCallback" in window) {
    requestIdleCallback(run, { timeout: 5000 });
} else {
    setTimeout(run, 1500);
}
