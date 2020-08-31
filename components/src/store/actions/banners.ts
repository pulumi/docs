import { TypeKeys } from "./index";

export interface DismissBanner {
    type: TypeKeys.DISMISS_BANNER;
    name: string;
}

// Dismiss the banner component.
export const dismissBanner = (name: string) => (dispatch, _getState) => {
    const action: DismissBanner = {
        type: TypeKeys.DISMISS_BANNER,
        name
    };
    dispatch(action);
};
