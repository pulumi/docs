export interface ConsentManagerConfig {
    writeKey: string;
    cdnHost: string;
}

export interface Destination {
    id: string;
    name: string;
    category?: string;
}

declare global {
    interface Window {
        consentManagerConfig?: ConsentManagerConfig;
        consentManager?: { openConsentManager: () => void };
        analytics?: SegmentAnalytics;
        // OneTrust bridge (see consent-manager/onetrust.ts). The inline
        // bootstrap in head.html installs runWithPulumiConsent before the
        // bundle loads; the bundle replaces it with the full engine.
        runWithPulumiConsent?: (category: string, callback: () => void) => void;
        __pulumiConsentQueue?: { category: string; callback: () => void }[];
        OnetrustActiveGroups?: string;
        OptanonActiveGroups?: string;
        OptanonWrapper?: () => void;
        OneTrust?: { ToggleInfoDisplay?: () => void };
    }
}

export interface SegmentAnalytics {
    load: (writeKey: string, options?: { integrations?: Record<string, boolean> }) => void;
    addSourceMiddleware: (middleware: (args: MiddlewareArgs) => void) => void;
    identify: (traits: Record<string, unknown>) => void;
    ready?: (callback: () => void) => void;
    initialized?: boolean;
}

interface MiddlewareArgs {
    payload: {
        obj: {
            context: {
                consent?: Record<string, unknown>;
            };
        };
    };
    next: (payload: MiddlewareArgs["payload"]) => void;
}
