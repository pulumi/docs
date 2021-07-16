import { newSpecPage } from '@stencil/core/testing';
import { PulumiMultiSelectForm } from '../pulumi-multi-select-form';

describe('pulumi-multi-select-form', () => {
  it('renders', async () => {
    const page = await newSpecPage({
      components: [PulumiMultiSelectForm],
      html: `<pulumi-multi-select-form></pulumi-multi-select-form>`,
    });
    expect(page.root).toEqualHtml(`
      <pulumi-multi-select-form>
        <div>
           <span>
             <span></span>
             <select></select>
           </span>
           <pulumi-hubspot-form></pulumi-hubspot-form>
        </div>
      </pulumi-multi-select-form>
    `);
  });
});
