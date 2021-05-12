import { Component, Element, h, Prop, State } from '@stencil/core';

export type SourceKind = "tf" | "kube" | "arm";
export type InputEditorMode = "ruby" | "javascript" | "yaml";
export type OutputEditorLanguage = "typescript" | "python" | "go" | "csharp";
export type OutputEditorFilename = "index.ts" | "index.js" | "__main__.py" | "main.go" | "MyStack.cs";

export interface SourceFile {
    name: string;
    filename: string;
    description: string,
    code: string;
}

interface SupportedLanguage {
    key: OutputEditorLanguage;
    name: string;
    filename: OutputEditorFilename;
}

interface ConvertServiceResult {
    files: {
        [filename: string]: string
    };
    diagnostics: string;
    error: string;
}

interface OutputEditorResult {
    filename: string;
    code: string;
    diagnostics: string;
    status: {
        success: boolean;
        message: string;
    }
}

@Component({
    tag: "pulumi-convert",
    styleUrl: "./convert.scss",
    shadow: false
})
export class Convert {

    @Prop()
    from: SourceKind;

    @Prop()
    endpoint: string;
    endpointURL: URL;

    @Prop()
    examples: string;

    @State()
    sourceFiles: SourceFile[] = [];

    @Prop()
    theme: string = "";

    @Element()
    el: HTMLElement;

    @State()
    converting: boolean = false;

    @State()
    convertible: boolean = false;

    inputEditor: CodeMirror.EditorFromTextArea;
    selectedSourceFile: SourceFile;
    customSourceFile: SourceFile;

    outputEditor: CodeMirror.EditorFromTextArea;
    selectedOutputLanguage: SupportedLanguage;
    outputResult: OutputEditorResult;

    supportedLanguages: SupportedLanguage[] = [
        { key: "typescript", name: "TypeScript", filename: "index.ts" },
        { key: "python", name: "Python", filename: "__main__.py" },
        { key: "go", name: "Go", filename: "main.go", },
        { key: "csharp", name: "C#", filename: "MyStack.cs" },
    ];

    componentDidLoad() {
        try {
            this.validateProps();
            this.validateGlobals();
            this.prepareEditors();
            this.prepareSourceFiles();
        }
        catch(error) {
            console.error(error.message);
        }
    }

    // The textarea input element that backs the CodeMirror UI.
    private get inputEditorEl() {
        return (this.el.querySelector("#editor-input") as HTMLTextAreaElement);
    }

    // The textarea output that backs the CodeMirror UI.
    private get outputEditorEl() {
        return (this.el.querySelector("#editor-output") as HTMLTextAreaElement);
    }

    // The CodeMirror language mode. https://codemirror.net/mode/
    private get inputEditorMode(): InputEditorMode {
        switch (this.from) {
            case "tf":
                return "ruby";
            case "kube":
                return "yaml";
            case "arm":
                return "javascript";
        }
    }

    // The content of the input editor.
    private get inputEditorValue() {
        return this.inputEditor.getValue();
    }

    // The default filename for the editor. Used only for display purposes.
    private get inputEditorDefaultFilename(): string {
        switch (this.from) {
            case "tf":
                return "main.tf";
            case "kube":
                return "kube.yaml";
            case "arm":
                return "azuredeploy.json";
        }
    }

    // The friendly name of the language we're converting from.
    private get sourceLanguageName(): string {
        switch (this.from) {
            case "tf":
                return "Terraform";
            case "kube":
                return "Kubernetes YAML";
            case "arm":
                return "ARM";
        }
    }

    // The relative path to the conversion endpoint.
    private get endpointPath(): string {
        switch (this.from) {
            case "tf":
                return "convert";
            case "arm":
                return "convertARM";
            case "kube":
                return "convertKube";
        }
    }

    // The CLI tool that corresponds with the language we're converting from.
    private get conversionTool(): { name: string; githubURL: string } {
        switch (this.from) {
            case "tf":
                return {
                    name: "tf2pulumi",
                    githubURL: "https://github.com/pulumi/tf2pulumi",
                };
            case "kube":
                return {
                    name: "kube2pulumi",
                    githubURL: "https://github.com/pulumi/kube2pulumi",
                };
            case "arm":
                return {
                    name: "arm2pulumi",
                    githubURL: "https://github.com/pulumi/arm2pulumi",
                };
            default:
                return {
                    name: `${this.from}2pulumi`,
                    githubURL: "https://github.com/pulumi/pulumi",
                };
        }
    }

