import { newE2EPage } from '@stencil/core/testing';

describe('pulumi-tertiary-nav', () => {
  it('renders', async () => {
    const page = await newE2EPage();
    await page.setContent('<pulumi-tertiary-nav></pulumi-tertiary-nav>');

    const element = await page.find('pulumi-tertiary-nav');
    expect(element).toHaveClass('hydrated');
  });
});
