module github.com/pulumi/pulumi-hugo

go 1.16

require (
	github.com/pulumi/pulumi-hugo/themes/default v0.0.0-20220504042409-82f5a4588c0e // indirect
	github.com/pulumi/registry/themes/default v0.0.0-20220810014150-58449a252395 // indirect
	github.com/pulumi/theme v0.0.0-20220810160558-2c1c6f6d4417 // indirect
)

replace github.com/pulumi/pulumi-hugo/themes/default => ./themes/default
