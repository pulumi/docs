const filterResourceItems = (filters) => {
    const monthGroups = document.querySelectorAll<HTMLElement>(".event-list .month-label");
    const separator = document.querySelector<HTMLElement>(".event-list .event-list-separator");
    const noResultsMessage = document.querySelector(".template-event-list .no-results");
    noResultsMessage?.classList.remove("hidden");

    const activeTab = location.hash.slice(1) || "all";

    monthGroups.forEach(group => {
        const groupFilters = (group.getAttribute("data-filters") || "").split(" ");

        // For the "all" tab, show all groups. Otherwise, only show matching tab.
        if (activeTab !== "all" && !groupFilters.includes(activeTab)) {
            group.style.display = "none";
            return;
        }

        const cards = group.querySelectorAll<HTMLElement>("li[data-filters]");
        let visibleCards = 0;

        cards.forEach(card => {
            const tags = (card.getAttribute("data-filters") || "").split(" ");

            if (filters.length > 0) {
                const matches = filters.some(f => tags.includes(f));
                if (matches) {
                    card.style.display = "";
                    visibleCards++;
                } else {
                    card.style.display = "none";
                }
            } else {
                card.style.display = "";
                visibleCards++;
            }
        });

        group.style.display = visibleCards > 0 ? "block" : "none";
        if (visibleCards > 0) {
            noResultsMessage?.classList.add("hidden");
        }
    });

    // Show separator only on "all" tab when no filters are active.
    if (separator) {
        separator.style.display = (activeTab === "all" && filters.length === 0) ? "" : "none";
    }
}

document.querySelector(".pulumi-event-list-container")?.addEventListener("filterSelect", (event: CustomEvent) => {
    const filters = event.detail as any[];
    const filtersText: string[] = [];

    filters.forEach(filter => {
        filtersText.push(filter.value);
    });

    filterResourceItems(filtersText);
});

window.addEventListener('hashchange', function() {
    const options = Array.from(document.querySelectorAll('pulumi-filter-select-option')) as any[];
    let selectedFilters = [];

    options.forEach((option) => {
        const shadow = option.shadowRoot;
        if (shadow?.querySelector('.selected')) {
            selectedFilters.push(option.value);
        }
    });
    filterResourceItems(selectedFilters);
});

// Client-side "in X days" / "Today" badges for upcoming events. Rendered here
// rather than at build time: the site rebuilds only periodically, so a baked-in
// relative label would go stale, and the correct day count depends on each
// visitor's own timezone. The card emits the absolute event datetime; we compute
// the relative label against the visitor's local midnight.
// Show the countdown badge only when the event is less than a week out.
const COUNTDOWN_MAX_DAYS = 6;

const renderEventCountdowns = () => {
    const startOfDay = (d: Date) => new Date(d.getFullYear(), d.getMonth(), d.getDate());
    const todayStart = startOfDay(new Date());

    document.querySelectorAll<HTMLElement>("[data-event-countdown]").forEach(el => {
        const iso = el.getAttribute("data-event-date");
        if (!iso) return;
        const event = new Date(iso);
        if (isNaN(event.getTime())) return;

        const diffDays = Math.round((startOfDay(event).getTime() - todayStart.getTime()) / 86_400_000);

        if (diffDays === 0) {
            el.textContent = "Today";
            el.className = "badge badge-default";
        } else if (diffDays >= 1 && diffDays <= COUNTDOWN_MAX_DAYS) {
            el.textContent = diffDays === 1 ? "in 1 day" : `in ${diffDays} days`;
            el.className = "badge badge-brand";
        } else {
            return; // more than a week out (or already past) — leave hidden
        }
        el.removeAttribute("hidden");
    });
};

// The date tile on an event card is rendered in the event's own timezone, which
// is only right for the people in it: a 6pm Pacific session is 3am the next day
// in Berlin, so the day and the month can both be off, not just the hour. Rewrite
// the whole tile against the visitor's clock and add the local start time — the
// case this exists for is an event offered on two dates for two regions, where
// "which one is actually convenient for me" is the only question the card has to
// answer.
const renderEventDateTiles = () => {
    document.querySelectorAll<HTMLElement>("[data-event-tile]").forEach(tile => {
        const iso = tile.getAttribute("data-event-date");
        if (!iso) return;
        const date = new Date(iso);
        if (isNaN(date.getTime())) return;

        const day = tile.querySelector<HTMLElement>("[data-event-tile-day]");
        const month = tile.querySelector<HTMLElement>("[data-event-tile-month]");
        const time = tile.querySelector<HTMLElement>("[data-event-tile-time]");

        if (day) day.textContent = date.toLocaleDateString(undefined, { day: "numeric" });
        if (month) month.textContent = date.toLocaleDateString(undefined, { month: "short" });
        if (time) {
            // "short", not "shortGeneric": the generic form reads better in the US
            // ("PT" over "PDT") but only there — every other zone falls back to a
            // full phrase ("9PM Germany Time", "12AM India Time") that a 4rem tile
            // clips. "short" stays abbreviated everywhere ("9PM GMT+2").
            // Minutes only when there are any, so the common on-the-hour case
            // stays narrow enough for the tile: "9AM PDT", not "9:00 AM PDT".
            const options: Intl.DateTimeFormatOptions = { hour: "numeric", timeZoneName: "short" };
            if (date.getMinutes() !== 0) {
                options.minute = "2-digit";
            }
            // Close up the gap before AM/PM ("9AM PDT") — it buys a character of
            // width in a 4rem tile and reads fine at this size. `\s` covers both
            // the plain space older browsers use and the narrow no-break space
            // (U+202F) current ones do; locales without AM/PM simply don't match.
            time.textContent = date
                .toLocaleTimeString(undefined, options)
                .replace(/\s+([AaPp]\.?[Mm]\.?)/, "$1");
            time.removeAttribute("hidden");
        }
    });
};

// Every other event date Hugo renders — the Date field in the timing row, the
// date on a session tab — localized to match the card tile above. Hugo can only
// format these in the event's own timezone, which puts the page a calendar day
// off from the card that linked to it: a 12PM Pacific session is 4AM the next
// morning in Tokyo, so the card says "20 Aug" and an un-rewritten page says
// "Aug 19". The server-rendered text stays as the no-JS fallback.
const LOCAL_DATE_FORMATS: Record<string, Intl.DateTimeFormatOptions> = {
    // "Aug 19" — the session tabs, where the year is noise.
    short: { month: "short", day: "numeric" },
    // "Aug 19, 2026" — matches Hugo's `:date_medium`.
    medium: { year: "numeric", month: "short", day: "numeric" },
};

const renderLocalDates = () => {
    document.querySelectorAll<HTMLElement>("[data-local-date]").forEach(el => {
        const iso = el.getAttribute("data-local-date");
        if (!iso) return;
        const date = new Date(iso);
        if (isNaN(date.getTime())) return;

        const options = LOCAL_DATE_FORMATS[el.getAttribute("data-local-date-format") || "medium"];
        if (!options) return;

        el.textContent = date.toLocaleDateString(undefined, options);
    });
};

// Apply initial filter state on page load.
if (document.querySelector(".template-event-list")) {
    filterResourceItems([]);
}

// Keyed off the cards themselves, not the event list: event cards also render
// outside /events/ (e.g. the homepage "what's new" row). No-ops when there are none.
renderEventCountdowns();
renderEventDateTiles();
renderLocalDates();
