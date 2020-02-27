import { SetLanguage, SetK8sLanguage, SetOS, SetCloud } from "./preferences";

export enum TypeKeys {
    SET_LANGUAGE = "SET_LANGUAGE",
    SET_K8S_LANGUAGE = "SET_K8S_LANGUAGE",
    SET_OS = "SET_OS",
    SET_CLOUD = "SET_CLOUD"
}

export type ActionTypes = SetLanguage | SetK8sLanguage | SetOS | SetCloud;
