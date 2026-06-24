type ThemePref = "light" | "dark" | "system";

const STORAGE_KEY = "pulumi-docs-theme";
const DARK_QUERY = "(prefers-color-scheme: dark)";

function isDocs(): boolean {
    return document.body.classList.contains("section-docs");
}

function readPref(): ThemePref {
    try {
        const stored = localStorage.getItem(STORAGE_KEY);
        if (stored === "light" || stored === "dark" || stored === "system") {
            return stored;
        }
    } catch (e) {
        return "system";
    }
    return "system";
}

function systemPrefersDark(): boolean {
    return typeof window.matchMedia === "function" && window.matchMedia(DARK_QUERY).matches;
}

function resolve(pref: ThemePref): "light" | "dark" {
    if (pref === "system") {
        return systemPrefersDark() ? "dark" : "light";
    }
    return pref;
}

function reflectButtons(pref: ThemePref): void {
    const buttons = document.querySelectorAll<HTMLButtonElement>("[data-theme-set]");
    buttons.forEach(button => {
        button.setAttribute("aria-pressed", String(button.dataset.themeSet === pref));
    });
}

function apply(pref: ThemePref): void {
    const el = document.documentElement;
    el.dataset.themePref = pref;
    if (resolve(pref) === "dark") {
        el.dataset.theme = "dark";
        document.body.dataset.theme = "dark";
    } else {
        delete el.dataset.theme;
        delete document.body.dataset.theme;
    }
    reflectButtons(pref);
}

function persist(pref: ThemePref): void {
    try {
        localStorage.setItem(STORAGE_KEY, pref);
    } catch (e) {
        return;
    }
}

function init(): void {
    if (!isDocs()) {
        return;
    }

    apply(readPref());

    const buttons = document.querySelectorAll<HTMLButtonElement>(".docs-theme-toggle [data-theme-set]");
    buttons.forEach(button => {
        button.addEventListener("click", () => {
            const next = button.dataset.themeSet as ThemePref;
            persist(next);
            apply(next);
        });
    });

    if (typeof window.matchMedia === "function") {
        const media = window.matchMedia(DARK_QUERY);
        const onChange = (): void => {
            if (readPref() === "system") {
                apply("system");
            }
        };
        if (typeof media.addEventListener === "function") {
            media.addEventListener("change", onChange);
        } else if (typeof media.addListener === "function") {
            media.addListener(onChange);
        }
    }
}

if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
} else {
    init();
}
