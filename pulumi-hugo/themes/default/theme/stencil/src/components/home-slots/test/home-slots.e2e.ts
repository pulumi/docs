import { newE2EPage } from '@stencil/core/testing';

describe('home-slots', () => {
  it('renders', async () => {
    const page = await newE2EPage();
    await page.setContent('<home-slots></home-slots>');

    const element = await page.find('home-slots');
    expect(element).toHaveClass('hydrated');
  });
});
