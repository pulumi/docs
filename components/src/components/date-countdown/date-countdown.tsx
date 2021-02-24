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
        this.countdownData = this.generateCountdownData(countdownEndDate)

        const self = this;
        setInterval(() => {
            self.countdownData = this.generateCountdownData(countdownEndDate);
        }, 1000);
    }

    private generateCountdownData(end: number): CountdownData {
        const now = new Date().getTime();
        const distance = end - now;
        return {
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
            { days }{this.renderValueLabel("days")} { hours }{this.renderValueLabel("hours")} { minutes }{this.renderValueLabel("minutes")} { seconds }{this.renderValueLabel("seconds")}
        </p>;
    }

    private renderLoading() {
        return <p class={this.textClass}>
            <i class="fa fa-spinner fa-spin"></i>
        </p>;
    }

    render() {
        return (
            <Host>
                { this.countdownData ? this.renderCountdown() : this.renderLoading() }
            </Host>
        );
    }
}
