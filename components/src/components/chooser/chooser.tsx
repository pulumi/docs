import { Component, h, Prop, State, Watch } from "@stencil/core";
import { Store, Unsubscribe } from "@stencil/redux";
import { AppState } from "../../store/state";
import { setLanguage, setK8sLanguage, setOS, setCloud } from "../../store/actions/preferences";

export type LanguageKey = "javascript" | "typescript" | "python" | "go" | "csharp" | "fsharp" | "visualbasic"
export type K8sLanguageKey = "typescript" | "yaml" | "typescript-kx"
export type OSKey = "macos" | "linux" | "windows"
export type CloudKey = "aws" | "azure" | "gcp"

export type ChooserType = "language" | "k8s-language" | "os" | "cloud";
export type ChooserKey = LanguageKey | K8sLanguageKey | OSKey | CloudKey;
export type ChooserOption = SupportedLanguage | SupportedK8sLanguage | SupportedOS | SupportedCloud;

interface SupportedLanguage {
    key: LanguageKey;
    name: string;
    preview: boolean;
}

interface SupportedK8sLanguage {
    key: K8sLanguageKey;
    name: string;
    preview: boolean;
}

interface SupportedOS {
    key: OSKey;
    name: string;
    preview: boolean;
}

interface SupportedCloud {
    key: CloudKey;
    name: string;
    preview: boolean;
}

export interface Choice {
    type: ChooserType;
    value: ChooserOption;
}

/**
 * The Chooser component renders a set of selectable tabs based on the type and options
 * properties provided. For example, this definition:
 *
 *     <pulumi-chooser type="language" value="typescript,python,go"></pulumi-chooser>
 *
 * ...would render three tabs. Clicking a tab dispatches an action that sets the
 * associated value on the store, allowing any pulumi-choosable component on the page to
 * be shown or hidden automatically.
 */
@Component({
    tag: "pulumi-chooser",
    styleUrl: "chooser.scss",
    shadow: false,
})
export class Chooser {
    private storeUnsubscribe: Unsubscribe;

    // A handle to the application store.
    @Prop({ context: "store" })
    store: Store;

    // The type of chooser to render (e.g., language, os, or cloud).
    @Prop({ mutable: true })
    type: ChooserType;

    // The options to use for the chooser tabs, represented as a comma-delimited string
    // (e.g., "typescript,csharp,go"). Order doesn't matter; it's handled internally.
    @Prop({ mutable: true })
    options: string;

    // The currently selected option.
    @Prop({ mutable: true })
    selection: ChooserKey;

    // The currently visible set of chooser options.
    @State()
    currentOptions: ChooserOption[] = [];

    // Dispatch functions for handling the selection of an option.
    setLanguage: typeof setLanguage;
    setK8sLanguage: typeof setK8sLanguage;
    setOS: typeof setOS;
    setCloud: typeof setCloud;

    componentWillLoad() {

        // Map currently selected values from the store, so we can use them in this component.
        this.storeUnsubscribe = this.store.mapStateToProps(this, (state: AppState) => {
            const { preferences: { language, k8sLanguage, os, cloud } } = state;

            switch (this.type) {
                case "language":
                    return { selection: language };
                case "k8s-language":
                     return { selection: k8sLanguage };
                case "os":
                    return { selection: os };
                case "cloud":
                    return { selection: cloud };
                default:
                    return {};
            }
        });

        // Map internal methods to actions defined on the store.
        this.store.mapDispatchToProps(this, { setLanguage, setK8sLanguage, setOS, setCloud });

        // Translate the set of options provided into choices.
        this.parseOptions();
    }

    componentDidUnload() {
        this.storeUnsubscribe();
    }

    @Watch("type")
    onType(_value: string) {
        this.parseOptions();
    }

    @Watch("options")
    onOptions(_value: string) {
        this.parseOptions();
    }

    @Watch("selection")
    onSelection(_value: LanguageKey) {
        this.parseOptions();
    }

    render() {
        return <ul>
            {
                // Render the current set of options, marking the selected one active.
                this.currentOptions.map(opt => <li class={this.selection === opt.key ? "active" : ""}>
                    <a onClick={() => this.makeChoice(this.type, opt)}>
                        {opt.name} { opt.preview ? <span>PREVIEW</span> : ""}
                    </a>
                </li>)
            }
        </ul>;
    }

    // Convert inbound options lists into ChooserKeys, so they can be converted into
    // ChooserOptions.
    private parseOptions() {
        this.currentOptions = [];

        if (this.type && this.options) {
            try {
                const keys: string[] = this.options.split(",").map(s => s.trim());
                this.mapOptions(this.type, keys as ChooserKey[]);
            }
            catch (err) {
                console.log(err);
            }
        }
    }

    // Convert a list of ChooserKeys values into a set of ChooserOptions.
    private mapOptions(type: ChooserType, keys: ChooserKey[]): void {
        let options: ChooserOption[] = [];

        switch (type) {
            case "language":
                options = this.supportedLanguages;
                break;
            case "k8s-language":
                options = this.supportedk8sLanguages;
                break;
            case "os":
                options = this.supportedOSs;
                break;
            case "cloud":
                options = this.supportedClouds;
                break;
        }

        this.currentOptions = options.filter(opt => keys.includes(opt.key))
    }

    // Handle the selection of chooser item.
    private makeChoice(type: ChooserType, choice: ChooserOption) {
        const key = choice.key;

        switch (type) {
            case "language":
                this.setLanguage(key as LanguageKey);
                break;
            case "k8s-language":
                this.setK8sLanguage(key as K8sLanguageKey);
                break;
            case "os":
                this.setOS(key as OSKey);
                break;
            case "cloud":
                this.setCloud(key as CloudKey);
                break;
        }
    }

    // The list of supported languages.
    private supportedLanguages: SupportedLanguage[] = [
        {
            key: "typescript",
            name: "TypeScript",
            preview: false,
        },
        {
            key: "javascript",
            name: "JavaScript",
            preview: false,
        },
        {
            key: "python",
            name: "Python",
            preview: false,
        },
        {
            key: "go",
            name: "Go",
            preview: true,
        },
        {
            key: "csharp",
            name: "C#",
            preview: true,
        },
        {
            key: "fsharp",
            name: "F#",
            preview: true,
        },
        {
            key: "visualbasic",
            name: "VB",
            preview: true,
        }
    ];

    // The list of supported Kubernetes languages.
    private supportedk8sLanguages: SupportedK8sLanguage[] = [
        {
            key: "typescript",
            name: "TypeScript",
            preview: false,
        },
        {
            key: "typescript-kx",
            name: "TypeScript KX",
            preview: false,
        },
        {
            key: "yaml",
            name: "YAML",
            preview: false,
        },
    ];

    // The list of supported operating systems.
    private supportedOSs: SupportedOS[] = [
        {
            key: "macos",
            name: "macOS",
            preview: false,
        },
        {
            key: "windows",
            name: "Windows",
            preview: false,
        },
        {
            key: "linux",
            name: "Linux",
            preview: false,
        },
    ];

    // The list of supported clouds.
    private supportedClouds: SupportedCloud[] = [
        {
            key: "aws",
            name: "AWS",
            preview: false,
        },
        {
            key: "azure",
            name: "Azure",
            preview: false,
        },
        {
            key: "gcp",
            name: "GCP",
            preview: false,
        },
    ];
}
