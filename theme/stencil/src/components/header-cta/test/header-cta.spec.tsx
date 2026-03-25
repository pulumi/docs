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
        <a class="" data-track="header-signup" data-role="cta-get-started" href="https://app.pulumi.com/signup?utm_source=header-button" title="Sign Up">Sign Up</a>
      </header-cta>
    `);
  });
});
