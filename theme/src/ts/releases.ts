// Changelog modal on /releases/ (see layouts/partials/releases/changelog-modal.html).
//
// Clicking a [data-changelog-link] row pushes the item's detail URL onto the
// history and opens the detail page's <article data-changelog-article>
// fragment in a modal, fetched from the URL the row already points at — so
// without JS (or on fetch failure) the row is a plain link and direct
// navigation renders the full page. Closing the modal goes back in history;
// back/forward buttons close/reopen it via popstate.

document.addEventListener("DOMContentLoaded", () => {
    const modal = document.querySelector<HTMLElement>("[data-changelog-modal]");
    if (!modal) return;

    const panel = modal.querySelector<HTMLElement>("[data-changelog-modal-panel]");
    const content = modal.querySelector<HTMLElement>("[data-changelog-modal-content]");
    const closeButton = modal.querySelector<HTMLButtonElement>("[data-changelog-modal-close]");
    if (!panel || !content || !closeButton) return;

    const cache = new Map<string, Element>();
    let isOpen = false;
    let lastTrigger: HTMLElement | null = null;
    let bgInerted: Element[] = [];

    function isInertBypass(el: Element): boolean {
        return el.id === "segment-consent-manager" || el.classList.contains("consent-dialog-overlay");
    }

    // Focus trap matching the mobile nav sheet in header-nav.ts, generalized
    // to a nested modal: walk from the modal up to <body>, inerting the
    // siblings at each level so Tab can't escape the dialog. The modal must
    // stay inside <main> — content styles like `main p a` are scoped to it,
    // so re-parenting the modal to <body> would unstyle the injected article.
    function setBackgroundInert(on: boolean): void {
        if (on) {
            let node: Element = modal;
            while (node.parentElement) {
                for (const sibling of Array.from(node.parentElement.children)) {
                    if (sibling !== node && !isInertBypass(sibling) && !sibling.hasAttribute("inert")) {
                        sibling.setAttribute("inert", "");
                        bgInerted.push(sibling);
                    }
                }
                node = node.parentElement;
                if (node === document.body) break;
            }
        } else {
            bgInerted.forEach(el => el.removeAttribute("inert"));
            bgInerted = [];
        }
    }

    async function fetchArticle(url: string): Promise<Element | null> {
        const cached = cache.get(url);
        if (cached) return cached;
        const response = await fetch(url);
        if (!response.ok) return null;
        const doc = new DOMParser().parseFromString(await response.text(), "text/html");
        const article = doc.querySelector("[data-changelog-article]");
        if (article) cache.set(url, article);
        return article;
    }

    function openModal(article: Element, trigger: HTMLElement | null): void {
        content.innerHTML = "";
        content.appendChild(article.cloneNode(true));
        modal.classList.remove("hidden");
        modal.scrollTop = 0;
        document.body.style.overflow = "hidden";
        setBackgroundInert(true);
        isOpen = true;
        lastTrigger = trigger;
        closeButton.focus();
    }

    function closeModal(): void {
        if (!isOpen) return;
        modal.classList.add("hidden");
        content.innerHTML = "";
        document.body.style.overflow = "";
        setBackgroundInert(false);
        isOpen = false;
        lastTrigger?.focus();
        lastTrigger = null;
    }

    async function show(url: string, trigger: HTMLElement | null): Promise<void> {
        let article: Element | null = null;
        try {
            article = await fetchArticle(url);
        } catch {
            article = null;
        }
        if (!article) {
            // Fall back to a regular navigation; the URL is already current.
            window.location.assign(url);
            return;
        }
        openModal(article, trigger);
    }

    // Close by unwinding the history entry we pushed, so the URL returns to
    // /releases/; the popstate handler does the actual close.
    function requestClose(): void {
        if (history.state && history.state.changelogUrl) {
            history.back();
        } else {
            closeModal();
        }
    }

    document.addEventListener("click", (e: MouseEvent) => {
        if (e.defaultPrevented || e.button !== 0 || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
        const link = (e.target as HTMLElement).closest("[data-changelog-link]") as HTMLAnchorElement | null;
        if (!link) return;
        e.preventDefault();
        history.pushState({ changelogUrl: link.href }, "", link.href);
        void show(link.href, link);
    });

    closeButton.addEventListener("click", requestClose);

    // A click on the backdrop (anywhere outside the panel) closes.
    modal.addEventListener("click", (e: MouseEvent) => {
        if (!panel.contains(e.target as Node)) requestClose();
    });

    document.addEventListener("keydown", (e: KeyboardEvent) => {
        if (e.key === "Escape" && isOpen) requestClose();
    });

    window.addEventListener("popstate", (e: PopStateEvent) => {
        const url = e.state?.changelogUrl;
        if (typeof url === "string") {
            void show(url, null);
        } else {
            closeModal();
        }
    });
});
