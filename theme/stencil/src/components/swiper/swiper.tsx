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
    private isTransitioning = false;
    private dragStartX = 0;
    private currentTranslate = 0;
    private isDragging = false;

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

    private slideTo(index: number) {
        this.wrapper.style.transitionDuration = `${this.speed}ms`;
        this.wrapper.style.transitionTimingFunction = "ease";
        this.currentTranslate = this.translateForIndex(index);
        this.wrapper.style.transform = `translate3d(${this.currentTranslate}px, 0, 0)`;
    }

    private advance = (dir: number) => {
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
        this.slideTo(this.currentIndex);
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

    private onPointerDown = (e: PointerEvent) => {
        if (e.button !== 0) return;
        if ((e.target as HTMLElement).closest(".swiper-button-prev, .swiper-button-next")) return;
        this.isDragging = true;
        this.dragStartX = e.clientX;
        this.clearAutoplay();
        this.wrapper.style.transitionDuration = "0ms";
        this.container.setPointerCapture(e.pointerId);
        document.addEventListener("pointermove", this.onPointerMove);
        document.addEventListener("pointerup", this.onPointerUp);
    };

    private onPointerMove = (e: PointerEvent) => {
        if (!this.isDragging) return;
        const delta = e.clientX - this.dragStartX;
        this.wrapper.style.transform = `translate3d(${this.currentTranslate + delta}px, 0, 0)`;
    };

    private onPointerUp = (e: PointerEvent) => {
        if (!this.isDragging) return;
        this.isDragging = false;
        document.removeEventListener("pointermove", this.onPointerMove);
        document.removeEventListener("pointerup", this.onPointerUp);
        const delta = e.clientX - this.dragStartX;
        if (Math.abs(delta) > 50) {
            this.advance(delta < 0 ? 1 : -1);
        } else {
            this.slideTo(this.currentIndex);
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
