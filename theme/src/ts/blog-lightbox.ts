// Blog media lightbox: click an image or video in a post body to see it larger,
// in the overlay rendered by layouts/partials/blog/lightbox.html.
//
// Only media that actually gains something from the treatment gets it. An
// inline icon, a badge, a logo, or a screenshot already shown at its full size
// gains nothing from a modal that redraws it at the same size — and making it
// clickable is noise, not a feature. So eligibility is measured, not marked up:
// an element becomes clickable only when the overlay could draw it meaningfully
// bigger than the post draws it. That check has to run in the browser, because
// it needs the intrinsic pixel size and the current viewport; post images are
// plain markdown references, many of them pointing at another post's bundle or
// at /static, so there's no dependable build-time size to test against. Videos
// are the same measurement against videoWidth/videoHeight — the {{< video >}}
// shortcode renders them `w-full`, so a screen recording shot at 1080p is
// always being squeezed into the ~768px column.
//
// Authors can opt an element (or a block of them) out explicitly by putting
// data-no-lightbox on it or any ancestor. Anything inside a link is always
// skipped — it already does something when clicked — which also covers the card
// embeds ({{< blog/card >}}) that render inside a post body. A video with
// controls is skipped too: a wrapping button would swallow clicks meant for the
// control bar, and those controls already carry a fullscreen button, which is
// the same offer the lightbox makes.

// Narrower than this on screen and it's a badge or an icon, not a figure.
const MIN_DISPLAY_WIDTH = 240;

// The source needs real detail to reveal: below the ~768px content column
// there's nothing behind the constraint worth opening. SVGs are measured the
// same way — the overlay draws everything at its intrinsic size at most, so a
// vector authored small has no more to show than a raster of the same size.
const MIN_INTRINSIC_WIDTH = 600;

// The overlay has to be at least this much wider than the inline image to be
// worth a click.
const MIN_ENLARGEMENT = 1.2;

// Room the overlay's own chrome takes off the viewport, mirroring
// partials/blog/lightbox.html: its md:p-8 side padding, and vertically that
// padding plus the 6rem the media yields to the caption.
const OVERLAY_MARGIN_X = 64;
const OVERLAY_MARGIN_Y = 160;

// The injected wrapper must not change the media's box: no padding, no border,
// and shrink-to-fit like the image it wraps. `group` drives the badge's
// hover/focus reveal (see the template in the partial).
const TRIGGER_CLASS =
    "group relative block cursor-zoom-in appearance-none border-0 bg-transparent p-0 " +
    "focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-violet-primary";

// Videos need the wrapper to span the column instead: the shortcode renders
// them `w-full`, and a percentage width resolved against a shrink-to-fit button
// would collapse the video to nothing.
const VIDEO_TRIGGER_CLASS = `${TRIGGER_CLASS} w-full`;

type Media = HTMLImageElement | HTMLVideoElement;

function isVideo(el: Media): el is HTMLVideoElement {
    return el.tagName === "VIDEO";
}

// Zero on either axis means hidden, still loading, or broken.
function intrinsicSize(el: Media): [number, number] {
    return isVideo(el) ? [el.videoWidth, el.videoHeight] : [el.naturalWidth, el.naturalHeight];
}

function worthEnlarging(el: Media): boolean {
    const displayWidth = el.clientWidth;
    const [intrinsicWidth, intrinsicHeight] = intrinsicSize(el);
    if (!displayWidth || !intrinsicWidth || !intrinsicHeight) {
        return false;
    }
    if (displayWidth < MIN_DISPLAY_WIDTH || intrinsicWidth < MIN_INTRINSIC_WIDTH) {
        return false;
    }

    // How wide the overlay would draw it: scaled down to fit the viewport box,
    // never up past its intrinsic size, since upscaling only adds blur.
    // Comparing that against the inline width is also what keeps a tall image
    // out — fitting one to the viewport height leaves it no wider than the
    // content column already made it.
    const fit = Math.min((window.innerWidth - OVERLAY_MARGIN_X) / intrinsicWidth, (window.innerHeight - OVERLAY_MARGIN_Y) / intrinsicHeight, 1);
    return intrinsicWidth * fit >= displayWidth * MIN_ENLARGEMENT;
}

// The alt text on an image, the title on a {{< video >}} clip.
function describe(el: Media): string {
    return isVideo(el) ? el.title : el.alt;
}

