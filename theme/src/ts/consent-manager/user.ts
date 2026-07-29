const USER_INFO_COOKIE = "pulumi_web_user_info";

export interface UserInfo {
    userId: string;
    traits: Record<string, unknown>;
}

// Reads the signed-in user from the auth cookie: a URL-encoded JSON string
// with Express's "j:" prefix. Returns userId plus any other fields as traits.
export function getUserInfo(): UserInfo | null {
    try {
        const cookie = document.cookie.split("; ").find(s => s.indexOf(`${USER_INFO_COOKIE}=`) === 0);
        if (!cookie) return null;

        const raw = decodeURIComponent(cookie.slice(cookie.indexOf("=") + 1));
        const json = raw.indexOf("j:") === 0 ? raw.slice(2) : raw;
        const parsed = JSON.parse(json);
        if (!parsed || !parsed.userId) return null;

        const { userId, ...traits } = parsed;
        return { userId: String(userId), traits };
    } catch {
        return null;
    }
}
