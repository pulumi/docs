import { ActionTypes, TypeKeys } from "../actions/index";
import { FormState } from "../../store/state";

// Define the default values of form state.
const getInitialState = (): FormState => {
    return {
        submittedFormIds: [],
    };
};

// The preferences reducer. Note that it does not mutate state, but rather always returns a fresh copy.
// https://redux.js.org/basics/reducers/
export const form = (currentState = getInitialState(), action: ActionTypes): FormState => {

    switch (action.type) {
        case TypeKeys.ADD_SUBMITTED_FORM_ID:
            const formId = action.key;

            // Check to see if the user has submitted the form before. If not,
            // add the formId.
            if (currentState.submittedFormIds.indexOf(formId) === -1) {
                currentState.submittedFormIds.push(action.key);
            }

            return currentState;
        default:
            return currentState;
    }
};
