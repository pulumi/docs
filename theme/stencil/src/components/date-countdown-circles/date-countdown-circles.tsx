import { Component, Host, h, Prop, State } from "@stencil/core";

interface CountdownData {
    remainingTimeInMS: number;
    weeks: number;
    days: number;
    hours: number;
    minutes: number;
    seconds: number;
    weeksPercent: number;
    daysPercent: number;
    hoursPercent: number;
    minutesPercent: number;
    secondsPercent: number;
}

@Component({
    tag: "pulumi-date-countdown-circles",
    styleUrl: "date-countdown-circles.scss",
    shadow: false,
})
export class DateCountdownCircles {
    @Prop()
    dateString: string;

    @Prop()
    containerClass = "";

    @Prop()
    valueLabelClass = "";

    @State()
    countdownData: CountdownData;

    componentWillLoad() {
        const countdownEndDate = new Date(this.dateString).getTime();
        this.generateCountdownData(countdownEndDate);
        setInterval(() => this.generateCountdownData(countdownEndDate), 1000);
    }

    private generateCountdownData(end: number) {
        const now = Date.now();
        const remainingTimeInMS = end - now;

        // calculate values
        const weeks = Math.floor(remainingTimeInMS / (1000 * 60 * 60 * 24 * 7));
        const days = Math.floor((remainingTimeInMS % (1000 * 60 * 60 * 24 * 7)) / (1000 * 60 * 60 * 24));
        const hours = Math.floor((remainingTimeInMS % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((remainingTimeInMS % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((remainingTimeInMS % (1000 * 60)) / 1000);

        // calculate circle percentages
        const weeksPercent = (weeks / 52) * 100;
        const daysPercent = (days / 7) * 100;
        const hoursPercent = (hours / 24) * 100;
        const minutesPercent = (minutes / 60) * 100;
        const secondsPercent = (seconds / 60) * 100;

        this.countdownData = {
            remainingTimeInMS,
            weeks,
            days,
            hours,
            minutes,
            seconds,
            weeksPercent,
            daysPercent,
            hoursPercent,
            minutesPercent,
            secondsPercent,
        };
    }

    private renderValueLabel(label: string) {
        return <span class={this.valueLabelClass}>{label}</span>;
    }

    private renderNumberCircle(value: number, percent: number) {
        return (
            <div class="timer-wrapper">
                <div class="circle" style={{ "--p": `${percent}` }}>
                    {value}
                </div>
            </div>
        );
    }

    private renderCountdownPart(value: number, label: string, percent) {
        return (
            <div class="mx-4 text-center">
                {this.renderNumberCircle(value, percent)}
                {this.renderValueLabel(label)}
            </div>
        );
    }

    private renderCountdown() {
        const { weeks, days, hours, minutes, seconds, weeksPercent, daysPercent, hoursPercent, minutesPercent, secondsPercent } = this.countdownData;
        return (
            <div class={this.containerClass}>
                {[
                    this.renderCountdownPart(weeks, "Weeks", weeksPercent),
                    this.renderCountdownPart(days, "Days", daysPercent),
                    this.renderCountdownPart(hours, "Hours", hoursPercent),
                    this.renderCountdownPart(minutes, "Minutes", minutesPercent),
                    this.renderCountdownPart(seconds, "Seconds", secondsPercent),
                ]}
            </div>
        );
    }

    render() {
        return <Host>{this.countdownData && this.renderCountdown()}</Host>;
    }
}
