import { ConsentManagerConfig, Destination } from "./types";
import { getPreferences, savePreferences } from "./cookies";
import { fetchDestinations, conditionallyLoadAnalytics } from "./analytics";
import { renderBanner, renderPreferencesDialog } from "./banner";
import { installOneTrustBridge, getActiveGroups, destinationPreferencesFromGroups, hasRevokedGroup } from "./onetrust";

let container: HTMLElement | null = null;
let destinations: Destination[] = [];
let isConsentRequired = false;
let config: ConsentManagerConfig;

function clearContainer() {
    if (container) container.innerHTML = "";
}

function showBanner() {
    clearContainer();
    if (!container) return;
    const banner = renderBanner(
        config,
        () => handleConsentChoice(true),
        () => handleConsentChoice(false),
        showPreferences,
    );
    container.appendChild(banner);
}

function showPreferences() {
    const { destinationPreferences } = getPreferences();
    const current: Record<string, boolean> = {};
    for (const dest of destinations) {
        current[dest.id] = destinationPreferences ? destinationPreferences[dest.id] !== false : true;
    }

    const dialog = renderPreferencesDialog(
        config,
        destinations,
        current,
        prefs => {
            saveAndLoad(prefs);
            if (dialog.parentNode) dialog.parentNode.removeChild(dialog);
        },
        () => {
            if (dialog.parentNode) dialog.parentNode.removeChild(dialog);
        },
    );
    document.body.appendChild(dialog);
}

function handleConsentChoice(acceptAll: boolean) {
    const prefs: Record<string, boolean> = {};
    for (const dest of destinations) {
        prefs[dest.id] = acceptAll;
    }
    saveAndLoad(prefs);
}

function saveAndLoad(destinationPreferences: Record<string, boolean>) {
    savePreferences(destinationPreferences);
    clearContainer();

    conditionallyLoadAnalytics(config.writeKey, destinations, destinationPreferences, isConsentRequired);

    if (window.analytics) {
        window.analytics.identify({
            destinationTrackingPreferences: destinationPreferences,
        });
    }
}

function openConsentManager() {
    showPreferences();
}

async function init() {
    config = window.consentManagerConfig as ConsentManagerConfig;
    if (!config || !config.writeKey || !config.container) return;

    container = document.querySelector(config.container);
    if (!container) return;

    window.consentManager = { openConsentManager };

    isConsentRequired = true;

    let fetchedDestinations: Destination[] = [];
    try {
        fetchedDestinations = await fetchDestinations(config.cdnHost, config.writeKey);
    } catch (e) {
        console.warn("Consent manager: failed to fetch destinations", e);
    }
    destinations = fetchedDestinations;

    const { destinationPreferences } = getPreferences();

    conditionallyLoadAnalytics(config.writeKey, destinations, destinationPreferences, isConsentRequired);

    if (isConsentRequired && !destinationPreferences) {
        showBanner();
    }
}

// OneTrust path: OneTrust owns the banner and the consent decision. We install
// the runWithPulumiConsent bridge (for directly-loaded integrations) and drive
// the existing Segment loader from the OneTrust categories instead of the
// custom banner/cookie.
async function initOneTrust(cfg: ConsentManagerConfig) {
    installOneTrustBridge();

    // The Cookie Settings control in the footer calls this; open the OneTrust
    // preference center rather than the custom dialog.
    window.consentManager = {
        openConsentManager: () => window.OneTrust?.ToggleInfoDisplay?.(),
    };

    // Revoking a category can't unload third-party code that already started, so
    // reload when one is withdrawn. Only a withdrawal reloads: OneTrust also fires
    // this event on page load and for grants, and reloading on those would loop.
    let seenGroups = getActiveGroups();
    window.addEventListener("OneTrustGroupsUpdated", () => {
        const active = getActiveGroups();
        if (hasRevokedGroup(seenGroups, active)) {
            window.location.reload();
            return;
        }
        seenGroups = active;
    });

    if (!cfg.writeKey || !cfg.cdnHost) {
        // No Segment config: the bridge still gates direct integrations.
        return;
    }

    let fetchedDestinations: Destination[] = [];
    try {
        fetchedDestinations = await fetchDestinations(cfg.cdnHost, cfg.writeKey);
    } catch (e) {
        console.warn("Consent manager: failed to fetch destinations", e);
    }

    // Segment can only be loaded once per page, so the first decision that
    // allows any destination wins. Destinations granted later on this page take
    // effect from the next page view.
    let segmentLoaded = false;
    const loadSegment = () => {
        if (segmentLoaded) return;
        const prefs = destinationPreferencesFromGroups(fetchedDestinations, getActiveGroups());
        conditionallyLoadAnalytics(cfg.writeKey, fetchedDestinations, prefs, true);
        segmentLoaded = Object.keys(prefs).some(id => prefs[id]);
    };

    window.addEventListener("OneTrustGroupsUpdated", loadSegment);
    // Catch a decision OneTrust may already have resolved before this ran.
    loadSegment();
}

const activeConfig = window.consentManagerConfig as ConsentManagerConfig;
if (activeConfig && activeConfig.provider === "onetrust") {
    initOneTrust(activeConfig);
} else {
    init();
}
