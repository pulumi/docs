module github.com/pulumi/pulumi-hugo

go 1.16

require (
	github.com/pulumi/pulumi-hugo/themes/default v0.0.0-20220504042409-82f5a4588c0e // indirect
	github.com/pulumi/registry/themes/default v0.0.0-20221206055211-f2a3cdf03021 // indirect
	github.com/pulumi/theme v0.0.0-20221212193340-ce466294500c // indirect
)

replace github.com/pulumi/pulumi-hugo/themes/default => ./themes/default
