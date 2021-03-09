import { DateCountdown } from './date-countdown';

describe('pulumi-date-countdown', () => {
  it('builds', () => {
    expect(new DateCountdown()).toBeTruthy();
  });
});
