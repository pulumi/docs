import { Component, h, Prop } from "@stencil/core";
import moment from "moment";
import { PulumiEvent } from "../../util/types/events";

@Component({
    tag: "pulumi-event-list-item",
    styleUrl: "event-list-item.scss",
    shadow: false,
})
export class EventListItem {

    // The event data.
    @Prop()
    event: PulumiEvent;

    render() {
        const {
            archetype, external, registrationUrl, title, description,
            startDate, type
        } = this.event;

        // Create the display date.
        const displayDate = moment(startDate).format("MMM D, YYYY");

        // Create the link props and add the proper values if the event is external.
        const eventLinkProps = {
            href: archetype === "webinar" && !external ? `/resources/${registrationUrl}` : registrationUrl,
            rel: external ? "noopener noreferrer" : undefined,
            target: external ? "_blank" : undefined,
        };

        // Set the icon for the listing item.
        let typeIcon = "users";
        if (type.indexOf("pulumitv") > -1) {
            typeIcon = "tv";
        } else if (type.indexOf("on-demand") > -1) {
            typeIcon = "video";
        }

        return [
            <li class="w-full m-0 p-2 event-list-item">
                <article class="rounded shadow-md bg-white border border-gray-200 mb-10 flex flex-col mx-auto">
                    <div class="w-full h-full p-3 pl-6 relative">
                        <div class="flex border-solid border-b border-gray-200 pb-2">
                            <div>
                                <div class="flex items-center justify-center h-12 w-12 rounded-full bg-purple-500 text-white mr-3">
                                    <i class={`fas fa-${typeIcon}`}></i>
                                </div>
                            </div>
                            <div>
                                <a {...eventLinkProps} class="font-bold text-xl">
                                    { title }
                                    { external ? <i class="text-sm ml-2 fas fa-external-link-alt"></i> : null }
                                </a>
                            </div>
                        </div>
                        <div>
                            <p class="m-0 pt-5">
                                { description }
                            </p>
                        </div>
                        <div class="absolute bottom-0 mb-5">
                            <span class="my-0 py-1 px-2 inline-block mr-3">
                                    <i class="fas fa-calendar mr-2"></i>
                                    { displayDate }
                            </span>
                        </div>
                    </div>
                </article>
            </li>,
            <slot></slot>
        ];
    }

}
