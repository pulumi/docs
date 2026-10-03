interface EditionRates {
    base_usd: number;
    included_credits: number;
    included_resources: number;
    iac_resource_month: number;
    iac_resource_hour: number;
    esc_secret_month: number;
    esc_secret_hour: number;
    insights_resource_month: number;
    insights_resource_hour: number;
}

interface CalculatorConfig {
    contact_sales_resources: number;
    meters: {
        workflow_minute: number;
        neo_tokens_per_million: number;
    };
    editions: Record<string, EditionRates>;
}

type RateUnit = "month" | "hour";

// On /hr the time-billed meters are entered in unit-hours instead of units, and
// a unit that exists all month is this many of them. Flipping the toggle
// converts the entered quantities by this factor rather than the total, so the
// estimate is still a monthly bill either way — /hr is for a reader who knows
// their usage in resource-hours, not a per-hour price.
const HOURS_PER_MONTH = 730;

// `hourly` is set only on the meters billed by time (IaC resources, ESC secrets,
// discovered resources) — the ones the /mo-/hr toggle switches. Workflow
// minutes and Neo tokens are billed per use and have no hourly form.
interface Meter {
    rate: ((config: CalculatorConfig, edition: EditionRates) => number) | null;
    unit: string;
    hourly?: {
        rate: (edition: EditionRates) => number;
        unit: string;
        valueText: (formatted: string) => string;
    };
    valueText: (formatted: string) => string;
}

const METERS: Record<string, Meter> = {
    iac_resources: {
        rate: (_c, e) => e.iac_resource_month,
        unit: "/resource/mo",
        hourly: { rate: e => e.iac_resource_hour, unit: "/resource/hr", valueText: v => `${v} resource-hours` },
        valueText: v => `${v} resources`,
    },
    esc_secrets: {
        rate: (_c, e) => e.esc_secret_month,
        unit: "/secret/mo",
        hourly: { rate: e => e.esc_secret_hour, unit: "/secret/hr", valueText: v => `${v} secret-hours` },
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
        hourly: { rate: e => e.insights_resource_hour, unit: "/resource/hr", valueText: v => `${v} resource-hours` },
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
    minimumFractionDigits: 2,
    maximumFractionDigits: 2,
});

const usdRate = new Intl.NumberFormat("en-US", {
    style: "currency",
    currency: "USD",
    minimumFractionDigits: 2,
    maximumFractionDigits: 5,
});

// Hourly rates run an order of magnitude smaller than monthly ones (down to
// $0.00025), so they need more room after the decimal than usdRate gives a
// monthly figure — otherwise they'd round to $0.00 or lose the digit that
// distinguishes them from a sibling edition's rate.
const usdRateHour = new Intl.NumberFormat("en-US", {
    style: "currency",
    currency: "USD",
    minimumFractionDigits: 2,
    maximumFractionDigits: 6,
});

const count = new Intl.NumberFormat("en-US", { maximumFractionDigits: 0 });

