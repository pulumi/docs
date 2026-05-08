type StatusIndicator = "none" | "minor" | "major" | "critical" | "maintenance";

interface StatusResponse {
    status: {
        indicator: StatusIndicator;
        description: string;
    };
}

interface CachedStatus {
    indicator: StatusIndicator;
    description: string;
    ts: number;
}

const CACHE_KEY = "pulumi:statuspage";
const CACHE_TTL_MS = 5 * 60 * 1000;
const STATUS_URL = "https://pulumi.statuspage.io/api/v2/status.json";

function readCache(): CachedStatus | null {
    try {
        const raw = localStorage.getItem(CACHE_KEY);
        if (!raw) return null;
        const parsed = JSON.parse(raw) as CachedStatus;
        if (Date.now() - parsed.ts > CACHE_TTL_MS) return null;
        return parsed;
    } catch {
        return null;
    }
}

function writeCache(value: CachedStatus): void {
    try {
        localStorage.setItem(CACHE_KEY, JSON.stringify(value));
    } catch {
        // Safari private mode etc.
    }
}

function applyStatus(indicator: StatusIndicator, description: string): void {
    const badges = document.querySelectorAll<HTMLElement>("[data-statuspage]");
    badges.forEach(badge => {
        badge.dataset.statuspageState = indicator;
        const label = badge.querySelector<HTMLElement>("[data-statuspage-label]");
        if (label && description) label.textContent = description;
    });
}

async function fetchStatus(): Promise<void> {
    const res = await fetch(STATUS_URL, { cache: "no-store" });
    if (!res.ok) return;
    const data = (await res.json()) as StatusResponse;
    const { indicator, description } = data.status;
    applyStatus(indicator, description);
    writeCache({ indicator, description, ts: Date.now() });
}

function init(): void {
    if (!document.querySelector("[data-statuspage]")) return;

    const cached = readCache();
    if (cached) {
        applyStatus(cached.indicator, cached.description);
        return;
    }

    fetchStatus().catch(() => {});
}

if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init, { once: true });
} else {
    init();
}
