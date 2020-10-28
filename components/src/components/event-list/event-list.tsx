import { Component, Host, h, Prop, State } from "@stencil/core";
import { PulumiEvent, PulumiRawEvent, PulumiRawWebinar } from "../../util/types/events";
import { classNames, shuffleArray } from "../../util/util";

// Event types
type EventFilterType = "featured" | "upcoming" | "on-demand" | "pulumitv";
type EventFilterChoiceText = "All" | "Featured" | "Upcoming Sessions" | "Videos" | "PulumiTV";
type EventFilter = "all" | EventFilterType;

interface EventFilterItem {
    text: EventFilterChoiceText;
    key: EventFilter;
    icon: string;
}

// parseEventsString takes an JSON string of the data for an "event"
// and returns a typed PulumiEvent that we use to create the listing.
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

// parseWebinarsString takes an JSON string of the data for an "webinar"
// and returns a typed PulumiEvent that we use to create the listing.
function parseWebinarsString(webinarString: string): PulumiEvent[] {
    const rawWebinars: PulumiRawWebinar[] = JSON.parse(webinarString);
    const result: PulumiEvent[] = [];

    for (let i = 0; i < rawWebinars.length; i++) {
        const webinar = rawWebinars[i];

        const types: EventFilterType[] = [];

        // Add the different types of webinars so we can attach the appropriate icon
        // to the listing.
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

        // Do not list the webinar if there is no available type.
        if (!types.length) {
            continue;
        }

        const pulumiEvent: PulumiEvent = {
            archetype: "webinar",
            title: webinar.title,
            description: webinar.meta_desc,
            startDate: new Date(webinar.main.sortable_date),
            registrationUrl: webinar.url_slug,
            external: webinar.external,
            type: types,
            imageSrc: webinar.preview_image,
        };

        result.push(pulumiEvent);
    }

    return result;
}

@Component({
    tag: "pulumi-event-list",
    styleUrl: "event-list.scss",
    shadow: false,
})
export class EventList {

    // A JSON string of the webinar data.
    // The data represents all pages with a "webinar" type
    // in the '/content/resources' directory.
    @Prop({ mutable: true })
    webinars: string;

    // A JSON string of the event data.
    // The data represents all pages with a "event" type
    // in the '/content/resources' directory.
    @Prop({ mutable: true })
    events: string;

    // The transformed webinar and event data ready to
    // turned into listings.
    @State()
    pulumiEvents: PulumiEvent[] = [];

    // The current choice of the event filter.
    @State()
    eventFilterChoice: EventFilter = "all";

    componentWillLoad() {
        // Parse the data strings.
        const webinars = parseWebinarsString(this.webinars);
        const events = parseEventsString(this.events).filter((event) => new Date().getTime() <= event.startDate.getTime());

        // Set the event data.
        this.pulumiEvents = this.pulumiEvents.concat(webinars).concat(events);
    }

    // Set the item filter when a filter item is clicked.
    private handleEventFilterItemClick(filter: EventFilter) {
        this.eventFilterChoice = filter;
    }

    private renderEventFilterItem(args: EventFilterItem) {
        // Mark an item as active if it is selected.
        const itemClass = classNames("w-1/12 text-center mx-5 event-filter-item", {
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
        // The event filter data.
        const items: EventFilterItem[] = [
            { text: "All", icon: "asterisk", key: "all" },
            { text: "Featured", icon: "star", key: "featured" },
            { text: "Upcoming Sessions", icon: "users", key: "upcoming" },
            { text: "Videos", icon: "video", key: "on-demand" },
            { text: "PulumiTV", icon: "tv", key: "pulumitv" },
        ];

        // Get the selected choice.
        const selectedChoice = items.find((item) => item.key === this.eventFilterChoice);

        return(
            <div class="w-full mb-5">
                <ul class="flex list-none event-list-filter">
                    { items.map(this.renderEventFilterItem.bind(this)) }
                </ul>
                <h2 class="px-5 mt-0">{selectedChoice.text}</h2>
            </div>
        );
    }

    private renderEventListRow(events: PulumiEvent[]) {
        return(
            <ul class="flex flex-wrap justify-center list-none p-0">
                {events.map((event, i) => {
                    return(
                        <pulumi-event-list-item key={i} event={event}></pulumi-event-list-item>
                    );
                })}
            </ul>
        );
    }

    render() {
        // Filter the events based on the currently selected filter.
        const filteredEvents = this.eventFilterChoice === "all" ? this.pulumiEvents : this.pulumiEvents.filter((event) => {
            return event.type.indexOf(this.eventFilterChoice) > -1;
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
