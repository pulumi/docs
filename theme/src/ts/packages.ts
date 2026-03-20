const filterByTextAndTags = (filters, filterText) => {
    const AMAZON_STRING: string = "amazon";
    const AWS_STRING: string = "aws";
    const GOOGLE_CLOUD_STRING: string = "gcp";
    const GCP_STRING: string = "google cloud";
    const GOOGLE_STRING: string = "google";

    const packages = document.querySelectorAll<HTMLElement>(".all-packages .package");

    const noSelectedType = filters.find(f => f.group === "type") === undefined;
    const noSelectedCategory = filters.find(f => f.group === "category") === undefined;

    if (filters.length > 0 || filterText) {
        packages.forEach(pkg => pkg.classList.add("hidden"));

        packages.forEach(pkg => {
            const el = pkg.querySelector("[data-category]") as HTMLElement;
            if (!el) return;

            const packageType = el.getAttribute("data-type");
            const packageCategory = el.getAttribute("data-category");
            const packageIsNative = packageType === "native-provider";

            const packageHasSelectedType =
                !!filters.find(f => f.group === "type" && f.value === packageType) || (filters.find(f => f.group === "type" && f.value === "provider") && packageIsNative);
            const packageHasSelectedCategory = !!filters.find(f => f.group === "category" && f.value === packageCategory);

            const packageTitle = el.getAttribute("data-title");
            const downcasedPackageTitle = packageTitle.toLowerCase();
            const downcasedFilterText = filterText?.trim().toLowerCase();

            let packageIsAMatch;

            if (downcasedFilterText === AMAZON_STRING || downcasedFilterText === AWS_STRING){
                packageIsAMatch = downcasedPackageTitle.includes(AMAZON_STRING) || downcasedPackageTitle.includes(AWS_STRING);
            } else if (downcasedFilterText === GOOGLE_CLOUD_STRING || downcasedFilterText === GCP_STRING || downcasedFilterText === GOOGLE_STRING){
                packageIsAMatch = downcasedPackageTitle.includes(GOOGLE_CLOUD_STRING) || downcasedPackageTitle.includes(GCP_STRING) || downcasedPackageTitle.includes(GOOGLE_STRING);
            } else {
                packageIsAMatch = downcasedPackageTitle.includes(downcasedFilterText);
            }

            if ((packageHasSelectedType || noSelectedType) && (packageHasSelectedCategory || noSelectedCategory) && (!filterText || packageIsAMatch)) {
                pkg.classList.remove("hidden");
            }
        });
    } else {
        packages.forEach(pkg => pkg.classList.remove("hidden"));
    }
}

document.querySelector(".section-registry")?.addEventListener("filterSelect", (event: CustomEvent) => {
    const source: any = event.target;
    const filters = event.detail as any[];

    const searchElement = document.querySelector("pulumi-registry-list-search") as any;
    const inputElement = searchElement?.querySelector('.registry-filter-input') as HTMLInputElement;
    const filterText = inputElement?.value || "";

    filterByTextAndTags(filters, filterText);

    const activeTags = document.querySelector("ul.active-tags");
    if (activeTags) {
        activeTags.innerHTML = "";

        filters.forEach(filter => {
            const template = document.getElementById("active-tag-template") as HTMLTemplateElement;
            if (!template) return;
            const wrapper = document.createElement("div");
            wrapper.innerHTML = template.innerHTML;
            const tag = wrapper.firstElementChild as HTMLElement;
            activeTags.appendChild(tag);
            tag.setAttribute("data-filter-group", filter.group);
            tag.setAttribute("data-filter-value", filter.value);
            const span = tag.querySelector("span");
            if (span) span.textContent = filter.label;
            const btn = tag.querySelector("button");
            if (btn) btn.addEventListener("click", () => source.deselect(filter));
        });
    }

    const selectedTypes = filters.filter(f => f.group === "type").map(t => t.value).join(",");
    const selectedCategories = filters.filter(f => f.group === "category").map(t => t.value).join(",");

    document.querySelectorAll(".packages, .active-tags").forEach(el => {
        el.setAttribute("data-selected-types", selectedTypes);
        el.setAttribute("data-selected-categories", selectedCategories);
    });

    const allCount = document.querySelectorAll(".all-packages .package:not(.hidden)").length;
    document.querySelectorAll(".all-count").forEach(el => el.textContent = String(allCount));

    document.querySelectorAll("pulumi-filter-select-option-group").forEach((el: any) => el.close());
});

document.querySelector(".section-registry .no-results .reset")?.addEventListener("click", event => {
    event.stopPropagation();

    const search = document.querySelector("pulumi-registry-list-search") as any;
    search?.reset();

    const fs = document.querySelector("pulumi-filter-select") as any;
    fs?.reset();

    filterByTextAndTags([], "");

    const allCount = document.querySelectorAll(".all-packages .package:not(.hidden)").length;
    document.querySelectorAll(".all-count").forEach(el => el.textContent = String(allCount));
});

document.querySelector(".section-registry")?.addEventListener("packageSearch", (event: CustomEvent) => {
    const filterText = event.detail as any;

    const filters = [];
    const activeTags = document.querySelectorAll("ul.active-tags li");

    activeTags.forEach(tag => {
        const tagCategory = tag.getAttribute("data-filter-group");
        const tagValue = tag.getAttribute("data-filter-value");
        const tagLabel = tag.getAttribute("data-filter-label");

        filters.push({group: tagCategory, value: tagValue, label: tagLabel});
    });

    filterByTextAndTags(filters, filterText);

    const allCount = document.querySelectorAll(".all-packages .package:not(.hidden)").length;
    document.querySelectorAll(".all-count").forEach(el => el.textContent = String(allCount));
});


document.addEventListener("DOMContentLoaded", function () {
    const logoNavMenuButton = document.querySelector(".logo-nav-button") as HTMLElement;
    const bgMask = document.querySelector(".logo-nav-bg-mask") as HTMLElement;
    const logoNavMenu = document.getElementById("logo-nav-menu");

    if (!logoNavMenuButton || !logoNavMenu) return;

    function toggleMenu() {
        logoNavMenu.classList.toggle("hidden");
        const navMenuVisible = !logoNavMenu.classList.contains("hidden");
        logoNavMenuButton.setAttribute("aria-expanded", `${navMenuVisible}`);
        document.querySelectorAll(".logo-nav-button .mobile-menu-toggle-icon").forEach(el => el.classList.toggle("hidden"));
        bgMask?.classList.toggle("hidden");
    }

    logoNavMenuButton.addEventListener("click", toggleMenu);
    bgMask?.addEventListener("click", toggleMenu);

    document.addEventListener("click", function (event) {
        const target = event.target as HTMLElement;
        if (!target.closest(".logo-nav-button") && !target.closest("#logo-nav-menu") && !logoNavMenu.classList.contains("hidden")) {
            toggleMenu();
        }
    });

    document.addEventListener("scroll", function () {
        const PRACTITIONER_NAV_HEIGHT = 53;
        if (window.scrollY > PRACTITIONER_NAV_HEIGHT && !logoNavMenu.classList.contains("hidden")) {
            toggleMenu();
        }
    });
});
