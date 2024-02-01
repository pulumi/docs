package myproject;

import com.pulumi.Pulumi;
import com.pulumi.core.Output;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {
            // Create a Pulumi Config
            var config = ctx.config();

            // Retrieve the value of "myEnvironment" from the Pulumi Config
            var myValue = config.get("myEnvironment");

            // Export the value as a stack output named 'Value'
            ctx.export("Value", Output.of(myValue));
        });
    }
}