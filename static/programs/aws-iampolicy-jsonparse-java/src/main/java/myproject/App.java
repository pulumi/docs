package myproject;

import com.pulumi.Pulumi;
import com.pulumi.core.Output;
import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;

import java.util.ArrayList;
import java.util.Map;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {
            var jsonIAMPolicy = Output.of("{\n" +
                "    \"Version\": \"2012-10-17\",\n" +
                "    \"Statement\": [\n" +
                "        {\n" +
                "            \"Sid\": \"VisualEditor0\",\n" +
                "            \"Effect\": \"Allow\",\n" +
                "            \"Action\": [\n" +
                "                \"s3:ListAllMyBuckets\",\n" +
                "                \"s3:GetBucketLocation\"\n" +
                "            ],\n" +
                "            \"Resource\": \"*\"\n" +
                "        },\n" +
                "        {\n" +
                "            \"Sid\": \"VisualEditor1\",\n" +
                "            \"Effect\": \"Allow\",\n" +
                "            \"Action\": \"s3:*\",\n" +
                "            \"Resource\": \"arn:aws:s3:::my-bucket\"\n" +
                "        }\n" +
                "    ]\n" +
                "}");

            // Parse the string output into a map and empty the policy's Statement list.
            var gson = new Gson();
            var policyWithNoStatements = jsonIAMPolicy.applyValue(json -> {
                Map<String, Object> policy = gson.fromJson(json, new TypeToken<Map<String, Object>>() {}.getType());
                policy.put("Statement", new ArrayList<>());
                return policy;
            });

            // Export the modified policy.
            ctx.export("policy", policyWithNoStatements);
        });
    }
}
