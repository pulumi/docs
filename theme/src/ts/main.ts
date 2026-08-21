import { defineCustomElements } from "../../stencil/dist/loader";

import "../scss/main.scss";

import "./misc";
import "./nav";
import "./carousel";
import "./chooser";
import "./noselect";
import "./tracking";
import "./docs-feedback";
import "./blog-list";
import "./blog-post";
import "./blog-lightbox";
import "./what-is-list";
import "./case-studies-list";
import "./details-dropdown";
import "./copybutton";
import "./copy-text";
import "./code-tabbed";
import "./code-snippets-dropdown";
import "./resources";
import "./event-sessions";
import "./releases";
import "./packages";
import "./pricing-calculator";
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
import "./intercom-identity";

// Register all Stencil components.
defineCustomElements();
