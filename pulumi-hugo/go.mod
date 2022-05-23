module github.com/pulumi/pulumi-hugo

go 1.16

require (
	github.com/pulumi/pulumi-hugo/themes/default v0.0.0-20220504042409-82f5a4588c0e // indirect
	github.com/pulumi/registry/themes/default v0.0.0-20220523130445-097f87b0f449 // indirect
	github.com/pulumi/theme v0.0.0-20220520223222-2dad01154364 // indirect
)

replace github.com/pulumi/pulumi-hugo/themes/default => ./themes/default
