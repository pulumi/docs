import { Destination } from "./types";
import { segmentIntegrations, wantsSegment } from "./onetrust";

export function fetchDestinations(cdnHost: string, writeKey: string): Promise<Destination[]> {
    return fetch(`https://${cdnHost}/v1/projects/${writeKey}/integrations`)
        .then((res) => {
            if (!res.ok) throw new Error(`Failed to fetch integrations: HTTP ${res.status}`);
            return res.json();
        })
        .then((integrations: { name: string; creationName: string; category?: string }[]) => {
            return integrations
                .map((i) => ({
                    id: i.name === "Fullstory" ? i.name : i.creationName,
                    name: i.name,
                    category: i.category,
                }))
                .filter((d) => d.id !== "Repeater");
        });
}

export function conditionallyLoadAnalytics(
    writeKey: string,
    destinations: Destination[],
    destinationPreferences: Record<string, boolean>,
    performanceAllowed: boolean,
): boolean {
    const analytics = window.analytics;
    if (!analytics) return false;

    const integrations = segmentIntegrations(destinations, destinationPreferences, performanceAllowed);
    const hasConsented = wantsSegment(integrations);

    if (hasConsented && !analytics.initialized) {
        analytics.addSourceMiddleware((args) => {
            args.payload.obj.context.consent = {
                defaultDestinationBehavior: "disable",
                destinationPreferences: destinationPreferences,
            };
            args.next(args.payload);
        });
        const load = () => analytics.load(writeKey, { integrations });
        if ("requestIdleCallback" in window) {
            requestIdleCallback(load);
        } else {
            load();
        }
    }
    return hasConsented;
}
