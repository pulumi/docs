import { newSpecPage } from '@stencil/core/testing';
import { EventSessionRegistrationModal } from '../event-session-registration-modal';

describe('event-session-registration-modal', () => {
  it('renders', async () => {
    const page = await newSpecPage({
      components: [EventSessionRegistrationModal],
      html: `<event-session-registration-modal></event-session-registration-modal>`,
    });
    expect(page.root).toEqualHtml(`
      <event-session-registration-modal>
        <mock:shadow-root>
          <slot></slot>
        </mock:shadow-root>
      </event-session-registration-modal>
    `);
  });
});
