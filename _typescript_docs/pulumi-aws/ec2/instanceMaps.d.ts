---
layout: typescript-reference
repo: pulumi-aws
subpath: ec2/instanceMaps.d.ts
---
export declare let instanceTypeArch: {
    [instanceType: string]: string;
};
export declare let regionArchLinuxAMI: {
    [region: string]: {
        [arch: string]: string;
    };
};
export declare function getLinuxAMI(instanceType: string): string;
