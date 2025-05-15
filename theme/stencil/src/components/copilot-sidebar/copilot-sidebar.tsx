import { Component, h, Host, Prop, State } from "@stencil/core";

@Component({
    tag: "copilot-sidebar",
    styleUrl: "copilot-sidebar.css",
    shadow: false,
})
export class CopilotSidebar {
    //
    // Props
    //

    // The atlasUrl is the URL where the Atlas web component is hosted
    @Prop()
    atlasUrl: string;

    //
    // Internal state
    //

    // Whether the Atlas scripts have been loaded
    @State()
    atlasScriptsLoaded = false;

    async componentWillLoad() {
        await this.loadAtlasScripts();
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
        if (!this.atlasScriptsLoaded) {
            return <Host></Host>;
        }

        return (
            <Host>
                <pulumi-copilot hostApp="docs" apiUrl={this.atlasUrl} />
            </Host>
        );
    }
}