document.addEventListener("DOMContentLoaded", () => {
    const dialog = document.querySelector<HTMLDialogElement>("[data-lightbox]");
    const postBody = document.querySelector<HTMLElement>(".blog-post-content");
    if (!dialog || !postBody) {
        return;
    }

    const overlayImage = dialog.querySelector<HTMLImageElement>("[data-lightbox-image]");
    const overlayVideo = dialog.querySelector<HTMLVideoElement>("[data-lightbox-video]");
    const caption = dialog.querySelector<HTMLElement>("[data-lightbox-caption]");
    const badge = dialog.querySelector<HTMLTemplateElement>("[data-lightbox-badge]");
    if (!overlayImage || !overlayVideo || !caption || !badge) {
        return;
    }

    // closest() matches the element itself, so this covers both an opted-out
    // element and an opted-out (or linked) container around one.
    const media = Array.from(postBody.querySelectorAll<Media>("img, video")).filter(
        el => !el.closest("a, [data-no-lightbox]") && !(isVideo(el) && el.controls),
    );
    if (media.length === 0) {
        return;
    }

    // The inline clip a video overlay was opened from, if opening it paused
    // one; it gets resumed on close.
    let pausedSource: HTMLVideoElement | null = null;

    function enable(el: Media): void {
        if (el.parentElement?.hasAttribute("data-lightbox-trigger")) {
            return;
        }
        const button = document.createElement("button");
        button.type = "button";
        button.setAttribute("data-lightbox-trigger", "");
        button.className = isVideo(el) ? VIDEO_TRIGGER_CLASS : TRIGGER_CLASS;
        // The alt text or title still names the media; the suffix says what the
        // button does with it.
        const description = describe(el);
        button.setAttribute("aria-label", description ? `${description} (view larger)` : "View larger");
        el.replaceWith(button);
        button.appendChild(el);
        button.appendChild(badge.content.cloneNode(true));
    }

    function disable(el: Media): void {
        const button = el.parentElement;
        if (button?.hasAttribute("data-lightbox-trigger")) {
            button.replaceWith(el);
        }
    }

    // Eligibility depends on the viewport, so it isn't decided once: an image
    // that gains nothing on a wide screen can gain plenty on a narrow one.
    function refresh(): void {
        for (const el of media) {
            if (worthEnlarging(el)) {
                enable(el);
            } else {
                disable(el);
            }
        }
    }

    function openVideo(video: HTMLVideoElement): void {
        overlayVideo.src = video.currentSrc;
        overlayVideo.muted = video.muted;
        overlayVideo.loop = video.loop;
        // Pick up where the inline clip was rather than restarting it, and hold
        // the inline copy still while its bigger twin plays. currentTime is only
        // settable once the new source has metadata.
        const resumeAt = video.currentTime;
        overlayVideo.addEventListener(
            "loadedmetadata",
            () => {
                overlayVideo.currentTime = resumeAt;
                void overlayVideo.play().catch(() => {
                    /* autoplay may be blocked; the first frame still shows */
                });
            },
            { once: true },
        );
        if (!video.paused) {
            video.pause();
            pausedSource = video;
        }
    }

    function open(el: Media): void {
        const video = isVideo(el);
        overlayImage.classList.toggle("hidden", video);
        overlayVideo.classList.toggle("hidden", !video);
        if (isVideo(el)) {
            openVideo(el);
        } else {
            overlayImage.src = el.currentSrc || el.src;
            overlayImage.alt = el.alt;
        }
        // Visible caption only — the overlay image's alt (and the video's own
        // title) already carry this text for assistive tech, hence aria-hidden
        // on the figcaption.
        caption.textContent = describe(el);
        document.body.style.overflow = "hidden";
        dialog.showModal();
    }

    postBody.addEventListener("click", (e: MouseEvent) => {
        const button = (e.target as HTMLElement).closest("[data-lightbox-trigger]");
        const el = button?.querySelector<Media>("img, video");
        if (el) {
            open(el);
        }
    });

    // Anywhere in the overlay, including the image itself: there's nothing to
    // interact with in there, so every click is a dismissal. That's also why
    // the close button needs no handler of its own — its click lands here.
    // The video is the exception: it carries controls at this size, and they
    // sit in a UA shadow root, so a click on play or the scrubber arrives here
    // retargeted to the <video> itself and must not also close the overlay.
    dialog.addEventListener("click", (e: MouseEvent) => {
        if (e.target !== overlayVideo) {
            dialog.close();
        }
    });

    // Fires for the close button, Escape, and the backdrop click alike. The UA
    // restores focus to the trigger on its own.
    dialog.addEventListener("close", () => {
        document.body.style.overflow = "";
        overlayImage.removeAttribute("src");
        // load() after dropping the source stops the download the paused
        // element would otherwise keep buffering.
        overlayVideo.pause();
        overlayVideo.removeAttribute("src");
        overlayVideo.load();
        pausedSource?.play().catch(() => {
            /* the inline clip was playing a moment ago; if it won't resume, leave it */
        });
        pausedSource = null;
        caption.textContent = "";
    });

    // Nothing that hasn't decoded yet has a size to measure. Both events fire
    // once per element, and anything already loaded is caught by the initial
    // refresh() below.
    for (const el of media) {
        el.addEventListener(isVideo(el) ? "loadedmetadata" : "load", refresh, { once: true });
    }

    let resizeTimer: number | undefined;
    window.addEventListener("resize", () => {
        window.clearTimeout(resizeTimer);
        resizeTimer = window.setTimeout(refresh, 200);
    });

    refresh();
});
