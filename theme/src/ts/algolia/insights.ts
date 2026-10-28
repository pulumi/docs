// Algolia search analytics (the "viewed" and "clicked" events Autocomplete sends
// to insights.algolia.io) is Performance tracking, so it waits for C0002. Until
// then, setup calls are queued and events are dropped; search itself doesn't
// depend on it. Under the Segment provider runWithPulumiConsent runs right away,
// so behavior there is unchanged.

type InsightsClient = ((...args: any[]) => unknown) & { version?: string };

const EVENT_METHOD = /ObjectIDs|Filters|sendEvents/;

export function createConsentGatedInsightsClient(client: InsightsClient): InsightsClient {
    let allowed = false;
    const queue: unknown[][] = [];

    const gated: InsightsClient = (method, ...args) => {
        if (allowed) return client(method, ...args);
        if (!EVENT_METHOD.test(method)) queue.push([method, ...args]);
    };
    // Autocomplete reads the version to decide how to pass credentials.
    gated.version = client.version;

    (window as any).runWithPulumiConsent("C0002", () => {
        allowed = true;
        for (const [method, ...args] of queue.splice(0)) client(method as string, ...args);
    });

    return gated;
}
