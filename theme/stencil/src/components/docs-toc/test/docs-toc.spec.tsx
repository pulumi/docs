import { newSpecPage } from '@stencil/core/testing';
import { DocsToc } from '../docs-toc';

describe('docs-toc', () => {
  it('renders', async () => {
    const page = await newSpecPage({
      components: [DocsToc],
      html: `<docs-toc></docs-toc>`,
    });
    expect(page.root).toEqualHtml(`
      <docs-toc>
        <mock:shadow-root>
          <slot></slot>
        </mock:shadow-root>
      </docs-toc>
    `);
  });
});
