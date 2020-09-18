import { TypeKeys } from "./index";

export interface DismissBanner {
    type: TypeKeys.DISMISS_BANNER;
    payload: {
        name: string;
        dismissedAt: number;
    }
}

// Dismiss the banner component.
export const dismissBanner = (name: string) => (dispatch, _getState) => {
    const action: DismissBanner = {
        type: TypeKeys.DISMISS_BANNER,
        payload: {
            name,
            dismissedAt: Date.now(),
        },
    };
    dispatch(action);
};
