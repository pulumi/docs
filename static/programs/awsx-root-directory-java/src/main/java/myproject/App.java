package myproject;

import com.pulumi.Context;
import com.pulumi.Pulumi;
import com.pulumi.deployment.Deployment;
import com.pulumi.awsx.ecr.Repository;
import com.pulumi.awsx.ecr.RepositoryArgs;
import com.pulumi.awsx.ecr.Image;
import com.pulumi.awsx.ecr.ImageArgs;
import java.nio.file.Paths;

public class App {
    public static void main(String[] args) {
        Pulumi.run(App::stack);
    }

    public static void stack(Context ctx) {
        var root = Deployment.getInstance().getRootDirectory();
        var cwd = System.getProperty("user.dir");
        var appPath = Paths.get(cwd).relativize(Paths.get(root, "app")).toString();

        var repository = new Repository("repository", RepositoryArgs.builder()
            .forceDelete(true)
            .build());

        var image = new Image("image", ImageArgs.builder()
            .repositoryUrl(repository.url())
            .context(appPath)
            .platform("linux/amd64")
            .build());

        ctx.export("url", repository.url());
    }
}
