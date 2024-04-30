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

        var sqlServer = Output.of(Map.of(
            "name", "myDbServer",
            "ipAddress", "10.0.0.0/24"
        ));

        var database = Output.of(Map.of(
            "name", "myExampleDatabase",
            "engine", "sql-db"
        ));

        ctx.export("sqlServerName", sqlServer.applyValue(values -> {
            return values.get("name");
        }));

        ctx.export("databaseName", database.applyValue(values -> {
            return values.get("name");
        }));
    }
}