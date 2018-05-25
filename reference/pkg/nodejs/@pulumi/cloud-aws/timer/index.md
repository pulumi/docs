---
title: Module timer
---

<a href="..">@pulumi/cloud-aws</a>

<h2 class="pdoc-module-header">Index</h2>

* <a href="#cron">function cron</a>
* <a href="#daily">function daily</a>
* <a href="#hourly">function hourly</a>
* <a href="#interval">function interval</a>

<a href="/timer/index.ts">timer/index.ts</a> 

<h2 class="pdoc-module-header">Modules</h2>


<h2 class="pdoc-module-header" id="cron">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/timer/index.ts#L33">function cron</a>
</h2>

```typescript
cron(name: string, cronTab: string, handler: timer.Action, opts?: pulumi.ResourceOptions): void
```

<h2 class="pdoc-module-header" id="daily">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/timer/index.ts#L38">function daily</a>
</h2>

```typescript
daily(name: string, scheduleOrHandler: timer.DailySchedule | timer.Action, handlerOrOptions?: timer.Action | pulumi.ResourceOptions, opts?: pulumi.ResourceOptions): void
```

<h2 class="pdoc-module-header" id="hourly">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/timer/index.ts#L62">function hourly</a>
</h2>

```typescript
hourly(name: string, scheduleOrHandler: timer.HourlySchedule | timer.Action, handlerOrOptions?: timer.Action | pulumi.ResourceOptions, opts?: pulumi.ResourceOptions): void
```

<h2 class="pdoc-module-header" id="interval">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/timer/index.ts#L9">function interval</a>
</h2>

```typescript
interval(name: string, options: timer.IntervalRate, handler: timer.Action, opts?: pulumi.ResourceOptions): void
```

