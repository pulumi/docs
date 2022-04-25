module github.com/pulumi/pulumi-hugo

go 1.16

require (
	github.com/pulumi/pulumi-hugo/themes/default v0.0.0-20211008162151-6e65a2068c3b // indirect
	github.com/pulumi/registry/themes/default v0.0.0-20220421161604-afeb673c253d // indirect
	github.com/pulumi/theme v0.0.0-20220420205818-619ff0a78fb7 // indirect
)

replace github.com/pulumi/pulumi-hugo/themes/default => ./themes/default
