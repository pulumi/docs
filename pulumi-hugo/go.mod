module github.com/pulumi/pulumi-hugo

go 1.16

require (
	github.com/pulumi/pulumi-hugo/themes/default v0.0.0-20211008162151-6e65a2068c3b // indirect
	github.com/pulumi/registry/themes/default v0.0.0-20220503211841-283f5195c90d // indirect
	github.com/pulumi/theme v0.0.0-20220502173708-1436bd2df058 // indirect
)

replace github.com/pulumi/pulumi-hugo/themes/default => ./themes/default
