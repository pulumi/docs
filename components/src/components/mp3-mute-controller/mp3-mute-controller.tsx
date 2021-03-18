import { Component, State, h, Prop } from "@stencil/core";

@Component({
    tag: "pulumi-mp3-mute-controller",
    shadow: false
})
export class Mp3MuteController {
    @Prop()
    file: string;

    @Prop()
    playingText: string;

    @Prop()
    pausedText: string;

    @Prop()
    audioElementId: string;

    @State()
    isPlaying = false;

    @State()
    muted: boolean = true;

    private toggleMute() {
        // Grab the audio element so we can manipulate the control attributes.
        const audio = document.getElementById(this.audioElementId) as HTMLAudioElement;

        // By default we do not autoplay the audio because many ad blocks (and browsers)
        // block auto-playing things because of ads. Instead we just start playing the audio
        // when the user "unmutes" the audio.
        if (!this.isPlaying) {
            audio.play();
            this.isPlaying = true;
        }

        if (this.muted) {
            audio.volume = 1;
            audio.muted = false;
            this.muted = false;
            return;
        }

        audio.muted = true;
        this.muted = true;
    }

    render() {
        const text = this.muted ? this.pausedText : this.playingText;
        return (
            <div class="mp3-mute-controller-container" onClick={this.toggleMute.bind(this)}>
                <div class="mp3-toggle-button"><i class="fas fa-music"></i>{ text }</div>
                <audio id={this.audioElementId} preload="none" loop>
                    <source src={this.file} type="audio/mpeg" />
                </audio>
            </div>
        );
    }
}
