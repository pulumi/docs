import { ConsentManagerConfig, Destination } from "./types";
import { inEU } from "./eu-detection";
import { getPreferences, savePreferences } from "./cookies";
import { fetchDestinations, conditionallyLoadAnalytics } from "./analytics";
import { renderBanner, renderPreferencesDialog } from "./banner";
import { getUserInfo } from "./user";

let container: HTMLElement | null = null;
let destinations: Destination[] = [];
let isConsentRequired = false;
let config: ConsentManagerConfig;

function clearContainer() {
    if (container) container.innerHTML = "";
}

// Identifies the signed-in user to Segment. Queued on the analytics stub, so
// it stays consent-gated: only flushed once analytics actually loads.
function identifyUser(extraTraits: Record<string, unknown> = {}) {
    if (!window.analytics) return;
    const user = getUserInfo();
    const traits = { ...(user ? user.traits : {}), ...extraTraits };
    if (user) {
        window.analytics.identify(user.userId, traits);
    } else if (Object.keys(traits).length > 0) {
        window.analytics.identify(traits);
    }
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

    identifyUser({ destinationTrackingPreferences: destinationPreferences });
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

    isConsentRequired = inEU();

    let fetchedDestinations: Destination[] = [];
    try {
        fetchedDestinations = await fetchDestinations(config.cdnHost, config.writeKey);
    } catch (e) {
        console.warn("Consent manager: failed to fetch destinations", e);
    }
    destinations = fetchedDestinations;

    const { destinationPreferences } = getPreferences();

    conditionallyLoadAnalytics(config.writeKey, destinations, destinationPreferences, isConsentRequired);

    identifyUser();

    if (isConsentRequired && !destinationPreferences) {
        showBanner();
    }
}

init();
