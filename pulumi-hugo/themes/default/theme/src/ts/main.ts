import { initDesignSystem, button, accordion, accordionItem, disclosure, treeItem, treeView } from "@pulumi/facet";
import { defineCustomElements } from "../../stencil/dist";

import "../scss/main.scss";

import "./misc";
import "./nav";
import "./carousel";
import "./chooser";
import "./price-toggle";
import "./noselect";
import "./tracking";
import "./docs-feedback";
import "./event-filtering";
import "./copybutton";
import "./code-tabbed";
import "./resources";
import "./search";
import "./packages";
import "./pricing-trial";
import "./developer-advocates";
import "./toc";

// Initialize the Facet design system and components.
initDesignSystem({
    prefix: "pulumi",
    components: [accordion(), accordionItem(), button(), disclosure(), treeItem(), treeView()],
});

// Register all Stencil components.
defineCustomElements();
