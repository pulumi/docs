import { Component, Prop, State, h, Host, Element } from "@stencil/core";
import * as clipboard from "clipboard-polyfill";
import TurndownService from "turndown";
import { gfm } from "turndown-plugin-gfm";

@Component({
    tag: "pulumi-llm-menu",
    shadow: false,
})
export class LlmMenu {
    @Element() el: HTMLElement;

    @Prop() pageUrl: string;
    @Prop() pageTitle: string;

    @State() isOpen: boolean = false;
    @State() copied: string = "";

    private turndown = new TurndownService({
        headingStyle: "atx",
        codeBlockStyle: "fenced",
        bulletListMarker: "-",
        emDelimiter: "*",
    });

    componentDidLoad() {
        document.addEventListener("click", this.handleClickOutside);

        // Add GitHub Flavored Markdown support (tables, strikethrough, etc.)
        this.turndown.use(gfm);

        // Capture the base URL for converting relative URLs
        const baseUrl = window.location.origin;

        // Configure TurndownService to remove unwanted elements
        this.turndown.remove([
            "button",
            "script",
            "style",
            "pulumi-tooltip",
            ".copy-button-container",
            ".example-program-footer",
            "pulumi-chooser > ul"  // Remove chooser navigation tabs (but keep choosable content)
        ]);

        // Custom rule for code blocks to avoid "Copy" button artifacts
        this.turndown.addRule("codeBlocks", {
            filter: function(node) {
                return node.nodeName === "DIV" &&
                       node.classList.contains("highlight");
            },
            replacement: function(content, node) {
                const codeElement = (node as HTMLElement).querySelector("code");
                if (!codeElement) return content;

                const language = Array.from(codeElement.classList)
                    .find(cls => cls.startsWith("language-"))
                    ?.replace("language-", "") || "";

                const code = (codeElement.textContent || "").trim();
                return `\n\`\`\`${language}\n${code}\n\`\`\`\n`;
            }
        });

        // Custom rule for mermaid diagrams
        this.turndown.addRule("mermaidDiagrams", {
            filter: function(node) {
                return node.nodeName === "PRE" &&
                       node.classList.contains("mermaid");
            },
            replacement: function(_content, node) {
                // Use preserved source if available, otherwise fall back to textContent
                const element = node as HTMLElement;
                const code = element.getAttribute('data-mermaid-source') || element.textContent || "";
                return `\n\`\`\`mermaid\n${code.trim()}\n\`\`\`\n`;
            }
        });

        // Custom rule for GoAT ASCII diagrams (rendered server-side, source not available)
        this.turndown.addRule("goatDiagrams", {
            filter: function(node) {
                return node.nodeName === "DIV" &&
                       node.classList.contains("goat");
            },
            replacement: function() {
                return `\n\n*[ASCII Diagram - rendered as SVG]*\n\n`;
            }
        });

        // Custom rule for links to convert relative URLs to absolute
        this.turndown.addRule("absoluteLinks", {
            filter: "a",
            replacement: function(content, node) {
                const href = (node as HTMLElement).getAttribute("href");
                if (!href) return `[${content}]()`;

                // Skip anchor links, mailto, and external links
                if (href.startsWith("#") || href.startsWith("mailto:") || href.startsWith("http")) {
                    return `[${content}](${href})`;
                }

                // Convert relative URL to absolute
                const absoluteUrl = baseUrl + (href.startsWith("/") ? href : "/" + href);
                return `[${content}](${absoluteUrl})`;
            }
        });

        // Custom rule for images to convert relative URLs to absolute
        this.turndown.addRule("absoluteImages", {
            filter: "img",
            replacement: function(_content, node) {
                const src = (node as HTMLElement).getAttribute("src");
                const alt = (node as HTMLElement).getAttribute("alt") || "";
                if (!src) return "";

                // Skip external images
                if (src.startsWith("http")) {
                    return `![${alt}](${src})`;
                }

                // Convert relative URL to absolute
                const absoluteUrl = baseUrl + (src.startsWith("/") ? src : "/" + src);
                return `![${alt}](${absoluteUrl})`;
            }
        });

        // Custom rule for choosable sections to add labels
        this.turndown.addRule("choosable", {
            filter: function(node) {
                return node.nodeName === "PULUMI-CHOOSABLE";
            },
            replacement: function(content, node) {
                const type = (node as HTMLElement).getAttribute("type") || "";
                const values = (node as HTMLElement).getAttribute("values") ||
                              (node as HTMLElement).getAttribute("value") || "";

                if (!content.trim()) return "";

                // Capitalize first letter of type for display
                const displayType = type.charAt(0).toUpperCase() + type.slice(1);

                // Check if this choosable is nested (parent is also a choosable)
                const parent = (node as HTMLElement).parentElement;
                const isNested = parent && parent.closest("pulumi-choosable");

                // Use different formatting for nested vs top-level
                // Trim content to remove leading/trailing whitespace
                const trimmedContent = content.trim();

                if (isNested) {
                    return `\n*${displayType}: ${values}*\n\n${trimmedContent}`;
                } else {
                    return `\n**${displayType}: ${values}**\n\n${trimmedContent}`;
                }
            }
        });

        // Custom rule for chooser wrapper - just pass through content
        this.turndown.addRule("chooser", {
            filter: "pulumi-chooser",
            replacement: function(content) {
                return content;
            }
        });

        // Custom rule for callouts/notes to make them stand out
        this.turndown.addRule("notes", {
            filter: function(node) {
                return node.nodeName === "DIV" &&
                       node.classList.contains("note");
            },
            replacement: function(content, node) {
                // Extract the note type from the class (e.g., "note-info", "note-warning", "note-tip")
                const classList = Array.from((node as HTMLElement).classList);
                const noteClass = classList.find(cls => cls.startsWith("note-"));
                const noteType = noteClass ? noteClass.replace("note-", "") : "info";

                // Get just the content div, not the icon
                const contentDiv = (node as HTMLElement).querySelector(".content");
                const noteContent = contentDiv ? contentDiv.innerHTML : content;

                // Choose emoji based on type
                let emoji = "ℹ️";
                let label = "Info";

                if (noteType === "warning") {
                    emoji = "⚠️";
                    label = "Warning";
                } else if (noteType === "tip") {
                    emoji = "💡";
                    label = "Tip";
                }

                // Convert content to markdown
                const markdownContent = new TurndownService({
                    headingStyle: "atx",
                    codeBlockStyle: "fenced",
                    bulletListMarker: "-",
                }).turndown(noteContent);

                // Format as blockquote with emoji prefix
                const lines = markdownContent.split("\n");
                const quotedLines = lines.map((line, index) =>
                    index === 0 ? `> ${emoji} **${label}:** ${line}` : `> ${line}`
                ).join("\n");

                return `\n${quotedLines}\n`;
            }
        });
    }

