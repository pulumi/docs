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
import "./external-links";
import "./neo-mode";

import "./experiments/terraform-compare";
import "./experiments/cta-activations-direct-vs-docs";

// Register all Stencil components.
defineCustomElements();
