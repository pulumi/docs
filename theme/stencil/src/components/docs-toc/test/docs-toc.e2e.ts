import { newE2EPage } from '@stencil/core/testing';

describe('docs-toc', () => {
  it('renders', async () => {
    const page = await newE2EPage();
    await page.setContent('<docs-toc></docs-toc>');

    const element = await page.find('docs-toc');
    expect(element).toHaveClass('hydrated');
  });
});
