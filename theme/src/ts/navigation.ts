type PageEvent = "load";

export const onPageEvent = (event: PageEvent, handler: () => void) => {
    const doc = window.document;

    doc.addEventListener("pulumi:load", () => {
        handler();
    });
}

document.addEventListener("DOMContentLoaded", () => {
    document.dispatchEvent(new Event("pulumi:load"));
});

document.addEventListener("click", async (event: any) => {
    const target = event.target;
    const nodeName = target.nodeName;
    const href = target.getAttribute("href");

    // TODO: Not quite done; still needs to be scoped to this domain, and doesn't seem to like clicks of nodes within A tags.

    if (target.getAttribute("href")) {
        event.preventDefault();
        event.stopPropagation();

        history.pushState({ url: href }, "", href);
        await getPage(href);

        return false;
    }

}, { capture: true });

window.addEventListener("popstate", async (event: PopStateEvent) => {
    if (event.state) {
        await getPage(event.state.url);
    }
});

async function getPage(url: string) {
    const response = await fetch(url);
    const content = await response.text();
    const html = new DOMParser().parseFromString(content, "text/html");
    const newHead = html.querySelector("head");
    const newBody = html.querySelector("body");
    const existingCopilotNode = document.querySelector("#copilot");
    let existingCopilotClone;

    if (existingCopilotNode) {
        existingCopilotClone = existingCopilotNode.cloneNode(true);
    }

    document.head.innerHTML = "";
    const headNodes = newHead.querySelectorAll("*");

    Array.from(headNodes).forEach(node => {

        // Skip HEAD scripts -- we only want to load those once. I think.
        if (node.nodeName === "SCRIPT") {
            // debugger;
            return;
        }

        const newNode = document.createElement(node.nodeName);

        node.getAttributeNames().map(name => {
            const val = node.getAttribute(name);
            newNode.setAttribute(name, val);
        });

        if (node.textContent) {
            newNode.textContent = node.textContent;
        }

        document.head.appendChild(newNode);
    })

    document.body.replaceWith(newBody);

    const bodyScripts = newBody.querySelectorAll("script");
    console.log({ bodyScripts });

    Array.from(bodyScripts).forEach(script=> {
        console.log(script);
        const newScript = document.createElement("script");

        script.getAttributeNames().map(name => {
            const val = script.getAttribute(name);
            newScript.setAttribute(name, val);
        });

        if (script.textContent) {
            newScript.textContent = script.textContent;
        }

        document.head.appendChild(newScript);
        script.remove();
    });

    const newCopilotNode = document.querySelector("#copilot");

    if (newCopilotNode && existingCopilotClone) {
        existingCopilotClone.classList.remove("hidden");
        newCopilotNode.replaceWith(existingCopilotClone);
    } else if (existingCopilotClone) {
        existingCopilotClone.classList.add("hidden");
        document.body.appendChild(existingCopilotClone);
    }

    document.dispatchEvent(new Event("pulumi:load"));
    window.scrollTo({ top: 0 });
}
