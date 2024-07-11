import '@hotwired/turbo';

import { Idiomorph } from "idiomorph/dist/idiomorph.esm"

addEventListener("turbo:before-render", (event: any) => {
  event.detail.render = (currentElement: any, newElement: any) => {
    Idiomorph.morph(currentElement, newElement)
  }
});
