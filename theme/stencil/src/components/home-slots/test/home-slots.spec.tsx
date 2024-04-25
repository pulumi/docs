import { newSpecPage } from '@stencil/core/testing';
import { HomeSlots } from '../home-slots';

describe('home-slots', () => {
  it('renders', async () => {
    const page = await newSpecPage({
      components: [HomeSlots],
      html: `<home-slots></home-slots>`,
    });
    expect(page.root).toEqualHtml(`
      <home-slots>
        <mock:shadow-root>
          <slot></slot>
        </mock:shadow-root>
      </home-slots>
    `);
  });
});
