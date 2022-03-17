module github.com/pulumi/pulumi-hugo

go 1.16

require (
	github.com/pulumi/pulumi-hugo/themes/default v0.0.0-20211008162151-6e65a2068c3b // indirect
	github.com/pulumi/registry/themes/default v0.0.0-20220317160931-9cb625ae1ca6 // indirect
	github.com/pulumi/theme v0.0.0-20220315170852-d5df94840cfe // indirect
)

replace github.com/pulumi/pulumi-hugo/themes/default => ./themes/default
