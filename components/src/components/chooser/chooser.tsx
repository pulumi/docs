import { Component, Element, h, Listen, Prop, State } from "@stencil/core";
import { Store, Unsubscribe } from "@stencil/redux";
import { AppState } from "../../store/state";
import { setLanguage, setK8sLanguage, setInputKind, setOS, setCloud } from "../../store/actions/preferences";

export type LanguageKey = "javascript" | "typescript" | "python" | "go" | "csharp" | "fsharp" | "visualbasic";
export type K8sLanguageKey = "typescript" | "yaml" | "typescript-kx";
export type InputKindKey = "code" | "url" | "upload";
export type OSKey = "macos" | "linux" | "windows";
export type CloudKey = "aws" | "azure" | "gcp" | "kubernetes";

export type ChooserMode = "local" | "global";
export type ChooserOptionStyle = "tabbed" | "none";
export type ChooserType = "language" | "k8s-language" | "input-kind" | "os" | "cloud";
export type ChooserKey = LanguageKey | K8sLanguageKey | InputKindKey | OSKey | CloudKey;
export type ChooserOption = SupportedLanguage | SupportedK8sLanguage | SupportedInputKind | SupportedOS | SupportedCloud;

interface SupportedLanguage {
    key: LanguageKey;
    name: string;
    extension: string;
    preview: boolean;
}

interface SupportedK8sLanguage {
    key: K8sLanguageKey;
    name: string;
    preview: boolean;
}

interface SupportedInputKind {
    key: InputKindKey;
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
 *
 * Alternatively, you can provide one or more pulumi-choosable components as children of
 * this component, which will have the effect of treating them as tabbed content,
 * irrespective of what may or may not be set on the global store. For example:
 *
 *     <pulumi-chooser type="language" value="typescript,javascript">
 *         <pulumi choosable type="language" value="typescript">Some TypeScript</pulumi-choosable>
 *         <pulumi choosable type="language" value="javascript">Some JavaScript</pulumi-choosable>
 *     </pulumi-chooser>
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

    // A handle to the host element.
    @Element()
    el: HTMLElement;

    // The type of chooser to render (e.g., "language", "os", "cloud").
    @Prop({ mutable: true })
    type: ChooserType;

    // The options to use for the chooser tabs, represented as a comma-delimited string
    // (e.g., "typescript,csharp,go"). Order doesn't matter; it's handled internally.
    @Prop({ mutable: true })
    options: string;

    // The currently selected option.
    @Prop({ mutable: true })
    selection: ChooserKey;

    // The current style option. Tabbed by default.
    @Prop({ mutable: true })
    optionStyle: ChooserOptionStyle;

    // The chooser mode -- either global (the default), meaning it works in conjunction
    // with the global state store, or local, meaning it operates solely on its
    // pulumi-chooser children.
    @Prop({ mutable: true })
    mode: ChooserMode;

    // The currently visible set of chooser options.
    @State()
    currentOptions: ChooserOption[] = [];

    // Dispatch functions for handling the selection of an option.
    setLanguage: typeof setLanguage;
    setK8sLanguage: typeof setK8sLanguage;
    setInputKind: typeof setInputKind;
    setOS: typeof setOS;
    setCloud: typeof setCloud;

    componentWillLoad() {

        // Translate the set of options provided into choices.
        this.parseOptions();
    }

    componentDidUnload() {
        if (this.storeUnsubscribe) {
            this.storeUnsubscribe();
        }
    }

    componentDidRender() {
        this.applyChoice();
    }

    @Listen("rendered", { target: "document" })
    onRendered(_event: CustomEvent) {

        // By default, choosers act globally and use a tabbed layout.
        this.mode = "global";
        this.optionStyle = "tabbed";

        // As this callback may be invoked before the component's first lifecycle method,
        // we parse the set of options provided just to be sure we have a default option
        // to select if we need to.
        this.parseOptions();

        // Map internal methods to actions defined on the store.
        this.store.mapDispatchToProps(this, { setLanguage, setK8sLanguage, setInputKind, setOS, setCloud });

        // Map currently selected values from the store, so we can use them in this component.
        this.storeUnsubscribe = this.store.mapStateToProps(this, (state: AppState) => {
            const { preferences: { language, k8sLanguage, inputKind, os, cloud } } = state;

            // In some cases, the user's preferred (i.e., most recently selected) choice
            // may not be available as an option. When that happens, we switch into local
            // mode and choose the first available option, to make sure at least one
            // choosable item is always visible.
            const preferredOrDefault = (key: ChooserKey) => {
                if (!this.currentOptions.find(o => o.key === key)) {
                    const defaultChoice = this.currentOptions[0];
                    key = defaultChoice.key;

                    if (this.choosables.length > 0) {
                        this.mode = "local";

                        // Tell the children of this chooser they're local now, too.
                        this.choosables.forEach(choosable => {
                            choosable.setAttribute("mode", "local");
                        })

                        // In local mode, there's no need to listen for store updates anymore,
                        // so we unsubscribe.
                        setTimeout(() => this.storeUnsubscribe());

                    } else {

                        // This is a global chooser with (presumably) on-page choosables,
                        // so we need to dispatch an event to reset the selected language.
                        setTimeout(() => this.setChoice(this.type, defaultChoice));
                    }
                }
                return { selection: key };
            }

            switch (this.type) {
                case "language":
                    return preferredOrDefault(language);
                case "k8s-language":
                    return preferredOrDefault(k8sLanguage);
                case "input-kind":
                    return preferredOrDefault(inputKind);
                case "os":
                    return preferredOrDefault(os);
                case "cloud":
                   return preferredOrDefault(cloud);
                default:
                    return {};
            }
        });
    }

