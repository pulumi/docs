import "@hotwired/turbo";

type PageEvent = "load";

export const onPageEvent = (event: PageEvent, handler: () => void) => {
    const doc = window.document;

    doc.addEventListener("turbo:load", () => {
        console.log("turbo:load");
        handler();
    });
}
