import { newE2EPage } from '@stencil/core/testing';

describe('pulumi-gpt', () => {
  it('renders', async () => {
    const page = await newE2EPage();
    await page.setContent('<pulumi-gpt></pulumi-gpt>');

    const element = await page.find('pulumi-gpt');
    expect(element).toHaveClass('hydrated');
  });
});
