// Test-only stand-in for @growthbook/growthbook, whose dom-mutator dependency
// requires a browser MutationObserver at import time and so can't load in the
// spec-test environment. Wired up via moduleNameMapper in stencil.config.ts.
/* eslint-disable @typescript-eslint/no-unused-vars */
export class GrowthBook {
    constructor(_options?: unknown) {}
    init(_options?: unknown): Promise<unknown> {
        return Promise.resolve({});
    }
    setTrackingCallback(_cb: unknown): void {}
    setAttributes(_attrs: unknown): void {}
    getAttributes(): Record<string, unknown> {
        return {};
    }
    isOn(_key: string): boolean {
        return false;
    }
    getFeatureValue<T>(_key: string, fallback: T): T {
        return fallback;
    }
}
