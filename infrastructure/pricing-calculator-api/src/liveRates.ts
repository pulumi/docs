// Copyright 2016-2026, Pulumi Corporation.  All rights reserved.

// Keeps a running Lambda's rates current between deploys. The deploy bakes in
// the rates it read (PRICING_RATES; see index.ts), and on top of that the
// handler re-reads the pricing page at most once per PRICING_REFRESH_SECONDS,
// so a price change on /pricing/ reaches callers within the hour without anyone
// running `pulumi up`.
//
// It fails safe: if the page can't be fetched or doesn't parse into a complete
// set of rates (toRates is all or nothing), the handler keeps serving the last
// good rates, which start as the deployed ones, and logs
// "pricing_rates_refresh_failed". index.ts turns that log line into an alarm.

import { comparePricing, fetchLivePricing, LivePricing, toRates } from "./livePricing";
import { PricingRates } from "./pricing";

export type RatesSource = "deployed" | "live";

export interface RefreshConfig {
    url?: string;
    ttlMs: number;
    fetchTimeoutMs: number;
}

// Mutated in place across invocations of a warm container. A plain object,
// not a class instance or Map, because the handler reaches it through Pulumi's
// closure serialization, which recreates captured objects as literals.
export interface RateCache {
    rates?: PricingRates;
    source: RatesSource;
    checkedAt?: number;
    refreshedAt?: number;
}

export interface CurrentRates {
    rates: PricingRates;
    source: RatesSource;
    refreshedAt?: number;
}

export function refreshConfigFromEnv(env: Record<string, string | undefined> = process.env): RefreshConfig {
    const seconds = Number(env.PRICING_REFRESH_SECONDS || "0");
    return {
        url: env.PRICING_URL || undefined,
        ttlMs: Number.isFinite(seconds) && seconds > 0 ? seconds * 1000 : 0,
        fetchTimeoutMs: 3000,
    };
}

export async function currentRates(
    cache: RateCache,
    deployed: PricingRates,
    config: RefreshConfig,
    now: number = Date.now(),
    fetchPricing: (url: string, timeoutMs: number) => Promise<LivePricing> = fetchLivePricing,
): Promise<CurrentRates> {
    const current = (): CurrentRates => cache.rates
        ? { rates: cache.rates, source: cache.source, refreshedAt: cache.refreshedAt }
        : { rates: deployed, source: "deployed" };

    if (!config.url || config.ttlMs <= 0) {
        return { rates: deployed, source: "deployed" };
    }
    if (cache.checkedAt !== undefined && now - cache.checkedAt < config.ttlMs) {
        return current();
    }

    // Stamped before the fetch, so a failing page is retried once per TTL
    // rather than on every request.
    cache.checkedAt = now;
    let problems: string[];
    try {
        const result = toRates(await fetchPricing(config.url, config.fetchTimeoutMs));
        if (result.ok) {
            const changed = comparePricing(fromRates(result.rates), cache.rates || deployed);
            if (changed.length > 0) {
                console.log(JSON.stringify({ type: "pricing_rates_refreshed", url: config.url, changed }));
            }
            cache.rates = result.rates;
            cache.source = "live";
            cache.refreshedAt = now;
            return current();
        }
        problems = result.problems;
    } catch (err) {
        problems = [err instanceof Error ? err.message : String(err)];
    }

    console.error(JSON.stringify({ type: "pricing_rates_refresh_failed", url: config.url, problems }));
    return current();
}

// comparePricing takes the page's shape; this rebuilds it from a complete set
// of rates so the refresh can log exactly which values moved.
function fromRates(rates: PricingRates): LivePricing {
    const editions: LivePricing["editions"] = {};
    for (const [id, edition] of Object.entries(rates.editions)) {
        editions[id] = { ...edition, ...rates.meters };
    }
    return { editions, contactSalesResources: rates.contactSalesResources };
}
