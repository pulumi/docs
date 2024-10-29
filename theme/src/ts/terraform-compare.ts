import { gb } from "../../stencil/src/util/util";

function initTerraformCompare() {

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

// Run when DOM is ready
document.addEventListener('DOMContentLoaded', initTerraformCompare);