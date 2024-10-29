import { gb } from "../../stencil/src/util/util";

function initTerraformCompare() {
    console.log("Terraform compare module initialized");

    // Elements for both variants
    const controlElements = document.querySelectorAll('[data-tf-variant="control"]');
    const newElements = document.querySelectorAll('[data-tf-variant="new"]');

    // Check feature flag
    const showNewVariant = gb.isOn('20241028-vs-terraform-new');
    // const showNewVariant = true;
    console.log("Terraform comparison variant:", showNewVariant ? "NEW" : "CONTROL");

    // Toggle visibility
    controlElements.forEach(element => {
        element.classList.toggle('hidden', showNewVariant);
    });
    newElements.forEach(element => {
        element.classList.toggle('hidden', !showNewVariant);
    });
}

// Run when DOM is ready
document.addEventListener('DOMContentLoaded', initTerraformCompare);