    disconnectedCallback() {
        document.removeEventListener("click", this.handleClickOutside);
    }

    private handleClickOutside = (event: MouseEvent) => {
        if (this.isOpen && !this.el.contains(event.target as Node)) {
            this.isOpen = false;
        }
    };

    private getMarkdown(): string {
        const content = document.querySelector(".docs-content");
        if (!content) return "";

        // Clone the content to avoid modifying the page
        const clone = content.cloneNode(true) as HTMLElement;

        // Remove unwanted elements before conversion
        const selectorsToRemove = [
            "button",
            ".copy-button",
            ".edit-link",
            "pulumi-tooltip",
            ".llm-menu-container",
            ".page-edit-links",
            "script",
            "style"
        ];

        selectorsToRemove.forEach(selector => {
            clone.querySelectorAll(selector).forEach(el => el.remove());
        });

        // Convert to markdown
        let md = this.turndown.turndown(clone.innerHTML);

        // Clean up the markdown
        md = md
            .replace(/\n{3,}/g, "\n\n") // Remove excessive newlines (max 1 blank line)
            .replace(/^\s+$/gm, "") // Remove whitespace-only lines
            .replace(/\[.*?\]\(\)/g, "") // Remove all empty links [text]() anywhere in content
            .replace(/^\s*(-\s*)+$/gm, "") // Remove lines with only dashes and whitespace (handles multiple dashes)
            .replace(/\n{3,}/g, "\n\n") // Collapse any remaining excessive newlines
            .trim();

        // Construct proper source URL using current window location
        // Extract just the pathname from pageUrl (in case it's a full URL or protocol-relative URL)
        let pathname = this.pageUrl;

        // Handle protocol-relative URLs (//domain/path)
        if (pathname.startsWith('//')) {
            pathname = pathname.substring(pathname.indexOf('/', 2));
        } else {
            // Try to parse as full URL to extract pathname
            try {
                const url = new URL(this.pageUrl, window.location.origin);
                pathname = url.pathname;
            } catch {
                // pageUrl is already a pathname, use as-is
            }
        }

        const sourceUrl = window.location.origin + pathname;

        return `# ${this.pageTitle}\n\n[View this page on Pulumi Docs](${sourceUrl})\n\n${md}`;
    }