    // Ensure the supporting libraries we expect have been loaded and their globals are usable.
    private validateGlobals() {
        const missingGlobals = [
            typeof CodeMirror,
            typeof JSZip,
            typeof saveAs,
            typeof clipboard,
        ].filter(result => result === "undefined");

        if (missingGlobals.length > 0) {
            throw new Error(
                "The pulumi-convert component requires CodeMirror, JZSip, FileSaver, and clipboard-polyfill. " +
                "Please ensure each of these scripts has been loaded into global before using it."
            );
        }
    }

    // Validate the set of input attributes. Only `from` and `endpoint` are required.
    private validateProps() {
        const errors: string[] = [];

        if (!this.from || !["tf", "kube", "arm"].includes(this.from)) {
            errors.push("A valid `from` attribute is required.");
        }

        try {
            this.endpointURL = new URL(this.endpoint);
        }
        catch(error) {
            errors.push("A valid `endpoint` attribute is required.");
        }

        if (!this.examples) {
            console.warn("A list of examples was provided.");
        }

        if (!this.theme) {
            console.warn("A CodeMirror theme was not specified. The Using `material-ocean`.");
        }

        if (errors.length) {
            throw new Error(errors.join("\n"));
        }
    }

    // Set up the CodeMirror editors.
    private prepareEditors() {
        this.selectedOutputLanguage = this.supportedLanguages[0];

        const config: CodeMirror.EditorConfiguration = {
            lineNumbers: true,
            theme: this.theme || "",
        };

        this.inputEditor = CodeMirror.fromTextArea(this.inputEditorEl, {
            ...config,
            indentUnit: this.from === "kube" ? 2 : 4,
            mode: this.inputEditorMode,
        });

        this.outputEditor = CodeMirror.fromTextArea(this.outputEditorEl, {
            ...config,
            readOnly: true,
        });

        this.inputEditor.on("change", () => {
            this.convertible = this.inputEditorValue.trim() !== "";

            if (this.selectedSourceFile === this.customSourceFile) {
                this.customSourceFile.code = this.inputEditorValue;
            }
        });

        this.inputEditor.on("keydown", (_instance: CodeMirror.Editor, event: KeyboardEvent) => {

            // On Command-Enter or Command-s, submit.
            if (event.metaKey && (event.key === "Enter" || event.key === "s")) {
                event.preventDefault();
                this.convert();
            }
        });
    }

    // Set up the input/example tabs.
    private prepareSourceFiles() {
        this.sourceFiles = [];

        if (this.examples && this.examples.length > 0) {
            try {
                this.sourceFiles.push(...JSON.parse(this.examples));
            }
            catch(error) {
                console.error("Failed to load examples:", error);
            }
        }

        this.customSourceFile  = {
            name: `Custom`,
            description: `Convert your own ${this.sourceLanguageName} code.`,
            filename: this.inputEditorDefaultFilename,
            code: "",
        }

        this.sourceFiles.push(this.customSourceFile);
        this.selectSourceFile(this.sourceFiles[0]);
        this.convert();
    }

    // Handle selection of an input tab.
    private selectSourceFile(file: SourceFile) {
        this.selectedSourceFile = file;
        this.inputEditor.setValue(file.code);
        this.inputEditor.clearHistory();
        this.convert();
    }

    // Handle selection of an output tab.
    private selectOutputLanguage(language: SupportedLanguage) {
        this.selectedOutputLanguage = language;
        this.convert();
    }

    // Set the output result, which updates the display of the output editor.
    private setOutputResult(result: OutputEditorResult) {
        this.outputResult = result;
        this.outputEditor.setValue(result ? result.code : "");
    }

    // clipboard is declared as a global and exposed by clipboard-polyfill.
    private copyToClipboard() {
        clipboard.writeText(this.outputEditor.getValue());
    }

    // saveAs is declared as a global by FileSaver.
    private downloadZip() {
        const zip = new JSZip();
        zip.file(this.outputResult.filename, this.outputResult.code);
        zip.generateAsync({ type: "blob" })
            .then(content => {
                saveAs(content, `${this.from}2pulumi.zip`);
            });
    }

