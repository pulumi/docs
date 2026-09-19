const STORIES_PARAM = "case-studies";

document.addEventListener("DOMContentLoaded", () => {
    const filterBar = document.querySelector<HTMLElement>("[data-customer-filter]");
    if (!filterBar) {
        return;
    }

    const fadeWrap = filterBar.parentElement;
    const pills = Array.from(filterBar.querySelectorAll<HTMLAnchorElement>("a[data-industry]"));
    const storiesToggle = document.querySelector<HTMLButtonElement>("[data-customer-toggle-stories]");
    const expandToggle = document.querySelector<HTMLButtonElement>("[data-customer-filter-expand]");
    const cells = Array.from(document.querySelectorAll<HTMLElement>("[data-customer-cell]"));
    const heading = document.getElementById("customers-heading");
    const originalTitle = heading?.dataset.defaultTitle ?? document.title;
    const originalHeading = heading?.dataset.defaultHeading ?? "";

    function hrefFor(industry: string, storiesOnly: boolean): string {
        const path = industry ? `/customers/industry/${industry}/` : "/customers/";
        return storiesOnly ? `${path}?${STORIES_PARAM}=1` : path;
    }

    function industryFromLocation(): string {
        const m = location.pathname.match(/^\/customers\/industry\/([^/]+)\/$/);
        return m ? m[1] : "";
    }

    function storiesFromLocation(): boolean {
        return new URLSearchParams(location.search).get(STORIES_PARAM) === "1";
    }

    function syncTitle(industry: string): void {
        const pill = industry ? pills.find(p => (p.dataset.industry || "") === industry) : null;
        const name = pill ? pill.textContent!.trim().split("\n")[0].trim() : "";
        document.title = name ? `${name} | Customers | Pulumi` : originalTitle;
        if (heading) {
            heading.textContent = name ? `${name} customers` : originalHeading;
        }
    }

    function render(industry: string, storiesOnly: boolean, pushHistory: boolean): void {
        pills.forEach(pill => {
            const isActive = (pill.dataset.industry || "") === industry;
            pill.classList.toggle("is-active", isActive);
            if (isActive) {
                pill.setAttribute("aria-current", "page");
            } else {
                pill.removeAttribute("aria-current");
            }
        });
        storiesToggle?.setAttribute("aria-checked", String(storiesOnly));
        cells.forEach(cell => {
            const wrongIndustry = industry !== "" && cell.dataset.industry !== industry;
            const noStory = storiesOnly && !("hasStory" in cell.dataset);
            cell.hidden = wrongIndustry || noStory;
        });
        if (pushHistory) {
            history.pushState(null, "", hrefFor(industry, storiesOnly));
        }
        syncTitle(industry);
    }

    function syncFades(): void {
        if (!fadeWrap) {
            return;
        }
        const scrolled = filterBar.scrollLeft;
        const remaining = filterBar.scrollWidth - filterBar.clientWidth - scrolled;
        fadeWrap.classList.toggle("has-overflow-start", scrolled > 1);
        fadeWrap.classList.toggle("has-overflow-end", remaining > 1);
    }

    filterBar.addEventListener("scroll", syncFades, { passive: true });
    window.addEventListener("resize", syncFades);
    syncFades();

    filterBar.addEventListener("click", e => {
        const pill = (e.target as HTMLElement).closest<HTMLAnchorElement>("a[data-industry]");
        if (!pill) {
            return;
        }
        e.preventDefault();
        render(pill.dataset.industry || "", storiesFromLocation(), true);
    });

    expandToggle?.addEventListener("click", () => {
        const bar = expandToggle.closest(".customer-filter-bar");
        const expanded = bar?.classList.toggle("is-expanded") ?? false;
        expandToggle.setAttribute("aria-expanded", String(expanded));
        syncFades();
    });

    storiesToggle?.addEventListener("click", () => {
        render(industryFromLocation(), !storiesFromLocation(), true);
    });

    window.addEventListener("popstate", () => {
        render(industryFromLocation(), storiesFromLocation(), false);
    });

    if (storiesFromLocation()) {
        render(industryFromLocation(), true, false);
    }
});
