import { newSpecPage } from '@stencil/core/testing';
import { PulumiRegistryListSearch } from '../pulumi-registry-list-search';

describe('pulumi-registry-list-search', () => {
  it('renders', async () => {
    const page = await newSpecPage({
      components: [PulumiRegistryListSearch],
      html: `<pulumi-registry-list-search></pulumi-registry-list-search>`,
    });
    expect(page.root).toEqualHtml(`
      <pulumi-registry-list-search>
        <mock:shadow-root>
          <slot></slot>
        </mock:shadow-root>
      </pulumi-registry-list-search>
    `);
  });
});
