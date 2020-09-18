import { BannersAction, TypeKeys } from "../actions/index";
import { BannersState } from "../../store/state";

// Define the default set of banners.
const getInitialState = (): BannersState => {
    return {
        dismissed: [],
    };
};

// The banners reducer. Note that it does not mutate state, but rather always returns a fresh copy.
// https://redux.js.org/basics/reducers/
export const banners = (currentState = getInitialState(), action: BannersAction): BannersState => {

    switch (action.type) {
        case TypeKeys.DISMISS_BANNER:
            const { name, dismissedAt } = action.payload;

            return {
                ...currentState,
                dismissed: [
                    ...currentState.dismissed.filter(b => b.name !== name),
                    { name, dismissedAt }
                ]
            };
        default:
            return currentState;
    }
};
