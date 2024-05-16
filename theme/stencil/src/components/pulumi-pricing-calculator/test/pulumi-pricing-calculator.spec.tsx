import { newSpecPage } from '@stencil/core/testing';
import { PulumiPricingCalculator } from '../pulumi-pricing-calculator';

describe('pulumi-pricing-calculator', () => {
  it('renders', async () => {
    const page = await newSpecPage({
      components: [PulumiPricingCalculator],
      html: `<pulumi-pricing-calculator></pulumi-pricing-calculator>`,
    });
    expect(page.root).toEqualHtml(`
      <pulumi-pricing-calculator>
        <mock:shadow-root>
          <slot></slot>
        </mock:shadow-root>
      </pulumi-pricing-calculator>
    `);
  });
});
