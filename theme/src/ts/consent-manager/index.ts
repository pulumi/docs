import { ConsentManagerConfig, Destination } from "./types";
import { fetchDestinations, conditionallyLoadAnalytics } from "./analytics";
import { installOneTrustBridge, getActiveGroups, destinationPreferencesFromGroups, hasRevokedGroup, PERFORMANCE } from "./onetrust";

// OneTrust owns the banner and the consent decision. We install the
// runWithPulumiConsent bridge (for directly-loaded integrations) and drive the
// Segment loader from the OneTrust categories.
async function init(cfg: ConsentManagerConfig) {
    installOneTrustBridge();

    // The Cookie Settings control in the footer calls this.
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

    let destinations: Destination[] = [];
    try {
        destinations = await fetchDestinations(cfg.cdnHost, cfg.writeKey);
    } catch (e) {
        console.warn("Consent manager: failed to fetch destinations", e);
    }

    // Segment can only be loaded once per page, so the first decision that
    // allows Segment's own collection or any destination wins. Anything granted
    // later on this page, Segment's collection included, takes effect from the
    // next page view.
    let segmentLoaded = false;
    const loadSegment = () => {
        if (segmentLoaded) return;
        const active = getActiveGroups();
        const prefs = destinationPreferencesFromGroups(destinations, active);
        segmentLoaded = conditionallyLoadAnalytics(cfg.writeKey, destinations, prefs, active.has(PERFORMANCE));
    };

    window.addEventListener("OneTrustGroupsUpdated", loadSegment);
    // Catch a decision OneTrust may already have resolved before this ran.
    loadSegment();
}

init(window.consentManagerConfig as ConsentManagerConfig);
