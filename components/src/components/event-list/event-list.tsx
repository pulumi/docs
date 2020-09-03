import { Component, Host, h, Prop, State } from "@stencil/core";
import { PulumiEvent, PulumiRawEvent, PulumiRawWebinar } from "../../util/types/events";
import { chunkArray } from "../../util/util";

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

  renderEventListRow(chunk: PulumiEvent[]) {
    const listItemClass = `w-1/${chunk.length}`;

    return(
      <ul class="flex list-none">
        {chunk.map((event) => {
          return(
            <pulumi-event-list-item class={listItemClass} event={event}></pulumi-event-list-item>
          );
        })}
      </ul>
    );
  }

  renderEventFilterItem(args: {text: string, icon: string}) {
    return(
      <li class="w-1/12 text-center mx-5">
        <i class={`fas fa-${args.icon} text-4xl`}></i>
        <p class="m-0 mt-3 font-bold">{args.text}</p>
      </li>
    );
  }

  renderEventFilter() {
    const items = [
      { text: "All", icon: "asterisk" },
      { text: "Upcoming Sessions", icon: "users" },
      { text: "On Demand Videos", icon: "video" },
      { text: "PulumiTV", icon: "tv" },
    ];

    return(
      <div class="w-full mb-5">
        <ul class="flex list-none">
          { items.map(this.renderEventFilterItem) }
        </ul>
      </div>
    );
  }

  render() {
    const chunkedEvents = chunkArray(this.pulumiEvents, 3);

    return (
      <Host>
        <div class="container mx-auto pt-10">
          { this.renderEventFilter() }
          { chunkedEvents.map(this.renderEventListRow) }
        </div>
        <slot></slot>
      </Host>
    );
  }

}
