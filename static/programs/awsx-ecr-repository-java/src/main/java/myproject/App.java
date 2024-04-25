package myproject;

import com.pulumi.Pulumi;
import com.pulumi.awsx.ecr.Repository;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {
            var repository = new Repository("repository");

            ctx.export("url", repository.url());
        });
    }
}
