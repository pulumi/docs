import { Component, Element, h, Listen, Prop, State, Watch } from "@stencil/core";
import { store, Unsubscribe } from "@stencil/redux";
import { AppState } from "../../store/state";
import { setLanguage } from "../../store/actions/preferences";
import { PulumiAIClient } from "./client";
import { ChatGptModel, Language, OutputChunkResponse } from "./types";
import { SupportedLanguage, LanguageKey } from "../chooser/chooser";

import * as clipboard from "clipboard-polyfill";
import * as marked from "marked";

type ConnectionStatus = "Not connected" | "Connecting" | "Connected" | "Disconnected";

interface Version {
    prompt: string;
    language: string;
    source: string;
    markup: string;
}

interface SupportedGPTModel {
    key: ChatGptModel,
    version: string,
    name: string,
}

type SelectableLanguage = SupportedLanguage & { abbrev: string };

@Component({
    tag: "pulumi-ai",
    styleUrl: "ai.scss",
    shadow: false,
})
export class PulumiAI {
    private client: PulumiAIClient;
    private storeUnsubscribe: Unsubscribe;

    @Prop()
    h1: string = "Pulumi AI";

    @Prop()
    welcomeContent: string = "";

    @Prop()
    welcomeSelector: string = ".welcome";

    @Prop()
    repoUrl: string;

    @Prop()
    wsEndpoint: string;

    @Prop()
    signupUrl: string;

    @Element()
    private el: HTMLElement;

    @State()
    private running: boolean = false;

    @State()
    private connectionStatus: ConnectionStatus;

    @State()
    private errorMessage: string;

    @State()
    private versions: Version[] = [];

    @State()
    private currentVersion: Version;

    @State()
    private animatingWelcomeMessage: string = "";
    private staticWelcomeMessage: string = "";

    @State()
    private selectedLanguage: SelectableLanguage;

    @State()
    private selectedModel: SupportedGPTModel;

    @State()
    private overMessageLimit: boolean = false;

    @Prop({ mutable: true })
    model: ChatGptModel;

    @Prop({ mutable: true })
    prompt: string;

    @Prop({ mutable: true })
    language: LanguageKey;

    @Prop()
    userID: string;

    @Watch("language")
    handleLanguageChanged() {
        const lang = this.supportedLanguages.find(lang => lang.key === this.language);
        if (lang) {
            this.selectLanguage(lang);
        }
    }

    @Watch("model")
    handleModelChanged() {
        const gpt = this.supportedModels.find(gpt => gpt.key === this.model);
        if (gpt) {
            this.selectGPTModel(gpt);
        }
    }

    @Watch("userID")
    handleUserIDChanged(newID: string, oldID: string) {
        if (oldID !== newID) {
            this.client.userID = newID;

            // If we're in the over-message state, and we now have a user ID, assume
            // that means the user is now signed in.
            if (this.userID && this.overMessageLimit) {
                this.overMessageLimit = false;
                this.errorMessage = "";
            }
        }
    }

    @Listen("rendered", { target: "document" })
    handleRendered(_event: CustomEvent) {
        store.mapDispatchToProps(this, {
            setLanguage,
        });

        this.storeUnsubscribe = store.mapStateToProps(this, (state: AppState) => {
            const {
                preferences: {
                    language,
                },
                user: {
                    id,
                },
            } = state;
            const lang = this.supportedLanguages.find(lang => lang.key === language) || this.supportedLanguages[0];
            return {
                language: lang.key,
                userID: id,
            }
        });
    }

    @Listen("resize", { target: "window" })
    handleResize(_event: CustomEvent) {
        this.onResize();
    }

    private autoScroll: boolean = true;
    setLanguage: typeof setLanguage;

    private supportedLanguages: SelectableLanguage[] = [
        { key: "typescript", name: "TypeScript", extension: "ts", abbrev: "Ts", preview: false },
        { key: "python", name: "Python", extension: "py", abbrev: "Py", preview: false },
        { key: "go", name: "Go", extension: "go", abbrev: "Go", preview: false },
        { key: "csharp", name: "C#", extension: "cs", abbrev: "C#", preview: false },
        { key: "java", name: "Java", extension: "java", abbrev: "Java", preview: true },
        { key: "yaml", name: "YAML", extension: "yaml", abbrev: "YAML", preview: true },
    ];

    private supportedModels: SupportedGPTModel[] = [
        { key: "gpt-3.5-turbo", name: "GPT 3.5 Turbo", version: "v3" },
        { key: "gpt-4", name: "GPT 4", version: "v4" }
    ];

