import { newE2EPage } from '@stencil/core/testing';

describe('pulumi-swipeable', () => {
  it('renders', async () => {
    const page = await newE2EPage();
    await page.setContent('<pulumi-swipeable></pulumi-swipeable>');

    const element = await page.find('pulumi-swipeable');
    expect(element).toHaveClass('hydrated');
  });
});
