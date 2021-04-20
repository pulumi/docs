import { SlotMachine } from './slot-machine';

describe('pulumi-slot-machine', () => {
  it('builds', () => {
    expect(new SlotMachine()).toBeTruthy();
  });
});
