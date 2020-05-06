import "@stencil/redux";
import { Component, Event, EventEmitter, Prop, h } from "@stencil/core";
import { Store } from "@stencil/redux";
import { configureStore } from "../../store";
import { LanguageKey } from "../chooser/chooser";
import { setLanguage } from "../../store/actions/preferences";

@Component({
    tag: "pulumi-root",
    shadow: false,
})
export class Root {

    @Prop({ context: "store" })
    store: Store;

    @Event()
    rendered: EventEmitter;

    // Dispatch functions for handling the selection of an option.
    setLanguage: typeof setLanguage;

    componentWillLoad() {

        // Initialize the store. This makes the store available to any component on the page.
        this.store.setStore(configureStore());
        // Map internal methods to actions defined on the store.
        this.store.mapDispatchToProps(this, { setLanguage });
    }

    componentDidRender() {
        
        // Since this element initializes the store, dispatch a DOM event letting
        // listeners know when rendering is complete.
        this.rendered.emit();
        this.setSelectedLanguage();
    }

    render() {
        return <div>
        </div>;
    }

    private setSelectedLanguage() {
        // Parse and set language from anchor tag if present.
        const anchorTag = window.location.hash;
        if (anchorTag) {
            const matches = /[^~]*$/gm.exec(anchorTag);
            if (matches) {
                const language = matches[0];
                this.setLanguage(language as LanguageKey);

            }
        }
    }
}
