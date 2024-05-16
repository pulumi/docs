import { Component, Element, Event, EventEmitter, h, State } from "@stencil/core";

@Component({
    tag: "pulumi-tabs",
    shadow: true,

    // Tabs have default structural styles, like block layout, horizontally aligned tabs,
    // and pointer cursors.
    styles: `
        :host {
            display: block;
        }
        ul {
            display: flex;
            width: 100%;
            align-items: center;
            margin: 0;
            padding: 0;
            width: auto;
            list-style-type: none;
        }
        li {
            display: flex;
            justify-content: center;
        }
        li a {
            cursor: pointer;
            display: flex;
            justify-content: center;
            flex: 1;
            text-align: center;
            white-space: nowrap;
        }
    `
})
export class Tabs {

    @Element()
    el: HTMLElement;

    @State()
    selectedTab: HTMLElement;

    @Event({ composed: true, bubbles: true })
    tabSelect: EventEmitter<any[]>;

    constructor() {

        // Check for an explicitly defined active tab.
        const activeTab = this.tabs.find(t => t.getAttribute("active"));

        // If an active tab was specified, use that; otherwise, use the first tab in the set.
        if (activeTab) {
            this.select(activeTab);
        } else if (!this.selectedTab && this.tabs.length > 0) {
            this.select(this.tabs[0]);
        }
    }

    // Select the specified tab.
    private select(tab: HTMLElement) {
        if (tab) {
            this.tabs.forEach(t => t.setAttribute("active", (t === tab).toString()))
            this.selectedTab = tab;

            // Emit an event to notify listeners of selection changes.
            this.tabSelect.emit([{ selectedTab: tab }]);
        }
    }

    // The set of pulumi-tab elements belonging to this set.
    private get tabs() {
        return Array.from(this.el.querySelectorAll("pulumi-tab") || []);
    }

    // Return the label for a given tab.
    private labelFor(tab: HTMLElement): string {
        return tab.getAttribute("label") || "";
    }

    // Return the CSS parts to assign to the specified tab.
    private partsFor(tab: HTMLElement): string {
        const parts = ["tab"];

        if (this.selectedTab === tab) {
            parts.push("active-tab");
        }

        return parts.join(" ");
    }

    render() {
        return <div>

            {/* We assemble the clickable elements based on the labels of the pulumi-tab children. */}
            <ul part="tabs" role="tablist">
                {
                    this.tabs.map(tab => {
                        return <li part={ this.partsFor(tab) } role="presentation">
                            <a part="anchor" onClick={ this.select.bind(this, tab) } role="tab" aria-selected={ this.selectedTab === tab }>
                                { this.labelFor(tab) }
                            </a>
                        </li>
                    })
                }
            </ul>

            {/* The tabs themselves. */}
            <slot />
        </div>;
    }
}
