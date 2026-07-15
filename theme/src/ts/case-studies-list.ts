// /case-studies/ industry filter: narrows the card grid to a single industry in
// place, defaulting to "All". Progressive enhancement — the pills are real anchor
// links to the canonical term pages (/case-studies/industry/<slug>/) as the no-JS
// / crawler fallback, and every card is server-rendered in the DOM on every page;
// this only shows/hides and swaps the address bar.
//
// Unlike the blog feed (paginated, so it fetches row fragments), the case-studies
// index renders all cards up front, so filtering is a pure show/hide. The URL is
// rewritten to the REAL term-page URL (like the blog filter) — not a query — so
// shared/bookmarked links hit the indexed, server-rendered page. The index and
// every term page render identical markup, so clicking a pill (or Back/Forward)
// never navigates: the hero and grid stay put and only the URL, active pill, and
// visible cards change.
//
// DOM contract (rendered by layouts/partials/case-studies/{filter-bar,board,card}.html):
//   [data-case-study-filter]                      the filter bar
//   [data-case-study-filter] a[data-industry]     a pill ("" = All), .is-active
//   [data-case-study-card][data-industry]         one card

document.addEventListener("DOMContentLoaded", () => {
    const filterBar = document.querySelector<HTMLElement>("[data-case-study-filter]");
    if (!filterBar) {
        return;
    }

    const pills = Array.from(filterBar.querySelectorAll<HTMLAnchorElement>("a[data-industry]"));
    const cards = Array.from(document.querySelectorAll<HTMLElement>("[data-case-study-card]"));
    const originalTitle = document.title;

    function industryUrl(industry: string): string {
        return industry ? `/case-studies/industry/${industry}/` : "/case-studies/";
    }

    function industryFromLocation(): string {
        const m = location.pathname.match(/^\/case-studies\/industry\/([^/]+)\/$/);
        return m ? m[1] : "";
    }

    function syncTitle(industry: string): void {
        const pill = industry ? pills.find(p => (p.dataset.industry || "") === industry) : null;
        // The pill text carries the count badge too; take the first line only.
        const name = pill ? pill.textContent!.trim().split("\n")[0].trim() : "";
        document.title = name ? `${name} | Case Studies | Pulumi` : originalTitle;
    }

    function apply(industry: string, push: boolean): void {
        pills.forEach(pill => {
            const on = (pill.dataset.industry || "") === industry;
            pill.classList.toggle("is-active", on);
            if (on) {
                pill.setAttribute("aria-current", "page");
            } else {
                pill.removeAttribute("aria-current");
            }
        });
        cards.forEach(card => {
            card.hidden = industry !== "" && card.dataset.industry !== industry;
        });
        if (push) {
            history.pushState(null, "", industryUrl(industry));
        }
        syncTitle(industry);
    }

    filterBar.addEventListener("click", e => {
        const pill = (e.target as HTMLElement).closest<HTMLAnchorElement>("a[data-industry]");
        if (!pill) {
            return;
        }
        e.preventDefault();
        apply(pill.dataset.industry || "", true);
    });

    // Back/Forward walks the pushed history entries in place (both the index and
    // every term page render the same DOM, so no reload is needed).
    window.addEventListener("popstate", () => {
        apply(industryFromLocation(), false);
    });
});
