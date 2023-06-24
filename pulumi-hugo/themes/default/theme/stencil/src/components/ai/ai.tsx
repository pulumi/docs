import { Component, Element, h, Listen, Prop, State, Watch } from "@stencil/core";
import { store, Unsubscribe } from "@stencil/redux";
import { AppState } from "../../store/state";
import { setLanguage } from "../../store/actions/preferences";
import { PulumiAIClient } from "./client";
import { ChatGptModel, GenerateNewOutputResponse, Language, OutputChunkResponse, CreateConnectionResponse, GetConversationResponse } from "./types";
import { SupportedLanguage, LanguageKey } from "../chooser/chooser";
import { getQueryVariable } from "../../util/util";

import * as clipboard from "clipboard-polyfill";
import * as marked from "marked";

type ConnectionStatus = "Not connected" | "Connecting" | "Connected" | "Disconnected";

interface Version {
    id: string;
    prompt: string;
    language: string;
    sourceChunks: string[];
    source: string;
    markup: string;

    // Feedback
    feedbackSubmitted: boolean;
    feedbackDisabled?: boolean;
    helpful?: boolean;
    comments?: string;
}

interface SupportedGPTModel {
    key: ChatGptModel,
    version: string,
    name: string,
}

type SelectableLanguage = SupportedLanguage & { abbrev: string };

