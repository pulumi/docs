module github.com/pulumi/pulumi-hugo

go 1.16

require (
	github.com/pulumi/pulumi-hugo/themes/default v0.0.0-20220504042409-82f5a4588c0e // indirect
	github.com/pulumi/registry/themes/default v0.0.0-20220520160733-be068f0ebeb1 // indirect
	github.com/pulumi/theme v0.0.0-20220523200601-35ae9cdab892 // indirect
)

replace github.com/pulumi/pulumi-hugo/themes/default => ./themes/default
