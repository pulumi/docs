type StatusIndicator = "none" | "minor" | "major" | "critical" | "maintenance";

interface StatusResponse {
    status: {
        indicator: StatusIndicator;
        description: string;
    };
}

const STATUS_URL = "https://pulumi.statuspage.io/api/v2/status.json";

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
    applyStatus(data.status.indicator, data.status.description);
}

function init(): void {
    if (!document.querySelector("[data-statuspage]")) return;
    fetchStatus().catch(() => {});
}

if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init, { once: true });
} else {
    init();
}
