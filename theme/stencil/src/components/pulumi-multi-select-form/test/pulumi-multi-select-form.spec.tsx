import { newSpecPage } from "@stencil/core/testing";
import { h } from "@stencil/core";
import { PulumiMultiSelectForm } from "../pulumi-multi-select-form";

describe("pulumi-multi-select-form", () => {
    it("renders", async () => {
        const page = await newSpecPage({
            components: [PulumiMultiSelectForm],
            html: `<pulumi-multi-select-form></pulumi-multi-select-form>`,
        });
        expect(page.root).toEqualHtml(`
      <pulumi-multi-select-form>
        <div>
           <div>
             <span></span>
             <div class="grid grid-cols-1 lg:grid-cols-4 gap-3" role="radiogroup"></div>
           </div>
        </div>
      </pulumi-multi-select-form>
    `);
    });

    it("forwards the selected item's key as form-name on the embedded pulumi-hubspot-form", async () => {
        const items = [
            { key: "general", hubspotFormId: "form-1" },
            { key: "sales", hubspotFormId: "form-2" },
        ];
        const page = await newSpecPage({
            components: [PulumiMultiSelectForm],
            template: () => <pulumi-multi-select-form items={items} />,
        });
        await page.waitForChanges();

        const embeddedForm = page.root.querySelector("pulumi-hubspot-form");
        expect(embeddedForm).not.toBeNull();
        expect(embeddedForm.getAttribute("form-id")).toBe("form-1");
        expect(embeddedForm.getAttribute("form-name")).toBe("general");
    });

    it("omits form-name when the selected item renders a CTA instead of a form", async () => {
        const items = [
            { key: "support", hubspotFormId: "cta1", cta: { label: "Submit a Request", url: "/support/new/" } },
        ];
        const page = await newSpecPage({
            components: [PulumiMultiSelectForm],
            template: () => <pulumi-multi-select-form items={items} />,
        });
        await page.waitForChanges();

        expect(page.root.querySelector("pulumi-hubspot-form")).toBeNull();
        const cta = page.root.querySelector("a");
        expect(cta.getAttribute("href")).toBe("/support/new/");
    });
});
