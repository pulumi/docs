import { Component, h, Listen, Prop } from "@stencil/core";
import { store, Unsubscribe } from "@stencil/redux";
import { AppState } from "../../store/state";
import { dismissBanner } from "../../store/actions/banners";

@Component({
    tag: "pulumi-banner",
    styleUrl: "./banner.scss",
    shadow: false,
})
export class Banner {
    private storeUnsubscribe: Unsubscribe;

    // The name of the banner. This property is used as a key to prevent banners that have
    // been dismissed from appearing again.
    @Prop()
    name: string;

    // Whether the banner can be closed. Controls whether the "x" symbol appears.
    @Prop()
    dismissible: boolean = true;

    // Whether the banner should be displayed.
    @Prop({ reflect: true, mutable: true })
    visible: boolean = false;

    dismissBanner: typeof dismissBanner;

    @Listen("rendered", { target: "document" })
    onRendered(_event: CustomEvent) {
        store.mapDispatchToProps(this, { dismissBanner });
        this.storeUnsubscribe = store.mapStateToProps(this, (state: AppState) => {
            return {
                // Banners are visible if they have a name and haven't been dismissed.
                visible: !!this.name && !state.banners.dismissed.find(b => b.name === this.name),
            }
        });
    }

    disconnectedCallback() {
        if (this.storeUnsubscribe) {
            this.storeUnsubscribe();
        }
    }

    render() {
        return (
            <div>
                <slot></slot>
                <div class="dismiss" onClick={ (event) => this.dismiss(event) } title="Dismiss">
                    <span>&times;</span>
                </div>
            </div>
        );
    }

    // Dismiss the banner.
    private dismiss(_event: Event) {
        this.dismissBanner(this.name);
    }
}
