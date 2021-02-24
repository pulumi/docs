import { Component, Host, h, State, Prop } from "@stencil/core";
import { waitForWindowPropertyToExist } from "../../util/util";

@Component({
    tag: "pulumi-youtube-audio-player",
    styleUrl: "youtube-audio-player.css",
    shadow: false
})
export class YoutubeAudioPlayer {
    @Prop()
    videoId: string = "";

    @State()
    loading: boolean = true;

    @State()
    muted: boolean = true;

    @State()
    player: any;

    componentWillLoad() {
        const tag = document.createElement("script");
        tag.src = "https://www.youtube.com/iframe_api";
        const firstScriptTag = document.getElementsByTagName("script")[0];
        firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

        const self = this;
        waitForWindowPropertyToExist("YT", 6000).then((value) => {
            setTimeout(() => {
                self.player = self.onYouTubeIframeAPIReady(value);
                self.loading = false;
            }, 50);
        });
    }

    private onYouTubeIframeAPIReady(yt: any) {
        // @ts-ignore
        return new yt.Player("youtube-audio-player", {
          height: "0",
          width: "0",
          videoId: this.videoId,
          playerVars: { autoplay: 1, mute: 1 },
        });
    }

    private muteAudio() {
        this.player.mute();
        this.muted = true;
    }

    private playAudio() {
        this.player.unMute();
        this.muted = false;
    }

    private renderLoading() {
        return <p>
            <i class="fa fa-spinner fa-spin"></i>
        </p>;
    }

    private renderMuted() {
        return <a class="cursor-pointer" onClick={() => this.playAudio()}>
            <i class="fa fa-volume-off"></i>
        </a>;
    }

    private renderPlayingSound() {
        return <a class="cursor-pointer" onClick={() => this.muteAudio()}>
            <i class="fa fa-volume-up"></i>
        </a>;
    }

    private renderIcon() {
        return this.muted ? this.renderMuted() : this.renderPlayingSound();
    }

    render() {
        return (
            <Host>
                { this.loading ? this.renderLoading() : this.renderIcon() }
                <div id="youtube-audio-player"></div>
            </Host>
        );
    }

}
