import { ActionTypes, TypeKeys } from "../actions/index";
import { PreferencesState } from "../../store/state";

const getInitialState = (): PreferencesState => {
    return {
        language: "typescript",
        k8sLanguage: "typescript",
        os: "macos",
        cloud: "aws",
    };
};

// The preferences reducer. Note that it does not mutate state, but rather always returns a fresh copy.
// https://redux.js.org/basics/reducers/
export const preferences = (currentState = getInitialState(), action: ActionTypes): PreferencesState => {

    switch (action.type) {
        case TypeKeys.SET_LANGUAGE: {
            return { ...currentState, language: action.key };
        }
        case TypeKeys.SET_K8S_LANGUAGE: {
            return { ...currentState, k8sLanguage: action.key };
        }
        case TypeKeys.SET_OS: {
            return { ...currentState, os: action.key };
        }
        case TypeKeys.SET_CLOUD: {
            return { ...currentState, cloud: action.key };
        }
        default:
            return currentState;
    }
};
