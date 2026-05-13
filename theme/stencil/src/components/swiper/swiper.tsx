import { Component, Element, h, Prop, Method } from "@stencil/core";

@Component({
    tag: "pulumi-swiper",
    shadow: false,
})
export class Swiper {
    @Element()
    el: HTMLElement;

    @Prop()
    speed = 300;

    @Prop()
    loop = false;

    @Prop()
    autoplay = false;

    @Prop()
    autoplayDelay = 3000;

    @Prop()
    navControls = false;

    @Prop()
    slides = 1;

    @Prop()
    centeredSlides = false;

    @Prop()
    initialSlide = 1;

    @Prop()
    direction: "vertical" | "horizontal" = "horizontal";

    @Prop()
    enableMouseEvents = true;

    @Prop()
    spaceBetween = 0;

    private wrapper: HTMLElement;
    private container: HTMLElement;
    private currentIndex = 0;
    private slideCount = 0;
    private cloneCount = 0;
    private autoplayTimer: ReturnType<typeof setInterval>;
    private resizeObserver: ResizeObserver;
    private isTransitioning = false;
    private dragStartX = 0;
    private currentTranslate = 0;
    private isDragging = false;
    private dragArmed = false;

    componentDidLoad() {
        this.container = this.el.querySelector(".swiper") as HTMLElement;
        this.wrapper = this.container.querySelector(".swiper-wrapper") as HTMLElement;
        const slideEls = Array.from(this.wrapper.querySelectorAll(":scope > .swiper-slide"));
        this.slideCount = slideEls.length;

        if (this.slideCount === 0) return;

        this.applySlideWidths();

        if (this.loop && this.slideCount > this.slides) {
            this.cloneCount = this.slides;
            const firstChild = this.wrapper.firstChild;
            for (let i = 0; i < this.cloneCount; i++) {
                const clone = slideEls[this.slideCount - this.cloneCount + i].cloneNode(true) as HTMLElement;
                this.wrapper.insertBefore(clone, firstChild);
            }
            for (let i = 0; i < this.cloneCount; i++) {
                const clone = slideEls[i].cloneNode(true) as HTMLElement;
                this.wrapper.appendChild(clone);
            }
            this.applySlideWidths();
        }

        this.currentIndex = this.initialSlide;
        this.jumpTo(this.currentIndex);

        this.wrapper.addEventListener("transitionend", this.onTransitionEnd);
        this.container.style.touchAction = "pan-y";
        this.container.addEventListener("pointerdown", this.onPointerDown);

        this.resizeObserver = new ResizeObserver(() => {
            this.applySlideWidths();
            this.isTransitioning = false;
            this.jumpTo(this.currentIndex);
        });
        this.resizeObserver.observe(this.container);

        if (this.autoplay) {
            this.startAutoplay();
            if (this.enableMouseEvents) {
                this.container.addEventListener("mouseenter", this.onMouseEnter);
                this.container.addEventListener("mouseleave", this.onMouseLeave);
            }
        }
    }

    disconnectedCallback() {
        this.clearAutoplay();
        this.resizeObserver?.disconnect();
        this.wrapper?.removeEventListener("transitionend", this.onTransitionEnd);
        this.container?.removeEventListener("pointerdown", this.onPointerDown);
        this.container?.removeEventListener("mouseenter", this.onMouseEnter);
        this.container?.removeEventListener("mouseleave", this.onMouseLeave);
        document.removeEventListener("pointermove", this.onPointerMove);
        document.removeEventListener("pointerup", this.onPointerUp);
    }

    private applySlideWidths() {
        const allSlides = Array.from(this.wrapper.querySelectorAll(":scope > .swiper-slide")) as HTMLElement[];
        const containerWidth = this.container.offsetWidth;
        const slideWidth = (containerWidth - this.spaceBetween * (this.slides - 1)) / this.slides;
        for (const slide of allSlides) {
            slide.style.width = `${slideWidth}px`;
            slide.style.marginRight = `${this.spaceBetween}px`;
        }
    }

    private getStep(): number {
        const containerWidth = this.container.offsetWidth;
        return (containerWidth - this.spaceBetween * (this.slides - 1)) / this.slides + this.spaceBetween;
    }

    private translateForIndex(index: number): number {
        const step = this.getStep();
        let tx = -(index + this.cloneCount) * step;
        if (this.centeredSlides && this.slides > 1) {
            const containerWidth = this.container.offsetWidth;
            tx += (containerWidth - (step - this.spaceBetween)) / 2;
        }
        return tx;
    }

    private jumpTo(index: number) {
        this.wrapper.style.transitionDuration = "0ms";
        this.currentTranslate = this.translateForIndex(index);
        this.wrapper.style.transform = `translate3d(${this.currentTranslate}px, 0, 0)`;
    }

    private slideTo(index: number, duration: number = this.speed) {
        this.wrapper.style.transitionDuration = `${duration}ms`;
        this.wrapper.style.transitionTimingFunction = "ease";
        this.currentTranslate = this.translateForIndex(index);
        this.wrapper.style.transform = `translate3d(${this.currentTranslate}px, 0, 0)`;
    }

    private advance = (dir: number, duration?: number) => {
        if (this.isTransitioning) return;
        const next = this.currentIndex + dir;
        if (!this.loop) {
            const clamped = Math.max(0, Math.min(next, this.slideCount - this.slides));
            if (clamped === this.currentIndex) return;
            this.currentIndex = clamped;
        } else {
            this.currentIndex = next;
        }
        this.isTransitioning = true;
        this.slideTo(this.currentIndex, duration);
    };

