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

    @Listen("rendered", { target: "document" })
    onRendered(_event: CustomEvent) {
        // By default, mode is global, until told otherwise by some parental chooser.
        this.mode = "global";

        if (this.mode === "global") {
            this.storeUnsubscribe = store.mapStateToProps(this, (state: AppState) => {
                const {
                    preferences: { language, k8sLanguage, os, cloud, persona, backend },
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
                }
            });
        }
    }

    render() {
        const values = this.values ? this.values.split(",").map(v => v.trim()) : [];
        const isActive = this.selection && (this.selection === this.value || values.includes(this.selection));

        return (
            <div class={isActive ? "active" : ""}>
                <slot></slot>
            </div>
        );
    }
}
