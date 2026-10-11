// NOTE: These tests do not run in CI. `make test` only runs the example-program tests,
// and the pull-request workflow never invokes `stencil test`. Run them by hand when
// touching the store:
//
//     cd theme/stencil && yarn install
//     npx stencil test --spec -- src/store/store.spec.ts
//
import { normalizeState } from "./index";

describe("normalizeState", () => {
    describe("given bogus data", () => {
        it("returns an empty state object", () => {
            expect(normalizeState({ lol: "haha" })).toStrictEqual({});
            expect(normalizeState("stuff")).toStrictEqual({});
            expect(normalizeState(14)).toStrictEqual({});
            expect(normalizeState(null)).toStrictEqual({});
            expect(normalizeState(undefined)).toStrictEqual({});
            expect(normalizeState(["sandwich", () => {}, false])).toStrictEqual({});
        });
    });

    describe("given a preferences slice", () => {
        let preferencesSlice;

        describe("that is incomplete", () => {
            beforeEach(() => {
                preferencesSlice = {
                    preferences: {
                        language: "typescript",
                    },
                };
            });

            it("returns the default preferences slice", () => {
                expect(normalizeState(preferencesSlice)).toStrictEqual({
                    preferences: {
                        language: "typescript",
                        os: "macos",
                        cloud: "aws",
                        k8sLanguage: "typescript",
                        persona: "developer",
                        backend: "service",
                        pythontoolchain: "pip",
                        tfTool: "terraform",
                    },
                });
            });
        });

        describe("with a persisted HCL language preference", () => {
            it("keeps HCL as the language", () => {
                const state = normalizeState({ preferences: { language: "hcl" } });
                expect(state.preferences.language).toBe("hcl");
            });
        });

        describe("with a persisted special-purpose language preference", () => {
            it("coerces OPA back to the default language", () => {
                const state = normalizeState({ preferences: { language: "opa" } });
                expect(state.preferences.language).toBe("typescript");
            });
        });
    });

    describe("given a banners slice", () => {
        let bannersSlice;

        describe("that is incomplete", () => {
            beforeEach(() => {
                bannersSlice = { banners: { dismissed: ["some-banner"] } };
            });

            it("returns the default banners slice", () => {
                expect(normalizeState(bannersSlice)).toStrictEqual({
                    banners: { dismissed: [] },
                });
            });
        });

        describe("with recent dismissals", () => {
            beforeEach(() => {
                const tenSecondsAgo = Date.now() - 10000;
                bannersSlice = {
                    banners: {
                        dismissed: [{ name: "some-banner", dismissedAt: tenSecondsAgo }],
                    },
                };
            });

            it("includes them in the list of dismissed banners", () => {
                expect(normalizeState(bannersSlice)).toStrictEqual(bannersSlice);
            });
        });

        describe("with outdated dismissals", () => {
            beforeEach(() => {
                const september7th2020 = 1599444674986;
                bannersSlice = {
                    banners: {
                        dismissed: [{ name: "some-banner", dismissedAt: september7th2020 }],
                    },
                };
            });

            it("excludes them from the list of dismissed banners", () => {
                expect(normalizeState(bannersSlice)).toStrictEqual({
                    banners: { dismissed: [] },
                });
            });
        });
    });
});
