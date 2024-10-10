import { newSpecPage } from '@stencil/core/testing';
import { CopilotSidebar } from '../copilot-sidebar';

describe('copilot-sidebar', () => {
  it('renders', async () => {
    const page = await newSpecPage({
      components: [CopilotSidebar],
      html: `<copilot-sidebar></copilot-sidebar>`,
    });
    expect(page.root).toEqualHtml(`
      <copilot-sidebar>
        <mock:shadow-root>
          <slot></slot>
        </mock:shadow-root>
      </copilot-sidebar>
    `);
  });
});
