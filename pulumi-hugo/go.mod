module github.com/pulumi/pulumi-hugo

go 1.16

require (
	github.com/pulumi/pulumi-hugo/themes/default v0.0.0-20211008162151-6e65a2068c3b // indirect
	github.com/pulumi/registry/themes/default v0.0.0-20220307140935-2b5aa4ad1467 // indirect
	github.com/pulumi/theme v0.0.0-20220304222238-692dd9b11752 // indirect
)

replace github.com/pulumi/pulumi-hugo/themes/default => ./themes/default
