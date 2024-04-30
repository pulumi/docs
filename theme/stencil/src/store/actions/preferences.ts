import { TypeKeys } from "./index";
import { LanguageKey, K8sLanguageKey, OSKey, CloudKey, PersonaKey, BackEndKey } from "../../components/chooser/chooser";

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

export interface SetBackEnd {
    type: TypeKeys.SET_BACKEND;
    key: BackEndKey;
}

const dispatchAction = <T>(action: T) => (dispatch, _getState) => dispatch(action);

// Set the currently selected language.
export const setLanguage = (key: LanguageKey) => dispatchAction<SetLanguage>({
    key,
    type: TypeKeys.SET_LANGUAGE,
});

// Set the currently Kubernetes language.
export const setK8sLanguage = (key: K8sLanguageKey) => dispatchAction<SetK8sLanguage>({
    key,
    type: TypeKeys.SET_K8S_LANGUAGE,
});

// Set the currently OS.
export const setOS = (key: OSKey) => dispatchAction<SetOS>({
    key,
    type: TypeKeys.SET_OS,
});

// Set the currently selected cloud.
export const setCloud = (key: CloudKey) => dispatchAction<SetCloud>({
    key,
    type: TypeKeys.SET_CLOUD,
});

// Set the currently selected persona.
export const setPersona = (key: PersonaKey) => dispatchAction<SetPersona>({
    key,
    type: TypeKeys.SET_PERSONA,
});

// Set the currently selected backend type.
export const setBackEnd = (key: BackEndKey) => dispatchAction<SetBackEnd>({
    key,
    type: TypeKeys.SET_BACKEND,
});
