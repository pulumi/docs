import { newSpecPage } from '@stencil/core/testing';
import { PulumiAI } from '../pulumi-ai';

describe('pulumi-gpt', () => {
  it('renders', async () => {
    const page = await newSpecPage({
      components: [PulumiAI],
      html: `<pulumi-gpt></pulumi-gpt>`,
    });
    expect(page.root).toEqualHtml(`
      <pulumi-gpt>
        <mock:shadow-root>
          <slot></slot>
        </mock:shadow-root>
      </pulumi-gpt>
    `);
  });
});
