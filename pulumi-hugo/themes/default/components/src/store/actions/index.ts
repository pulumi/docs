import { SetLanguage, SetK8sLanguage, SetInputKind, SetOS, SetCloud } from "./preferences";

export enum TypeKeys {
    SET_LANGUAGE = "SET_LANGUAGE",
    SET_K8S_LANGUAGE = "SET_K8S_LANGUAGE",
    SET_INPUT_KIND = "SET_INPUT_KIND",
    SET_OS = "SET_OS",
    SET_CLOUD = "SET_CLOUD"
}

export type ActionTypes = SetLanguage | SetK8sLanguage | SetInputKind | SetOS | SetCloud;
