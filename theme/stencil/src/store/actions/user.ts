import { TypeKeys } from "./index";

export interface GetUser {
    type: TypeKeys.GET_USER_INFO;
}

export const getUser = () => (dispatch, _getState) => {
    const action: GetUser = {
        type: TypeKeys.GET_USER_INFO,
    };
    dispatch(action);
};
