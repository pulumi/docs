import { newSpecPage } from '@stencil/core/testing';
import { PulumiTertiaryNav } from '../pulumi-tertiary-nav';

describe('pulumi-tertiary-nav', () => {
  it('renders', async () => {
    const page = await newSpecPage({
      components: [PulumiTertiaryNav],
      html: `<pulumi-tertiary-nav></pulumi-tertiary-nav>`,
    });
    expect(page.root).toEqualHtml(`
      <pulumi-tertiary-nav>
        <mock:shadow-root>
          <slot></slot>
        </mock:shadow-root>
      </pulumi-tertiary-nav>
    `);
  });
});
