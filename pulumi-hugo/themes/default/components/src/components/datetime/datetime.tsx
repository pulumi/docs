import { Component, Prop, h } from "@stencil/core";

@Component({
    tag: "pulumi-datetime",
    styleUrl: "datetime.scss",
    shadow: true,
})
export class Datetime {

    @Prop()
    class?: string;

    @Prop({ mutable: true })
    date: string;

    componentWillLoad() {
        const date = new Date(this.date);

        const options: Intl.DateTimeFormatOptions = {
            timeZoneName: "short",
            weekday: "short",
            year: "numeric",
            month: "long",
            day: "numeric",
            hour: "numeric",
            minute: "2-digit"
        };

        this.date = date.toLocaleString(undefined, options);
    }

    render() {
        return (
            <time class={this.class || ""}>
                <span>{this.date}</span>
            </time>
        );
    }

}
