import { Component, h, Prop } from "@stencil/core";
//import { Swiper } from "../swiper/swiper";
import SwiperJS, { Autoplay } from "swiper";

@Component({
    tag: "pulumi-slot-machine",
    styleUrl: "slot-machine.css",
    shadow: false,
})
export class SlotMachine {
    @Prop()
    leftImages: string;

    @Prop()
    centerImages: string;

    @Prop()
    rightImages: string;

    leftSwiper!: HTMLPulumiSwiperElement;
    centerSwiper!: HTMLPulumiSwiperElement;
    rightSwiper!: HTMLPulumiSwiperElement;

    componentWillLoad() {
        SwiperJS.use([ Autoplay ]);
    }

    componentDidLoad() {
        this.runSlotMachine()
    }

    private runSlotMachine() {
        (this.leftSwiper as any).stopSwiper();
        (this.centerSwiper as any).stopSwiper();
        (this.rightSwiper as any).stopSwiper();

        setTimeout(() => {
            (this.leftSwiper as any).startSwiper();
        }, 100);

        setTimeout(() => {
            (this.centerSwiper as any).startSwiper();
        }, 500);

        setTimeout(() => {
            (this.rightSwiper as any).startSwiper();
        }, 1000);

        setTimeout(() => {
            (this.leftSwiper as any).stopSwiper();
        }, 3000);

        setTimeout(() => {
            (this.centerSwiper as any).stopSwiper();
        }, 3500);

        setTimeout(() => {
            (this.rightSwiper as any).stopSwiper();
        }, 4000);

        setTimeout(() => {
            (this.leftSwiper as any).startSwiper();
            (this.centerSwiper as any).startSwiper();
            (this.rightSwiper as any).startSwiper();
            this.runSlotMachine();
        }, 7000)
    }

    private renderImageList(images: string[]) {
        return images.map((image) => {
            return(
                <pulumi-swipeable>
                    <img src={image} alt="" />
                </pulumi-swipeable>
            );
        });
    }

    render() {
        return (
            <ul>
                <li>
                    <pulumi-swiper
                        ref={(el) => this.leftSwiper = el}
                        direction="vertical"
                        slides={3}
                        centered-slides={true}
                        loop={true}
                        autoplay={true}
                        autoplayDelay={300}
                        speed={1000}
                        enable-mouse-events={false}
                        space-between={120}
                    >
                        {this.renderImageList(this.leftImages.split(","))}
                    </pulumi-swiper>
                </li>

                <li>
                    <pulumi-swiper
                        ref={(el) => this.centerSwiper = el}
                        direction="vertical"
                        slides={3}
                        centered-slides={true}
                        loop={true}
                        autoplay={true}
                        autoplayDelay={300}
                        speed={1000}
                        enable-mouse-events={false}
                        space-between={120}
                    >
                        {this.renderImageList(this.centerImages.split(","))}
                    </pulumi-swiper>
                </li>

                <li>
                    <pulumi-swiper
                        ref={(el) => this.rightSwiper = el}
                        direction="vertical"
                        slides={3}
                        centered-slides={true}
                        loop={true}
                        autoplay={true}
                        autoplayDelay={300}
                        speed={1000}
                        enable-mouse-events={false}
                        space-between={120}
                    >
                        {this.renderImageList(this.rightImages.split(","))}
                    </pulumi-swiper>
                </li>
            </ul>
        );
    }

}
