import { newSpecPage } from "@stencil/core/testing";
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
});
