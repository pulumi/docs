import { gb } from "../../stencil/src/util/util";

function runTerraformExperiment() {

    // Elements for both variants
    const controlElements = document.querySelectorAll('[data-tf-variant="control"]');
    const newElements = document.querySelectorAll('[data-tf-variant="new"]');

    // Check feature flag
    const showNewVariant = gb.isOn('20241028-vs-terraform-new');

    // Toggle visibility
    controlElements.forEach(element => {
        element.classList.toggle('hidden', showNewVariant);
    });
    newElements.forEach(element => {
        element.classList.toggle('hidden', !showNewVariant);
    });
}

document.addEventListener("DOMContentLoaded", () => {
    if (window.location.pathname === "/docs/iac/concepts/vs/terraform/") {
        runTerraformExperiment();
    }
});