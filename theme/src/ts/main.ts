import { defineCustomElements } from "../../stencil/dist";
import { onPageEvent } from "./navigation";

// Register all Stencil components.
defineCustomElements();

import "../scss/main.scss";

import "./navigation";
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
import "./pricing-trial";
import "./developer-advocates";
import "./toc";
import "./docs-main";
import "./redirects";
import "./algolia/autocomplete";
import "./anchors";
import "./copilot.ts";

console.log("in the bundle");
