package myproject;

import com.pulumi.Pulumi;
import com.pulumi.core.Output;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {
            // Create a Pulumi Config
            var config = ctx.config();

            // Retrieve the values of "myEnvironment" and "myPassword"
            var environment = config.get("myEnvironment");
            var password = config.getSecret("myPassword");

            // Export the values as a stack outputs
            ctx.export("Environment", Output.of(environment));
            ctx.export("Password", Output.of(password));
        });
    }
}