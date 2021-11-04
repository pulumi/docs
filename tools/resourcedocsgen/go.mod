module github.com/pulumi/docs/tools/resourcedocsgen

go 1.16

require (
	github.com/ghodss/yaml v1.0.0
	github.com/golang/glog v0.0.0-20160126235308-23def4e6c14b
	github.com/pkg/errors v0.9.1
	github.com/pulumi/pulumi/pkg/v3 v3.7.1
	github.com/pulumi/pulumi/sdk/v3 v3.17.0
	github.com/spf13/cobra v1.2.1
	gopkg.in/yaml.v2 v2.4.0
)

replace (
	github.com/Sirupsen/logrus => github.com/sirupsen/logrus v1.5.0
	github.com/pulumi/pulumi/pkg/v3 => ../../../pulumi/pkg
	github.com/pulumi/pulumi/sdk/v3 => ../../../pulumi/sdk
)
