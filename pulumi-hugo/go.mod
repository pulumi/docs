module github.com/pulumi/pulumi-hugo

go 1.16

require (
	github.com/pulumi/pulumi-hugo/themes/default v0.0.0-20220504042409-82f5a4588c0e // indirect
	github.com/pulumi/registry/themes/default v0.0.0-20221216072715-e0a9f29d7c54 // indirect
	github.com/pulumi/theme v0.0.0-20221214194142-d255deee0790 // indirect
)

replace github.com/pulumi/pulumi-hugo/themes/default => ./themes/default
