import { newE2EPage } from '@stencil/core/testing';

describe('pulumi-value-calculator', () => {
  it('renders', async () => {
    const page = await newE2EPage();
    await page.setContent('<pulumi-value-calculator></pulumi-value-calculator>');

    const element = await page.find('pulumi-value-calculator');
    expect(element).toHaveClass('hydrated');
  });
});
