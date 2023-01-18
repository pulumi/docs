import { Component, h, Prop, State } from "@stencil/core";
import { debounce } from "lodash";
export interface APINavNode {
    // The below properties come from the JSON data.
    name: string;
    type: APINavNodeType;
    // Relative path to the relevant page.
    link: string;
    children?: APINavNode[];
    // The below properties are added during the filtering search process
    // to allow for accurate rendering of the rebuilt tree after search.
    isExpanded?: boolean;
    parentName?: string;
    rootName: string;
}

export type APINavNodeType = "module" | "function" | "resource";

@Component({
    tag: "pulumi-api-doc-filterable-nav",
    styleUrl: "pulumi-api-doc-filterable-nav.scss",
    shadow: false,
})
export class PulumiApiDocFilterableNav {
    constructor() {
        // We debounce the filter tree call so that we are not performing unnecessary work while
        // a user is in the middle of typing their filter criteria.  Eg, if a user is typing
        // "cats", debouncing helps keep us from invoking the tree filtering function
        // with "c", then with "ca", then "cat", then "cats," and instead lets us wait until enough
        // time has passed that a user is likely done typing, and we only invoke with "cats."
        this.debouncedFilterTree = debounce(this.debouncedFilterTree, 300);
    }

    componentWillLoad() {
        this.loadNavigationData().then(() => {});
    }

    async loadNavigationData() {
        this.isLoading = true;

        try {
            const response = await fetch(`/registry/packages/navs/${this.packageName}.json`);
            const data = await response.json();
            this.parsedNodes = data;

            // Before the user interacts with the filter, the nodes to render should be the full nav tree.
            this.currentlyRenderedNodes = this.parsedNodes;
        } catch (error) {
            return;
        }

        this.isLoading = false;
    }

    @Prop()
    baseDirectory: string;

    @Prop()
    packageName: string;

    @State()
    isLoading: boolean;

    @State()
    parsedNodes: APINavNode[];

    @State()
    currentlyRenderedNodes: APINavNode[];

    @State()
    filterContent: string = "";

    filterTreeToMatchingContent(nodesToRender: APINavNode[], nodesToSearch: APINavNode[], rootNode?: APINavNode, directParentNode?: APINavNode) {
        // call recursive helper method, only setting this.currentlyRenderedNodes once at the end to trigger re-painting the DOM.
        const resultNodes = this.filterTreeToMatchingRecursive(
            nodesToRender,
            nodesToSearch,
            rootNode,
            directParentNode
        );
        this.currentlyRenderedNodes = resultNodes;
    }