    @Listen("click", {
        target: "document",
    })
    handleClick(event: MouseEvent) {
        const el = event.target as HTMLElement;
        const tagName = el.tagName;
        if (tagName === "BUTTON" && el.getAttribute("class")?.includes("copy")) {
            const code = el.closest("ul")?.nextElementSibling.querySelector("code").textContent;
            if (code) {
                clipboard.writeText(code);

                var tipEl = el.closest("pulumi-tooltip");
                var tipContentEl = tipEl.querySelector("[slot='content']");
                tipContentEl.textContent = "Copied!";
                setTimeout(() => tipContentEl.textContent = this.copyButtonTooltip, 1000);
            }
        }
    }

    @Listen("wheel", {
        target: "window",
    })
    handleWheel() {
        this.onScroll();
    }

    @Listen("touchmove", {
        target: "window",
    })
    handleTouchMove() {
        this.onScroll();
    }

    private onResize() {
        const widget = this.el.querySelector(".chat-widget-container");
        widget.setAttribute("style", `width: ${ widget.parentElement.clientWidth}px`);
    }

    private onScroll() {
        this.autoScroll = false;
        if (window.innerHeight + window.scrollY >= document.body.offsetHeight - 5) {
            this.autoScroll = true;
        }
    }

    private get placeholder() {
        switch (this.versions.length) {
            case 0:
                return "Example: A static website on AWS behind a CDN.";
            case 1:
                return "Example: Add a serverless REST API";
        }
        return "";
    }

    componentWillLoad() {
        this.selectedModel = this.supportedModels.find(m => m.key === this.model) || this.supportedModels.reverse()[0];
        this.selectedLanguage = this.supportedLanguages[0];
        this.connectionStatus = "Not connected";

        this.validateProps();
        this.validateGlobals();
    }

    componentDidLoad() {
        try {
            this.prepareInput();
            this.renderWelcomeMessage();
            this.onResize();

            this.client = new PulumiAIClient(
                this.wsEndpoint,
                (event) => this.onConnected(event),
                (response) => this.onContent(response),
                () => this.onComplete(),
                () => this.onOverMessageLimit(),
                () => this.onOverCapacity(),
                (error) => this.onError(error),
                (message) => this.onClose(message),
            );
            this.client.connect();

        } catch (error) {
            console.error(error.message);
        }
    }

    disconnectedCallback() {
        if (this.storeUnsubscribe) {
            this.storeUnsubscribe();
        }
    }

    private onConnected(_event: Event) {
        this.connectionStatus = "Connected";
    }

    private onSubmit(event: Event) {
        event.preventDefault();
        this.submit();
    }

    private get runnable() {
        return this.connectionStatus === "Connected" && !this.running && this.input.value != "";
    }

    private highlight(parentNode: HTMLElement): void {
        if (parentNode) {
            requestAnimationFrame(() => {
                Prism.highlightAllUnder(parentNode);
            });
        }
    }

    private copyButtonTooltip = "Copy to clipboard";

    private addButtons(versionMarkup: string) {
        const el = document.createElement("div");
        el.innerHTML = versionMarkup;

        // Find all of this version's `pre` elements.
        const pres = el.querySelectorAll("pre");

        // For each one, create a new element to contain both the pre and a set of button controls.
        pres.forEach(pre => {

            // Create a code-block container.
            const codeBlock = document.createElement("div");
            codeBlock.setAttribute("class", "code-block");

            // Append the container just before the pre element.
            pre.insertAdjacentElement("beforebegin", codeBlock);

            // Add the markup for the button controls.
            codeBlock.innerHTML = `<ul class="controls">
                <li>
                    <pulumi-tooltip>
                        <button class="copy">
                            <i></i>
                        </button>
                        <span slot="content">${ this.copyButtonTooltip }</span>
                    </pulumi-tooltip>
                </li>
            </ul>`;

            // Reparent the pre element under the code block.
            codeBlock.appendChild(pre);
        });

        return el.innerHTML;
    }

    private onContent(content: OutputChunkResponse) {
        this.currentVersion.source = this.currentVersion.source.replace(" ⎸", "");
        this.currentVersion.source += content.content + " ⎸";
        this.currentVersion = Object.assign({}, this.currentVersion);

        this.scroll();
        this.highlight(this.outputStream);
    }

    private onComplete() {
        const versionMarkup = marked.marked.parse(this.currentVersion.source.replace(" ⎸", ""));
        const markupWithButtons = this.addButtons(versionMarkup);

        this.currentVersion.markup = markupWithButtons;
        this.versions.push(Object.assign({}, this.currentVersion));
        this.versions = Array.from(this.versions);
        this.currentVersion = null;

        this.running = false;
        this.scroll();
        this.clear();
        this.focus();

        // Wait a bit for the versions to render, then colorize them.
        setTimeout(() => this.highlight(this.outputVersions), 250);
    }