    // Convert the code provided.
    private async convert() {
        this.setOutputResult(null);

        const code = this.inputEditorValue;
        const language = this.selectedOutputLanguage;

        if (!code) {
            return;
        }

        this.converting = true;

        try {
            const response = await fetch([ this.endpointURL, this.endpointPath].join("/"), {
                method: "POST",
                mode: "cors",
                body: JSON.stringify({
                    code,
                    language: language.key,
                }),
            });

            const result: ConvertServiceResult = await response.json();

            if (result.error) {
                this.setOutputResult({
                    filename: "",
                    code: "",
                    diagnostics: result.diagnostics || "",
                    status: {
                        success: false,
                        message: result.error,
                    }
                });

            } else if (result.files) {
                let [ filename, code ] = Object.entries(result.files)[0];

                // Nasty hack alert: The service currently returns bogus filenames like
                // "ouput" and "output". While we await a service-side fix for this, if
                // what we get back doesn't look like an actual filename, hard-code
                // something appropriate for the selected language.
                if (!filename.match(/\w+\.\w+/)) {
                    filename = this.supportedLanguages.find(sl => sl.key === language.key).filename;
                }

                // Additionally, the kube2pulumi endpoint returns "no diagnostics" when
                // there are no diagnostics.
                const diagnostics = result.diagnostics?.replace(/^no diagnostics$/, "") || ""

                if (filename && code) {
                    this.setOutputResult({
                        filename,
                        code,
                        diagnostics,
                        status: {
                            success: true,
                            message: filename,
                        }
                    });
                }

                if (diagnostics) {
                    this.outputResult.diagnostics = diagnostics;
                }
            }
        }
        catch(error) {
            console.error(`Submission failed: ${error}`);
        }

        this.converting = false;
    }

    // Assemble the classNames for use in the status bar.
    private get statusBarClasses(): string {
        const classes = ["status-bar"];

        if (this.converting) {
            classes.push("converting");
        };

        if (this.outputResult) {
            if (this.outputResult.diagnostics) {
                classes.push("warn");
            } else {
                classes.push(this.outputResult.status.success ? "success" : "error");
            }
        }

        return classes.join(" ");
    }

    // A helper function that turns an array of classNames into a space-delimited string.
    private combineClasses(...classes: string[]) {
        return classes.filter(c => c && c !== "").join(" ");
    }

    // Render the editor's "window" bar.
    private renderWindowBar() {
        return <div class="window-bar">
            <div class="window-bar-buttons">
                <div class="window-bar-button"></div>
                <div class="window-bar-button"></div>
                <div class="window-bar-button"></div>
            </div>
        </div>;
    }

    // Render an individual editor tab.
    private renderTab(item: any, activeItem: any, label: string, title: string, handler: Function): HTMLLIElement {
        return <li onClick={ handler.bind(this, item) }
            class={ this.combineClasses("tab", item === activeItem ? "active" : "") }
            title={ title }>
            <span class="label">{ label }</span>
            <span class="indicator"></span>
        </li>;
    }

    // Render a convert button.
    private renderConvertButton(withTooltip: boolean) {
        const title = `Convert this ${ this.sourceLanguageName } code to ${ this.selectedOutputLanguage?.name }`;

        const button = <button
            onClick={ this.convert.bind(this) }
            class={ this.combineClasses("btn-convert", this.converting ? "converting" : "") }
            title={ title }
            disabled={ !this.convertible || this.converting }>
            <span class="label">Convert</span>
            <span class="icon"></span>
        </button>;

        if (!withTooltip) {
            return button;
        }

        return <pulumi-tooltip>
            { button }
            <span slot="content">
                { title }
            </span>
        </pulumi-tooltip>
    }

