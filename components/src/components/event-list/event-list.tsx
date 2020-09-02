import { Component, Host, h, Prop, State } from "@stencil/core";
import { PulumiEvent, PulumiRawEvent, PulumiRawWebinar } from "../../util/types/events";

function parseEventsString(eventsString: string): PulumiEvent[] {
  const rawEvents: PulumiRawEvent[] = JSON.parse(eventsString);
  return rawEvents.map((event) => {
    return {
      archetype: "event",
      title: event.title,
      description: event?.event?.description || "",
      startDate: new Date(event?.event?.start_date || ""),
      registrationUrl: event?.event?.registration_url || "",
      external: true,
      type: [],
      imageSrc: "/images/webinar/pulumi_tech_talk.jpg"
    }
  });
}

function parseWebinarsString(webinarString: string): PulumiEvent[] {
  const rawWebinars: PulumiRawWebinar[] = JSON.parse(webinarString);
  return rawWebinars.map((webinar) => {
    return {
      archetype: "webinar",
      title: webinar.title,
      description: webinar.meta_desc,
      startDate: new Date(webinar.main.sortable_date),
      registrationUrl: webinar.url_slug,
      external: webinar.external,
      type: [],
      imageSrc: webinar.preview_image,
    };
  });
}

@Component({
  tag: "pulumi-event-list",
  styleUrl: "event-list.scss",
  shadow: false,
})
export class EventList {

  @Prop({ mutable: true })
  webinars: string;

  @Prop({ mutable: true })
  events: string;

  @State()
  pulumiEvents: PulumiEvent[] = [];

  componentWillLoad() {
    const webinars = parseWebinarsString(this.webinars);
    const events = parseEventsString(this.events);

    this.pulumiEvents = this.pulumiEvents.concat(webinars).concat(events);
  }

  render() {
    console.log(this.pulumiEvents);

    return (
      <Host>
        { this.pulumiEvents.map((event) => <pulumi-event-list-item event={event}></pulumi-event-list-item>) }
        <slot></slot>
      </Host>
    );
  }

}
