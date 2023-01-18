import { newE2EPage } from '@stencil/core/testing';

describe('pulumi-registry-list-search', () => {
  it('renders', async () => {
    const page = await newE2EPage();
    await page.setContent('<pulumi-registry-list-search></pulumi-registry-list-search>');

    const element = await page.find('pulumi-registry-list-search');
    expect(element).toHaveClass('hydrated');
  });
});
