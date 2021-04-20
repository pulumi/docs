import { newE2EPage } from '@stencil/core/testing';

describe('pulumi-slot-machine', () => {
  it('renders', async () => {
    const page = await newE2EPage();
    await page.setContent('<pulumi-slot-machine></pulumi-slot-machine>');

    const element = await page.find('pulumi-slot-machine');
    expect(element).toHaveClass('hydrated');
  });
});
