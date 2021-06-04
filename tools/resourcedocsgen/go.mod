module github.com/pulumi/docs/tools/resourcedocsgen

go 1.16

require (
	github.com/golang/glog v0.0.0-20160126235308-23def4e6c14b
	github.com/pkg/errors v0.9.1
	github.com/pulumi/pulumi/pkg/v3 v3.3.1
	github.com/pulumi/pulumi/sdk/v3 v3.3.1
)

replace (
	github.com/Sirupsen/logrus => github.com/sirupsen/logrus v1.5.0
)
