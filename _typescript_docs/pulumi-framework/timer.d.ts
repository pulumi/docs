---
layout: typescript-reference
repo: pulumi-framework
subpath: timer.d.ts
---
export interface IntervalRate {
    minutes?: number;
    hours?: number;
    days?: number;
}
export interface DailySchedule {
    hourUTC?: number;
    minuteUTC?: number;
}
export declare function interval(name: string, options: IntervalRate, handler: () => Promise<void>): void;
export declare function cron(name: string, cronTab: string, handler: () => Promise<void>): void;
export declare function daily(name: string, schedule: DailySchedule, handler: () => Promise<void>): void;
