import { newE2EPage } from '@stencil/core/testing';

describe('pulumi-swiper', () => {
  it('renders', async () => {
    const page = await newE2EPage();
    await page.setContent('<pulumi-swiper></pulumi-swiper>');

    const element = await page.find('pulumi-swiper');
    expect(element).toHaveClass('hydrated');
  });
});
