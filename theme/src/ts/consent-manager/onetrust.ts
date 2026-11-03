// OneTrust consent bridge.
//
// OneTrust owns the visitor's consent decision; this module translates that
// decision into the two things the Pulumi website needs:
//
//   1. runWithPulumiConsent(category, callback) — the single gate every
//      directly-loaded integration (Common Room, OpenAI, Floqer, HubSpot forms,
//      YouTube embeds) calls. It runs the callback once the
//      visitor has allowed the requested OneTrust category, queues it until
//      then, and fails closed (never runs an optional-category callback) when
//      OneTrust is unavailable or consent can't be determined.
//
//   2. destinationPreferencesFromGroups() — maps the active OneTrust categories
//      onto the Segment destinations we already fetch, so the existing Segment
//      loader (analytics.ts) can be driven from the OneTrust decision instead
//      of the custom banner.
//
// The inline bootstrap in layouts/partials/head.html defines a minimal queueing
// runWithPulumiConsent before this bundle loads, so an integration that
// initializes early is captured rather than lost. installOneTrustBridge()
// adopts that queue and takes over execution.
//
// Category reference (configured in OneTrust, not here):
//   C0001 Strictly Necessary — always on, never gated.
//   C0002 Performance
//   C0003 Functional
//   C0004 Targeting

export type ConsentCategory = string;

export const STRICTLY_NECESSARY: ConsentCategory = "C0001";

// Segment destination name -> OneTrust category. Keyed by the destination
// `name` Segment reports (see fetchDestinations in analytics.ts). Any Segment
// destination not listed here defaults to disabled (fail closed). Several
// aliases are included because Segment's display names drift ("Google Ads" vs
// "Google Ads (Gtag)", "Intercom Web Actions" vs "Intercom Web (Actions)").
export const SEGMENT_DESTINATION_CATEGORIES: Record<string, ConsentCategory> = {
    "AWS S3": "C0002",
    "Amazon S3": "C0002",
    "Google Analytics 4": "C0002",
    "Google Analytics 4 Web": "C0002",
    "Intercom": "C0003",
    "Intercom Web Actions": "C0003",
    "Intercom Web (Actions)": "C0003",
    "HubSpot": "C0004",
    "Google Ads": "C0004",
    "Google Ads (Gtag)": "C0004",
    "LinkedIn Insight Tag": "C0004",
};

export function categoryForDestination(name: string): ConsentCategory | null {
    return SEGMENT_DESTINATION_CATEGORIES[name] || null;
}

// Parse OneTrust's active-groups string (e.g. ",C0001,C0003,") into a set of
// category ids. Tolerates the leading/trailing commas OneTrust emits.
export function parseActiveGroups(raw: unknown): Set<string> {
    const groups = new Set<string>();
    if (typeof raw !== "string") {
        return groups;
    }
    for (const part of raw.split(",")) {
        const group = part.trim();
        if (group) {
            groups.add(group);
        }
    }
    return groups;
}

export function getActiveGroups(win: Window = window): Set<string> {
    const w = win as unknown as Record<string, unknown>;
    const raw = typeof w.OnetrustActiveGroups === "string" ? w.OnetrustActiveGroups : w.OptanonActiveGroups;
    return parseActiveGroups(raw);
}

// True once the OneTrust SDK has populated its active-groups global. Until then
// consent is undetermined and optional integrations must stay blocked.
export function isOneTrustAvailable(win: Window = window): boolean {
    const w = win as unknown as Record<string, unknown>;
    return typeof w.OnetrustActiveGroups === "string" || typeof w.OptanonActiveGroups === "string";
}

// True when a category active in `before` is no longer active in `after`.
export function hasRevokedGroup(before: Set<string>, after: Set<string>): boolean {
    return Array.from(before).some(group => !after.has(group));
}

interface MinimalDestination {
    id: string;
    name: string;
}

// Produce the destinationPreferences shape the existing Segment loader expects
// (keyed by destination id), from the active OneTrust categories. Unmapped
// destinations default to disabled.
export function destinationPreferencesFromGroups(destinations: MinimalDestination[], active: Set<string>): Record<string, boolean> {
    const prefs: Record<string, boolean> = {};
    for (const dest of destinations) {
        const category = categoryForDestination(dest.name);
        prefs[dest.id] = category ? active.has(category) : false;
    }
    return prefs;
}

interface QueueItem {
    category: ConsentCategory;
    callback: () => void;
}

// The consent state machine. Kept free of any `window` access so it can be unit
// tested directly; installOneTrustBridge() wires it to the DOM.
export class ConsentEngine {
    private active = new Set<string>();
    private available = false;
    private resolved = false;
    private queue: QueueItem[] = [];
    private ran = new Set<() => void>();

    // Record the latest consent decision and run anything it unblocks.
    setGroups(active: Set<string>, available: boolean): void {
        this.active = active;
        this.available = available;
        this.resolved = true;
        this.drain();
    }

    isActive(category: ConsentCategory): boolean {
        if (category === STRICTLY_NECESSARY) {
            return true;
        }
        // Fail closed: no optional category is active until OneTrust resolves.
        if (!this.available) {
            return false;
        }
        return this.active.has(category);
    }

    // Gate a single integration loader on an OneTrust category. Runs it at most
    // once, immediately if already allowed, otherwise when consent is granted.
    run(category: ConsentCategory, callback: () => void): void {
        if (this.ran.has(callback)) {
            return;
        }
        const runnableNow = this.isActive(category) && (this.resolved || category === STRICTLY_NECESSARY);
        if (runnableNow) {
            this.markAndRun(callback);
            return;
        }
        this.queue.push({ category, callback });
    }

    private drain(): void {
        const pending: QueueItem[] = [];
        for (const item of this.queue) {
            if (this.ran.has(item.callback)) {
                continue;
            }
            if (this.isActive(item.category)) {
                this.markAndRun(item.callback);
            } else {
                pending.push(item);
            }
        }
        this.queue = pending;
    }

    private markAndRun(callback: () => void): void {
        this.ran.add(callback);
        try {
            callback();
        } catch (e) {
            // A failing vendor loader must not take down the consent pipeline or
            // block the other queued integrations.
            console.warn("Consent: integration loader threw", e);
        }
    }
}

// Wire a ConsentEngine to the OneTrust globals and expose runWithPulumiConsent.
// Idempotent-ish: safe to call once per page from the consent-manager bundle.
export function installOneTrustBridge(win: Window = window): ConsentEngine {
    const w = win as unknown as Record<string, unknown>;
    const engine = new ConsentEngine();

    // Take over from the inline bootstrap: replace the queueing stub with the
    // real engine, then replay anything already queued.
    const boot = w.__pulumiConsentQueue as QueueItem[] | undefined;
    w.runWithPulumiConsent = (category: ConsentCategory, callback: () => void) => engine.run(category, callback);
    if (Array.isArray(boot)) {
        for (const item of boot) {
            engine.run(item.category, item.callback);
        }
        w.__pulumiConsentQueue = [];
    }

    const refresh = () => engine.setGroups(getActiveGroups(win), isOneTrustAvailable(win));

    win.addEventListener("OneTrustGroupsUpdated", refresh as EventListener);

    // OneTrust also invokes OptanonWrapper after it loads and on every save;
    // chain onto any existing handler so we refresh there too.
    const priorWrapper = typeof w.OptanonWrapper === "function" ? (w.OptanonWrapper as () => void) : null;
    w.OptanonWrapper = () => {
        if (priorWrapper) {
            priorWrapper();
        }
        refresh();
    };

    // OneTrust may already have resolved by the time this bundle executes.
    refresh();

    return engine;
}