    private scroll() {
        if (this.autoScroll) {
            requestAnimationFrame(() => window.scrollTo(0, document.body.scrollHeight));
        }
    }

    private clear() {
        requestAnimationFrame(() => {
            this.input.value = "";
            this.prompt = "";
        });
    }

    private focus() {
        requestAnimationFrame(() => {
            this.input.focus();
        });
    }

    private onOverMessageLimit() {
        this.errorMessage = "message limit reached";
        this.overMessageLimit = true;
        this.autoScroll = true;
        this.running = false;
        this.scroll();
    }

    private onError(error: string) {
        this.errorMessage = error;
        this.running = false;

        if (error === "error fetching chatgpt response") {
            this.errorMessage = "trouble communicating with server";
        }
    }

    private onOverCapacity() {
        this.errorMessage = "We are currently over capacity. Please try again momentarily.";
        this.running = false;
    }

    private onClose(_message: string) {
        this.connectionStatus = "Disconnected";
    }

    private onInput() {
        this.prompt = (this.input.value || "").trim();
    }

    private validateProps() {
        const errors: string[] = [];

        if (!this.wsEndpoint) {
            errors.push("Missing `ws-endpoint` attribute.");
        }

        try {
            new URL(this.wsEndpoint);
        } catch (error) {
            errors.push("Invalid `ws-endpoint` URL.");
        }

        if (!this.repoUrl) {
            errors.push("Missing `repo-url` attribute.");
        }

        try {
            new URL(this.repoUrl);
        } catch (error) {
            errors.push("Invalid `repo-url` URL.");
        }

        if (!this.welcomeContent) {
            console.warn("Missing welcome content.");
        }

        if (!this.signupUrl) {
            errors.push("Missing `signup-url` attribute.");
        }

        if (errors.length) {
            throw new Error(errors.join("\n"));
        }
    }

    private validateGlobals() {
        if (typeof Prism === "undefined") {
            throw new Error(
                "The pulumi-ai component requires the Prism syntax highlighter. Ensure Prism and all language-support scripts have been loaded into the global scope before using it.",
            );
        }
    }

    private prepareInput() {
        this.input.addEventListener("keydown", (event: KeyboardEvent) => {
            if (event.metaKey && (event.key === "Enter")) {
                event.preventDefault();
                this.submit();
            }
        });
        this.focus();
    }

    private combineClasses(...classes: string[]) {
        return classes.filter(c => c && c !== "").join(" ");
    }

    private trackEventLabel(source: string): string {
        if (!this.selectedLanguage) {
            return "";
        }
        return ["pulumi-ai", source, this.selectedLanguage.key].join("-");
    }

    private renderSubmitButton(withTooltip: boolean) {
        const title = `Generate Pulumi ${this.selectedLanguage?.name} program`;

        let label = this.versions.length > 0 ? "Update program" : "Generate program";
        let runningLabel = this.currentVersion?.source ? "Responding..." : "Thinking...";

        const button = <button
            title={title}
            class={this.combineClasses("submit", this.running ? "running" : "")}
            data-track={this.trackEventLabel("button")}
            disabled={ !this.runnable }>
            <span class="label">{ this.running ? runningLabel : label }</span>
            <span class="icon"></span>
        </button>;

        if (!withTooltip) {
            return button;
        }

        return (
            <pulumi-tooltip>
                {button}
                <span slot="content">{title}</span>
            </pulumi-tooltip>
        );
    }

    private renderLanguageSelector() {
        return <ul class="languages">
            {
                this.supportedLanguages.map(language => {
                    const tooltipFull = `Generate code in ${language.name}`;

                    return <li class={this.combineClasses("language", this.selectedLanguage === language ? "active" : "")}>
                        <button onClick={this.selectLanguage.bind(this, language)}
                            data-track={this.trackEventLabel("tab")}
                            title={tooltipFull}
                            disabled={ this.running }>
                            <span class="label-abbrev">{ language.abbrev }</span>
                            <span class="label">{ language.name }</span>
                        </button>
                    </li>;
                })
            }
        </ul>
    }

    private selectLanguage(language: SelectableLanguage) {
        this.selectedLanguage = language;
        this.focus();

        if (this.setLanguage && language) {
            this.setLanguage(language.key);
        }
    }

    private selectGPTModel(gpt: SupportedGPTModel) {
        this.selectedModel = gpt;
    }

    private get input() {
        return this.el.querySelector("form input") as HTMLInputElement;
    }

