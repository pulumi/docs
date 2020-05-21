import { TypeKeys } from "./index";

export interface AddSubmittedFormId {
    type: TypeKeys.ADD_SUBMITTED_FORM_ID;
    key: string;
}

// Add a HubSpot formId to submitted forms list.
export const addSubmittedFormId = (formId: string) => (dispatch, _getState) => {
    const action: AddSubmittedFormId = {
        type: TypeKeys.ADD_SUBMITTED_FORM_ID,
        key: formId,
    };
    dispatch(action);
};
