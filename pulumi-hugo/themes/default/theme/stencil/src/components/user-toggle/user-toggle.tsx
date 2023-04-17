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
    private get signedIn(): boolean {
        return !!this.userId;
    }

    render() {
        return <span class={ this.signedIn ? "signed-in" : "signed-out" }>
            <slot name="signed-in"></slot>
            <slot name="signed-out"></slot>
        </span>;
    }
}
