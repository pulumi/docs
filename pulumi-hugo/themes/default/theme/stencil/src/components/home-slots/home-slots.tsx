import { Host, Component, State, h, Prop } from "@stencil/core";

@Component({
    tag: "home-slots",
    styleUrl: "home-slots.scss",
    shadow: false,
})
export class HomeSlots {
    @Prop()
    leftItems: string = "";

    @Prop()
    centerItems: string = "";

    @Prop()
    rightItems: string = "";

    @Prop()
    imageClass: string = "";

    @State()
    columnOne: string[] = [];

    @State()
    columnOneRotator: NodeJS.Timeout;

    @State()
    columnTwo: string[] = [];

    @State()
    columnTwoRotator: NodeJS.Timeout;

    @State()
    columnThree: string[] = [];

    @State()
    columnThreeRotator: NodeJS.Timeout;

    componentDidLoad() {
        this.columnOne = this.shuffleArray(this.leftItems.split(","));
        this.columnTwo = this.shuffleArray(this.centerItems.split(","));
        this.columnThree = this.shuffleArray(this.rightItems.split(","));
        this.startRotators();
    }

    private shuffleArray(arr: string[]): string[] {
        for (let i = arr.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [arr[i], arr[j]] = [arr[j], arr[i]];
        }
        return arr;
    }

    private startRotators() {
        this.columnOneRotator = setInterval(() => this.incrementColumnOne(), 400);

        setTimeout(() => {
            this.columnTwoRotator = setInterval(() => this.incrementColumnTwo(), 400);
        }, 500);

        setTimeout(() => {
            this.columnThreeRotator = setInterval(() => this.incrementColumnThree(), 400);
        }, 1000);

        setTimeout(() => this.stopRotators(), 3000);
    }

    private stopRotators() {
        clearInterval(this.columnOneRotator);
        setTimeout(() => clearInterval(this.columnTwoRotator), 500);
        setTimeout(() => clearInterval(this.columnThreeRotator), 1000);

        setTimeout(() => this.startRotators(), 10000);
    }

    private incrementColumnOne() {
        this.columnOne = this.updateOrder(this.columnOne);
    }

    private incrementColumnTwo() {
        this.columnTwo = this.updateOrder(this.columnTwo);
    }

    private incrementColumnThree() {
        this.columnThree = this.updateOrder(this.columnThree);
    }

    private updateOrder(items: string[]): string[] {
        const newItems = [...items];
        const oldFirst = newItems.shift();
        newItems.push(oldFirst);
        return newItems;
    }

    render() {
        const itemOne = this.columnOne[0];
        const itemTwo = this.columnTwo[0];
        const itemThree = this.columnThree[0];
        return (
            <Host>
                <div>
                    <div class="slot-container">
                        <div class="item-container">
                            <img key={itemOne} class={this.imageClass} src={itemOne} />
                        </div>

                        <div class="separator-container">+</div>

                        <div class="item-container">
                            <img key={itemTwo} class={this.imageClass} src={itemTwo} />
                        </div>

                        <div class="separator-container">+</div>

                        <div class="item-container">
                            <img key={itemThree} class={this.imageClass} src={itemThree} />
                        </div>
                    </div>
                </div>
            </Host>
        );
    }

}
