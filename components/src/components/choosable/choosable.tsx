import { Component, h, Prop } from '@stencil/core';
import { Store, Unsubscribe } from "@stencil/redux";
import { AppState } from "../../store/state";
import { ChooserType, ChooserKey } from "../chooser/chooser";

/**
 * The Choosable component is useful for showing or hiding information based on the
 * currently selected ChooserType and and value. For example, a component defined as:
 *
 *     <pulumi-choosable type="language" value="typescript">
 *         I <3 TypeScript.
 *     </pulumi-choosable>
 *
 * ...would display "I <3 TypeScript" only when the user's currently (or most recently)
 * selected language choice is TypeScript.
 */
@Component({
    tag: 'pulumi-choosable',
    styleUrl: 'choosable.scss',
    shadow: false
})
export class Choosable {
    private storeUnsubscribe: Unsubscribe;

    // A handle to the application store.
    @Prop({ context: "store" })
    store: Store;

    // The type of chooser to associate with this component instance (e.g., a language chooser).
    @Prop({ mutable: true })
    type: ChooserType;

    // The value to use for determining whether to show or hide this component instance's
    // slotted content.
    @Prop({ mutable: true })
    value: ChooserKey;

    // The currently selected value of the supplied chooser type.
    @Prop({ mutable: true })
    selection: ChooserKey;

    componentWillLoad() {

        // Map currently selected values from the store, so we can use them in this component.
        this.storeUnsubscribe = this.store.mapStateToProps(this, (state: AppState) => {
            const { preferences: { language, k8sLanguage, os, cloud } } = state;

            switch (this.type) {
                case "language":
                    return { selection: language };
                case "k8s-language":
                    return { selection: k8sLanguage };
                case "os":
                    return { selection: os };
                case "cloud":
                    return { selection: cloud };
            }
        });
    }

    componentDidUnload() {
        this.storeUnsubscribe();
    }

    render() {
        return (
            // If the currently selected value of the selected chooser type matches the
            // one assigned to this instance, mark it active.
            <div class={this.selection === this.value ? "active" : ""}>
                <slot></slot>
            </div>
        );
    }
}
