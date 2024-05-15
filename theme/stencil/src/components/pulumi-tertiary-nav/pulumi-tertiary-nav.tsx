import { Component, Host, h, Prop } from "@stencil/core";

export interface TertiaryNavItem {
    // The anchor of the content that the nav item shows.
    anchor: string;
    // The text that should show for the nav item.
    label: string;
}

@Component({
    tag: "pulumi-tertiary-nav",
    styleUrl: "pulumi-tertiary-nav.css",
    shadow: false,
})
export class PulumiTertiaryNav {
    // TertiaryNavItem[], passed into the component as stringified JSON.
    @Prop({ mutable: true })
    items: string;

    @Prop({ mutable: true })
    tabContent: string[];

    // The currently selected tab.
    @Prop({ mutable: true })
    selection: any;

    parsedItems: TertiaryNavItem[];

    componentWillLoad() {
        this.parsedItems = JSON.parse(this.items);

        // Collection of anchor tags
        this.tabContent = this.parsedItems.map((item) => item.anchor);

        // The first tab is selected on initial load.
        this.selectTab(this.parsedItems[0]);
    }

    private selectTab(item: TertiaryNavItem) {
        this.selection = item.anchor;

        document.getElementById(`${item.anchor}`).classList.remove("hidden");

        const unselectedTabs = this.tabContent.filter((value) => value !== item.anchor);

        unselectedTabs.forEach((tab) => {
            document.getElementById(`${tab}`).classList.add("hidden");
        });
    }

    render() {
        return (
            <Host>
                <ul>
                    {this.parsedItems.map((item: TertiaryNavItem) => (
                        <li class={this.selection === item.anchor ? "active" : ""}>
                            <a onClick={() => this.selectTab(item)}>{item.label}</a>
                        </li>
                    ))}
                </ul>
            </Host>
        );
    }
}
