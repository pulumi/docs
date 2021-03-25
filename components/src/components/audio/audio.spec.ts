import { Audio } from './audio';

describe('pulumi-audio', () => {
  it('builds', () => {
    expect(new Audio()).toBeTruthy();
  });
});
