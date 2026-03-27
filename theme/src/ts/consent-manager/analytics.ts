import { Destination } from "./types";

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
    destinationPreferences: Record<string, boolean> | undefined,
    isConsentRequired: boolean,
    categoryPreferences?: Record<string, boolean | null>,
): void {
    const analytics = window.analytics;
    if (!analytics) return;

    if (destinationPreferences) {
        const integrations: Record<string, boolean> = { All: false, "Segment.io": true };
        let hasConsented = false;

        for (const dest of destinations) {
            const allowed = Boolean(destinationPreferences[dest.id]);
            if (allowed) hasConsented = true;
            integrations[dest.id] = allowed;
        }

        if (hasConsented && !analytics.initialized) {
            analytics.addSourceMiddleware((args) => {
                args.payload.obj.context.consent = {
                    defaultDestinationBehavior: "disable",
                    categoryPreferences: categoryPreferences,
                    destinationPreferences: destinationPreferences,
                };
                args.next(args.payload);
            });
            analytics.load(writeKey, { integrations });
        }
    } else {
        if (isConsentRequired) return;
        if (!analytics.initialized) {
            analytics.load(writeKey);
        }
    }
}
