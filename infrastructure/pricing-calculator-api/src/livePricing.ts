// Copyright 2016-2026, Pulumi Corporation.  All rights reserved.

// Reads the rates from the live /pricing/ page, so a deploy can't ship an
// estimator that quotes stale prices: index.ts either deploys with the live
// rates (toRates) or stops when they differ from ./pricing.ts (comparePricing).
// It runs before any resources are declared, which means on every `pulumi
// preview` and `pulumi up`.
//
// The source is /pricing.md, the Markdown rendering of the page that
// pulumi/marketing-web publishes for agents. Two parts of it are read:
//
//   - the "Cost estimation" section, one block per edition: a bold
//     "**Essentials** — $40/month base, which includes 40 credits and covers up
//     to 500 IaC resources." line followed by a Unit | Rate table of per-month
//     rates, then the "Past about 4,750 IaC resources" volume-pricing sentence;
//   - the edition comparison tables, for the hourly rates, which the
//     estimation section doesn't list ("$0.00025/hour ($0.1825/month)").
//
// A value the parser can't find is reported as a failure too: it means the
// page's format changed, and the check would otherwise pass by checking nothing.

import { DEFAULT_RATES, EditionRates, EDITIONS, MeterRates, METERS, PricingRates } from "./pricing";

export const DEFAULT_PRICING_URL = "https://www.pulumi.com/pricing.md";

const EDITION_KEYS = Object.keys(EDITIONS.essentials) as (keyof EditionRates)[];
const METER_KEYS = Object.keys(METERS) as (keyof MeterRates)[];

export interface LivePricing {
    editions: Record<string, Partial<EditionRates & MeterRates>>;
    contactSalesResources?: number;
}

const ESTIMATE_ROWS: Record<string, keyof (EditionRates & MeterRates)> = {
    "IaC resource, per month": "iac_resource_month",
    "ESC secret, per month": "esc_secret_month",
    "Discovered resource, per month": "insights_resource_month",
    "Workflow minute": "workflow_minute",
    "1M Neo tokens": "neo_tokens_per_million",
};

const HOURLY_ROWS: Record<string, keyof EditionRates> = {
    "Managed resource pricing": "iac_resource_hour",
    "On-demand secret price": "esc_secret_hour",
    "On-demand resource price": "insights_resource_hour",
};

const EDITION_LINE = /^\*\*(\w+)\*\* — \$([\d,.]+)\/month base, which includes ([\d,]+) credits and covers up to ([\d,]+) IaC resources\./;
const CONTACT_SALES = /Past about ([\d,]+) IaC resources/;
const HOURLY_CELL = /\$([\d.]+)\/hour/;
const DOLLARS = /^\$([\d,.]+)$/;

const num = (s: string): number => Number(s.replace(/,/g, ""));

const cells = (line: string): string[] => line.trim().replace(/^\||\|$/g, "").split("|").map(c => c.trim());

export function parseLivePricing(markdown: string): LivePricing {
    const editions: LivePricing["editions"] = {};
    const lines = markdown.split("\n");

    let current: string | undefined;
    let header: string[] = [];

    for (const line of lines) {
        const edition = EDITION_LINE.exec(line);
        if (edition) {
            current = edition[1].toLowerCase();
            editions[current] = {
                ...editions[current],
                base_usd: num(edition[2]),
                included_credits: num(edition[3]),
                included_resources: num(edition[4]),
            };
            continue;
        }
        if (line.startsWith("## ") || line.startsWith("### ")) {
            current = undefined;
        }
        if (!line.startsWith("|")) {
            continue;
        }

        const row = cells(line);
        if (row[0] === "" && row.length > 1) {
            header = row;
            continue;
        }

        const estimateKey = ESTIMATE_ROWS[row[0]];
        const rate = DOLLARS.exec(row[1] || "");
        if (current && estimateKey && rate) {
            editions[current][estimateKey] = num(rate[1]);
            continue;
        }

        const hourlyKey = HOURLY_ROWS[row[0]];
        if (hourlyKey) {
            row.forEach((cell, i) => {
                const hourly = HOURLY_CELL.exec(cell);
                const id = header[i]?.toLowerCase();
                if (hourly && id) {
                    editions[id] = { ...editions[id], [hourlyKey]: num(hourly[1]) };
                }
            });
        }
    }

    const contactSales = CONTACT_SALES.exec(markdown);
    return {
        editions,
        contactSalesResources: contactSales ? num(contactSales[1]) : undefined,
    };
}

