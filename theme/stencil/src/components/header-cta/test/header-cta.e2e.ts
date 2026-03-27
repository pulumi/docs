import { newE2EPage } from '@stencil/core/testing';

describe('header-cta', () => {
  it('renders', async () => {
    const page = await newE2EPage();
    await page.setContent('<header-cta></header-cta>');

    const element = await page.find('header-cta');
    expect(element).toHaveClass('hydrated');
  });
});
