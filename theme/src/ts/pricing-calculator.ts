interface EditionRates {
    base_usd: number;
    included_credits: number;
    included_resources: number;
    iac_resource_month: number;
    esc_secret_month: number;
    insights_resource_month: number;
}

interface CalculatorConfig {
    contact_sales_usd: number;
    meters: {
        workflow_minute: number;
        neo_tokens_per_million: number;
    };
    editions: Record<string, EditionRates>;
}

interface Meter {
    rate: ((config: CalculatorConfig, edition: EditionRates) => number) | null;
    unit: string;
    valueText: (formatted: string) => string;
}

const METERS: Record<string, Meter> = {
    iac_resources: {
        rate: (_c, e) => e.iac_resource_month,
        unit: "/resource/mo",
        valueText: v => `${v} resources`,
    },
    esc_secrets: {
        rate: (_c, e) => e.esc_secret_month,
        unit: "/secret/mo",
        valueText: v => `${v} secrets`,
    },
    neo_tokens: {
        rate: c => c.meters.neo_tokens_per_million,
        unit: "/M tokens",
        valueText: v => `${v} million tokens`,
    },
    workflow_minutes: {
        rate: c => c.meters.workflow_minute,
        unit: "/minute",
        valueText: v => `${v} minutes`,
    },
    insights_resources: {
        rate: (_c, e) => e.insights_resource_month,
        unit: "/resource/mo",
        valueText: v => `${v} resources`,
    },
};

const usd = new Intl.NumberFormat("en-US", {
    style: "currency",
    currency: "USD",
    maximumFractionDigits: 0,
});

const usdRate = new Intl.NumberFormat("en-US", {
    style: "currency",
    currency: "USD",
    minimumFractionDigits: 2,
    maximumFractionDigits: 4,
});

const count = new Intl.NumberFormat("en-US", { maximumFractionDigits: 0 });

function creditsForResources(resources: number, edition: EditionRates): number {
    if (resources <= edition.included_resources) {
        return resources * (edition.included_credits / edition.included_resources);
    }
    const beyond = resources - edition.included_resources;
    return edition.included_credits + beyond * edition.iac_resource_month;
}

