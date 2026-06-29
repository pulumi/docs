import { Component, Element, Host, h, Listen, Prop, State } from "@stencil/core";
import { store, Unsubscribe } from "@stencil/redux";
import { AppState } from "../../store/state";
import { setLanguage, setK8sLanguage, setOS, setCloud, setPersona, setBackEnd, setPythonToolchain } from "../../store/actions/preferences";

export type LanguageKey = "javascript" | "typescript" | "python" | "go" | "csharp" | "fsharp" | "visualbasic" | "java" | "yaml" | "opa";
export type K8sLanguageKey = "typescript" | "yaml" | "typescript-kx";
export type OSKey = "macos" | "linux" | "windows";
export type CloudKey = "aws" | "azure" | "gcp" | "kubernetes" | "digitalocean" | "oci" | "docker";
export type PersonaKey = "developer" | "devops" | "security" | "leader";
export type BackEndKey = "service" | "self-managed";
export type PythonToolchainKey = "pip" | "uv" | "poetry";

export type ChooserMode = "local" | "global";
export type ChooserOptionStyle = "tabbed" | "none";
export type ChooserType = "language" | "k8s-language" | "os" | "cloud" | "persona" | "backend" | "pythontoolchain";
export type ChooserKey = LanguageKey | K8sLanguageKey | OSKey | CloudKey | PersonaKey | BackEndKey | PythonToolchainKey;
export type ChooserOption = SupportedLanguage | SupportedK8sLanguage | SupportedOS | SupportedCloud | SupportedPersona | SupportedBackEnd | SupportedPythonToolchain;

export interface SupportedLanguage {
    key: LanguageKey;
    name: string;
    extension: string;
    logo: string;
    // Optional dark-mode logo variant. Set only for languages whose light logo
    // doesn't read on a dark background (e.g. YAML's black wordmark). When
    // present, the toolbar emits both images and the docs theme's
    // .docs-logo-light/.docs-logo-dark CSS swaps them on dark docs pages.
    logoOnDark?: string;
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

interface SupportedPersona {
    key: PersonaKey;
    name: string;
    preview: boolean;
}

interface SupportedBackEnd {
    key: BackEndKey;
    name: string;
    preview: boolean;
}

interface SupportedPythonToolchain {
    key: PythonToolchainKey;
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
    setOS: typeof setOS;
    setCloud: typeof setCloud;
    setPersona: typeof setPersona;
    setBackEnd: typeof setBackEnd;
    setPythonToolchain: typeof setPythonToolchain;

    componentWillLoad() {
        // By default, choosers act globally and use a tabbed layout.
        this.mode = "global";
        this.optionStyle = "tabbed";

        // Translate the set of options provided into choices.
        this.parseOptions();

        // Map internal methods to actions defined on the store.
        store.mapDispatchToProps(this, {
            setLanguage,
            setK8sLanguage,
            setOS,
            setCloud,
            setPersona,
            setBackEnd,
            setPythonToolchain,
        });

        // Try to subscribe immediately if the store is ready.
        // This avoids waiting for the "rendered" event when possible.
        if (store.getStore()) {
            this.subscribeToStore();
            // Apply the current selection to children immediately so that choosables
            // can read the correct `selection` attribute before they upgrade. Without
            // this, choosables that start in local mode (because the globally-preferred
            // language isn't one of this chooser's options) would render with no
            // selection on their first pass and briefly show empty content.
            this.applyChoice();
        }
    }

    @Listen("rendered", { target: "document" })
    onRendered(_event: CustomEvent) {
        // Subscribe to the store when it's ready (if not already subscribed).
        if (!this.storeUnsubscribe) {
            this.subscribeToStore();
        }
    }

    disconnectedCallback() {
        if (this.storeUnsubscribe) {
            this.storeUnsubscribe();
        }
    }

    componentDidRender() {
        this.applyChoice();
    }

