import { Component, Host, h, Prop, State } from "@stencil/core";
import { PulumiEvent, PulumiRawEvent, PulumiRawWebinar } from "../../util/types/events";
import { classNames, shuffleArray } from "../../util/util";

type EventFilterType = "featured" | "upcoming" | "on-demand" | "pulumitv";
type EventFilterChoiceText = "All" | "Featured" | "Upcoming Sessions" | "On Demand Videos" | "PulumiTV";
type EventFilter = "all" | EventFilterType;

interface EventFilterItem {
  text: EventFilterChoiceText;
  key: EventFilter;
  icon: string;
}

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
      type: [ "upcoming "],
      imageSrc: "/images/webinar/pulumi_tech_talk.jpg"
    }
  });
}

function parseWebinarsString(webinarString: string): PulumiEvent[] {
  const rawWebinars: PulumiRawWebinar[] = JSON.parse(webinarString);
  return rawWebinars.map((webinar) => {
    const types: EventFilterType[] = [];

    if (new Date().getTime() <= new Date(webinar.main.sortable_date).getTime()) {
      types.push("upcoming");
    }

    if (webinar.pre_recorded) {
      types.push("on-demand");
    }

    if (webinar.pulumi_tv) {
      types.push("pulumitv");
    }

    if (webinar.featured) {
      types.push("featured");
    }

    return {
      archetype: "webinar",
      title: webinar.title,
      description: webinar.meta_desc,
      startDate: new Date(webinar.main.sortable_date),
      registrationUrl: webinar.url_slug,
      external: webinar.external,
      type: types,
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

  @State()
  eventFilterChoice: EventFilter = "all";

  componentWillLoad() {
    const webinars = parseWebinarsString(this.webinars);
    const events = parseEventsString(this.events).filter((event) => new Date().getTime() <= event.startDate.getTime());

    this.pulumiEvents = this.pulumiEvents.concat(webinars).concat(events);
  }

  private handleEventFilterItemClick(filter: EventFilter) {
    this.eventFilterChoice = filter;
  }

  private renderEventFilterItem(args: EventFilterItem) {
    const itemClass = classNames("w-1/12 text-center mx-5", {
      "active": this.eventFilterChoice === args.key,
    });

    return(
      <li class={itemClass} onClick={() => this.handleEventFilterItemClick(args.key)}>
        <i class={`fas fa-${args.icon} text-4xl`}></i>
        <p class="hidden sm:block m-0 mt-3">{args.text}</p>
      </li>
    );
  }

  private renderEventFilter() {
    const items: EventFilterItem[] = [
      { text: "All", icon: "asterisk", key: "all" },
      { text: "Featured", icon: "star", key: "featured" },
      { text: "Upcoming Sessions", icon: "users", key: "upcoming" },
      { text: "On Demand Videos", icon: "video", key: "on-demand" },
      { text: "PulumiTV", icon: "tv", key: "pulumitv" },
    ];

    const selectedChoice = items.find((item) => item.key === this.eventFilterChoice);

    return(
      <div class="w-full mb-5">
        <ul class="flex p-2 sm:p-0 list-none event-list-filter">
          { items.map(this.renderEventFilterItem.bind(this)) }
        </ul>
        <h2 class="px-5">{selectedChoice.text}</h2>
      </div>
    );
  }

  private renderEventListRow(chunk: PulumiEvent[]) {
    return(
      <ul class="flex flex-wrap list-none p-0">
        {chunk.map((event) => {
          return(
            <pulumi-event-list-item class="mx-auto" event={event}></pulumi-event-list-item>
          );
        })}
      </ul>
    );
  }

  render() {
    const filteredEvents = this.pulumiEvents.filter((event) => {
      return this.eventFilterChoice === "all" ? true : event.type.indexOf(this.eventFilterChoice) > -1;
    });


    return (
      <Host>
        <div class="container mx-auto pt-10">
          { this.renderEventFilter() }
          { [shuffleArray<PulumiEvent>(filteredEvents)].map(this.renderEventListRow) }
        </div>
        <slot></slot>
      </Host>
    );
  }

}
