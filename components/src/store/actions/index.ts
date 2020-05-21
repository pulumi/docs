import { SetLanguage, SetK8sLanguage, SetOS, SetCloud } from "./preferences";
import { AddSubmittedFormId } from "./form";

export enum TypeKeys {
    SET_LANGUAGE = "SET_LANGUAGE",
    SET_K8S_LANGUAGE = "SET_K8S_LANGUAGE",
    SET_OS = "SET_OS",
    SET_CLOUD = "SET_CLOUD",
    ADD_SUBMITTED_FORM_ID = "ADD_SUBMITTED_FORM_ID",
}

export type ActionTypes = SetLanguage | SetK8sLanguage | SetOS | SetCloud | AddSubmittedFormId;
