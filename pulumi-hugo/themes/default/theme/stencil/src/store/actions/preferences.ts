import { TypeKeys } from "./index";
import { LanguageKey, K8sLanguageKey, OSKey, CloudKey, PersonaKey } from "../../components/chooser/chooser";

export interface SetLanguage {
    type: TypeKeys.SET_LANGUAGE;
    key: LanguageKey;
}

export interface SetK8sLanguage {
    type: TypeKeys.SET_K8S_LANGUAGE;
    key: K8sLanguageKey;
}

export interface SetOS {
    type: TypeKeys.SET_OS;
    key: OSKey;
}

export interface SetCloud {
    type: TypeKeys.SET_CLOUD;
    key: CloudKey;
}

export interface SetPersona {
    type: TypeKeys.SET_PERSONA;
    key: PersonaKey;
}

// Set the currently selected language.
export const setLanguage = (key: LanguageKey) => (dispatch, _getState) => {
    const action: SetLanguage = {
        type: TypeKeys.SET_LANGUAGE,
        key: key,
    };
    dispatch(action);
};

// Set the currently Kubernetes language.
export const setK8sLanguage = (key: K8sLanguageKey) => (dispatch, _getState) => {
    const action: SetK8sLanguage = {
        type: TypeKeys.SET_K8S_LANGUAGE,
        key: key,
    };
    dispatch(action);
};

// Set the currently OS.
export const setOS = (key: OSKey) => (dispatch, _getState) => {
    const action: SetOS = {
        type: TypeKeys.SET_OS,
        key: key,
    };
    dispatch(action);
};

// Set the currently selected cloud.
export const setCloud = (key: CloudKey) => (dispatch, _getState) => {
    const action: SetCloud = {
        type: TypeKeys.SET_CLOUD,
        key: key,
    };
    dispatch(action);
};

// Set the currently selected persona.
export const setPersona = (key: PersonaKey) => (dispatch, _getState) => {
    const action: SetPersona = {
        type: TypeKeys.SET_PERSONA,
        key: key,
    };
    dispatch(action);
};
