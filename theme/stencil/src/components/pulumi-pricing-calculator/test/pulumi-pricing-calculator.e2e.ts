import { newE2EPage } from '@stencil/core/testing';

describe('pulumi-pricing-calculator', () => {
  it('renders', async () => {
    const page = await newE2EPage();
    await page.setContent('<pulumi-pricing-calculator></pulumi-pricing-calculator>');

    const element = await page.find('pulumi-pricing-calculator');
    expect(element).toHaveClass('hydrated');
  });
});
