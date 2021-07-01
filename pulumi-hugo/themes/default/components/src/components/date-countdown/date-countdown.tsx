import { Component, Host, h, Prop, State } from "@stencil/core";

interface CountdownData {
    remainingTimeInMS: number;
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
    textClass = "";

    @Prop()
    valueLabelClass = "";

    @Prop()
    countdownOverText = "";

    @State()
    countdownData: CountdownData;

    componentWillLoad() {
        const countdownEndDate = new Date(this.dateString).getTime();
        this.generateCountdownData(countdownEndDate)
        setInterval(() => this.generateCountdownData(countdownEndDate), 1000);
    }

    private generateCountdownData(end: number) {
        const now = Date.now();
        const remainingTimeInMS = end - now;
        this.countdownData = {
            remainingTimeInMS,
            days: Math.floor(remainingTimeInMS / (1000 * 60 * 60 * 24)),
            hours: Math.floor((remainingTimeInMS % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)),
            minutes: Math.floor((remainingTimeInMS % (1000 * 60 * 60)) / (1000 * 60)),
            seconds: Math.floor((remainingTimeInMS % (1000 * 60)) / 1000),
        }
    }

    private renderValueLabel(label: string) {
        return <span class={this.valueLabelClass}>{ label }</span>
    }

    private renderCountdown() {
        const { days, hours, minutes, seconds, remainingTimeInMS } = this.countdownData;
        return <p class={this.textClass}>
            { remainingTimeInMS > 0 ?
                <span>
                    <span>{ days }{this.renderValueLabel("days")} </span>
                    <span>{ hours }{this.renderValueLabel("hours")} </span>
                    <span>{ minutes }{this.renderValueLabel("minutes")} </span>
                    <span>{ seconds }{this.renderValueLabel("seconds")}</span>
                </span>
            :
                this.countdownOverText
            }
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