    // Render an editor status bar.
    private renderStatusBar(type: "input" | "output") {
        switch (type) {
            case "input":
                return <div class="status-bar">
                    <span class="message">
                        { this.selectedSourceFile?.filename }
                        { this.selectedSourceFile?.description ? ` • ${this.selectedSourceFile.description}` : ""}
                    </span>
                </div>;
            case "output":
                const issueURL = this.conversionTool.githubURL + "/issues"
                return <div class={ this.statusBarClasses }>
                    <span class="icon"></span>
                    <span class="message">{ this.outputResult?.status?.message }</span>
                    <div class="alert alert-error">
                        <p>
                            <strong>Sorry, we were unable to convert your code.</strong>
                        </p>
                        <p>
                            There could be a problem with the code you submitted, or it might use a
                            feature { this.conversionTool.name } doesn't yet support. See below for details.
                            Please also check the <a href={issueURL}>known issues</a> or
                            report a <a href={issueURL}>new issue</a> if you believe this
                            might be a bug or missing feature in { this.conversionTool.name }.

                            For help converting this or another { this.sourceLanguageName } project to Pulumi,
                            please join us in the <a href="https://slack.pulumi.com/">Pulumi Community Slack</a>.
                            We're here to help!
                        </p>
                    </div>
                    <div class="alert alert-warn">
                        <p>
                            <strong>Sorry, we were unable to convert your code completely.</strong>
                        </p>
                        <p>
                            The code you submitted was valid, but { this.conversionTool.name } was unable to
                            convert it completely, so a partial conversion has been provided for you. See below
                            for details. Please also check the <a href={issueURL}>known issues</a> or
                            report a <a href={issueURL}>new issue</a> if you believe this
                            might be a bug or missing feature in { this.conversionTool.name }.

                            For help converting this or another { this.sourceLanguageName } project to Pulumi,
                            please join us in the <a href="https://slack.pulumi.com/">Pulumi Community Slack</a>.
                            We're here to help!
                        </p>
                    </div>
                </div>;
            default:
                return <div class="status-bar">
                    <span class="message">&nbsp;</span>
                </div>;
        }
    }

    private renderDiagnostics() {
        if (this.outputResult?.diagnostics) {
            console.log("Conversion completed with errors. Diagnostics:")
            console.log(this.outputResult?.diagnostics);

            return <div class="diagnostics">
                <p>
                    <strong>Diagnostics:</strong>
                </p>
                <p class="details">
                    { this.outputResult.diagnostics }
                </p>
            </div>;
        }
    }

    // Render the full component.
    render() {
        return <div>
            <div id="editors">
                <div class="editor editor-input">
                    <div class="editor-heading">
                        <h3>
                            <span class="editor-step">1</span>
                            Start with some { this.sourceLanguageName }.
                        </h3>
                        <p>
                            We've included a few examples for reference &mdash; feel free to edit them as you like,
                            or replace them with your own code. (And don't worry, we send your code over SSL
                            and don't store anything on our servers.) When you're ready to transform
                            your { this.sourceLanguageName } code to Pulumi, click <strong>Convert</strong>.
                        </p>
                    </div>
                    <div class="editor-container">
                        { this.renderWindowBar() }
                        <ul class="tabs">
                            {
                                this.sourceFiles.map(file =>
                                    this.renderTab(file, this.selectedSourceFile, file.name, file.description, this.selectSourceFile)
                                )
                            }
                            <li class="actions">
                                { this.renderConvertButton(true) }
                            </li>
                        </ul>
                        <textarea id="editor-input"></textarea>
                        { this.renderStatusBar("input") }
                    </div>
                </div>
                <div class={ this.combineClasses("editor", "editor-output", this.converting ? "converting" : "") }>
                    <div class="editor-heading">
                        <h3>
                            <span class="editor-step">2</span>
                            Turn it into your language of choice.
                        </h3>
                        <p>
                            Your code will be converted
                            with { this.conversionTool.githubURL ? <a href={ this.conversionTool.githubURL }>{ this.conversionTool.name }</a> : this.conversionTool.name },
                            an open-source command-line tool we built to make it as easy as possible for you to migrate
                            your existing { this.sourceLanguageName } projects to Pulumi. The resulting file can
                            be copied or downloaded for use with <a href="https://pulumi.com/start">a new Pulumi project</a>.
                        </p>
                        <div>
                            { this.renderConvertButton(false) }
                        </div>
                    </div>
                    <div class="editor-container">
                        { this.renderWindowBar() }
                        <ul class="tabs">
                            {
                                this.supportedLanguages.map(language =>
                                    this.renderTab(language, this.selectedOutputLanguage, language.name, language.name, this.selectOutputLanguage)
                                )
                            }
                            <li class="actions">
                                <pulumi-tooltip>
                                    <button onClick={ this.copyToClipboard.bind(this) } class="btn-copy">
                                        <i></i>
                                    </button>
                                    <span slot="content">Copy to clipboard</span>
                                </pulumi-tooltip>
                                <pulumi-tooltip>
                                    <button onClick={ this.downloadZip.bind(this) } class="btn-download">
                                        <i></i>
                                    </button>
                                    <span slot="content">Download as .zip</span>
                                </pulumi-tooltip>
                            </li>
                        </ul>
                        <div class="editor-spinner"></div>
                        <textarea id="editor-output"></textarea>
                        { this.renderStatusBar("output") }
                    </div>
                    { this.renderDiagnostics() }
                </div>
            </div>
        </div>;
    }
}
