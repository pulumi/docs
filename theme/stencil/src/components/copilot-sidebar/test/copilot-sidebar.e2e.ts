import { newE2EPage } from '@stencil/core/testing';

describe('copilot-sidebar', () => {
  it('renders', async () => {
    const page = await newE2EPage();
    await page.setContent('<copilot-sidebar></copilot-sidebar>');

    const element = await page.find('copilot-sidebar');
    expect(element).toHaveClass('hydrated');
  });
});
