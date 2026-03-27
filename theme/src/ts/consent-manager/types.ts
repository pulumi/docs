export interface ConsentManagerConfig {
    writeKey: string;
    cdnHost: string;
    container: string;
    privacyPolicyUrl: string;
    bannerText: string;
    preferencesDialogTitle: string;
    preferencesDialogContent: string;
    cancelDialogTitle: string;
    cancelDialogContent: string;
}

export interface Destination {
    id: string;
    name: string;
    category?: string;
}

export interface TrackingPreferences {
    version: number;
    destinations: Record<string, boolean>;
    custom?: Record<string, boolean | null>;
}

declare global {
    interface Window {
        consentManagerConfig?: ConsentManagerConfig;
        consentManager?: { openConsentManager: () => void };
        analytics?: SegmentAnalytics;
    }
}

export interface SegmentAnalytics {
    load: (writeKey: string, options?: { integrations?: Record<string, boolean> }) => void;
    addSourceMiddleware: (middleware: (args: MiddlewareArgs) => void) => void;
    identify: (traits: Record<string, unknown>) => void;
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
