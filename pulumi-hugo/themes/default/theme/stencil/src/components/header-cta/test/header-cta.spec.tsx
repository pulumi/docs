import { newSpecPage } from '@stencil/core/testing';
import { HeaderCta } from '../header-cta';

describe('header-cta', () => {
  it('renders', async () => {
    const page = await newSpecPage({
      components: [HeaderCta],
      html: `<header-cta></header-cta>`,
    });
    expect(page.root).toEqualHtml(`
      <header-cta>
        <mock:shadow-root>
          <slot></slot>
        </mock:shadow-root>
      </header-cta>
    `);
  });
});
