import { YoutubeAudioPlayer } from './youtube-audio-player';

describe('pulumi-youtube-audio-player', () => {
  it('builds', () => {
    expect(new YoutubeAudioPlayer()).toBeTruthy();
  });
});
