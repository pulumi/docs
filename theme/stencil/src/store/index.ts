import { createStore, applyMiddleware } from "redux";
import { combineReducers } from "redux";
import { composeWithDevTools } from "redux-devtools-extension/developmentOnly";
import thunk from "redux-thunk";

import { AppState } from "./state";
import { preferences } from "./reducers/preferences";
import { banners } from "./reducers/banners";
import { user } from "./reducers/user";

import { TypeKeys } from "./actions";

export const rootReducer = combineReducers({
    preferences,
    banners,
    user,
});

// Page-scoped languages that are never persisted as the global preference (see the
// serializer in configureStore). OPA is only offered on a handful of policy pages;
// a lingering preference for it would be useless everywhere else. HCL used to be in
// this list, but it is now offered across the docs (including the get-started
// guides, where the selection must survive page navigation), and a chooser that
// doesn't offer the preferred language falls back to its first option without
// touching the store.
const specialPurposeLanguages: string[] = ["opa"];

// The Redux store. See https://redux.js.org/ for general information about Redux and
// https://stenciljs.com/docs/stencil-redux for details about Stencil's implementation.
export const configureStore = () => {
    // Deserialize from localStorage.
    let local: string | null;

    try {
        // localStorage.getItem can fail when cookies are blocked.
        local = localStorage.getItem("pulumi_state");
    } catch (e) {
        console.error("Failed to read pulumi_state from localStorage:", e);
    }

    const persistedState: any = local ? JSON.parse(local) : {};
    const initialState = normalizeState(persistedState);

    const store = createStore(rootReducer, initialState, composeWithDevTools(applyMiddleware(thunk)));

    // OPA is a page-scoped language: it displays while you're on one of the few pages
    // that offer it, but must never become your persisted preference, or every other
    // page would inherit a language it can't render. So we never write it to storage --
    // while it is selected we keep persisting your last real language, leaving your
    // actual preference intact across the visit.
    let lastRealLanguage = (initialState.preferences && initialState.preferences.language) || "typescript";

    // Serialize to localStorage.
    store.subscribe(() => {
        const state = store.getState();

        if (!specialPurposeLanguages.includes(state.preferences.language)) {
            lastRealLanguage = state.preferences.language;
        }
        const toPersist =
            state.preferences.language === lastRealLanguage
                ? state
                : { ...state, preferences: { ...state.preferences, language: lastRealLanguage } };

        // localStorage.setItem can fail when cookies are blocked or when the
        // the browser's storage limit has been exceeded.
        try {
            localStorage.setItem("pulumi_state", JSON.stringify(toPersist));
        } catch (e) {
            console.error("Failed to save pulumi_state:", e);
        }
    });

    // While we await broader support for the CookieStore API, we poll every
    // few seconds for any changes to user-info cookies.
    // https://developer.mozilla.org/en-US/docs/Web/API/Cookie_Store_API
    setInterval(() => {
        store.dispatch({
            type: TypeKeys.GET_USER_INFO,
        });
    }, 3000);

    return store;
};

// normalizeState transforms slices of serialized state into a shape that conforms to
// our current expectations.
export function normalizeState(persistedState: any): Partial<AppState> {
    let state: Partial<AppState> = {};

    try {
        // state.banners
        if (persistedState.banners && Array.isArray(persistedState.banners.dismissed)) {
            // Only load banner dismissals recorded within the last four days.
            const fourDaysAgo = Date.now() - 60 * 60 * 24 * 4 * 1000;
            state.banners = {
                dismissed: persistedState.banners.dismissed.filter(b => {
                    return !!b.name && b.dismissedAt && b.dismissedAt > fourDaysAgo;
                }),
            };
        }

        // state.preferences
        if (persistedState.preferences) {
            // Coerce a stale special-purpose language (e.g. an OPA preference left over
            // from before we stopped persisting them) back to a real one on load, so it
            // never re-enters the store.
            const persistedLanguage = persistedState.preferences.language;
            state.preferences = {
                language: persistedLanguage && !specialPurposeLanguages.includes(persistedLanguage) ? persistedLanguage : "typescript",
                os: persistedState.preferences.os || "macos",
                cloud: persistedState.preferences.cloud || "aws",
                k8sLanguage: persistedState.preferences.k8sLanguage || "typescript",
                persona: persistedState.preferences.persona || "developer",
                backend: persistedState.preferences.backend || "service",
                pythontoolchain: persistedState.preferences.pythontoolchain || "pip",
                tfTool: persistedState.preferences.tfTool || "terraform",
            };
        }
    } catch (e) {
        return state;
    }

    return state;
}
