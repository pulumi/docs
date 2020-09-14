import { Component, h, Prop } from "@stencil/core";
import moment from "moment";
import { PulumiEvent } from "../../util/types/events";

@Component({
  tag: "pulumi-event-list-item",
  styleUrl: "event-list-item.scss",
  shadow: false,
})
export class EventListItem {

  @Prop()
  event: PulumiEvent;

  @Prop()
  class: string = "";

  render() {
    const {
      archetype, external, registrationUrl, imageSrc, title, description,
      startDate,
    } = this.event;

    const displayDate = moment(startDate).format("MMM D, YYYY");

    const eventLinkProps = {
      href: archetype === "webinar" && !external ? `/resources/${registrationUrl}` : registrationUrl,
      rel: external ? "noopener noreferrer" : undefined,
      target: external ? "_blank" : undefined,
    };

    const key = new Date().getTime();

    return [
      <li key={key} class="w-full m-0 p-2 event-list-item">
        <article class="rounded shadow-md bg-white border border-gray-200 mb-10 flex flex-col mx-auto">
          <div class="w-full event-list-item-image">
            <a {...eventLinkProps}>
              <img src={imageSrc} />
            </a>
          </div>
          <div class="w-full p-3 pl-6 event-list-item-info">
            <div class="event-title">
              <a {...eventLinkProps} class="font-bold text-xl">
                { title }
                { external ? <i class="text-sm ml-2 fas fa-external-link-alt"></i> : null }
              </a>
            </div>
            <div class="event-description">
              <p class="m-0 pt-5">
                { description }
              </p>
            </div>
            <div class="event-details">
              <span class="my-0 py-1 px-2 text-lg rounded-full bg-orange-500 inline-block text-white mr-3">
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
