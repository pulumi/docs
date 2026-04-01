package myproject;

import com.pulumi.Pulumi;
import com.pulumi.aws.acm.Certificate;
import com.pulumi.aws.acm.CertificateArgs;
import com.pulumi.aws.route53.Record;
import com.pulumi.aws.route53.RecordArgs;
import com.pulumi.aws.route53.Zone;
import com.pulumi.aws.route53.ZoneArgs;
import com.pulumi.core.Either;
import java.util.List;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {
            var zone = new Zone("zone",
                ZoneArgs.builder()
                    .name("example.com")
                    .build());

            var cert = new Certificate("cert",
                CertificateArgs.builder()
                    .domainName("example.com")
                    .validationMethod("DNS")
                    .build());

            // Using apply to access nested output values
            var certValidation = new Record("certValidationApply",
                RecordArgs.builder()
                    .name(cert.domainValidationOptions()
                        .applyValue(opts -> opts.get(0).resourceRecordName().get()))
                    .type(cert.domainValidationOptions()
                        .applyValue(opts -> Either.ofLeft(opts.get(0).resourceRecordType().get())))
                    .zoneId(zone.zoneId())
                    .ttl(60)
                    .records(cert.domainValidationOptions()
                        .applyValue(opts -> opts.get(0).resourceRecordValue().get())
                        .applyValue(String::valueOf)
                        .applyValue(List::of))
                    .build());
        });
    }
}
