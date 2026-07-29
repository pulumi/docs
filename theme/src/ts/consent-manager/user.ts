const USER_INFO_COOKIE = "pulumi_web_user_info";

export interface UserInfo {
    userId: string;
    traits: Record<string, unknown>;
}

// Reads the auth cookie the app sets for a signed-in user. The value is a
// URL-encoded JSON string prefixed with Express's "j:" marker. Returns the
// userId plus every other field in the cookie as identify traits, so any
// user info the app adds later (email, name, orgs, ...) flows through
// automatically. Returns null when no identifiable user is present.
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