    private onTransitionEnd = () => {
        this.isTransitioning = false;
        if (!this.loop) return;
        if (this.currentIndex >= this.slideCount) {
            this.currentIndex -= this.slideCount;
            this.jumpTo(this.currentIndex);
        } else if (this.currentIndex < 0) {
            this.currentIndex += this.slideCount;
            this.jumpTo(this.currentIndex);
        }
    };

    private startAutoplay() {
        this.clearAutoplay();
        this.autoplayTimer = setInterval(() => this.advance(1), this.autoplayDelay);
    }

    private clearAutoplay() {
        if (this.autoplayTimer) {
            clearInterval(this.autoplayTimer);
            this.autoplayTimer = null;
        }
    }

    private onMouseEnter = () => this.clearAutoplay();
    private onMouseLeave = () => { if (this.autoplay) this.startAutoplay(); };

    // Pointer handling treats every press as a potential tap until movement
    // crosses the 5px threshold in onPointerMove. Only then do we commit to a
    // drag and call setPointerCapture — capturing earlier retargets the eventual
    // click away from anchors inside slides, breaking link navigation.
    private onPointerDown = (e: PointerEvent) => {
        if (e.button !== 0) return;
        if ((e.target as HTMLElement).closest(".swiper-button-prev, .swiper-button-next")) return;
        this.dragArmed = true;
        this.isDragging = false;
        this.dragStartX = e.clientX;
        document.addEventListener("pointermove", this.onPointerMove);
        document.addEventListener("pointerup", this.onPointerUp);
    };

    private onPointerMove = (e: PointerEvent) => {
        if (!this.dragArmed) return;
        const delta = e.clientX - this.dragStartX;
        if (!this.isDragging) {
            if (Math.abs(delta) < 5) return;
            this.isDragging = true;
            this.isTransitioning = false;
            this.clearAutoplay();
            this.wrapper.style.transitionDuration = "0ms";
            try { this.container.setPointerCapture(e.pointerId); } catch {}
        }
        const tx = this.clampTranslate(this.currentTranslate + delta);
        this.wrapper.style.transform = `translate3d(${tx}px, 0, 0)`;
    };

    // Bounds the wrapper translate to its content extent so dragging past the
    // first or last slide never exposes whitespace beyond the cloned edges.
    private clampTranslate(tx: number): number {
        const step = this.getStep();
        const totalSlides = this.slideCount + 2 * this.cloneCount;
        const totalWidth = totalSlides * step - this.spaceBetween;
        const containerWidth = this.container.offsetWidth;
        const offset = this.centeredSlides && this.slides > 1
            ? (containerWidth - (step - this.spaceBetween)) / 2
            : 0;
        const maxTx = offset;
        const minTx = Math.min(offset, containerWidth - totalWidth + offset);
        return Math.max(minTx, Math.min(maxTx, tx));
    }

    private onPointerUp = (e: PointerEvent) => {
        if (!this.dragArmed) return;
        this.dragArmed = false;
        document.removeEventListener("pointermove", this.onPointerMove);
        document.removeEventListener("pointerup", this.onPointerUp);
        // No drag committed → tap. Bail out and let the native click reach the link.
        if (!this.isDragging) return;
        this.isDragging = false;
        const delta = e.clientX - this.dragStartX;
        // SNAP_MS is intentionally short so post-drag positioning feels responsive
        // even when `this.speed` is tuned for a slow autoplay drift (e.g. 8000ms).
        const SNAP_MS = 300;
        // Drag was committed → swallow the trailing click that some browsers fire
        // after pointerup so the user doesn't accidentally navigate a slide link
        // they were swiping. The setTimeout guards against touch devices that
        // don't fire a trailing click at all — otherwise the suppressor would
        // sit armed and eat the user's next legitimate tap.
        const suppressClick = (ev: Event) => {
            ev.preventDefault();
            ev.stopPropagation();
        };
        this.container.addEventListener("click", suppressClick, { capture: true, once: true });
        setTimeout(() => {
            this.container.removeEventListener("click", suppressClick, true);
        }, 300);
        if (Math.abs(delta) > 50) {
            this.advance(delta < 0 ? 1 : -1, SNAP_MS);
        } else {
            this.slideTo(this.currentIndex, SNAP_MS);
        }
        if (this.autoplay) this.startAutoplay();
    };

    @Method()
    public async stopSwiper() {
        this.clearAutoplay();
    }

    @Method()
    public async startSwiper() {
        if (this.autoplay) this.startAutoplay();
    }

    render() {
        return (
            <div class="swiper">
                <div class="swiper-wrapper">
                    <slot></slot>
                </div>

                {this.navControls && (
                    <span>
                        <div class="swiper-button-prev" onClick={() => this.advance(-1)}>
                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 27 44">
                                <path d="M0,22L22,0l2.1,2.1L4.2,22l19.9,19.9L22,44L0,22z" />
                            </svg>
                        </div>
                        <div class="swiper-button-next" onClick={() => this.advance(1)}>
                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 27 44">
                                <path d="M27,22L5,44l-2.1-2.1L22.8,22L2.9,2.1L5,0L27,22z" />
                            </svg>
                        </div>
                    </span>
                )}
            </div>
        );
    }
}
