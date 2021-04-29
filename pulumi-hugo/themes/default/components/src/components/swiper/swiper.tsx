import { Component, Element, h, Prop, State, Method } from "@stencil/core";
import SwiperJS, { Autoplay, Navigation } from "swiper";
import { AutoplayOptions } from "swiper/components/autoplay";
import { NavigationOptions } from "swiper/components/navigation";

@Component({
    tag: "pulumi-swiper",
    shadow: false,
})
export class Swiper {
    @Element()
    el: Element;

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

    @State()
    swiperID = Math.random().toString(5).substring(2, 15) + Math.random().toString(5).substring(2, 15);

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

        this.containerClass = `swiper-container-${this.swiperID}`;
        this.nextBtnClass = `swiper-button-next-${this.swiperID}`;
        this.previousBtnClass = `swiper-button-prev-${this.swiperID}`;
    }

    componentDidLoad() {

        const autoplayOptions: AutoplayOptions = {
            delay: this.autoplayDelay,
            disableOnInteraction: true,
        };

        let navigationOptions: NavigationOptions = {
            nextEl: `.swiper-button-next.${this.nextBtnClass}`,
            prevEl: `.swiper-button-prev.${this.previousBtnClass}`,
        };

        const swipeContainer = this.el.querySelector(`.swiper-container.${this.containerClass}`) as HTMLElement;
        this.swiper = new SwiperJS(swipeContainer, {
            speed: this.speed,
            direction: this.direction,
            loop: this.loop,
            centeredSlides: this.centeredSlides,
            initialSlide: this.initialSlide,
            autoplay: this.autoplay ? autoplayOptions : false,
            navigation: this.navControls ? navigationOptions : false,
            slidesPerView: this.slides,
            spaceBetween: this.spaceBetween,
        });

        if (this.autoplay) {
            this.startSwiper();

            if (this.enableMouseEvents) {
                swipeContainer.addEventListener("mouseenter", this.stopSwiper.bind(this));
                swipeContainer.addEventListener("mouseleave", this.startSwiper.bind(this));
            }
        }
    }

    @Method()
    public async stopSwiper() {
        if (this.autoplay) {
            this.swiper.autoplay.stop();
        }
    }

    @Method()
    public async startSwiper() {
        if (this.autoplay) {
            this.swiper.autoplay.start();
        }
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
