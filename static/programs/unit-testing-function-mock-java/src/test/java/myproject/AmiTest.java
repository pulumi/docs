package myproject;

import static org.junit.jupiter.api.Assertions.assertEquals;

import java.util.HashMap;
import java.util.Map;
import java.util.Optional;
import java.util.concurrent.CompletableFuture;

import com.pulumi.aws.ec2.Instance;
import com.pulumi.test.Mocks;
import com.pulumi.test.PulumiTest;
import com.pulumi.test.TestOptions;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.Test;

class MyMocks implements Mocks {
    @Override
    public CompletableFuture<ResourceResult> newResourceAsync(ResourceArgs args) {
        var state = new HashMap<>(args.inputs);
        return CompletableFuture.completedFuture(
            ResourceResult.of(Optional.of(args.name + "_id"), state)
        );
    }

    @Override
    public CompletableFuture<Map<String, Object>> callAsync(CallArgs args) {
        if ("aws:ec2/getAmi:getAmi".equals(args.token)) {
            return CompletableFuture.completedFuture(Map.of(
                "id", "ami-0eb1f3cdeeb8eed2a",
                "architecture", "x86_64"
            ));
        }
        return CompletableFuture.completedFuture(Map.of());
    }
}

class AmiTest {
    @AfterEach
    void cleanup() {
        PulumiTest.cleanup();
    }

    @Test
    void instanceUsesLookedUpAmi() {
        var result = PulumiTest
            .withMocks(new MyMocks())
            .withOptions(TestOptions.builder()
                // Project and stack names; they show up in mocked URNs.
                .projectName("project").stackName("stack").preview(false)
                .build())
            .runTest(App::stack);

        var instance = result.resources().stream()
            .filter(resource -> resource instanceof Instance)
            .map(resource -> (Instance) resource)
            .findFirst()
            .orElseThrow(() -> new AssertionError("the program created no EC2 instance"));

        assertEquals("ami-0eb1f3cdeeb8eed2a", PulumiTest.extractValue(instance.ami()));
    }
}
