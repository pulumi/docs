import { Component, Host, h, Prop } from "@stencil/core";
import { classNames } from "../../util/util";
import { PulumiEvent } from "../../util/types/events";

@Component({
  tag: "pulumi-event-list-item",
  styleUrl: "event-list-item.scss",
  shadow: false,
})
export class EventListItem {

  @Prop()
  event: PulumiEvent;

  render() {
    const {
      archetype, external, registrationUrl, imageSrc, title, description,
      startDate,
    } = this.event;
    const containerClass = classNames("w-full m-0 p-2", {
      "order-first": false,
    });

    const eventLinkProps = {
      href: archetype === "webinar" && external ? `/webinars/${registrationUrl}` : registrationUrl,
      rel: external ? "noopener noreferrer" : undefined,
      target: external ? "_blank" : undefined,
    };

    return [
      <li class={containerClass}>
        <article class="rounded shadow-md bg-white border border-gray-200 mb-10 flex flex-col lg:flex-row mx-auto">
          <div class="w-full lg:w-4/12">
            <a {...eventLinkProps}>
              <img class="w-full" src={imageSrc} />
            </a>
          </div>
          <div class="w-full lg:w-8/12 p-3 ml-3">
            <a {...eventLinkProps}>
              { title }
              { external ? <i class="text-sm ml-2 fas fa-external-link-alt"></i> : null }
            </a>
            <p class="mb-5">
              { description }
            </p>
            <p class="my-0 text-lg">
                <i class="fas fa-calendar mr-2"></i>
                <span>{ startDate }</span>
            </p>
            <p class="my-0 text-lg">
                <i class="fas fa-clock mr-2"></i>
                1 hour
            </p>
          </div>
        </article>
      </li>,
      <slot></slot>
    ];
  }

}
