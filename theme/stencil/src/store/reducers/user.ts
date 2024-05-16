import { UserAction, TypeKeys } from "../actions/index";
import { UserState } from "../state";
import { parseCookie } from "../../util/util";

interface UserInfoCookie {
    userId: string;
}

const getInitialState = (): UserState => {
    return {
        id: getUserInfoCookie().userId,
    };
};

function getUserInfoCookie(): UserInfoCookie {
    const cookie = parseCookie();
    const pulumiWebUserInfo = cookie["pulumi_web_user_info"];
    let userId: string;

    if (pulumiWebUserInfo) {
        try {
            userId = JSON.parse(decodeURIComponent(pulumiWebUserInfo).replace("j:", "")).userId;
        } catch (error) {
            console.error(`Failed to parse pulumi_web_user_info cookie '${pulumiWebUserInfo}'.`);
        }
    }

    return {
        userId,
    };
}

export const user = (currentState = getInitialState(), action: UserAction): UserState => {
    switch (action.type) {
        case TypeKeys.GET_USER_INFO:
            return {
                ...currentState,
                id: getUserInfoCookie().userId,
            };
        default:
            return currentState;
    }
};
