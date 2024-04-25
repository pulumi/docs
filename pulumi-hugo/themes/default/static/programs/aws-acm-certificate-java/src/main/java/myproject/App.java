package myproject;

import com.pulumi.Context;
import com.pulumi.Pulumi;
import com.pulumi.core.Output;
import com.pulumi.aws.acm.Certificate;
import com.pulumi.aws.acm.CertificateArgs;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {
            var cert = new Certificate("cert",
                CertificateArgs.builder()
                    .domainName("example")
                    .validationMethod("DNS")
                    .build());
        });
    }
}
