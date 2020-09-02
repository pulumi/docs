import { newE2EPage } from '@stencil/core/testing';

describe('pulumi-event-list-item', () => {
  it('renders', async () => {
    const page = await newE2EPage();
    await page.setContent('<pulumi-event-list-item></pulumi-event-list-item>');

    const element = await page.find('pulumi-event-list-item');
    expect(element).toHaveClass('hydrated');
  });
});
