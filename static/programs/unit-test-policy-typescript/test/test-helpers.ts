import * as policy from "@pulumi/policy";

export function getEmptyOptions(): policy.PolicyResourceOptions {
    return {
        protect: false,
        ignoreChanges: [],
        aliases: [],
        customTimeouts: {
            createSeconds: 0,
            updateSeconds: 0,
            deleteSeconds: 0,
        },
        additionalSecretOutputs: [],
    };
}

export function getEmptyArgs(): policy.ResourceValidationArgs {
    return {
        type: "",
        props: {},
        urn: "unknown",
        name: "unknown",
        opts: getEmptyOptions(),
        isType: () => true,
        asType: () => undefined,
        getConfig: <T>() => <T>{},
    };
}

export const reportThrow = (message: string) => {
    throw message;
};

export function runResourcePolicy(resourcePolicy: policy.ResourceValidationPolicy, args: policy.ResourceValidationArgs, report = reportThrow) {
    const validations = Array.isArray(resourcePolicy.validateResource) ? resourcePolicy.validateResource : [resourcePolicy.validateResource];

    for (const validation of validations) {
        if (validation) {
            validation(args, report);
        }
    }
}
