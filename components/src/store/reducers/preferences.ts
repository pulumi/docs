import { ActionTypes, TypeKeys } from "../actions/index";
import { PreferencesState } from "../../store/state";
import { OSKey } from "../../components/chooser/chooser";

// Define the default set of preferences.
const getInitialState = (): PreferencesState => {
    return {
        language: "typescript",
        k8sLanguage: "typescript",
        inputKind: "code",
        os: guessOS(),
        cloud: "aws",
    };
};

// Do our best to detect the OS using the browser.
function guessOS(): OSKey {
    const appVersion = navigator.appVersion;

    if (appVersion.indexOf("Win") !== -1) {
        return "windows";
    } else if (appVersion.indexOf("Mac") !== -1) {
        return "macos";
    } else if (appVersion.indexOf("Linux") !== -1) {
        return "linux";
    }

    return "macos";
}

// The preferences reducer. Note that it does not mutate state, but rather always returns a fresh copy.
// https://redux.js.org/basics/reducers/
export const preferences = (currentState = getInitialState(), action: ActionTypes): PreferencesState => {

    switch (action.type) {
        case TypeKeys.SET_LANGUAGE:
            return { ...currentState, language: action.key };
        case TypeKeys.SET_K8S_LANGUAGE:
            return { ...currentState, k8sLanguage: action.key };
        case TypeKeys.SET_INPUT_KIND:
            return { ...currentState, inputKind: action.key };
        case TypeKeys.SET_OS:
            return { ...currentState, os: action.key };
        case TypeKeys.SET_CLOUD:
            return { ...currentState, cloud: action.key };
        default:
            return currentState;
    }
};
