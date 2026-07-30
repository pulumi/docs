import { defineCustomElements } from "../../stencil/dist/loader";

import "../scss/main.scss";

import "./misc";
import "./nav";
import "./carousel";
import "./chooser";
import "./price-toggle";
import "./noselect";
import "./tracking";
import "./docs-feedback";
import "./blog-list";
import "./blog-post";
import "./what-is-list";
import "./case-studies-list";
import "./details-dropdown";
import "./copybutton";
import "./code-tabbed";
import "./code-snippets-dropdown";
import "./resources";
import "./releases";
import "./packages";
import "./pricing-trial";
import "./extend-trial";
import "./developer-advocates";
import "./toc";
import "./docs-main";
import "./docs-theme";
import "./redirects";
// Algolia is built as a separate entry point (algolia-entry.ts) and loaded
// only on pages with a #search element. See assets.html.
import "./external-links";
import "./neo-mode";
import "./console-banner";
import "./announcement-banner";
import "./statuspage";
import "./mktg-ctas-experiment";

// Register all Stencil components.
defineCustomElements();
