module github.com/pulumi/pulumi-hugo

go 1.16

require (
	github.com/pulumi/pulumi-hugo/themes/default v0.0.0-20211008162151-6e65a2068c3b // indirect
	github.com/pulumi/registry/themes/default v0.0.0-20220317204921-3e1681097cf8 // indirect
	github.com/pulumi/theme v0.0.0-20220317180341-91d6648e25d4 // indirect
)

replace github.com/pulumi/pulumi-hugo/themes/default => ./themes/default
