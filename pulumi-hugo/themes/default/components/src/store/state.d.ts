import { LanguageKey, K8sLanguageKey, OSKey, CloudKey, PersonaKey } from "../components/chooser/chooser";

// PreferencesState tracks settings like preferred language, cloud and operating system.
// Values tracked in this state slice persist between pages and reloads.
export interface PreferencesState {
    language: LanguageKey;
    k8sLanguage: K8sLanguageKey
    os: OSKey;
    cloud: CloudKey,
    persona: PersonaKey,
}

export interface Banner {
    name: string;
    dismissedAt: number;
}

export interface BannersState {
    dismissed: Banner[];
}

export interface AppState {
    preferences: PreferencesState,
    banners: BannersState,
}