function init(): void {
    const configEl = document.getElementById("pricing-calculator-config");
    const root = document.getElementById("calculator");
    if (!configEl || !configEl.textContent || !root) {
        return;
    }

    let config: CalculatorConfig;
    try {
        config = JSON.parse(configEl.textContent) as CalculatorConfig;
    } catch {
        return;
    }

    const rows = Array.from(root.querySelectorAll<HTMLElement>("[data-calc-meter]")).filter(
        row => METERS[row.dataset.calcMeter || ""] !== undefined,
    );
    const editionButtons = Array.from(root.querySelectorAll<HTMLButtonElement>("[data-calc-edition]"));

    const el = <T extends HTMLElement>(selector: string): T | null => root.querySelector<T>(selector);
    const totalBlock = el("[data-calc-total]");
    const totalValue = el("[data-calc-total-value]");
    const contactBlock = el("[data-calc-contact]");
    const ctaDefault = el("[data-calc-cta-default]");
    const ctaContact = el("[data-calc-cta-contact]");
    const usageBlock = el("[data-calc-usage]");
    const creditsUsed = el("[data-calc-credits-used]");
    const creditsIncluded = el("[data-calc-credits-included]");
    const baseOut = el("[data-calc-base]");
    const overageOut = el("[data-calc-overage]");

    const currentEdition = (): EditionRates => {
        const pressed = editionButtons.filter(button => button.getAttribute("aria-pressed") === "true")[0];
        const id = pressed ? pressed.dataset.calcEdition : undefined;
        const rates = id ? config.editions[id] : undefined;
        return rates || config.editions[Object.keys(config.editions)[0]];
    };

    const parts = (row: HTMLElement) => ({
        id: row.dataset.calcMeter as string,
        range: row.querySelector<HTMLInputElement>("[data-calc-range]"),
        number: row.querySelector<HTMLInputElement>("[data-calc-number]"),
        rate: row.querySelector<HTMLElement>("[data-calc-rate]"),
    });

    const valueOf = (row: HTMLElement): number => {
        const { number, range } = parts(row);
        const raw = parseFloat((number || range)?.value || "");
        return isFinite(raw) ? raw : 0;
    };

    const paintRange = (range: HTMLInputElement, value: number): void => {
        const min = parseFloat(range.min) || 0;
        const max = parseFloat(range.max) || 100;
        const pct = max > min ? Math.min(100, Math.max(0, ((value - min) / (max - min)) * 100)) : 0;
        range.style.setProperty("--form-range-fill", `${pct}%`);
    };

    const recompute = (): void => {
        const edition = currentEdition();
        const values: Record<string, number> = {};
        rows.forEach(row => {
            values[row.dataset.calcMeter as string] = valueOf(row);
        });

        let credits = creditsForResources(values.iac_resources || 0, edition);
        credits += (values.esc_secrets || 0) * edition.esc_secret_month;
        credits += (values.workflow_minutes || 0) * config.meters.workflow_minute;
        credits += (values.neo_tokens || 0) * config.meters.neo_tokens_per_million;
        credits += (values.insights_resources || 0) * edition.insights_resource_month;

        const overage = Math.max(0, credits - edition.included_credits);
        const total = edition.base_usd + overage;
        const contact = total > config.contact_sales_usd;

        if (totalValue) totalValue.textContent = usd.format(total);
        if (creditsUsed) creditsUsed.textContent = count.format(credits);
        if (creditsIncluded) creditsIncluded.textContent = count.format(edition.included_credits);
        if (baseOut) baseOut.textContent = usd.format(edition.base_usd);
        if (overageOut) overageOut.textContent = usd.format(overage);

        totalBlock?.classList.toggle("hidden", contact);
        contactBlock?.classList.toggle("hidden", !contact);
        usageBlock?.classList.toggle("hidden", contact);
        ctaDefault?.classList.toggle("hidden", contact);
        ctaContact?.classList.toggle("hidden", !contact);
    };

    const paintRates = (): void => {
        const edition = currentEdition();
        rows.forEach(row => {
            const { id, rate } = parts(row);
            const meter = METERS[id];
            if (!rate) return;
            rate.textContent = meter.rate ? `${usdRate.format(meter.rate(config, edition))}${meter.unit}` : "";
        });
    };

    const syncRow = (row: HTMLElement, source: "range" | "number"): void => {
        const { id, range, number } = parts(row);
        if (range && number) {
            if (source === "range") number.value = range.value;
            else range.value = number.value;
        }
        const value = valueOf(row);
        if (range) {
            paintRange(range, value);
            range.setAttribute("aria-valuetext", METERS[id].valueText(count.format(value)));
        }
    };

    const clamp = (input: HTMLInputElement, floor: boolean): void => {
        const min = parseFloat(input.min);
        const max = parseFloat(input.max);
        const value = parseFloat(input.value);
        if (!isFinite(value)) {
            if (floor && isFinite(min)) input.value = String(min);
            return;
        }
        if (isFinite(max) && value > max) input.value = String(max);
        else if (floor && isFinite(min) && value < min) input.value = String(min);
    };

    rows.forEach(row => {
        const { range, number } = parts(row);

        range?.addEventListener("input", () => {
            syncRow(row, "range");
            recompute();
        });

        number?.addEventListener("input", () => {
            clamp(number, false);
            syncRow(row, "number");
            recompute();
        });

        number?.addEventListener("change", () => {
            clamp(number, true);
            syncRow(row, "number");
            recompute();
        });

        syncRow(row, "range");
    });

    editionButtons.forEach(button => {
        button.addEventListener("click", () => {
            editionButtons.forEach(other => other.setAttribute("aria-pressed", String(other === button)));
            paintRates();
            recompute();
        });
    });

    paintRates();
    recompute();
}

if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init, { once: true });
} else {
    init();
}
