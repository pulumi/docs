import { Component, Host, h, Prop, State } from "@stencil/core";

interface CountdownData {
    days: number;
    hours: number;
    minutes: number;
    seconds: number;
}

@Component({
    tag: "pulumi-date-countdown",
    styleUrl: "date-countdown.css",
    shadow: false
})
export class DateCountdown {
    @Prop()
    dateString: string;

    @Prop()
    textClass: string = "";

    @Prop()
    valueLabelClass: string = "";

    @State()
    countdownData: CountdownData;

    componentWillLoad() {
        const countdownEndDate = new Date(this.dateString).getTime();
        this.generateCountdownData(countdownEndDate)
        setInterval(() => this.generateCountdownData(countdownEndDate), 1000);
    }

    private generateCountdownData(end: number) {
        const now = Date.now();
        const distance = end - now;
        this.countdownData = {
            days: Math.floor(distance / (1000 * 60 * 60 * 24)),
            hours: Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)),
            minutes: Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60)),
            seconds: Math.floor((distance % (1000 * 60)) / 1000),
        }
    }

    private renderValueLabel(label: string) {
        return <span class={this.valueLabelClass}>{ label }</span>
    }

    private renderCountdown() {
        const { days, hours, minutes, seconds } = this.countdownData;
        return <p class={this.textClass}>
            <span>{ days }{this.renderValueLabel("days")} </span>
            <span>{ hours }{this.renderValueLabel("hours")} </span>
            <span>{ minutes }{this.renderValueLabel("minutes")} </span>
            <span>{ seconds }{this.renderValueLabel("seconds")}</span>
        </p>;
    }

    render() {
        return (
            <Host>
                { this.countdownData && this.renderCountdown() }
            </Host>
        );
    }
}