    private subscribeToStore() {
        // Map currently selected values from the store, so we can use them in this component.
        this.storeUnsubscribe = store.mapStateToProps(this, (state: AppState) => {
            const {
                preferences: { language, k8sLanguage, os, cloud, persona, backend, pythontoolchain },
            } = state;

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
                        });

                        // In local mode, there's no need to listen for store updates anymore,
                        // so we unsubscribe.
                        if (this.storeUnsubscribe) {
                            this.storeUnsubscribe();
                        }
                    } else {
                        // This is a global chooser with (presumably) on-page choosables,
                        // so we need to dispatch an event to reset the selected language.
                        this.setChoice(this.type, defaultChoice);
                    }
                }
                return { selection: key };
            };

            switch (this.type) {
                case "language":
                    return preferredOrDefault(language);
                case "k8s-language":
                    return preferredOrDefault(k8sLanguage);
                case "os":
                    return preferredOrDefault(os);
                case "cloud":
                    return preferredOrDefault(cloud);
                case "persona":
                    return preferredOrDefault(persona);
                case "backend":
                    return preferredOrDefault(backend);
                case "pythontoolchain":
                    return preferredOrDefault(pythontoolchain);
                default:
                    return {};
            }
        });
    }

    render() {
        // Render the current set of options, marking the selected one active. For
        // language choosers the button text is the uppercased file extension (e.g. TS,
        // PY); every other type keeps rendering the full name and PREVIEW badge as before.
        const list = (
            <ul>
                {this.currentOptions.map(opt => (
                    <li class={this.selection === opt.key ? "active" : ""}>
                        <a onClick={event => this.makeChoice(event, this.type, opt)}>
                            {this.optionLabel(opt)} {opt.preview ? <span>PREVIEW</span> : ""}
                        </a>
                    </li>
                ))}
            </ul>
        );

        if (this.type === "language") {
            const selected = this.currentOptions.find(o => o.key === this.selection) as SupportedLanguage;
            return (
                <Host selection={this.selection}>
                    <div class="chooser-toolbar">
                        <span class="chooser-toolbar-label">
                            {selected ? this.renderToolbarLogo(selected) : ""}
                            {selected ? selected.name : ""}
                            {selected && selected.preview ? <span class="badge badge-preview">Preview</span> : ""}
                        </span>
                        {list}
                    </div>
                    <slot></slot>
                </Host>
            );
        }

        return (
            <Host selection={this.selection}>
                {list}
                <slot></slot>
            </Host>
        );
    }

    // The language logo in the toolbar. When the language ships a dark-mode
    // variant, emit both images tagged with the docs theme's .docs-logo-light /
    // .docs-logo-dark classes: the dark one is hidden everywhere by default and
    // revealed only on dark-mode docs pages, so the right logo shows in every
    // context (and non-docs pages keep the light one). Languages without a dark
    // variant render a single full-color logo that reads on both backgrounds.
    private renderToolbarLogo(lang: SupportedLanguage) {
        if (lang.logoOnDark) {
            return [
                <img class="chooser-toolbar-logo docs-logo-light" src={lang.logo} alt="" aria-hidden="true" />,
                <img class="chooser-toolbar-logo docs-logo-dark" src={lang.logoOnDark} alt="" aria-hidden="true" />,
            ];
        }
        return <img class="chooser-toolbar-logo" src={lang.logo} alt="" aria-hidden="true" />;
    }

    // The text shown on a chooser tab. For languages we use the uppercased file
    // extension (TS, PY, GO, …) so 7+ options fit on one row; everything else uses the
    // full option name.
    private optionLabel(opt: ChooserOption): string {
        const ext = (opt as SupportedLanguage).extension;
        return ext ? ext.toUpperCase() : opt.name;
    }

    // The choosable elements of this chooser, if any.
    // Only returns choosables that match this chooser's type.
    private get choosables() {
        return this.el.querySelectorAll(`pulumi-choosable[type="${this.type}"]`);
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
        } catch (err) {
            console.error(`Error parsing chooser options "${this.options}"`);
            throw err;
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
            case "persona":
                options = this.supportedPersonas;
                break;
            case "backend":
                options = this.supportedBackEnds;
                break;
            case "pythontoolchain":
                options = this.supportedPythonToolchains;
                break;
        }

        this.currentOptions = options.filter(opt => keys.includes(opt.key));
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

        window.requestAnimationFrame(() => {
            // Get the element's *new* position, post-reflow.
            const distanceFromDocumentTop = this.getDistanceFromDocumentTop(el);
            window.scroll(0, distanceFromDocumentTop - distanceFromViewportTop);
        });
    }

    // Return the distance between the upper edge of an element and the top of the document.
    // https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/offsetTop
    // https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/offsetParent
    private getDistanceFromDocumentTop(el: Element): number {
        let offsetTop = 0;
        while (el) {
            offsetTop += el["offsetTop"];
            el = el["offsetParent"];
        }
        return offsetTop;
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
                case "os":
                    this.setOS(key as OSKey);
                    break;
                case "cloud":
                    this.setCloud(key as CloudKey);
                    break;
                case "persona":
                    this.setPersona(key as PersonaKey);
                    break;
                case "backend":
                    this.setBackEnd(key as BackEndKey);
                    break;
                case "pythontoolchain":
                    this.setPythonToolchain(key as PythonToolchainKey);
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

    // The list of supported backends.
    private supportedBackEnds: SupportedBackEnd[] = [
        {
            key: "service",
            name: "Service",
            preview: false,
        },
        {
            key: "self-managed",
            name: "Self Managed",
            preview: false,
        },
    ];

    // The list of supported personas.
    private supportedPersonas: SupportedPersona[] = [
        {
            key: "developer",
            name: "Developers",
            preview: false,
        },
        {
            key: "devops",
            name: "DevOps & Infra Teams",
            preview: false,
        },
        {
            key: "security",
            name: "Security Engineers",
            preview: false,
        },
        {
            key: "leader",
            name: "Engineering Leaders",
            preview: false,
        },
    ];

    // The list of supported languages.
    private supportedLanguages: SupportedLanguage[] = [
        {
            key: "typescript",
            name: "TypeScript",
            extension: "ts",
            logo: "/logos/tech/typescript.svg",
            preview: false,
        },
        {
            key: "javascript",
            name: "JavaScript",
            extension: "js",
            logo: "/logos/tech/javascript.svg",
            preview: false,
        },
        {
            key: "python",
            name: "Python",
            extension: "py",
            logo: "/logos/tech/python.svg",
            preview: false,
        },
        {
            key: "go",
            name: "Go",
            extension: "go",
            logo: "/logos/tech/go.svg",
            preview: false,
        },
        {
            key: "csharp",
            name: "C#",
            extension: "cs",
            logo: "/logos/tech/csharp.svg",
            preview: false,
        },
        {
            key: "fsharp",
            name: "F#",
            extension: "fs",
            logo: "/logos/tech/fsharp.svg",
            preview: false,
        },
        {
            key: "visualbasic",
            name: "VB",
            extension: "vb",
            logo: "/logos/tech/visualbasic.svg",
            preview: false,
        },
        {
            key: "java",
            name: "Java",
            extension: "java",
            // Mark-only Java cup (no "Java" wordmark), already used elsewhere in docs.
            logo: "/images/docs/icons/languages/java-color-32-32.svg",
            preview: false,
        },
        {
            key: "yaml",
            name: "YAML",
            extension: "yaml",
            // The matched light/dark pair already used elsewhere in docs (the
            // div.yaml-color-32-32 icon); the -on-dark recolor keeps the black
            // wordmark legible on dark backgrounds.
            logo: "/images/docs/icons/languages/yaml-color-32-32.svg",
            logoOnDark: "/images/docs/icons/languages/yaml-color-32-32-on-dark.svg",
            preview: false,
        },
        {
            key: "opa",
            name: "OPA",
            extension: "rego",
            logo: "/logos/tech/logo-opa.png",
            preview: false,
        },
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
            name: "Google Cloud",
            preview: false,
        },
        {
            key: "kubernetes",
            name: "Kubernetes",
            preview: false,
        },
        {
            key: "digitalocean",
            name: "DigitalOcean",
            preview: false,
        },
        {
            key: "oci",
            name: "Oracle Cloud",
            preview: false,
        },
        {
            key: "docker",
            name: "Docker",
            preview: false,
        },
    ];

    // The list of supported Python toolchains.
    private supportedPythonToolchains: SupportedPythonToolchain[] = [
        {
            key: "pip",
            name: "pip",
            preview: false,
        },
        {
            key: "uv",
            name: "uv",
            preview: false,
        },
        {
            key: "poetry",
            name: "poetry",
            preview: false,
        },
    ];
}
