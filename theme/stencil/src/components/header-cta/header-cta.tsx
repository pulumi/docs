import { Component, Prop, State, h } from "@stencil/core";
import { parseCookie } from "../../util/util";

@Component({
    tag: "header-cta",
    styleUrl: "header-cta.scss",
    shadow: false,
})
export class HeaderCta {
    @Prop()
    buttonClass = "";

    @State()
    loading = true;

    @State()
    isLoggedIn = false;

    componentWillRender() {
        try {
            const cookie = parseCookie();
            const userCookie = cookie["pulumi_web_user_info"] ?? "j:{}";
            const userInfo = JSON.parse(decodeURIComponent(userCookie).slice(2));

            if (userInfo && userInfo.userId && userInfo.userId !== "") {
                this.isLoggedIn = true;
            }
        } catch (e) {
            // Swallow the error and so the component shows the "Get Started" button.
        }

        this.loading = false;
    }

    render() {
        if (this.loading) {
            return;
        }

        if (this.isLoggedIn) {
            return(
                <a class={this.buttonClass} data-track="header-get-started-mobile" href="https://app.pulumi.com/signup/" target="_blank" rel="noopener noreferrer" title="Dashboard">Dashboard</a>
            );
        }

        return (
            <a class={this.buttonClass} data-track="header-get-started" href="/docs/get-started" title="Get Started">Get Started</a>
        );
    }

}
