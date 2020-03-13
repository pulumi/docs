import "@stencil/redux";
import { Component, Event, EventEmitter, Prop, h } from "@stencil/core";
import { Store } from "@stencil/redux";
import { configureStore } from "../../store";

@Component({
    tag: "pulumi-root",
    shadow: false,
})
export class Root {

    @Prop({ context: "store" })
    store: Store;

    @Event()
    rendered: EventEmitter;

    componentWillLoad() {

        // Initialize the store. This makes the store available to any component on the page.
        this.store.setStore(configureStore());
    }

    componentDidRender() {

        // Since this element initializes the store, dispatch a DOM event letting
        // listeners know when rendering is complete.
        this.rendered.emit();
    }

    render() {
        return <div>
        </div>;
    }
}
