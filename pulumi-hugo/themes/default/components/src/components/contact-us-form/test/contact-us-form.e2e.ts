import { newE2EPage } from '@stencil/core/testing';

describe('contact-us-form', () => {
  it('renders', async () => {
    const page = await newE2EPage();
    await page.setContent('<pulumi-contact-us-form items="[]"></pulumi-contact-us-form>');

    const element = await page.find('pulumi-contact-us-form');
    expect(element).toHaveClass('hydrated');
  });
});
