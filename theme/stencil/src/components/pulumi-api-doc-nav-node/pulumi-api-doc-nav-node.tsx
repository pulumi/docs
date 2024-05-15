import { Component, h, Prop } from "@stencil/core";
import { APINavNode, APINavNodeType } from "../pulumi-api-doc-filterable-nav/pulumi-api-doc-filterable-nav";

@Component({
    tag: "pulumi-api-doc-nav-node",
    shadow: false,
})
export class PulumiApiDocNavNode {
    @Prop()
    node: APINavNode;

    @Prop()
    href: string;

    @Prop()
    depth: number = 0;

    @Prop({ mutable: true })
    isExpanded: boolean;

    componentWillLoad() {
        this.isExpanded = !!this.node.isExpanded || this.isNodeInPathForCurrentlyVisiblePage(this.node.name);
    }

    onExpansionChange(href: string, isLink = false) {
        if (isLink) {
            window.location.href = href;
        }

        this.isExpanded = !this.isExpanded;
    }

    // For whatever reason, the <a> href doesn't work
    // in Safari, so we handle the routing explicitly.
    handleLinkClick(e: MouseEvent, href: string) {
        e.stopPropagation();
        window.location.href = href;
    }

    componentShouldUpdate(newVal, oldVal, propName) {
        // When the node is expanded, we render child nodes.
        // When we collapse that same node, we want to avoid throwing out
        // the rendered nodes. (Helps with toggling nodes open/close repeatedly)
        if (propName === "isExpanded") {
            if (oldVal === true && newVal === false) {
                return false;
            }

            return true;
        }
    }

    getIcon(nodeType: APINavNodeType) {
        return (
            <div class="symbol-container">
                <slot name="before-content">
                    <span class={`symbol ${nodeType}`}></span>
                </slot>
            </div>
        );
    }

    // If a node is in the path for the page a user is currently on, it should
    // be expanded, even if the expansion icon has not been clicked.
    isNodeInPathForCurrentlyVisiblePage(nodeName) {
        const currentPath = window.location.pathname;
        return currentPath.includes(`/${nodeName}/`);
    }

    // If a node is an exact match for the page a user is currently on
    // (not just in the path), it should be selected,
    // even if it has not been clicked by the user.
    shouldNodeBeSelected(nodeHref) {
        // To compare the current path to the href, we strip the starting and ending slashes.
        const formattedCurrentPath = window.location.pathname
            .split("/")
            .filter(item => item !== "")
            .join("/");
        const formattedNodeHref = nodeHref
            .split("/")
            .filter(item => item !== "")
            .join("/");

        return formattedCurrentPath === formattedNodeHref;
    }

    getChildNodes(nodes: APINavNode[], isRootExpanded: boolean, depth: number = 1, linkBase = this.href) {
        const dummyNode = <pulumi-tree-item slot="item" selected={false} expanded={false} title="dummy"></pulumi-tree-item>;
        // By default, we render all of the root nodes.  Whether we use a "dummy" node or not
        // depends on if the root is expanded.  If it is expanded, we need to show its children.
        // If not, we don't need to render those children until the root is expanded.
        if (!isRootExpanded && nodes?.length) {
            return dummyNode;
        }

        return nodes?.map(node => {
            // Some links come back with a trailing slash, while others do not. We want all
            // links to end in a trailing slash for SEO reasons, so we check if it already exists.
            // If so, we leave it alone, otherwise we add it.
            const nodeLinkLastChar = node.link.charAt(node.link.length - 1);
            const nodeLink = nodeLinkLastChar === "/" ? node.link : `${node.link}/`;
            const nodeHref = `${linkBase}${nodeLink}`;
            const hasChildren = node.children ? node.children.length === 0 : false;

            return (
                            <details
                    open={this.isExpanded}
                    data-expandable={
                        node.children && node.children.length > 0
                            ? "true"
                            : "false"
                    }
                    
                    class="nav-tree-item nested"
                                    id={node.name}
                title={node.name}
                onClick={() => this.onExpansionChange(nodeHref, !hasChildren)}
                >
                    <summary class={`content-container ${hasChildren ? "" : "is-link"}`} data-selected={this.shouldNodeBeSelected(nodeHref) ? "true" : "false"}>
                     <a class={`depth-${depth}`} href={nodeHref} onClick={(e) => this.handleLinkClick(e, nodeHref)}>
                         {this.getIcon(node.type)}
                         <span class="link-container">{node.name}</span>
                     </a>
                    </summary>
                    {this.getChildNodes(node.children, this.isExpanded, depth + 1, nodeHref)}
                </details>
            );
        });
    }

    render() {
        return (
            <details
                    open={this.isExpanded}
                    data-expandable={
                        this.node.children && this.node.children.length > 0
                            ? "true"
                            : "false"
                    }
                    class="nav-tree-item nested"
                                    id={this.node.name}
                                    
                title={this.node.name}
                onClick={() => this.onExpansionChange(this.href, this.node.children.length === 0)}
                >
                    <summary class="content-container" data-selected={this.shouldNodeBeSelected(this.href) ? "true" : "false"}>
                     <a class={`depth-${this.depth}`} href={this.href} onClick={(e) => this.handleLinkClick(e, this.href)}>
                         {this.getIcon(this.node.type)}
                         <span class="link-container">{this.node.name}</span>
                     </a>
                    </summary>
                    {this.getChildNodes(this.node.children, this.isExpanded)}
                </details>
        );
    }
}
