import { LanguageKey, K8sLanguageKey, OSKey, CloudKey } from "../components/chooser/chooser";

// PreferencesState tracks settings like preferred language, cloud and operating system.
// Values tracked in this state slice persist between pages and reloads.
export interface PreferencesState {
    language: LanguageKey;
    k8sLanguage: K8sLanguageKey
    os: OSKey;
    cloud: CloudKey,
}

export interface AppState {
    preferences: PreferencesState
}
