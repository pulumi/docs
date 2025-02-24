import { Component, h, Host, Prop, State } from "@stencil/core";
import { gb } from "../../util/util";

const ATLAS_LOCAL_STORAGE_KEY = "pulumi-ai-use-atlas";


@Component({
    tag: "copilot-sidebar",
    styleUrl: "copilot-sidebar.css",
    shadow: false,
})
export class CopilotSidebar {
    // The copilotSrc is URL where the copilot sidebar is hosted
    @Prop()
    copilotSrc: string;

    @Prop()
    atlasUrl: string;

    @State()
    showSidebar = false;

    @State()
    showAtlas = false;

    // Add new state to track script loading
    @State()
    atlasScriptsLoaded = false;

    async componentWillLoad() {
        this.showSidebar = gb.isOn("copilot-on-docs");
        gb.setRenderer(() => (this.showSidebar = gb.isOn("copilot-on-docs")));

        // pulumi-ai-use-atlas
        this.showAtlas = this.atlasUrl && window.localStorage.getItem(ATLAS_LOCAL_STORAGE_KEY) === "true";
        if (this.showAtlas) {
            await this.loadAtlasScripts();
        }
    }

    private async loadAtlasScripts() {
        const atlasWebComponentPath = this.atlasUrl + "/main.js";
        const atlasWebComponentPolyfillsPath = this.atlasUrl + "/polyfills.js";
        try {
            await Promise.all([this.loadScriptOnce(atlasWebComponentPath), this.loadScriptOnce(atlasWebComponentPolyfillsPath)]);
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

        // Using import() requires
        // 1. Telling webpack to ignore the module.
        // 2. Telling tsconfig to ignore the module.
        // So we use a simple promise to load the script.
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