    private async copyPage() {
        await clipboard.writeText(this.getMarkdown());
        this.showCopied("page");
        this.trackEvent("copy-page");
    }

    private viewMarkdown() {
        try {
            // Get the markdown content (same as copy)
            const markdown = this.getMarkdown();

            // Create a Blob with the markdown content (UTF-8 charset for emoji support)
            const blob = new Blob([markdown], { type: 'text/plain; charset=utf-8' });
            const url = URL.createObjectURL(blob);

            // Open in new tab
            const newWindow = window.open(url, '_blank');

            // Clean up the blob URL after a short delay
            // (window needs time to load the content)
            if (newWindow) {
                setTimeout(() => URL.revokeObjectURL(url), 1000);
            }

            this.trackEvent("view-markdown");
        } catch (error) {
            console.error('Failed to view markdown:', error);
        }
    }

    private showCopied(type: string) {
        this.copied = type;
        setTimeout(() => this.copied = "", 2000);
    }

    private trackEvent(action: string) {
        const analytics = (window as any).analytics;
        if (analytics?.track) {
            analytics.track("llm-helper", { action, page: this.pageUrl });
        }
    }

    private openInChatGPT() {
        const prompt = `Read from https://pulumi.com${new URL(this.pageUrl).pathname} so I can ask questions about it.`;
        window.open(`https://chat.openai.com/?q=${encodeURIComponent(prompt)}`, "_blank");
        this.trackEvent("open-chatgpt");
    }

    private openInClaude() {
        const prompt = `Read from https://pulumi.com${new URL(this.pageUrl).pathname} so I can ask questions about it.`;
        window.open(`https://claude.ai/new?q=${encodeURIComponent(prompt)}`, "_blank");
        this.trackEvent("open-claude");
    }

    private async copyUrl() {
        await clipboard.writeText(window.location.href);
        this.showCopied("url");
        this.trackEvent("copy-url");
    }