    private get output() {
        return this.el.querySelector(".output") as HTMLDivElement;
    }

    private get outputVersions() {
        return this.output.querySelector(".versions ol") as HTMLElement;
    }

    private get outputStream() {
        return this.output.querySelector(".stream") as HTMLElement;
    }

    private submit() {
        this.running = true;
        this.autoScroll = true;
        this.errorMessage = null;
        this.staticWelcomeMessage = this.welcomeContent;
        this.overMessageLimit = false;

        const query = this.input.value?.trim()

        if (!query) {
            return;
        }

        this.currentVersion = {
            prompt: this.input.value,
            language: this.selectedLanguage.name,
            source: "",
            markup: "",
        };

        this.versions = Array.from(this.versions);

        this.client.submit(
            this.selectedLanguage.name as Language,
            this.versions && this.versions.length > 0 ? this.versions[this.versions.length - 1].source : "",
            this.input.value,
            this.versions.length,
            this.selectedModel.key,
        );
    }

    private renderStream(markdown: string = "") {
        return marked.marked.parse(markdown);
    }

    private renderVersion(version: Version) {
        return version.markup;
    }

    private renderWelcomeMessage() {
        const message = this.welcomeContent.split("");
        message.map((char, i) => setTimeout(() => {
            this.animatingWelcomeMessage += char;
            this.scroll();
         }, i * 25));
    }

    private renderPrompt(version: Version) {
        return <div class="prompt">
            <i></i>
            <div>
                <h3>{ version.prompt }</h3>
                <div class="language">{ version.language }</div>
            </div>
        </div>;
    }

    private renderOverLimitMessage() {
        return <div class="over-limit">
            <h5>Enjoying Pulumi AI?</h5>
            <p>
                <a href={ this.signupUrl }>Create a free Pulumi Cloud account</a> for unlimited use.
            </p>
        </div>;
    }

    render() {
        return (
            <div>

                {/* Welcome message.  */}
                <div class="welcome" >
                    <div innerHTML={ this.staticWelcomeMessage || this.animatingWelcomeMessage }></div>
                </div>

                {/* Output. */}
                <div class="output">

                    {/* Previous versions.  */}
                    <div class="versions">
                        {
                            this.versions.length > 0 && <div>
                                <ol>
                                {
                                    this.versions.map((version, i) => <li key={i}>
                                        <hr />
                                        { this.renderPrompt(version) }
                                        <div class="version" innerHTML={ this.renderVersion(version) }></div>
                                    </li>)
                                }
                                </ol>
                            </div>
                        }
                    </div>

                    {/* Currently running request. */}
                    {
                        this.currentVersion?.source && <div>
                            <hr />
                            { this.renderPrompt(this.currentVersion) }
                            <div class="stream" innerHTML={ this.renderStream(this.currentVersion.source) }></div>
                        </div>
                    }

                    {/* Message limit */}
                    {
                        this.overMessageLimit && this.renderOverLimitMessage()
                    }
                </div>

                {/* Chat widget. */}
                <div class="chat-widget-container">
                    <div class="chat-widget">
                        <div class="chat-widget-form-container">
                            <div class="chat-widget-form">
                                { this.renderLanguageSelector() }
                                <form onSubmit={ this.onSubmit.bind(this) }>
                                    <input type="text" placeholder={ this.placeholder } disabled={ this.running } onInput={ this.onInput.bind(this) } maxLength={ this.client?.MAX_PROMPT_LENGTH } value={ this.prompt }></input>
                                    { this.renderSubmitButton(true) }
                                </form>
                            </div>
                        </div>
                        <div class="chat-status">
                            <div>
                                <span>{ this.connectionStatus }</span>
                                {
                                    this.connectionStatus === "Connected" && this.selectedModel && <span>
                                        <span> &bull; </span>
                                        <span class="models">
                                            <span class="label">GPT</span>
                                            {
                                                this.supportedModels.map(model => <span>
                                                    <a
                                                        class={ model.key === this.selectedModel.key ? "active" : "" }
                                                        onClick={ this.selectGPTModel.bind(this, model) }>
                                                            <span>{ model.version }</span>
                                                    </a>
                                                </span>)
                                            }
                                        </span>
                                    </span>
                                }
                                {
                                    this.connectionStatus === "Disconnected" && <span>
                                        <span> &bull; </span>
                                        <a class="alert" onClick={ () => location.reload() }>Reload</a>
                                    </span>
                                }
                                {
                                    this.errorMessage && <span>
                                        <span> &bull; </span>
                                        <span class="alert">Error: { this.errorMessage }</span>
                                    </span>
                                }
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        );
    }
}
