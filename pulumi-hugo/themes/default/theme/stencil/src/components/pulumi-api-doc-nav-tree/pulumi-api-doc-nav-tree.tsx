import { Component, h, Prop } from "@stencil/core";
import { APINavNode } from "../pulumi-api-doc-filterable-nav/pulumi-api-doc-filterable-nav";

@Component({
    tag: "pulumi-api-doc-nav-tree",
    styleUrl: "pulumi-api-doc-nav-tree.scss",
    shadow: false,
})
export class PulumiApiDocNavTree {
    @Prop()
    nodes: APINavNode[];

    @Prop()
    baseDirectory: string;

    getNodes(nodes: APINavNode[] = this.nodes) {
        return nodes?.map(node => {
            // Some links come back with a trailing slash, while others do not. We want all
            // links to end in a trailing slash for SEO reasons, so we check if it already exists.
            // If so, we leave it alone, otherwise we add it.
            const nodeLinkLastChar = node.link.charAt(node.link.length - 1);
            const nodeLink = nodeLinkLastChar === "/" ? node.link : `${node.link}/`
            const nodeHref = `${this.baseDirectory}${nodeLink}`;

            return <pulumi-api-doc-nav-node node={node} isExpanded={node.isExpanded} href={nodeHref}></pulumi-api-doc-nav-node>;
        });
    }

    render() {
        return <pulumi-tree-view>{this.getNodes()}</pulumi-tree-view>;
    }
}
