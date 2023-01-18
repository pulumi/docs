import { newE2EPage } from '@stencil/core/testing';

describe('event-session-registration-modal', () => {
  it('renders', async () => {
    const page = await newE2EPage();
    await page.setContent('<event-session-registration-modal></event-session-registration-modal>');

    const element = await page.find('event-session-registration-modal');
    expect(element).toHaveClass('hydrated');
  });
});
