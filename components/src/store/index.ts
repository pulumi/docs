import { createStore, applyMiddleware } from "redux";
import { combineReducers } from "redux";
import { composeWithDevTools } from "redux-devtools-extension/developmentOnly";
import thunk from "redux-thunk";

import { AppState } from "./state";
import { preferences } from "./reducers/preferences";
import { banners } from "./reducers/banners";

export const rootReducer = combineReducers({
    preferences,
    banners,
});

// The Redux store. See https://redux.js.org/ for general information about Redux and
// https://stenciljs.com/docs/stencil-redux for details about Stencil's implementation.
export const configureStore = () => {

    // Deserialize from localStorage.
    let local: string | null;

    try {
        // localStorage.getItem can fail when cookies are blocked.
        local = localStorage.getItem("pulumi_state");
    } catch (e){
        console.error("Failed to read pulumi_state from localStorage:", e);
    }

    const persistedState: Partial<AppState> = local ? JSON.parse(local) : {};

    const store = createStore(
        rootReducer,
        persistedState,
        composeWithDevTools(applyMiddleware(thunk))
    );

    // Serialize to localStorage.
    store.subscribe(() => {
        const state = store.getState();

        // localStorage.setItem can fail when cookies are blocked or when the
        // the browser's storage limit has been exceeded.
        try {
            localStorage.setItem("pulumi_state", JSON.stringify(state));
        } catch (e) {
            console.error("Failed to save pulumi_state:", e);
        }
    });

    return store;
}
