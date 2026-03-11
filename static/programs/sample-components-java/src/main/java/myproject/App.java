package myproject;

import com.pulumi.Pulumi;
import com.pulumi.core.Output;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {
            final var pageHTML = "<h1>I love Pulumi!</h1>";

            var page = new StaticPage("my-static-page", new StaticPageArgs(
                Output.of(pageHTML)
            ), null);

            ctx.export("websiteURL", page.endpoint.applyValue(endpoint -> "http://" + endpoint));
        });
    }
}
