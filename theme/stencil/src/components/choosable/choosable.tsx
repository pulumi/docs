import { Component, Element, h, Listen, Prop, Watch } from "@stencil/core";
import { store, Unsubscribe } from "@stencil/redux";
import { AppState } from "../../store/state";
import { ChooserType, ChooserKey, ChooserMode } from "../chooser/chooser";

/**
 * The Choosable component is useful for showing or hiding information based on the
 * currently selected ChooserType and value. For example, a component defined as:
 *
 *     <pulumi-choosable type="language" value="typescript">
 *         I <3 TypeScript.
 *     </pulumi-choosable>
 *
 * ...would display "I <3 TypeScript" only when the user's currently (or most recently)
 * selected language choice is TypeScript.
 */
@Component({
    tag: "pulumi-choosable",
    styleUrl: "choosable.scss",
    shadow: false,
})
export class Choosable {
    private storeUnsubscribe: Unsubscribe;

    @Element()
    el: HTMLElement;

    // The type of chooser to associate with this component instance (e.g., a language chooser).
    @Prop({ mutable: true })
    type: ChooserType;

    // The value to use for determining whether to show or hide this component instance's
    // slotted content.
    @Prop({ mutable: true })
    value: ChooserKey;

    // Similarly to value, this prop allows for providing multiple comma-delimited values.
    @Prop({ mutable: true })
    values: ChooserKey;

    // Choosables are local by default, allowing users to opt into having free-form bits
    // of content simply honor whatever happens to be set on the global store (accepting
    // those bits of content may not show up in all situations).
    @Prop({ mutable: true })
    mode: ChooserMode;

    @Watch("mode")
    onModeChange(newMode: ChooserMode) {
        if (newMode === "local") {
            if (this.storeUnsubscribe) {
                this.storeUnsubscribe();
            }
        }
    }

    // The currently selected value of the supplied chooser type, as .
    @Prop({ mutable: true })
    selection: ChooserKey;

    disconnectedCallback() {
        if (this.storeUnsubscribe) {
            this.storeUnsubscribe();
        }
    }

    componentWillLoad() {
        // By default, mode is global, until told otherwise by some parental chooser.
        // Only set the default if the mode hasn't already been set (e.g., by a parent
        // chooser that called setAttribute("mode", "local") before this element upgraded).
        if (!this.mode) {
            this.mode = "global";
        }

        // Try to subscribe immediately if the store is ready.
        // This avoids waiting for the "rendered" event when possible.
        if (store.getStore()) {
            this.subscribeToStore();
        }
    }

    @Listen("rendered", { target: "document" })
    onRendered(_event: CustomEvent) {
        // Subscribe to the store when it's ready (if not already subscribed).
        if (!this.storeUnsubscribe && this.mode === "global") {
            this.subscribeToStore();
        }
    }

    private subscribeToStore() {
        if (this.mode === "global") {
            // @ts-ignore-next-line
            this.storeUnsubscribe = store.mapStateToProps(this, (state: AppState) => {
                const {
                    preferences: { language, k8sLanguage, os, cloud, persona, backend, pythontoolchain, tfTool },
                } = state;

                switch (this.type) {
                    case "language":
                        return { selection: language };
                    case "k8s-language":
                        return { selection: k8sLanguage };
                    case "os":
                        return { selection: os };
                    case "cloud":
                        return { selection: cloud };
                    case "persona":
                        return { selection: persona };
                    case "backend":
                        return { selection: backend };
                    case "pythontoolchain":
                        return { selection: pythontoolchain };
                    case "tf-tool":
                        return { selection: tfTool };
                }
            });
        }
    }

