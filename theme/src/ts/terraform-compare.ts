import { gb } from "../../stencil/src/util/util";
import { generateOnThisPage } from "./misc";
import { getQueryVariable } from "./util";

 // Add type declarations for global functions we'll use
declare global {
    interface Window {
        jQuery: any;
    }
}

function runTerraformExperiment() {

    // Elements for both variants
    const controlElements = document.querySelectorAll('[data-tf-variant="control"]');
    const newElements = document.querySelectorAll('[data-tf-variant="new"]');

    // Check feature flag
    const urlVariant = getQueryVariable('variant-vs-terraform-docs-page');
    const showNewVariant = urlVariant ? urlVariant === '1' : gb.isOn('20241028-vs-terraform-new');

    // Toggle visibility
    controlElements.forEach(element => {
        element.classList.toggle('hidden', showNewVariant);
    });
    newElements.forEach(element => {
        element.classList.toggle('hidden', !showNewVariant);
    });

    // Clear and regenerate the "On This Page" navigation
    window.jQuery(".table-of-contents .content ul.table-of-contents-list").empty();
    generateOnThisPage();
}

gb.setRenderer(() => {
    if (window.location.pathname === "/docs/iac/concepts/vs/terraform/") {
        runTerraformExperiment();
    }
});