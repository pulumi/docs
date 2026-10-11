import { Component, h, Listen, Prop } from "@stencil/core";
import { store, Unsubscribe } from "@stencil/redux";
import { AppState } from "../../store/state";

@Component({
  tag: "pulumi-user-toggle",
  styleUrl: "user-toggle.scss",
  shadow: false,
})
export class PulumiUserToggle {
    private storeUnsubscribe: Unsubscribe;

    @Prop({ mutable: true })
    userId: string;

    @Listen("rendered", { target: "document" })
    handleRendered(_event: CustomEvent) {
        this.storeUnsubscribe = store.mapStateToProps(this, (state: AppState) => {
            const { user: { id } } = state;
            return {
                userId: id,
            };
        });
    }

    disconnectedCallback() {
        if (this.storeUnsubscribe) {
            this.storeUnsubscribe();
        }
    }

    // Consider the user signed in if there's a user ID set.
    // Commented out becuase of this issue: https://github.com/pulumi/pulumi-hugo/issues/3089
    // We may eventually want to return to dynamic content here, so
    // just commenting this out for now instead of deleting it.
    // private get signedIn(): boolean {
    //     return !!this.userId;
    // }

    render() {
        return <span class="signed-out">
            <slot name="signed-in"></slot>
            <slot name="signed-out"></slot>
        </span>;
    }
}
