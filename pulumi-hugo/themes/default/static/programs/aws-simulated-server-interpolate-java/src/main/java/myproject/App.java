package myproject;

import com.pulumi.Context;
import com.pulumi.Pulumi;
import com.pulumi.core.Output;
import java.util.Map;

public class App {
    public static void main(String[] args) {
        Pulumi.run(App::stack);
    }

    public static void stack(Context ctx) {

        var webServer = Output.of(Map.of(
            "hostName", "www.mywebserver.com",
            "port", "8080"
        ));

        var url = Output.format("http://%s:%s/", webServer.hostName, webServer.port);

        ctx.export("serverUrl", url);
    }
}