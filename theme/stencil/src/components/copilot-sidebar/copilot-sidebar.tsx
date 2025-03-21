import { Component, h, Host, Prop, State } from "@stencil/core";
import { gb } from "../../util/util";

const ATLAS_LOCAL_STORAGE_KEY = "pulumi-ai-use-atlas";


@Component({
    tag: "copilot-sidebar",
    styleUrl: "copilot-sidebar.css",
    shadow: false,
})
export class CopilotSidebar {

    //
    // Props
    //

    // The copilotSrc is URL where the copilot sidebar is hosted
    @Prop()
    copilotSrc: string;

    // The atlasUrl is the URL where the Atlas web component is hosted
    @Prop()
    atlasUrl: string;

    //
    // Internal state
    //

    // Whether to show the sidebar (growthbook flag)
    @State()
    showSidebar = false;

    // Whether to show the Atlas web component (local storage flag)
    @State()
    showAtlas = false;

    // Whether the Atlas scripts have been loaded
    @State()
    atlasScriptsLoaded = false;

    async componentWillLoad() {
        this.showSidebar = gb.isOn("copilot-on-docs");
        gb.setRenderer(() => (this.showSidebar = gb.isOn("copilot-on-docs")));

        this.showAtlas = this.atlasUrl && window.localStorage.getItem(ATLAS_LOCAL_STORAGE_KEY) !== "false";
        if (this.showAtlas) {
            await this.loadAtlasScripts();
        }
    }

    private async loadAtlasScripts() {
        const atlasWebComponentPolyfillsPath = this.atlasUrl + "/polyfills.js";
        const atlasWebComponentPath = this.atlasUrl + "/main.js";
        try {
            await this.loadScriptOnce(atlasWebComponentPolyfillsPath);
            await this.loadScriptOnce(atlasWebComponentPath);
            this.atlasScriptsLoaded = true;
        } catch (error) {
            console.error("Failed to load Atlas scripts:", error);
        }
    }

    private async loadScriptOnce(src: string): Promise<void> {
        // Skip if already loaded
        if (document.querySelector(`script[src="${src}"]`)) {
            return;
        }

        return new Promise((resolve, reject) => {
            const script = document.createElement("script");
            script.src = src;
            script.async = true;
            // Importing the script as a module is required for the script to be loaded.
            script.type = "module";
            script.onload = () => resolve();
            script.onerror = err => reject(err);
            document.head.appendChild(script);
        });
    }

    render() {
        if (this.showAtlas) {
            if (!this.atlasScriptsLoaded) {
                return <Host></Host>;
            }

            return (
                <Host>
                    <pulumi-copilot hostApp="docs" apiUrl={this.atlasUrl} />
                </Host>
            );
        }

        if (!this.showSidebar) {
            return <Host></Host>;
        }

        return (
            <Host>
                <aside id="ai-sidebar-target"></aside>
                <iframe id="ai-sidebar-host" src={this.copilotSrc}></iframe>
            </Host>
        );
    }
}
