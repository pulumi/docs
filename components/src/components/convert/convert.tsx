import { Component, Element, h, Prop, State } from '@stencil/core';
import { awsEC2Ubuntu } from "./examples/tf";

interface CannedExample {
    [key: string]: string;
}

@Component({
    tag: "pulumi-convert",
    styleUrl: "./convert.scss",
    shadow: false
})
export class Convert {

    @Prop()
    kind: "tf" | "k8s" | "crd" | "arm";

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
        if (this.kind === "tf") {
            this.setInput(this.tf.awsEC2Ubuntu);
            this.submit();
        }
    }

    private get inputEl() {
        return (this.el.querySelector("#code-input") as HTMLTextAreaElement);
    }

    private get outputEl() {
        return (this.el.querySelector("#code-output") as HTMLTextAreaElement);
    }

    // private get inputLangEl() {
    //     return (this.el.querySelector("#code-input-language") as HTMLTextAreaElement);
    // }

    private get outputLangEl() {
        return (this.el.querySelector("#code-output-language") as HTMLTextAreaElement);
    }

    private setInput(value: string) {
        this.inputEl.value = value;
    }

    private setOutput(_filename: string, value: string) {
        this.outputEl.value = value;
    }

    private async fetchResult(code: string, language: string) {
        this.fetching = true;

        // Endpoint will need to handle the selected kind -- tf, etc. (Right now, it's all tf.)

        try {
            const response = await fetch(`${this.endpoint}`, {
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

    private submit() {
        this.fetchResult(this.inputEl.value, this.outputLangEl.value);
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
                <div>
                    <div>
                        <textarea id="code-input"></textarea>
                        <button onClick={this.submit.bind(this)}>Submit</button>
                    </div>
                    <textarea id="code-output"></textarea>
                </div>
                <div>

                </div>
            </div>
        );
    }
}
