import { newE2EPage } from '@stencil/core/testing';

describe('pulumi-date-countdown', () => {
  it('renders', async () => {
    const page = await newE2EPage();
    await page.setContent('<pulumi-date-countdown></pulumi-date-countdown>');

    const element = await page.find('pulumi-date-countdown');
    expect(element).toHaveClass('hydrated');
  });
});
