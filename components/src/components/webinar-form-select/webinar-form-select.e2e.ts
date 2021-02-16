import { newE2EPage } from '@stencil/core/testing';

describe('pulumi-webinar-form-select', () => {
  it('renders', async () => {
    const page = await newE2EPage();
    await page.setContent('<pulumi-webinar-form-select></pulumi-webinar-form-select>');

    const element = await page.find('pulumi-webinar-form-select');
    expect(element).toHaveClass('hydrated');
  });
});
