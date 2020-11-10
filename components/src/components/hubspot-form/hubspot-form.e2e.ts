import { newE2EPage } from '@stencil/core/testing';

describe('pulumi-hubspot-form', () => {
  it('renders', async () => {
    const page = await newE2EPage();
    await page.setContent('<pulumi-hubspot-form></pulumi-hubspot-form>');

    const element = await page.find('pulumi-hubspot-form');
    expect(element).toHaveClass('hydrated');
  });
});
