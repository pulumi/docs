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

    @Prop()
    href = "https://app.pulumi.com/signup";

    @Prop()
    label = "Sign Up";

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
                <a class={this.buttonClass} href="https://app.pulumi.com/?utm_source=header-button" title="Dashboard">Dashboard</a>
            );
        }

        return (
            <a class={this.buttonClass} data-track="header-signup" data-role="cta-get-started" href={`${this.href}?utm_source=header-button`} title={this.label}>{this.label}</a>
        );
    }

}
