// Copyright 2016-2026, Pulumi Corporation.  All rights reserved.

// The arithmetic of the /pricing/ cost calculator, ported from the Hugo-era
// theme/src/ts/pricing-calculator.ts and the `calculator:` block of
// data/pulumi_pricing.yaml (both removed in 812ea928fe when /pricing moved to
// pulumi/marketing-web). marketing-web's apps/www/src/data/pricing/ owns the
// list prices now. The running Lambda picks up changed prices from the live
// page on its own (liveRates.ts), but keep EDITIONS and METERS in step: they're
// what it serves until the first refresh, and whenever the page can't be read.
//
// Everything is denominated in Pulumi Credits (1 credit = $1) drawn from one
// shared pool, and the monthly base buys the first tranche of it.

export type RateUnit = "month" | "hour";

export const HOURS_PER_MONTH = 730;

// Above this many IaC resources (per month), volume pricing usually applies, so
// the list-rate figure is an upper bound rather than a quote.
export const CONTACT_SALES_RESOURCES = 4750;

export interface EditionRates {
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

// Meters priced the same on every edition.
export interface MeterRates {
    workflow_minute: number;
    neo_tokens_per_million: number;
}

export const METERS: MeterRates = {
    workflow_minute: 0.01,
    neo_tokens_per_million: 3,
};

export const EDITIONS: Record<string, EditionRates> = {
    essentials: {
        base_usd: 40,
        included_credits: 40,
        included_resources: 500,
        iac_resource_month: 0.1825,
        iac_resource_hour: 0.00025,
        esc_secret_month: 0.50,
        esc_secret_hour: 0.000685,
        insights_resource_month: 0.0185,
        insights_resource_hour: 0.000025,
    },
    pro: {
        base_usd: 400,
        included_credits: 400,
        included_resources: 2000,
        iac_resource_month: 0.365,
        iac_resource_hour: 0.0005,
        esc_secret_month: 0.75,
        esc_secret_hour: 0.001,
        insights_resource_month: 0.0365,
        insights_resource_hour: 0.00005,
    },
    enterprise: {
        base_usd: 2000,
        included_credits: 2000,
        included_resources: 4750,
        iac_resource_month: 0.5475,
        iac_resource_hour: 0.00075,
        esc_secret_month: 1.00,
        esc_secret_hour: 0.00137,
        insights_resource_month: 0.05475,
        insights_resource_hour: 0.000075,
    },
};

// Everything an estimate depends on. DEFAULT_RATES is the copy kept in this
// file; the running Lambda replaces it with the rates read from the live
// pricing page when it can (see liveRates.ts).
export interface PricingRates {
    editions: Record<string, EditionRates>;
    meters: MeterRates;
    contactSalesResources: number;
}

export const DEFAULT_RATES: PricingRates = {
    editions: EDITIONS,
    meters: METERS,
    contactSalesResources: CONTACT_SALES_RESOURCES,
};

// iacResources, escSecrets, and insightsResources are counts held for the whole
// month, priced at the monthly rates. The matching *Hours fields are
// unit-hours, priced at the hourly rates, and a request can use both: a
// resource that existed for only part of the month goes in iacResourceHours.
// Workflow minutes and Neo tokens are billed per use, so they have no hourly
// form.
export interface Usage {
    edition: string;
    iacResources: number;
    iacResourceHours: number;
    escSecrets: number;
    escSecretHours: number;
    workflowMinutes: number;
    neoMillionTokens: number;
    insightsResources: number;
    insightsResourceHours: number;
}

export interface Estimate {
    edition: string;
    creditsUsed: number;
    includedCredits: number;
    baseUsd: number;
    overageUsd: number;
    totalUsd: number;
    volumePricingLikely: boolean;
}

// The included credits cover the first tranche of resources at a discounted
// rate; resources beyond it are charged the list rate. This is what makes
// Essentials exactly $40 at 500 resources and $131.25 at 1,000.
export function creditsForResources(quantity: number, edition: EditionRates, unit: RateUnit): number {
    const hourly = unit === "hour";
    const included = edition.included_resources * (hourly ? HOURS_PER_MONTH : 1);
    if (quantity <= included) {
        return quantity * (edition.included_credits / included);
    }
    const beyond = quantity - included;
    return edition.included_credits + beyond * (hourly ? edition.iac_resource_hour : edition.iac_resource_month);
}

const roundCents = (n: number): number => Math.round(n * 100) / 100;

// Resources and resource-hours share one included tranche, so they're pooled
// as resource-hours before it applies: on Essentials, 400 resources plus 73,000
// resource-hours (100 resources' worth) exactly fill the 500 included. A
// request with no hours is priced in months, which keeps a month-only estimate
// on the monthly rates.
export function iacCredits(resources: number, hours: number, edition: EditionRates): number {
    if (hours === 0) {
        return creditsForResources(resources, edition, "month");
    }
    return creditsForResources(resources * HOURS_PER_MONTH + hours, edition, "hour");
}

export function estimate(usage: Usage, rates: PricingRates = DEFAULT_RATES): Estimate {
    const e = Object.prototype.hasOwnProperty.call(rates.editions, usage.edition)
        ? rates.editions[usage.edition]
        : undefined;
    if (!e) {
        throw new Error(`unknown edition ${JSON.stringify(usage.edition)}`);
    }

    let credits = iacCredits(usage.iacResources, usage.iacResourceHours, e);
    credits += usage.escSecrets * e.esc_secret_month + usage.escSecretHours * e.esc_secret_hour;
    credits += usage.workflowMinutes * rates.meters.workflow_minute;
    credits += usage.neoMillionTokens * rates.meters.neo_tokens_per_million;
    credits += usage.insightsResources * e.insights_resource_month +
        usage.insightsResourceHours * e.insights_resource_hour;

    const overage = Math.max(0, credits - e.included_credits);
    const monthlyResources = usage.iacResources + usage.iacResourceHours / HOURS_PER_MONTH;

    return {
        edition: usage.edition,
        creditsUsed: Math.round(credits * 1e6) / 1e6,
        includedCredits: e.included_credits,
        baseUsd: e.base_usd,
        overageUsd: roundCents(overage),
        totalUsd: roundCents(e.base_usd + overage),
        volumePricingLikely: monthlyResources > rates.contactSalesResources,
    };
}
