import { Component, Element, h, Prop, State } from '@stencil/core';
import { awsEC2Ubuntu } from "./examples/tf";

// import monaco from "monaco-editor";

interface CannedExample {
    [key: string]: string;
}

export type ConvertKind = "tf" | "k8s" | "arm";
export type EditorLanguage = "hcl" | "json" | "yaml";

@Component({
    tag: "pulumi-convert",
    styleUrl: "./convert.scss",
    shadow: false
})
export class Convert {

    @Prop()
    kind: ConvertKind;

    @Prop()
    endpoint: string;

    @Element()
    el: HTMLElement;

    @State()
    fetching: boolean = false;

    // Canned examples
    private tf: CannedExample = {
        awsEC2Ubuntu,
    }

    componentDidLoad() {
        console.log(Date.now());

        if (this.kind === "tf") {
            this.prepareEditors(this.tf.awsEC2Ubuntu);
            // this.setInput(this.tf.awsEC2Ubuntu);
            this.submit();
        }
    }

    inputEditor: any;
    outputEditor: any;

    private get inputEditorEl() {
        return (this.el.querySelector("#editor-input") as HTMLElement);
    }

    private get outputEditorEl() {
        return (this.el.querySelector("#editor-output") as HTMLElement);
    }

    private get outputLangEl() {
        return (this.el.querySelector("#code-output-language") as HTMLTextAreaElement);
    }

    private setOutput(_filename: string, value: string) {
        this.outputEditor.setValue(value);
    }

    private async fetchResult(code: string, language: string) {
        this.fetching = true;

        try {
            const response = await fetch(`${this.endpoint}/${this.endpointPath}`, {
                method: "POST",
                mode: "cors",
                body: JSON.stringify({
                    code,
                    language,
                }),
            });

            // TODO: Type the result.
            const result: any = await response.json();
            const filenames = Object.keys(result.files);
            const filename = filenames[0];

            if (filename) {
                this.setOutput(filename, result.files[filename]);
            }
        }
        catch(e) {
            console.error(e);
        }

        this.fetching = false;
    }

    private prepareEditors(code: string) {
        const monaco = window["monaco"];

        if (!monaco) {
            console.log("This component requires Monaco editor.");
            return;
        }

        /**
         * Input editor.
         */

        this.inputEditor = monaco.editor.create(
            this.inputEditorEl,
            {
                theme: "vc",
                roundedSelection: true,
                lineNumbers: "off",
                minimap: {
                    enabled: false,
                },

                language: this.inputEditorLanguage,
                value: code,
            },
        );

        this.inputEditor.onDidChangeModelContent(() => {
            this.submit();
        });

        /**
         * Output editor.
         */

        this.outputEditor = monaco.editor.create(
            this.outputEditorEl,
            {
                theme: "vc",
                roundedSelection: true,
                lineNumbers: "off",
                minimap: {
                    enabled: false,
                },
                readOnly: true,
                language: this.outputLangEl.value,
            },
        );
    }

    private submit() {
        this.fetchResult(this.inputEditor.getValue(), this.outputLangEl.value);
    }

    private get inputEditorLanguage(): EditorLanguage | undefined {
        switch (this.kind) {
            case "tf":
                return "hcl";
            case "k8s":
                return "yaml";
            case "arm":
                return "json";
        }
    }

    private get endpointPath(): string {
        switch (this.kind) {
            case "tf":
                return "convert";
            case "arm":
                return "convertARM";
            case "k8s":
                return "convertKube";
        }
    }

    render() {
        return (
            <div>
                <p>
                    <span>Convert your </span>
                    <select id="code-input-language" onChange={this.submit.bind(this)}>
                        <option value="tf">Terraform</option>
                        <option value="k8s">Kubernetes YAML</option>
                        <option value="arm">ARM Template</option>
                    </select>
                    <span>to Pulumi!</span>
                    <select id="code-output-language" onChange={this.submit.bind(this)}>
                        <option value="typescript">TypeScript</option>
                        <option value="python">Python</option>
                        <option value="go">Go</option>
                        <option value="csharp">C#</option>
                    </select>
                </p>
                <div id="editors">
                    <div id="editor-input"></div>
                    <div id="editor-output"></div>
                </div>
            </div>
        );
    }
}