    render() {
        const values = this.values ? this.values.split(",").map(v => v.trim()) : [];
        let isActive = this.selection && (this.selection === this.value || values.includes(this.selection));

        // Headless fallback. A global-mode choosable that isn't governed by a chooser
        // reads the global store directly, so when the global selection isn't one this
        // choosable's peer group offers (e.g. a reader who picked HCL lands on a page
        // whose inline choosables only cover TypeScript/Python/...), every member of the
        // group hides and the reader sees an empty gap. To avoid that, mirror the
        // chooser's preferredOrDefault behavior: if the selection matches no choosable in
        // the contiguous peer group, the group's first member shows itself. Choosables
        // inside a chooser are left alone -- the chooser already handles their fallback.
        //
        // The fallback only fires when the selection is offered nowhere on the page.
        // A group can omit a language deliberately -- a run of "see the X docs" links
        // with no Java member because there is no Java page to link, say -- and if the
        // page serves Java readers elsewhere, showing them the group's first member
        // would silently present the wrong language as if it were theirs. Blank is
        // correct there. Only when the whole page has nothing for the selection (the
        // headless-HCL case) is falling back better than hiding everything.
        if (!isActive && this.mode === "global" && this.selection && !this.el.closest("pulumi-chooser")) {
            const group = this.peerGroup();
            // The group check is subsumed by the page-wide check; it runs first only
            // because it short-circuits the common case cheaply.
            if (group.length > 1 && group[0] === this.el && !group.some(c => this.matchesSelection(c)) && !this.selectionOfferedOnPage()) {
                isActive = true;
            }
        }

        return (
            <div class={isActive ? "active" : ""}>
                <slot></slot>
            </div>
        );
    }

    // Whether any same-type choosable anywhere on the page offers the current
    // selection. If one does, the page has real content for the reader's choice, and a
    // peer group without a matching member is a deliberate omission that should stay
    // hidden rather than fall back to the wrong language.
    private selectionOfferedOnPage(): boolean {
        const all = this.el.ownerDocument.querySelectorAll(`pulumi-choosable[type="${this.type}"]`);
        return Array.from(all).some(c => this.matchesSelection(c));
    }

    // Whether a choosable element's value/values attributes include the current selection.
    private matchesSelection(choosable: Element): boolean {
        const value = choosable.getAttribute("value");
        const values = (choosable.getAttribute("values") || "").split(",").map(v => v.trim());
        return value === this.selection || values.includes(this.selection);
    }

    // The contiguous run of same-type choosables this element belongs to -- a "toggle
    // set" the author intends to show exactly one of. The shortcode wraps each choosable
    // in a bare <div>, so we walk element siblings of that wrapper (or of the choosable
    // itself, for the inline form) and stop at the first sibling that isn't another
    // same-type choosable (a heading, paragraph, example-program, chooser, etc.).
    private peerGroup(): HTMLElement[] {
        const unitOf = (choosable: Element): Element => {
            const parent = choosable.parentElement;
            // The block shortcode's wrapper is a <div> whose only element child is the
            // choosable; treat it as the unit. The inline form has no such wrapper.
            if (parent && parent.tagName === "DIV" && parent.children.length === 1 && parent.firstElementChild === choosable) {
                return parent;
            }
            return choosable;
        };
        const choosableIn = (unit: Element): HTMLElement | null => {
            if (unit.tagName.toLowerCase() === "pulumi-choosable") {
                return unit.getAttribute("type") === this.type ? (unit as HTMLElement) : null;
            }
            const child = unit.querySelector(":scope > pulumi-choosable");
            return child && child.getAttribute("type") === this.type ? (child as HTMLElement) : null;
        };

        const group: HTMLElement[] = [this.el];
        const unit = unitOf(this.el);

        for (let sib = unit.previousElementSibling; sib; sib = sib.previousElementSibling) {
            const c = choosableIn(sib);
            if (!c) break;
            group.unshift(c);
        }
        for (let sib = unit.nextElementSibling; sib; sib = sib.nextElementSibling) {
            const c = choosableIn(sib);
            if (!c) break;
            group.push(c);
        }
        return group;
    }
}
