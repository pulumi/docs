import { Datetime } from './datetime';

describe('pulumi-datetime', () => {
  it('builds', () => {
    expect(new Datetime()).toBeTruthy();
  });
});
