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
import "./event-filtering";
import "./copybutton";
import "./code-tabbed";
import "./resources";
import "./packages";
import "./pricing-trial";
import "./pulumi-cloud";
import "./developer-advocates";
import "./toc";
import "./docs-main";
import "./redirects";
import "./algolia/autocomplete";
import "./terraform-compare";
import "./external-links";
import "./neo-mode";

// Register all Stencil components.
defineCustomElements();
