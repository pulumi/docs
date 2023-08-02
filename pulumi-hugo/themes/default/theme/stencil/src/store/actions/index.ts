import { SetLanguage, SetK8sLanguage, SetOS, SetCloud, SetPersona, SetBackEnd } from "./preferences";
import { DismissBanner } from "./banners";
import { GetUser } from "./user";

export enum TypeKeys {
    // Chooser-related action types.
    SET_LANGUAGE = "SET_LANGUAGE",
    SET_K8S_LANGUAGE = "SET_K8S_LANGUAGE",
    SET_INPUT_KIND = "SET_INPUT_KIND",
    SET_OS = "SET_OS",
    SET_CLOUD = "SET_CLOUD",
    SET_PERSONA = "SET_PERSONA",
    SET_BACKEND = "SET_BACKEND",

    // Banner-related action types.
    DISMISS_BANNER = "DISMISS_BANNER",

    // User-related action types.
    GET_USER_INFO = "GET_USER_INFO",
}

export type PreferencesAction = SetLanguage | SetK8sLanguage | SetOS | SetCloud | SetPersona | SetBackEnd;
export type BannersAction = DismissBanner;
export type UserAction = GetUser;
