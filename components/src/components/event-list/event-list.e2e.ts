import { newE2EPage } from '@stencil/core/testing';

describe('pulumi-event-list', () => {
  it('renders', async () => {
    const page = await newE2EPage();
    await page.setContent('<pulumi-event-list></pulumi-event-list>');

    const element = await page.find('pulumi-event-list');
    expect(element).toHaveClass('hydrated');
  });
});
