import { newE2EPage } from '@stencil/core/testing';

describe('pulumi-mp3-mute-contorller', () => {
  it('renders', async () => {
    const page = await newE2EPage();
    await page.setContent('<pulumi-mp3-mute-controller></pulumi-mp3-mute-controller>');

    const element = await page.find('pulumi-mp3-mute-controller');
    expect(element).toHaveClass('hydrated');
  });
});