const MAX_INPUT_ROWS = 6;

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

    @Prop()
    siteUrl: string;

    @Element()
    private el: HTMLElement;

    @State()
    private conversationId: string;

    @State()
    private running: boolean = false;

    @State()
    private connectionStatus: ConnectionStatus;

    @State()
    private errorMessage: string;

    @State()
    private versions: Version[] = [];

    @State()
    private submissionCount = 0;

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

    @State()
    private pingListener: NodeJS.Timeout;

    @State()
    private existingConversationId: string;

    @State()
    private showShareMenu = false;

    @State()
    private shareMenuElement: HTMLElement;

    @State()
    private disableShareButtons = false;

    @State()
    private copyLinkText = "Copy Link";

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

        if (this.shareMenuElement && !this.shareMenuElement.contains(el)) {
            this.showShareMenu = false;
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

    private get shareableLink(): string {
        let baseUrl = this.siteUrl;
        if (baseUrl.slice(-1) === "/") {
            baseUrl = baseUrl.substring(0, baseUrl.length - 1);
        }

        if (this.versions.length === 0) {
            return `${baseUrl}/ai/`;
        }

        if (this.submissionCount === 0) {
            return `${baseUrl}/ai/?convid=${this.existingConversationId}`;
        }

        return `${baseUrl}/ai/?convid=${this.conversationId}`;
    }

    private get twitterLink() {
        let postText = "Check out what I generated with Pulumi AI!";
        if (this.versions.length === 0) {
            postText = "Pulumi AI can help you generate infrastructure as code specific to your use case. Give it a try!"
        }

        const tweet = `${postText} ${this.shareableLink}`;
        return `https://twitter.com/intent/tweet?text=${encodeURIComponent(tweet)}`;
    }

    componentWillLoad() {
        this.selectedModel = this.supportedModels.find(m => m.key === this.model) || this.supportedModels.reverse()[0];
        this.selectedLanguage = this.supportedLanguages[0];
        this.connectionStatus = "Not connected";

        this.existingConversationId = getQueryVariable("convid");
        if (this.existingConversationId) {
            this.staticWelcomeMessage = this.welcomeContent;
        }

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
                (response) => this.onComplete(response),
                () => this.onOverMessageLimit(),
                () => this.onOverCapacity(),
                (error) => this.onError(error),
                (message) => this.onClose(message),
                (data) => this.onGetConverstation(data),
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

        if (this.pingListener) {
            clearInterval(this.pingListener);
        }

        this.versions.forEach(v => {
            if (!v.feedbackSubmitted && v.helpful !== undefined) {
                this.sendFeedback(v.id);
            }
        });
    }

    private onConnected(data: CreateConnectionResponse) {
        this.connectionStatus = "Connected";
        this.conversationId = data.conversationId;

        if (this.existingConversationId) {
            console.log("exisiting conversation", this.existingConversationId);
            this.client.getConversation(this.existingConversationId);
        }

        // We ping the backend every 30 seconds to ensure
        // we are keeping connections alive.
        this.pingListener = setInterval(() => this.client.ping(), 30000);
    }

    private onGetConverstation(data: GetConversationResponse) {
        const versions: Version[] = data.conversation.map(c => {
            return {
                id: "",
                prompt: c.prompt,
                sourceChunks: [],
                source: c.response,
                language: c.language,
                markup: this.addButtons(marked.marked.parse(c.response)),
                feedbackSubmitted: false,
                feedbackDisabled: true,
            };
        });

        this.currentVersion = versions[versions.length - 1];
        this.versions = Array.from(versions);
        this.currentVersion = null;

        this.running = false;
        this.scroll();
        this.clear();
        this.focus();

        // Wait a bit for the versions to render, then colorize them.
        setTimeout(() => this.highlight(this.outputVersions), 250);
    }

    private onSubmit(event: Event) {
        event.preventDefault();
        this.submit();
    }

    private copyShareableLink() {
        clipboard.writeText(this.shareableLink);
        this.disableShareButtons = true;
        this.copyLinkText = "Link Copied!";

        setTimeout(() => {
            this.copyLinkText = "Copy Link";
            this.showShareMenu = false;
            this.disableShareButtons = false;
        }, 2000);
    }

    private get runnable() {
        return this.connectionStatus === "Connected" && !this.running && this.input.value.trim() !== "";
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
        const orderDiff = content.order - this.currentVersion.sourceChunks.length;
        if (orderDiff > 1) {
            for (let i = 0; i < (orderDiff + 1); i++) {
                this.currentVersion.sourceChunks.push("");
            }
        }

        const shouldDelete = orderDiff === 0 ? 0 : 1;
        this.currentVersion.sourceChunks.splice(content.order, shouldDelete, content.content);
        this.currentVersion.source = [ ...this.currentVersion.sourceChunks, " ⎸"].join("");
        this.currentVersion = Object.assign({}, this.currentVersion);

        this.scroll();
        this.highlight(this.outputStream);
    }

    private onComplete(response: GenerateNewOutputResponse) {
        const versionMarkup = marked.marked.parse(this.currentVersion.source.replace(" ⎸", ""));
        const markupWithButtons = this.addButtons(versionMarkup);

        this.currentVersion.id = response.resultId;
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
            this.input.rows = 1;
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

        const rows = this.input.value.split("\n").length;
        if (rows <= MAX_INPUT_ROWS) {
            this.input.rows = rows;
        }
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
            if (event.key === "Enter") {

                // If shift was pressed, add a row (up to the max number of rows).
                if (event.shiftKey && this.input.rows <= MAX_INPUT_ROWS) {
                    this.input.rows++;
                    return;
                }

                event.preventDefault();

                // If control or enter was pressed, or there's only one row, submit.
                if (this.runnable && (this.input.rows === 1 || (event.ctrlKey || event.metaKey))) {
                    this.submit();
                }
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

    private toggleShareMenu() {
        this.showShareMenu = !this.showShareMenu;
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
        return this.el.querySelector("form textarea") as HTMLTextAreaElement;
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
        this.submissionCount++;

        const query = this.input.value?.trim();

        if (!query) {
            return;
        }

        this.currentVersion = {
            prompt: query,
            id: "",
            language: this.selectedLanguage.name,
            sourceChunks: [],
            source: "",
            markup: "",
            feedbackSubmitted: false,
        };

        this.versions = Array.from(this.versions);

        this.client.submit(
            this.conversationId,
            this.selectedLanguage.name as Language,
            this.versions && this.versions.length > 0 ? this.versions[this.versions.length - 1].source : "",
            query,
            this.versions.length,
            this.selectedModel.key,
            this.existingConversationId,
        );
    }

    private handleFeedback(resultId: string, helpful: boolean) {
        const versions = [ ...this.versions ];
        const versionIndex = this.versions.findIndex(v => v.id === resultId);
        const version = this.versions[versionIndex];
        this.versions[versionIndex].helpful = helpful;
        versions[versionIndex] = version;
        this.versions = versions;
        this.scroll()
    }

    private updateFeedbackComment(resultId: string, comments: string) {
        const versions = [ ...this.versions ];
        const versionIndex = this.versions.findIndex(v => v.id === resultId);
        const version = this.versions[versionIndex];
        this.versions[versionIndex].comments = comments;
        versions[versionIndex] = version;
        this.versions = versions;
    }

    private sendFeedback(resultId: string) {
        const versions = [ ...this.versions ];
        const versionIndex = versions.findIndex(v => v.id === resultId);
        const version = versions[versionIndex];

        this.client.sendFeedback(version.id, version.helpful, version.comments);

        version.feedbackSubmitted = true;
        versions[versionIndex] = version;
        this.versions = versions;
    }

    private renderStream(markdown: string = "") {
        return marked.marked.parse(markdown);
    }

    private renderVersion(version: Version) {
        return version.markup;
    }

    private renderWelcomeMessage() {
        if (this.staticWelcomeMessage) {
            return;
        }

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

    private renderSpinner() {
        if (this.currentVersion && !this.currentVersion.source && this.running) {
            return <div class="loading-spinner">
                <div class="b1"></div>
                <div class="b2"></div>
                <div class="b3"></div>
            </div>;
        }
    }

    private renderFeedback(version: Version) {
        if (version.helpful !== undefined && !version.feedbackSubmitted) {
            return(
                <div class="feedback">
                    <p class="feedback-description">Would you like to leave a comment (optional)?</p>
                    <div class="feedback-comments">
                        <textarea rows={2} value={version.comments} onChange={(e: any) => this.updateFeedbackComment(version.id, e.target.value)} />
                        <div class="feedback-submit-button-container">
                            <button onClick={() => this.sendFeedback(version.id)} class="feedback-submit-button">Send Feedback</button>
                        </div>
                    </div>
                </div>
            );
        }

        if (version.feedbackSubmitted) {
            return(
                <div class="feedback">
                    <p class="feedback-description">Thank you for your feedback!</p>
                </div>
            );
        }

        return(
            <div class="feedback">
                <p class="feedback-description">Was this response helpful?</p>
                <div class="feedback-actions">
                    <div class="feedback-button" onClick={() => this.handleFeedback(version.id, true)}>
                        <i class="fas fa-thumbs-up"></i>
                        Yes
                    </div>

                    <div class="feedback-button" onClick={() => this.handleFeedback(version.id, false)}>
                        <i class="fas fa-thumbs-down"></i>
                        No
                    </div>
                </div>
            </div>
        );
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
                                        { !this.currentVersion && !version.feedbackDisabled ? this.renderFeedback(version) : undefined }
                                    </li>)
                                }
                                </ol>
                            </div>
                        }
                    </div>

                    {/* Loading spinner. */}
                    { this.renderSpinner() }

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
                                    <textarea rows={1} placeholder={ this.placeholder } disabled={ this.running } onInput={ this.onInput.bind(this) } maxLength={ this.client?.MAX_PROMPT_LENGTH } value={ this.prompt }></textarea>
                                    { this.renderSubmitButton(true) }
                                </form>
                            </div>
                        </div>
                        <div class="chat-details">
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

                            <div class="chat-share">
                                <div class="share-button">
                                    { this.showShareMenu ? <ul class="share-button-options" ref={(el) => this.shareMenuElement = el}>
                                        <div class="caret"></div>

                                        <li class={this.disableShareButtons ? "disabled" : ""} onClick={() => this.copyShareableLink()}>
                                            <span><i class="fas fa-link"></i>{this.copyLinkText}</span>
                                        </li>

                                        <li class={this.disableShareButtons ? "disabled" : ""}>
                                            <a href={this.twitterLink} target="_blank" rel="noopener noreferrer"><i class="fab fa-twitter"></i>Share on Twitter</a>
                                        </li>
                                    </ul> : undefined}

                                    { this.versions.length ? <div class="share-link" onClick={() => this.toggleShareMenu()}>
                                        <span><i class="fas fa-share-square"></i> Share conversation</span>
                                    </div> : undefined }
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        );
    }
}