// `quantity` is resources on /mo and resource-hours on /hr. The included tranche
// scales with it, so 500 resources and 365,000 resource-hours both cost exactly
// the Essentials base, and only the rate beyond the tranche differs by unit.
function creditsForResources(quantity: number, edition: EditionRates, unit: RateUnit): number {
    const hourly = unit === "hour";
    const included = edition.included_resources * (hourly ? HOURS_PER_MONTH : 1);
    if (quantity <= included) {
        return quantity * (edition.included_credits / included);
    }
    const beyond = quantity - included;
    return edition.included_credits + beyond * (hourly ? edition.iac_resource_hour : edition.iac_resource_month);
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
    const rateUnitButtons = Array.from(root.querySelectorAll<HTMLButtonElement>("[data-calc-rate-unit]"));

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

    const currentRateUnit = (): RateUnit => {
        const pressed = rateUnitButtons.find(button => button.getAttribute("aria-pressed") === "true");
        return (pressed?.dataset.calcRateUnit as RateUnit | undefined) || "month";
    };

    // How many of the row's entered units make one month of one unit: 730 for a
    // time-billed meter on /hr, 1 everywhere else. The slider's ceiling scales by
    // it too, so a thumb sits in the same place before and after a flip.
    const unitFactor = (id: string): number =>
        currentRateUnit() === "hour" && METERS[id].hourly ? HOURS_PER_MONTH : 1;

    const parts = (row: HTMLElement) => {
        const id = row.dataset.calcMeter as string;
        return {
            id,
            max: (parseFloat(row.dataset.calcMax || "") || 0) * unitFactor(id),
            range: row.querySelector<HTMLInputElement>("[data-calc-range]"),
            number: row.querySelector<HTMLInputElement>("[data-calc-number]"),
            rate: row.querySelector<HTMLElement>("[data-calc-rate]"),
        };
    };

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

        // On /hr the three time-billed values are unit-hours, priced at the
        // published hourly rate; everything is still a month's usage, so the
        // total stays a monthly figure.
        const unit = currentRateUnit();
        const hourly = unit === "hour";
        let credits = creditsForResources(values.iac_resources || 0, edition, unit);
        credits += (values.esc_secrets || 0) * (hourly ? edition.esc_secret_hour : edition.esc_secret_month);
        credits += (values.workflow_minutes || 0) * config.meters.workflow_minute;
        credits += (values.neo_tokens || 0) * config.meters.neo_tokens_per_million;
        credits +=
            (values.insights_resources || 0) *
            (hourly ? edition.insights_resource_hour : edition.insights_resource_month);

        const overage = Math.max(0, credits - edition.included_credits);
        const total = edition.base_usd + overage;
        // The threshold is a resource count, so resource-hours are brought back
        // to resources before comparing.
        const volume = (values.iac_resources || 0) / unitFactor("iac_resources") > config.contact_sales_resources;

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
        const hourly = currentRateUnit() === "hour";
        rows.forEach(row => {
            const { id, rate } = parts(row);
            const meter = METERS[id];
            if (!rate) return;
            if (!meter.rate) {
                rate.textContent = "";
                return;
            }
            // Swaps in the other already-published rate rather than deriving one
            // from the other, so it can't drift from the comparison table the way
            // monthly / 730 could. recompute() prices by it too.
            if (hourly && meter.hourly) {
                rate.textContent = `${usdRateHour.format(meter.hourly.rate(edition))}${meter.hourly.unit}`;
                return;
            }
            rate.textContent = `${usdRate.format(meter.rate(config, edition))}${meter.unit}`;
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
            const meter = METERS[id];
            const valueText = currentRateUnit() === "hour" && meter.hourly ? meter.hourly.valueText : meter.valueText;
            range.setAttribute("aria-valuetext", valueText(count.format(valueAt(pos, max))));
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

    // The number input's own ceiling has to move with the unit, or clamp() would
    // cap a resource-hour figure at the resource ceiling.
    rows.forEach(row => {
        const { number } = parts(row);
        if (number) number.dataset.calcNumberMax = number.max;
    });

    const paintUnit = (): void => {
        const hourly = currentRateUnit() === "hour";
        rows.forEach(row => {
            const { id, number } = parts(row);
            if (!METERS[id].hourly) return;
            row.querySelector("[data-calc-label-month]")?.classList.toggle("hidden", hourly);
            row.querySelector("[data-calc-label-hour]")?.classList.toggle("hidden", !hourly);
            const base = parseFloat(number?.dataset.calcNumberMax || "");
            if (number && isFinite(base)) number.max = String(base * unitFactor(id));
        });
    };

    // Converting the entered quantities, not the total, is what keeps the
    // estimate unchanged across a flip: 500 resources becomes 365,000
    // resource-hours and back. A figure typed in hours that isn't a whole month
    // of whole units rounds to the nearest unit on the way back to /mo.
    const selectRateUnit = (unit: RateUnit): void => {
        if (unit === currentRateUnit()) return;
        rows.forEach(row => {
            const { id, number } = parts(row);
            if (!METERS[id].hourly || !number) return;
            const value = valueOf(row);
            number.value = String(Math.round(unit === "hour" ? value * HOURS_PER_MONTH : value / HOURS_PER_MONTH));
        });
        rateUnitButtons.forEach(other => other.setAttribute("aria-pressed", String(other.dataset.calcRateUnit === unit)));
        paintUnit();
        rows.forEach(row => syncRow(row, "number"));
        paintRates();
        recompute();
    };

    rateUnitButtons.forEach(button => {
        button.addEventListener("click", () => {
            selectRateUnit(button.dataset.calcRateUnit as RateUnit);
        });
    });

    const buttonFor = (id: string): HTMLButtonElement | undefined =>
        editionButtons.filter(button => button.dataset.calcEdition === id)[0];

    const selectEdition = (id: string): boolean => {
        const target = buttonFor(id);
        if (!target) return false;
        editionButtons.forEach(other => other.setAttribute("aria-pressed", String(other === target)));
        paintRates();
        recompute();
        return true;
    };

    editionButtons.forEach(button => {
        button.addEventListener("click", () => {
            selectEdition(button.dataset.calcEdition || "");
        });
    });

    // Deep links from the pricing cards: #calculator-<edition> scrolls here and
    // presses that edition's toggle, so a reader who clicked "Estimate your cost"
    // on the Enterprise card doesn't land on a Team estimate. The same URL works
    // pasted into Slack.
    //
    // The hash names an edition, which is deliberately not the id of any element:
    // the section is #calculator and the toggles are buttons, and hanging the id
    // on a toggle would make the browser scroll to a control partway down the
    // card instead of to the card. So the browser has nothing to jump to and the
    // scrolling is ours — scrollIntoView honours the section's scroll-margin, so
    // it lands exactly where a plain #calculator link does.
    const EDITION_HASH = /^#calculator-(.+)$/;

    const goToEdition = (id: string, focus: boolean): boolean => {
        if (!selectEdition(id)) return false;
        root.scrollIntoView();
        // Focus follows the scroll, so a keyboard reader carries on from the
        // calculator rather than from the card they left, and a screen reader is
        // told which edition is now pressed. Not on load, where moving focus is
        // something the reader didn't ask for.
        if (focus) buttonFor(id)?.focus({ preventScroll: true });
        return true;
    };

    // Handling the click rather than leaning on `hashchange` alone is what makes
    // the second click on the same link work: the hash is already set by then, so
    // no event fires and a plain listener would sit there doing nothing.
    document.addEventListener("click", event => {
        const target = event.target as Element | null;
        const link = target && target.closest ? target.closest<HTMLAnchorElement>('a[href^="#calculator-"]') : null;
        if (!link) return;
        const match = EDITION_HASH.exec(link.hash);
        // An edition the calculator doesn't price falls through to the browser
        // rather than being swallowed here.
        if (!match || !goToEdition(decodeURIComponent(match[1]), true)) return;
        event.preventDefault();
        history.pushState(null, "", link.hash);
    });

    window.addEventListener("hashchange", () => {
        const match = EDITION_HASH.exec(window.location.hash);
        if (match) goToEdition(decodeURIComponent(match[1]), true);
    });

    paintRates();
    recompute();

    const initial = EDITION_HASH.exec(window.location.hash);
    if (initial) goToEdition(decodeURIComponent(initial[1]), false);
}

if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init, { once: true });
} else {
    init();
}
