import { SetLanguage, SetK8sLanguage, SetInputKind, SetOS, SetCloud } from "./preferences";
import { DismissBanner } from "./banners";

export enum TypeKeys {

    // Chooser-related action types.
    SET_LANGUAGE = "SET_LANGUAGE",
    SET_K8S_LANGUAGE = "SET_K8S_LANGUAGE",
    SET_INPUT_KIND = "SET_INPUT_KIND",
    SET_OS = "SET_OS",
    SET_CLOUD = "SET_CLOUD",

    // Banner-related action types.
    DISMISS_BANNER = "DISMISS_BANNER",
}

export type PreferencesAction = SetLanguage | SetK8sLanguage | SetInputKind | SetOS | SetCloud;
export type BannersAction = DismissBanner;
