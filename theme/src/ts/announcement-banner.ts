import { LocalStorageService } from "./state";

(function () {
    const STORAGE_KEY = "announcement-banner";
    const DISMISSED_FIELD = "dismissed";
    const REVEAL_STYLE_ID = "announcement-banner-reveal";

    function init() {
        const wrapper = document.getElementById("announcement-banner");
        if (!wrapper) return;

        const store = new LocalStorageService(STORAGE_KEY);
        const allIds = Array.from(wrapper.querySelectorAll<HTMLElement>(".announcement"))
            .map((el) => el.dataset.announcementId || "")
            .filter(Boolean);

        let marqueeCleanup: (() => void) | null = null;

        const getDismissed = (): string[] => {
            const d = store.getKey(DISMISSED_FIELD);
            return Array.isArray(d) ? d : [];
        };

        const updateRevealStyle = (id: string | null) => {
            let styleEl = document.getElementById(REVEAL_STYLE_ID) as HTMLStyleElement | null;
            if (!styleEl) {
                styleEl = document.createElement("style");
                styleEl.id = REVEAL_STYLE_ID;
                document.head.appendChild(styleEl);
            }
            if (id) {
                styleEl.textContent =
                    '#announcement-banner{display:block!important}' +
                    `#announcement-banner .announcement[data-announcement-id="${id}"]{display:flex!important}`;
                document.documentElement.setAttribute("data-announcement-chosen", id);
            } else {
                styleEl.textContent = "#announcement-banner{display:none!important}";
                document.documentElement.removeAttribute("data-announcement-chosen");
            }
        };

        const setupMarquee = (el: HTMLElement) => {
            if (marqueeCleanup) {
                marqueeCleanup();
                marqueeCleanup = null;
            }
            const marquee = el.querySelector<HTMLElement>("[data-announcement-marquee]");
            const content = el.querySelector<HTMLElement>("[data-announcement-content]");
            const text = el.querySelector<HTMLElement>(".announcement-text");
            if (!marquee || !content || !text) return;

            let clone: HTMLElement | null = null;
            let rafId = 0;
            const check = () => {
                rafId = 0;
                const overflows = text.scrollWidth > marquee.clientWidth;
                marquee.classList.toggle("is-overflowing", overflows);
                if (overflows && !clone) {
                    clone = text.cloneNode(true) as HTMLElement;
                    clone.setAttribute("aria-hidden", "true");
                    clone.classList.add("announcement-text-clone");
                    content.appendChild(clone);
                } else if (!overflows && clone) {
                    clone.remove();
                    clone = null;
                }
            };
            const onResize = () => {
                if (rafId) return;
                rafId = window.requestAnimationFrame(check);
            };
            check();
            window.addEventListener("resize", onResize, { passive: true });
            marqueeCleanup = () => {
                window.removeEventListener("resize", onResize);
                if (rafId) cancelAnimationFrame(rafId);
                if (clone) clone.remove();
                marquee.classList.remove("is-overflowing");
            };
        };

        const wireDismiss = (el: HTMLElement, id: string) => {
            const btn = el.querySelector<HTMLButtonElement>("[data-announcement-dismiss]");
            btn?.addEventListener(
                "click",
                () => {
                    const dismissed = getDismissed();
                    if (!dismissed.includes(id)) {
                        store.updateKey(DISMISSED_FIELD, [...dismissed, id]);
                    }
                    showNext(id);
                },
                { once: true },
            );
        };

        const showNext = (currentId: string | null) => {
            const dismissed = getDismissed();
            const remaining = allIds.filter(
                (id) => id !== currentId && !dismissed.includes(id),
            );
            if (remaining.length === 0) {
                updateRevealStyle(null);
                if (marqueeCleanup) {
                    marqueeCleanup();
                    marqueeCleanup = null;
                }
                return;
            }
            const next = remaining[Math.floor(Math.random() * remaining.length)];
            updateRevealStyle(next);
            const nextEl = wrapper.querySelector<HTMLElement>(
                `.announcement[data-announcement-id="${next}"]`,
            );
            if (nextEl) {
                wireDismiss(nextEl, next);
                setupMarquee(nextEl);
            }
        };

        const initialId = document.documentElement.getAttribute("data-announcement-chosen");
        if (!initialId) return;
        const initialEl = wrapper.querySelector<HTMLElement>(
            `.announcement[data-announcement-id="${initialId}"]`,
        );
        if (!initialEl) return;
        wireDismiss(initialEl, initialId);
        setupMarquee(initialEl);
    }

    if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", init, { once: true });
    } else {
        init();
    }
})();
