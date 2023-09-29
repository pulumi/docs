module github.com/pulumi/pulumi-hugo

go 1.16

replace github.com/pulumi/pulumi-hugo/themes/default => ./themes/default

require (
	github.com/pulumi/pulumi-hugo/themes/default v0.0.0-20220504042409-82f5a4588c0e // indirect
	github.com/pulumi/registry/themes/default v0.0.0-20230929193425-5c3ad6ef8ad6 // indirect
)
