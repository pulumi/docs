import { EventList } from './event-list';

describe('pulumi-event-list', () => {
  it('builds', () => {
    expect(new EventList()).toBeTruthy();
  });
});
