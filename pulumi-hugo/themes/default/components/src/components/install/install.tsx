import { Component, Element, h, Prop, State } from '@stencil/core';
import { OSKey } from "../chooser/chooser";

@Component({
    tag: "pulumi-install",
    styleUrl: "install.scss",
})
export class Install {

    @Element()
    el: HTMLElement;

    @Prop({ mutable: true })
    os?: OSKey;

    @State()
    tooltipContent: string;

    defaultTooltipContent = "Copy command";

    componentWillLoad() {
        this.tooltipContent = this.defaultTooltipContent
    }

    componentDidLoad() {
        if (!this.os) {
            this.os = this.detectOS();
        }
    }

    private detectOS(): OSKey {
        const appVersion = navigator.appVersion;

        if (appVersion.indexOf("Win") !== -1) {
            return "windows";
        } else if (appVersion.indexOf("Mac") !== -1) {
            return "macos";
        }

        return "linux";
    }

    private get installCommand(): string {
        const commands = {
            macos: "brew install pulumi",
            windows: "choco install pulumi",
            linux: "curl -fsSL https://get.pulumi.com | sh",
        };
        return commands[this.os];
    }

    private copyToClipboard() {
        clipboard.writeText(this.installCommand.toString())
            .then(() => {
                this.tooltipContent = "Copied!";
                setTimeout(() => this.tooltipContent = this.defaultTooltipContent, 3000);
            });
    }

    render() {
        return (
            <div>
                <div class="command-text">
                    <p>
                        <span>{this.installCommand}</span>
                    </p>
                </div>
                <div class="copy-button">
                    <pulumi-tooltip>
                        <button onClick={this.copyToClipboard.bind(this)}>
                            <i class="far fa-copy"></i>
                        </button>
                        <span slot="content">{this.tooltipContent}</span>
                    </pulumi-tooltip>
                </div>
            </div>
        );
    }
}
