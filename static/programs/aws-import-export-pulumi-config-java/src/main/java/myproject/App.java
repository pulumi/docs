package myproject;

import com.pulumi.Pulumi;
import com.pulumi.core.Output;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {
            // Create a Pulumi Config
            var config = ctx.config();

            // Retrieve the values of "region" and "apiKey"
            var region = config.get("region");
            var apiKey = config.getSecret("apiKey");

            // Export the values as a stack outputs
            ctx.export("Region", Output.of(region));
            ctx.export("ApiKey", Output.of(apiKey));
        });
    }
}