import { newE2EPage } from '@stencil/core/testing';

describe('pulumi-datetime', () => {
  it('renders', async () => {
    const page = await newE2EPage();
    await page.setContent('<pulumi-datetime></pulumi-datetime>');

    const element = await page.find('pulumi-datetime');
    expect(element).toHaveClass('hydrated');
  });
});
