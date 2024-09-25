import { Component, Prop, State, h } from "@stencil/core";
import { parseCookie } from "../../util/util";

@Component({
    tag: "pricing-cta",
    shadow: false,
})
export class pricingCta {
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
                <a class={this.buttonClass} href="https://app.pulumi.com/?create-organization=1" target="_blank">Create an Organization</a>
            );
        }

        return (
            <a class={this.buttonClass} href="https://app.pulumi.com/signup/" target="_blank">Sign Up</a>
        );
    }

}
