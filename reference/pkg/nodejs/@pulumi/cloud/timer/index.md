---
title: Module timer
---

<a href="..">@pulumi/cloud</a>

<h2 class="pdoc-module-header">Index</h2>

* <a href="#cron">function cron</a>
* <a href="#daily">function daily</a>
* <a href="#hourly">function hourly</a>
* <a href="#interval">function interval</a>
* <a href="#DailySchedule">interface DailySchedule</a>
* <a href="#HourlySchedule">interface HourlySchedule</a>
* <a href="#IntervalRate">interface IntervalRate</a>
* <a href="#Action">type Action</a>

<a href="/timer/index.ts">timer/index.ts</a> 

<h2 class="pdoc-module-header">Modules</h2>


<h2 class="pdoc-module-header" id="cron">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/timer/index.ts#L76">function cron</a>
</h2>

```typescript
cron(name: string, cronTab: string, handler: Action, opts?: pulumi.ResourceOptions): void
```


A cron timer, which fires on based on a specificied cron schedule.

<h2 class="pdoc-module-header" id="daily">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/timer/index.ts#L87">function daily</a>
</h2>

```typescript
daily(name: string, handler: Action, opts?: pulumi.ResourceOptions): void
```


A daily timer, firing each day, on the day (at UTC midnight).


```typescript
daily(name: string, schedule: DailySchedule, handler: Action, opts?: pulumi.ResourceOptions): void
```


A daily timer, firing at the specified UTC hour and minute each day.

<h2 class="pdoc-module-header" id="hourly">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/timer/index.ts#L108">function hourly</a>
</h2>

```typescript
hourly(name: string, handler: Action, opts?: pulumi.ResourceOptions): void
```


An hourly timer, firing each hour, on the hour.


```typescript
hourly(name: string, schedule: HourlySchedule, handler: Action, opts?: pulumi.ResourceOptions): void
```


An hourly timer, firing at the specified UTC minute each hour.

<h2 class="pdoc-module-header" id="interval">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/timer/index.ts#L63">function interval</a>
</h2>

```typescript
interval(name: string, options: IntervalRate, handler: Action, opts?: pulumi.ResourceOptions): void
```


An interval timer, which fires on a regular time interval.

<h2 class="pdoc-module-header" id="DailySchedule">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/timer/index.ts#L34">interface DailySchedule</a>
</h2>

DailySchedule describes a time of day ([[hourUTC]] and [[minuteUTC]]) at which a daily timer should fire.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/timer/index.ts#L38">property hourUTC</a>
</h3>

```typescript
hourUTC?: undefined | number;
```


The hour, in UTC, that the timer should fire.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/timer/index.ts#L42">property minuteUTC</a>
</h3>

```typescript
minuteUTC?: undefined | number;
```


The minute, in UTC, that the timer should fire.

<h2 class="pdoc-module-header" id="HourlySchedule">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/timer/index.ts#L48">interface HourlySchedule</a>
</h2>

HourlySchedule describes a time of the hour ([[minuteUTC]]) at which an hourly timer should fire.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/timer/index.ts#L52">property minuteUTC</a>
</h3>

```typescript
minuteUTC?: undefined | number;
```


The minute, in UTC, that the timer should fire.

<h2 class="pdoc-module-header" id="IntervalRate">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/timer/index.ts#L16">interface IntervalRate</a>
</h2>

IntervalRate describes the rate at which a timer will fire.

At least one of [[minutes]], [[hours]] or [[days]] must be provided.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/timer/index.ts#L28">property days</a>
</h3>

```typescript
days?: undefined | number;
```


The number of days in the interval.  Must be a positive integer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/timer/index.ts#L24">property hours</a>
</h3>

```typescript
hours?: undefined | number;
```


The number of hours in the interval.  Must be a positive integer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/timer/index.ts#L20">property minutes</a>
</h3>

```typescript
minutes?: undefined | number;
```


The number of minutes in the interval.  Must be a positive integer.

<h2 class="pdoc-module-header" id="Action">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/timer/index.ts#L8">type Action</a>
</h2>

```typescript
type Action = { ... };
```


Action is a handler that performs an action in response to a timer firing.

