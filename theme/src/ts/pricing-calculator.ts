interface EditionRates {
    base_usd: number;
    included_credits: number;
    included_resources: number;
    iac_resource_month: number;
    esc_secret_month: number;
    insights_resource_month: number;
}

interface CalculatorConfig {
    contact_sales_resources: number;
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

// The sliders are a power curve, not a linear scale. Their ceilings are sized at
// a very large customer fully using each product (see the meter table in
// layouts/partials/pricing/calculator.html), three to four orders of magnitude
// above where a Team reader sits — linear, that reader's entire range would be
// the first two or three pixels of travel. So a range input holds a position
// from 0 to POSITIONS and the meter's value is max * (pos/POSITIONS)^CURVE,
// which spends the first third of the travel on the first few percent of the
// range and still lands exactly on max at the far end.
const POSITIONS = 1000;
const CURVE = 3;

// Two significant figures, so dragging lands on a number someone would say out
// loud (31,000) instead of wherever the curve happened to fall (31,247). The
// number input beside the slider is what exact figures are for, and it is not
// snapped.
function snap(value: number): number {
    if (value <= 0) return 0;
    if (value < 10) return Math.round(value);
    const magnitude = Math.pow(10, Math.floor(Math.log10(value)) - 1);
    return Math.round(value / magnitude) * magnitude;
}

function valueAt(pos: number, max: number): number {
    return snap(max * Math.pow(pos / POSITIONS, CURVE));
}

// Values past the ceiling pin the thumb at the far end rather than rescaling the
// slider: the number input accepts them, and the estimate is computed from it.
function posFor(value: number, max: number): number {
    if (!(value > 0) || !(max > 0)) return 0;
    return Math.round(POSITIONS * Math.pow(Math.min(1, value / max), 1 / CURVE));
}

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
    const totalValue = el("[data-calc-total-value]");
    const volumeNote = el("[data-calc-volume-note]");
    const ctaDefault = el("[data-calc-cta-default]");
    const ctaContact = el("[data-calc-cta-contact]");
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
        max: parseFloat(row.dataset.calcMax || "") || 0,
        range: row.querySelector<HTMLInputElement>("[data-calc-range]"),
        number: row.querySelector<HTMLInputElement>("[data-calc-number]"),
        rate: row.querySelector<HTMLElement>("[data-calc-rate]"),
    });

    // The number input is the meter's value; the range only ever holds a curve
    // position. Negatives floor at zero here rather than in the input handler,
    // so a half-typed "-" never briefly subtracts from the estimate.
    const valueOf = (row: HTMLElement): number => {
        const { number } = parts(row);
        const raw = parseFloat(number?.value || "");
        return isFinite(raw) && raw > 0 ? raw : 0;
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
        const volume = (values.iac_resources || 0) > config.contact_sales_resources;

        if (totalValue) totalValue.textContent = usd.format(total);
        if (creditsUsed) creditsUsed.textContent = count.format(credits);
        if (creditsIncluded) creditsIncluded.textContent = count.format(edition.included_credits);
        if (baseOut) baseOut.textContent = usd.format(edition.base_usd);
        if (overageOut) overageOut.textContent = usd.format(overage);

        totalValue?.classList.toggle("text-gray-500", volume);
        volumeNote?.classList.toggle("hidden", !volume);
        ctaDefault?.classList.toggle("hidden", volume);
        ctaContact?.classList.toggle("hidden", !volume);
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
        const { id, max, range, number } = parts(row);
        if (range && number) {
            if (source === "range") number.value = String(valueAt(parseFloat(range.value) || 0, max));
            else range.value = String(posFor(valueOf(row), max));
        }
        if (range) {
            const pos = parseFloat(range.value) || 0;
            range.style.setProperty("--form-range-fill", `${(pos / POSITIONS) * 100}%`);
            // What the thumb's position selects, not what the reader typed: past
            // the ceiling the two differ, and this attribute describes the slider.
            range.setAttribute("aria-valuetext", METERS[id].valueText(count.format(valueAt(pos, max))));
        }
    };

    // Holds a typed figure to the number input's own min/max, which is a sanity
    // ceiling well above the slider's — a reader whose fleet is off the end of
    // the slider still gets a real estimate, a fat-fingered extra digit doesn't.
    // The floor is only applied on `change`, so typing "1" toward "100" is left
    // alone mid-keystroke.
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

        // "number", not "range": the markup's starting values live on the number
        // inputs, and they are chosen to produce exactly the edition's base price.
        // Seeding from the range would round them off through the curve first.
        syncRow(row, "number");
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
