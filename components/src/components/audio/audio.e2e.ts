import { newE2EPage } from '@stencil/core/testing';

describe('pulumi-audio', () => {
  it('renders', async () => {
    const page = await newE2EPage();
    await page.setContent('<pulumi-audio></pulumi-audio>');

    const element = await page.find('pulumi-audio');
    expect(element).toHaveClass('hydrated');
  });
});