    // By default, this component renders the full navigation tree, which includes all of the nodes represented in the
    // `nodes` prop.  However, when a user interacts with the text input that is a part of this component, the expectation
    // is that the tree will update to only render nodes that match the text input (and their parents/root nodes, where applicable).
    // This function filters the full tree to find the matches to render, and then reconstructs the tree.
    filterTreeToMatchingRecursive(
        nodesToRender: APINavNode[],
        nodesToSearch: APINavNode[],
        rootNode?: APINavNode,
        directParentNode?: APINavNode,
        nodeCache: { [key: string]: boolean } = {},
        nodePath: string[] = [""],
    ): APINavNode[] {
        nodesToSearch.map(node => {
            const nodeName = nodePath.join("") + node.name;
            const parentName = nodePath.join("");
            const rootName = rootNode ? rootNode.name : "";

            // Check if the nodes we're currently working with are already represented in the array of nodes to render.
            const isNodeDuplicate = !!nodeCache[nodeName];
            const isRootDuplicate = rootNode ? !!nodeCache[rootName] : false;
            const isParentDuplicate = directParentNode ? !!nodeCache[parentName] : false;

            // If the node's already in our flat array, it will be rendered, and no more logic needs to be executed.
            if (isNodeDuplicate) {
                return;
            }

            // Check if the node is a match to the filter content.  If it is a match,
            // we need to add it to our array to be rendered, and perform some additional checks.
            if (node.name.toLowerCase().includes(this.filterContent)) {
                // If the node is a child, we need to ensure the full tree path to get to the child is also rendered.
                // To accomplish that, we check that the current node's root node is not already in our array to be rendered, and then add
                // it with an empty list of children.  The empty list of children ensures that the only children rendered will
                // be matches to the filter content.
                if (!isRootDuplicate && rootNode) {
                    const treeNode = { ...rootNode, children: [], isExpanded: true, rootName };
                    nodesToRender.push(treeNode);
                    nodeCache[rootName] = true;
                }

                // We do the same as above, but for the current node's direct parent.  The only difference is that
                // we know the direct parent's parent is the root node, so we add that for reconstructing the new
                // tree later on.
                if (!isParentDuplicate && directParentNode) {
                    const treeNode = {
                        ...directParentNode,
                        children: [],
                        isExpanded: true,
                        parentName: rootNode.name,
                        rootName,
                    };
                    nodesToRender.push(treeNode);
                    nodeCache[parentName] = true;
                }

                // Now we add the matching node to the array to be rendered.
                // The only difference in logic is that we need to name the current node's parent, to recontruct the tree correctly.

                // If there's a direct parent node, that's the parent.
                if (directParentNode) {
                    const treeNode = {
                        ...node,
                        children: [],
                        parentName: directParentNode.name,
                        isExpanded: true,
                        rootName,
                    };
                    nodesToRender.push(treeNode);
                    nodeCache[nodeName] = true;
                    // If there's no direct parent, but there is a root, then the root's the parent.
                } else if (rootNode) {
                    const treeNode = { ...node, children: [], parentName: rootNode.name, isExpanded: true, rootName };
                    nodesToRender.push(treeNode);
                    nodeCache[nodeName] = true;
                    // Otherwise, the current node is a root, with no parent.
                } else {
                    const treeNode = { ...node, children: [], parentName: undefined, isExpanded: true, rootName };
                    nodesToRender.push(treeNode);
                    nodeCache[nodeName] = true;
                }
            }

            // Now, we have to check if any children of the current node are matches and execute the same logic.
            // That includes passing along the node's root and direct parent, since we'll need them if the child is a match.
            if (!!node.children) {
                const nodesRootParent = rootNode ? rootNode : node;
                const nodesDirectParent = rootNode ? node : null;
                // we recurse to children passing along the cache and building up the nodePath array so we dedupe items by fully qualified name.
                // node that this function mutates nodesToRender, accumulating child state.
                this.filterTreeToMatchingRecursive(
                    nodesToRender,
                    node.children,
                    nodesRootParent,
                    nodesDirectParent,
                    nodeCache,
                    nodePath.concat([node.name])
                );
            }
        });

        // Now that we have a flat array of all the nodes we need to render, we need to reconstruct the tree of matches.

        // Iterate over all the nodes to match the parents with their children, starting with the root nodes.
        const reconstructedTreeOfMatches = nodesToRender.filter(nodeToRender => nodeToRender.parentName === undefined);
        reconstructedTreeOfMatches.map(root => {
            root.children = nodesToRender.filter(nodeToRender => nodeToRender.parentName === root.name);

            root.children?.map((child) => {
                // We check that both the parent and the root match to handle the case where there are multiple parents
                // with the same name (eg "v1").
                child.children = nodesToRender.filter(
                    (nodeToRender) => nodeToRender.parentName === child.name && nodeToRender.rootName === root.name
                );
            });
        });

        // Update the currently rendered nodes to be the matches found above.
        // We return reconstructedTreeOfMatches and allow the calling function to set this.currentlyRenderedNodes
        // to prevent excessive repainting.
        return [...reconstructedTreeOfMatches];
    }

    onChange(event: KeyboardEvent) {
        this.debouncedFilterTree(event);
    }

    onClearFilter() {
        this.filterContent = "";
        this.currentlyRenderedNodes = this.parsedNodes;
        return;
    }

    debouncedFilterTree(event: KeyboardEvent) {
        this.filterContent = (event.target as HTMLInputElement).value.trim().toLowerCase();
        // performance for large packages like azure-native is too slow for filtering on single characters.
        // instead, we will skip filtering for single character queries so the UI doesn't hang.
        if (this.filterContent.length < 2) {
            this.currentlyRenderedNodes = this.parsedNodes;
            return;
        }
        // Otherwise, find the nodes that match the filter content.
        this.filterTreeToMatchingContent([], this.parsedNodes);
    }

    getFilterAndNavTree() {
        return (
            <div class="filter-and-nav-tree">
                <div class="input-container">
                    <input class="navigation-filter-input" placeholder="Filter" onInput={this.onChange.bind(this)} value={this.filterContent}></input>
                    {this.filterContent && (
                        <div class="clear-container">
                            <button onClick={this.onClearFilter.bind(this)} class="clear-filter-button">
                                X
                            </button>
                        </div>
                    )}
                </div>
                {this.filterContent?.length === 1 && <div class="filter-help-text">Provide at least two characters to filter.</div>}
                {this.currentlyRenderedNodes?.length < 1 && <div class="no-results">No results found. Try a different filter.</div>}
                <pulumi-api-doc-nav-tree class="nav-tree" baseDirectory={this.baseDirectory} nodes={this.currentlyRenderedNodes}></pulumi-api-doc-nav-tree>
            </div>
        );
    }

    getLoadingState() {
        return (
            <div class="loading">
                <i class="loading-icon fas fa-spinner"></i>
                <span class="loading-text">Loading...</span>
            </div>
        );
    }

    render() {
        return (
            <section class="api-doc-nav">
                <h3 class="navigation-header">API Navigation</h3>
                {this.isLoading ? this.getLoadingState() : this.getFilterAndNavTree()}
            </section>
        );
    }
}
