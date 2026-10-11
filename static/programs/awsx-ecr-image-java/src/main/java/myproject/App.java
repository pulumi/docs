package myproject;

import com.pulumi.Context;
import com.pulumi.Pulumi;
import com.pulumi.awsx.ecr.Repository;
import com.pulumi.awsx.ecr.RepositoryArgs;
import com.pulumi.awsx.ecr.Image;
import com.pulumi.awsx.ecr.ImageArgs;

public class App {
    public static void main(String[] args) {
        Pulumi.run(App::stack);
    }

    public static void stack(Context ctx) {
        var repository = new Repository("repository", RepositoryArgs.builder()
            .forceDelete(true)
            .build());

        var image = new Image("image", ImageArgs.builder()
            .repositoryUrl(repository.url())
            .context("./app")
            .platform("linux/amd64")
            .build());

        ctx.export("url", repository.url());
    }
}
