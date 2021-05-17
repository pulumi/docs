import "@stencil/redux";
import { Component, Event, EventEmitter, h } from "@stencil/core";
import { store } from "@stencil/redux";
import { configureStore } from "../../store";
import { LanguageKey } from "../chooser/chooser";
import { setLanguage } from "../../store/actions/preferences";
import { getQueryVariable } from "../../util/util";

@Component({
    tag: "pulumi-root",
    shadow: false,
})
export class Root {

    @Event()
    rendered: EventEmitter;

    // Dispatch functions for handling the selection of an option.
    setLanguage: typeof setLanguage;

    componentWillLoad() {

        // Initialize the store. This makes the store available to any component on the page.
        store.setStore(configureStore());
        // Map internal methods to actions defined on the store.
        store.mapDispatchToProps(this, { setLanguage });
    }

    componentDidRender() {

        // Set language if specified by query param or is part of an anchor tag (e.g. #anchor~nodejs).
        this.setSelectedLanguage();
        // Since this element initializes the store, dispatch a DOM event letting
        // listeners know when rendering is complete.
        this.rendered.emit();
    }

    render() {
        return <div>
        </div>;
    }

    private setSelectedLanguage() {

        // Check if language is specified in the query params and set language if present.
        const queryParamLanguage = getQueryVariable("language");
        if (queryParamLanguage){
            this.setLanguage(queryParamLanguage as LanguageKey);
        }

        // Parse and set language from anchor tag if present, this will override what the query param says if
        // both are present because the anchor will not work otherwise.
        const anchorTag = window.location.hash;
        if (anchorTag) {
            const language = anchorTag.split("_")
                .slice(-1)
                .find(lang => ["typescript", "javascript", "csharp", "go", "python"].includes(lang));
            if (language) {
                this.setLanguage(language as LanguageKey);
            }
        }
    }
}