    render() {
        return [
            <ul>
                {
                    // Render the current set of options, marking the selected one active.
                    this.currentOptions.map(opt => <li class={this.selection === opt.key ? "active" : ""}>
                        <a onClick={(event) => this.makeChoice(event, this.type, opt)}>
                            {opt.name} { opt.preview ? <span>PREVIEW</span> : ""}
                        </a>
                    </li>)
                }
            </ul>,
            <slot></slot>
        ];
    }

    // The choosable elements of this chooser, if any.
    private get choosables() {
        return this.el.querySelectorAll("pulumi-choosable");
    }

    // Convert inbound options lists into ChooserKeys, so they can be converted into
    // ChooserOptions.
    private parseOptions() {
        this.currentOptions = [];

        if (!this.type) {
            throw new Error("Chooser attribute `type` is required.");
        }

        if (!this.options) {
            throw new Error("Chooser attribute `options` is required.");
        }

        try {
            const keys: string[] = this.options.split(",").map(s => s.trim());
            this.mapOptions(this.type, keys as ChooserKey[]);
        }
        catch (err) {
            console.error(`Error parsing chooser options "${this.options}"`);
            throw(err);
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
            case "input-kind":
                options = this.supportedInputKinds;
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
    private makeChoice(event: Event, type: ChooserType, choice: ChooserOption) {
        this.setChoice(type, choice);

        // Since choosing a tab toggles the visibility of an unknowable number of elements
        // on the page (causing unpredictable reflows), we note the current position of
        // the clicked element relative to the upper edge of the viewport, do the
        // selection, then scroll to the same location once the reflow is complete.
        var el = event.target as Element;
        var distanceFromViewportTop = el.getBoundingClientRect().top;

        window.requestAnimationFrame(function() {
            window.scroll(0, el["offsetTop"] - distanceFromViewportTop);
        });
    }

    private setChoice(type: ChooserType, choice: ChooserOption) {
        const key = choice.key;
        this.selection = key;

        if (this.mode !== "local") {
            switch (type) {
                case "language":
                    this.setLanguage(key as LanguageKey);
                    break;
                case "k8s-language":
                    this.setK8sLanguage(key as K8sLanguageKey);
                    break;
                case "input-kind":
                    this.setInputKind(key as InputKindKey);
                    break;
                case "os":
                    this.setOS(key as OSKey);
                    break;
                case "cloud":
                    this.setCloud(key as CloudKey);
                    break;
            }
        }
    }

    // Apply the currently selected value to all choosables, allowing them to decide
    // whether to show or hide themselves.
    private applyChoice() {
        if (this.selection) {
            this.choosables.forEach(choosable => {
                choosable.setAttribute("selection", this.selection);
            });
        }
    }

    // The list of supported languages.
    private supportedLanguages: SupportedLanguage[] = [
        {
            key: "typescript",
            name: "TypeScript",
            extension: "ts",
            preview: false,
        },
        {
            key: "javascript",
            name: "JavaScript",
            extension: "js",
            preview: false,
        },
        {
            key: "python",
            name: "Python",
            extension: "py",
            preview: false,
        },
        {
            key: "go",
            name: "Go",
            extension: "go",
            preview: false,
        },
        {
            key: "csharp",
            name: "C#",
            extension: "cs",
            preview: false,
        },
        {
            key: "fsharp",
            name: "F#",
            extension: "fs",
            preview: false,
        },
        {
            key: "visualbasic",
            name: "VB",
            extension: "vb",
            preview: false,
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

    // The list of supported input kinds.
    private supportedInputKinds: SupportedInputKind[] = [
        {
            key: "code",
            name: "Code",
            preview: false,
        },
        {
            key: "url",
            name: "URL",
            preview: false,
        },
        {
            key: "upload",
            name: "Upload",
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
        {
            key: "kubernetes",
            name: "Kubernetes",
            preview: false,
        },
    ];
}