    render() {
        const linkIcon = (
            <svg class="llm-menu-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M9.172 14.828L14.828 9.172M7.05 11.293L4.222 14.121C2.562 15.781 2.562 18.439 4.222 20.099C5.882 21.759 8.54 21.759 10.2 20.099L13.029 17.271M10.971 6.729L13.8 3.901C15.46 2.241 18.118 2.241 19.778 3.901C21.438 5.561 21.438 8.219 19.778 9.879L16.95 12.707" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
        );

        const chatGptLogo = (
            <svg class="llm-menu-icon" viewBox="0 0 320 320" xmlns="http://www.w3.org/2000/svg">
                <path fill="currentColor" d="m297.06 130.97c7.26-21.79 4.76-45.66-6.85-65.48-17.46-30.4-52.56-46.04-86.84-38.68-15.25-17.18-37.16-26.95-60.13-26.81-35.04-.08-66.13 22.48-76.91 55.82-22.51 4.61-41.94 18.7-53.31 38.67-17.59 30.32-13.58 68.54 9.92 94.54-7.26 21.79-4.76 45.66 6.85 65.48 17.46 30.4 52.56 46.04 86.84 38.68 15.24 17.18 37.16 26.95 60.13 26.8 35.06.09 66.16-22.49 76.94-55.86 22.51-4.61 41.94-18.7 53.31-38.67 17.57-30.32 13.55-68.51-9.94-94.51zm-120.28 168.11c-14.03.02-27.62-4.89-38.39-13.88.49-.26 1.34-.73 1.89-1.07l63.72-36.8c3.26-1.85 5.26-5.32 5.24-9.07v-89.83l26.93 15.55c.29.14.48.42.52.74v74.39c-.04 33.08-26.83 59.9-59.91 59.97zm-128.84-55.03c-7.03-12.14-9.56-26.37-7.15-40.18.47.28 1.3.79 1.89 1.13l63.72 36.8c3.23 1.89 7.23 1.89 10.47 0l77.79-44.92v31.1c.02.32-.13.63-.38.83l-64.41 37.19c-28.69 16.52-65.33 6.7-81.92-21.95zm-16.77-139.09c7-12.16 18.05-21.46 31.21-26.29 0 .55-.03 1.52-.03 2.2v73.61c-.02 3.74 1.98 7.21 5.23 9.06l77.79 44.91-26.93 15.55c-.27.18-.61.21-.91.08l-64.42-37.22c-28.63-16.58-38.45-53.21-21.95-81.89zm221.26 51.49-77.79-44.92 26.93-15.54c.27-.18.61-.21.91-.08l64.42 37.19c28.68 16.57 38.51 53.26 21.94 81.94-7.01 12.14-18.05 21.44-31.2 26.28v-75.81c.03-3.74-1.96-7.2-5.2-9.06zm26.8-40.34c-.47-.29-1.3-.79-1.89-1.13l-63.72-36.8c-3.23-1.89-7.23-1.89-10.47 0l-77.79 44.92v-31.1c-.02-.32.13-.63.38-.83l64.41-37.16c28.69-16.55 65.37-6.7 81.91 22 6.99 12.12 9.52 26.31 7.15 40.1zm-168.51 55.43-26.94-15.55c-.29-.14-.48-.42-.52-.74v-74.39c.02-33.12 26.89-59.96 60.01-59.94 14.01 0 27.57 4.92 38.34 13.88-.49.26-1.33.73-1.89 1.07l-63.72 36.8c-3.26 1.85-5.26 5.31-5.24 9.06l-.04 89.79zm14.63-31.54 34.65-20.01 34.65 20v40.01l-34.65 20-34.65-20z"/>
            </svg>
        );

        const claudeLogo = (
            <svg class="llm-menu-icon" viewBox="0 0 1200 1200" xmlns="http://www.w3.org/2000/svg">
                <path fill="currentColor" d="M 233.959793 800.214905 L 468.644287 668.536987 L 472.590637 657.100647 L 468.644287 650.738403 L 457.208069 650.738403 L 417.986633 648.322144 L 283.892639 644.69812 L 167.597321 639.865845 L 54.926208 633.825623 L 26.577238 627.785339 L 3.3e-05 592.751709 L 2.73832 575.27533 L 26.577238 559.248352 L 60.724873 562.228149 L 136.187973 567.382629 L 249.422867 575.194763 L 331.570496 580.026978 L 453.261841 592.671082 L 472.590637 592.671082 L 475.328857 584.859009 L 468.724915 580.026978 L 463.570557 575.194763 L 346.389313 495.785217 L 219.543671 411.865906 L 153.100723 363.543762 L 117.181267 339.060425 L 99.060455 316.107361 L 91.248367 266.01355 L 123.865784 230.093994 L 167.677887 233.073853 L 178.872513 236.053772 L 223.248367 270.201477 L 318.040283 343.570496 L 441.825592 434.738342 L 459.946411 449.798706 L 467.194672 444.64447 L 468.080597 441.020203 L 459.946411 427.409485 L 392.617493 305.718323 L 320.778564 181.932983 L 288.80542 130.630859 L 280.348999 99.865845 C 277.369171 87.221436 275.194641 76.590698 275.194641 63.624268 L 312.322174 13.20813 L 332.8591 6.604126 L 382.389313 13.20813 L 403.248352 31.328979 L 434.013519 101.71814 L 483.865753 212.537048 L 561.181274 363.221497 L 583.812134 407.919434 L 595.892639 449.315491 L 600.40271 461.959839 L 608.214783 461.959839 L 608.214783 454.711609 L 614.577271 369.825623 L 626.335632 265.61084 L 637.771851 131.516846 L 641.718201 93.745117 L 660.402832 48.483276 L 697.530334 24.000122 L 726.52356 37.852417 L 750.362549 72 L 747.060486 94.067139 L 732.886047 186.201416 L 705.100708 330.52356 L 686.979919 427.167847 L 697.530334 427.167847 L 709.61084 415.087341 L 758.496704 350.174561 L 840.644348 247.490051 L 876.885925 206.738342 L 919.167847 161.71814 L 946.308838 140.29541 L 997.61084 140.29541 L 1035.38269 196.429626 L 1018.469849 254.416199 L 965.637634 321.422852 L 921.825562 378.201538 L 859.006714 462.765259 L 819.785278 530.41626 L 823.409424 535.812073 L 832.75177 534.92627 L 974.657776 504.724915 L 1051.328979 490.872559 L 1142.818848 475.167786 L 1184.214844 494.496582 L 1188.724854 514.147644 L 1172.456421 554.335693 L 1074.604126 578.496765 L 959.838989 601.449829 L 788.939636 641.879272 L 786.845764 643.409485 L 789.261841 646.389343 L 866.255127 653.637634 L 899.194702 655.409424 L 979.812134 655.409424 L 1129.932861 666.604187 L 1169.154419 692.537109 L 1192.671265 724.268677 L 1188.724854 748.429688 L 1128.322144 779.194641 L 1046.818848 759.865845 L 856.590759 714.604126 L 791.355774 698.335754 L 782.335693 698.335754 L 782.335693 703.731567 L 836.69812 756.885986 L 936.322205 846.845581 L 1061.073975 962.81897 L 1067.436279 991.490112 L 1051.409424 1014.120911 L 1034.496704 1011.704712 L 924.885986 929.234924 L 882.604126 892.107544 L 786.845764 811.48999 L 780.483276 811.48999 L 780.483276 819.946289 L 802.550415 852.241699 L 919.087341 1027.409424 L 925.127625 1081.127686 L 916.671204 1098.604126 L 886.469849 1109.154419 L 853.288696 1103.114136 L 785.073914 1007.355835 L 714.684631 899.516785 L 657.906067 802.872498 L 650.979858 806.81897 L 617.476624 1167.704834 L 601.771851 1186.147705 L 565.530212 1200 L 535.328857 1177.046997 L 519.302124 1139.919556 L 535.328857 1066.550537 L 554.657776 970.792053 L 570.362488 894.68457 L 584.536926 800.134277 L 592.993347 768.724976 L 592.429626 766.630859 L 585.503479 767.516968 L 514.22821 865.369263 L 405.825531 1011.865906 L 320.053711 1103.677979 L 299.516815 1111.812256 L 263.919525 1093.369263 L 267.221497 1060.429688 L 287.114136 1031.114136 L 405.825531 880.107361 L 477.422913 786.52356 L 523.651062 732.483276 L 523.328918 724.671265 L 520.590698 724.671265 L 205.288605 929.395935 L 149.154434 936.644409 L 124.993355 914.01355 L 127.973183 876.885986 L 139.409409 864.80542 L 234.201385 799.570435 L 233.879227 799.8927 Z"/>
            </svg>
        );

        return (
            <Host>
                <div class="llm-menu-container">
                    <button
                        class="llm-menu-trigger text-gray-600 hover:text-gray-700 text-xs"
                        onClick={() => this.isOpen = !this.isOpen}
                    >
                        <i class="fas fa-copy"></i>
                        Copy Page
                        <i class={`fas fa-chevron-${this.isOpen ? 'up' : 'down'}`}></i>
                    </button>

                    {this.isOpen && (
                        <div class="llm-menu-dropdown">
                            <div>
                                <button class="llm-menu-item" onClick={() => this.copyUrl()}>
                                    {linkIcon}
                                    <div class="llm-menu-text">
                                        <div class="llm-menu-title">{this.copied === "url" ? "Copied!" : "Copy URL"}</div>
                                        <div class="llm-menu-subtitle">Copy page link to share</div>
                                    </div>
                                </button>
                                <button class="llm-menu-item" onClick={() => this.copyPage()}>
                                    <i class="fas fa-copy llm-menu-icon"></i>
                                    <div class="llm-menu-text">
                                        <div class="llm-menu-title">{this.copied === "page" ? "Copied!" : "Copy as Markdown"}</div>
                                        <div class="llm-menu-subtitle">Copy page for LLMs</div>
                                    </div>
                                </button>
                                <button class="llm-menu-item" onClick={() => this.viewMarkdown()}>
                                    <i class="fab fa-markdown llm-menu-icon"></i>
                                    <div class="llm-menu-text">
                                        <div class="llm-menu-title">View as Markdown</div>
                                        <div class="llm-menu-subtitle">Open Markdown in new tab</div>
                                    </div>
                                    <i class="fas fa-external-link-alt llm-menu-external"></i>
                                </button>
                                <hr />
                                <button class="llm-menu-item" onClick={() => this.openInChatGPT()}>
                                    {chatGptLogo}
                                    <div class="llm-menu-text">
                                        <div class="llm-menu-title">Open in ChatGPT</div>
                                        <div class="llm-menu-subtitle">Ask ChatGPT about this page</div>
                                    </div>
                                    <i class="fas fa-external-link-alt llm-menu-external"></i>
                                </button>
                                <button class="llm-menu-item" onClick={() => this.openInClaude()}>
                                    {claudeLogo}
                                    <div class="llm-menu-text">
                                        <div class="llm-menu-title">Open in Claude</div>
                                        <div class="llm-menu-subtitle">Ask Claude about this page</div>
                                    </div>
                                    <i class="fas fa-external-link-alt llm-menu-external"></i>
                                </button>
                            </div>
                        </div>
                    )}
                </div>
            </Host>
        );
    }
}
