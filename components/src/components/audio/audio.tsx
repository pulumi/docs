import { Component, h, Prop, Element, State } from "@stencil/core";

@Component({
    tag: "pulumi-audio",
    shadow: false
})
export class Audio {
    @Element()
    el: Element;

    @Prop()
    url: string;

    @Prop()
    playingText: string;

    @Prop()
    pausedText: string;

    @State()
    paused: boolean = true;

    @State()
    isLoading: boolean = false;

    @State()
    error: boolean = false;

    componentDidLoad() {
        const audio = this.getAudio();
        if (audio) {
            audio.volume = 1;
            audio.muted = false;
        }
        audio.addEventListener("pause", () => this.paused = true);
        audio.addEventListener("play", () => this.paused = false);
    }

    private toggleMute() {
        if (this.isLoading) {
            return;
        }

        const audio = this.getAudio();
        if (!audio.paused) {
            audio.pause();
            return;
        }

        this.isLoading = true;
        audio.play().then(() => {
            this.isLoading = false;
        }).catch(() => {
            this.error = true;
        });
    }

    private getAudio() {
        return this.el.querySelector("audio");
    }

    private renderError() {
        return <div class="audio-container"><div class="error-callout">Music Cannot Be Played</div></div>;
    }

    private renderAudio() {
        const text = this.paused ? this.pausedText : this.playingText;
        const icon = this.isLoading ? "fa-cog fa-spin" : "fas fa-music";
        return (
            <div class="audio-container" onClick={this.toggleMute.bind(this)}>
                <div class="audio-button"><i class={`fas ${icon}`}></i>{ text }</div>
                <audio preload="none" loop>
                    <source src={this.url} type="audio/mpeg" />
                </audio>
            </div>
        );
    }

    render() {
        return this.error ? this.renderError() : this.renderAudio();
    }
}