// Returns one human-readable line per difference; empty means the rates match.
export function comparePricing(live: LivePricing, expected: PricingRates = DEFAULT_RATES): string[] {
    const problems: string[] = [];
    const check = (what: string, want: number, actual: number | undefined) => {
        if (actual === undefined) {
            problems.push(`${what}: not found on the pricing page (expected ${want})`);
        } else if (actual !== want) {
            problems.push(`${what}: src/pricing.ts has ${want}, the pricing page has ${actual}`);
        }
    };

    for (const [id, rates] of Object.entries(expected.editions)) {
        const liveRates = live.editions[id] || {};
        for (const [key, want] of Object.entries(rates)) {
            check(`${id}.${key}`, want, liveRates[key as keyof EditionRates]);
        }
        for (const [key, want] of Object.entries(expected.meters)) {
            check(`${id}.${key}`, want, liveRates[key as keyof MeterRates]);
        }
    }

    for (const id of liveEditionIds(live)) {
        if (!(id in expected.editions)) {
            problems.push(`${id}: edition is on the pricing page but not in src/pricing.ts`);
        }
    }

    check("contact_sales_resources", expected.contactSalesResources, live.contactSalesResources);
    return problems;
}

// The editions the page offers an estimate for. The hourly rows also mention
// Free, which has no estimate block and so no base price.
function liveEditionIds(live: LivePricing): string[] {
    return Object.keys(live.editions).filter(id => live.editions[id].base_usd !== undefined);
}

export type RatesResult = { ok: true; rates: PricingRates } | { ok: false; problems: string[] };

// Builds a complete set of rates from the page, for a deploy to use in place of
// DEFAULT_RATES. All or nothing: a value missing from the page means the format
// changed, and half-live rates would be worse than either complete set.
export function toRates(live: LivePricing): RatesResult {
    const problems: string[] = [];
    const editions: Record<string, EditionRates> = {};
    const ids = liveEditionIds(live);
    if (ids.length === 0) {
        problems.push("no editions found on the pricing page");
    }

    for (const id of ids) {
        const found = live.editions[id];
        const missing = EDITION_KEYS.filter(key => found[key] === undefined);
        if (missing.length > 0) {
            problems.push(`${id}: not found on the pricing page: ${missing.join(", ")}`);
            continue;
        }
        const rates = {} as EditionRates;
        for (const key of EDITION_KEYS) {
            rates[key] = found[key] as number;
        }
        editions[id] = rates;
    }

    // The page repeats the shared meters under every edition, so they have to
    // agree before there's one value to use.
    const meters = {} as MeterRates;
    for (const key of METER_KEYS) {
        const values = Array.from(new Set(ids.map(id => live.editions[id][key])));
        if (values.length !== 1 || values[0] === undefined) {
            problems.push(`${key}: expected one value across editions, found ${values.join(", ")}`);
        } else {
            meters[key] = values[0];
        }
    }

    if (live.contactSalesResources === undefined) {
        problems.push("contact_sales_resources: not found on the pricing page");
    }

    if (problems.length > 0) {
        return { ok: false, problems };
    }
    return { ok: true, rates: { editions, meters, contactSalesResources: live.contactSalesResources as number } };
}

export async function fetchLivePricing(url: string = DEFAULT_PRICING_URL, timeoutMs = 15000): Promise<LivePricing> {
    const res = await fetch(url, { signal: AbortSignal.timeout(timeoutMs) });
    if (!res.ok) {
        throw new Error(`GET ${url} returned ${res.status}`);
    }
    return parseLivePricing(await res.text());
}
