import { newE2EPage } from '@stencil/core/testing';

describe('pulumi-youtube-audio-player', () => {
  it('renders', async () => {
    const page = await newE2EPage();
    await page.setContent('<pulumi-youtube-audio-player></pulumi-youtube-audio-player>');

    const element = await page.find('pulumi-youtube-audio-player');
    expect(element).toHaveClass('hydrated');
  });
});
