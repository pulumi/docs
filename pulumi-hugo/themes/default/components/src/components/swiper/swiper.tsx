import { Component, Element, h, Prop, State, Method } from "@stencil/core";
import SwiperJS, { Autoplay, Navigation, SwiperOptions } from "swiper";

@Component({
    tag: "pulumi-swiper",
    shadow: false,
})
export class Swiper {
    @Element()
    el: Element;

    @Prop()
    speed = "300";

    @Prop()
    loop = false;

    @Prop()
    autoplay = false;

    @Prop()
    autoplayDelay = "3000";

    @Prop()
    navControls = false;

    @Prop()
    slides = "1";

    @Prop()
    centeredSlides = false;

    @Prop()
    initialSlide = "1";

    @Prop()
    direction: SwiperOptions["direction"] = "horizontal";

    @Prop()
    enableMouseEvents = true;

    @Prop()
    spaceBetween = "0";

    @State()
    swiperHash = Math.random().toString(5).substring(2, 15) + Math.random().toString(5).substring(2, 15);

    @State()
    containerClass: string;

    @State()
    nextBtnClass: string;

    @State()
    previousBtnClass: string;

    swiper: SwiperJS;

    componentWillLoad() {
        const modules = [];
        if (this.autoplay) {
            modules.push(Autoplay);
        }

        if (this.navControls) {
            modules.push(Navigation);
        }

        SwiperJS.use(modules);

        this.containerClass = `swiper-container-${this.swiperHash}`;
        this.nextBtnClass = `swiper-button-next-${this.swiperHash}`;
        this.previousBtnClass = `swiper-button-prev-${this.swiperHash}`;
    }

    componentDidLoad() {
        let autoplay: any = false;
        if (this.autoplay) {
            autoplay = {
                delay: parseInt(this.autoplayDelay),
                disableOnInteraction: true,
            };
        }

        let navigation: any = false;
        if (this.navControls) {
            navigation = {
                nextEl: `.swiper-button-next.${this.nextBtnClass}`,
                prevEl: `.swiper-button-prev.${this.previousBtnClass}`,
            };
        }

        const swipeContainer = this.el.querySelector(`.swiper-container.${this.containerClass}`) as HTMLElement;
        this.swiper = new SwiperJS(swipeContainer, {
            speed: parseInt(this.speed),
            direction: this.direction,
            loop: this.loop,
            centeredSlides: this.centeredSlides,
            initialSlide: parseInt(this.initialSlide),
            autoplay,
            navigation,
            slidesPerView: parseInt(this.slides),
            spaceBetween: parseInt(this.spaceBetween),
        });

        this.stopSwiper();

        if (this.autoplay) {
            this.swiper.autoplay.start();
            if (this.enableMouseEvents) {
                swipeContainer.addEventListener("mouseenter", this.stopSwiper.bind(this));
                swipeContainer.addEventListener("mouseleave", this.startSwiper.bind(this));
            }
        }
    }

    @Method()
    public stopSwiper() {
        this.swiper.autoplay.stop();
    }

    @Method()
    public startSwiper() {
        this.swiper.autoplay.start();
    }

    render() {
        return (
            <div class={`swiper-container ${this.containerClass}`}>
                <div class="swiper-wrapper">
                    <slot></slot>
                </div>

                {!this.navControls ? null :
                    <span>
                        <div class={`swiper-button-prev ${this.previousBtnClass}`}></div>
                        <div class={`swiper-button-next ${this.nextBtnClass}`}></div>
                    </span>
                }
            </div>
        );
    }
}
