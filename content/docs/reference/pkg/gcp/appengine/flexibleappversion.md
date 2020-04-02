
---
title: "FlexibleAppVersion"
block_external_search_index: true
---

Flexible App Version resource to create a new version of flexible GAE Application. Based on Google Compute Engine,
the App Engine flexible environment automatically scales your app up and down while also balancing the load.
Learn about the differences between the standard environment and the flexible environment
at https://cloud.google.com/appengine/docs/the-appengine-environments.


To get more information about FlexibleAppVersion, see:

* [API documentation](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions)
* How-to Guides
    * [Official Documentation](https://cloud.google.com/appengine/docs/flexible)

> This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/app_engine_flexible_app_version.html.markdown.



## Create a FlexibleAppVersion Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/appengine/#FlexibleAppVersion">FlexibleAppVersion</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/appengine/#FlexibleAppVersionArgs">FlexibleAppVersionArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">FlexibleAppVersion</span><span class="p">(resource_name, opts=None, </span>api_config=None<span class="p">, </span>automatic_scaling=None<span class="p">, </span>beta_settings=None<span class="p">, </span>default_expiration=None<span class="p">, </span>delete_service_on_destroy=None<span class="p">, </span>deployment=None<span class="p">, </span>endpoints_api_service=None<span class="p">, </span>entrypoint=None<span class="p">, </span>env_variables=None<span class="p">, </span>inbound_services=None<span class="p">, </span>instance_class=None<span class="p">, </span>liveness_check=None<span class="p">, </span>manual_scaling=None<span class="p">, </span>network=None<span class="p">, </span>nobuild_files_regex=None<span class="p">, </span>noop_on_destroy=None<span class="p">, </span>project=None<span class="p">, </span>readiness_check=None<span class="p">, </span>resources=None<span class="p">, </span>runtime=None<span class="p">, </span>runtime_api_version=None<span class="p">, </span>runtime_channel=None<span class="p">, </span>runtime_main_executable_path=None<span class="p">, </span>service=None<span class="p">, </span>serving_status=None<span class="p">, </span>version_id=None<span class="p">, </span>vpc_access_connector=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewFlexibleAppVersion<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/appengine?tab=doc#FlexibleAppVersionArgs">FlexibleAppVersionArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/appengine?tab=doc#FlexibleAppVersion">FlexibleAppVersion</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Appengine.FlexibleAppVersion.html">FlexibleAppVersion</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.AppEngine.FlexibleAppVersionArgs.html">FlexibleAppVersionArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language nodejs %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resource.</dd>
    <dt class="property-optional" title="Optional">
        <span>args</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The arguments to use to populate this resource's properties.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

{{% choosable language python %}}
<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resource.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>
{{% /choosable %}}

{{% choosable language go %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resource.</dd>
    <dt class="property-optional" title="Optional">
        <span>args</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The arguments to use to populate this resource's properties.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

{{% choosable language csharp %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resource.</dd>
    <dt class="property-optional" title="Optional">
        <span>args</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The arguments to use to populate this resource's properties.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

#### Resource Arguments




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Api<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionapiconfig">Flexible<wbr>App<wbr>Version<wbr>Api<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Serving configuration for Google Cloud Endpoints.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Automatic<wbr>Scaling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionautomaticscaling">Flexible<wbr>App<wbr>Version<wbr>Automatic<wbr>Scaling<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Automatic scaling is based on request rate, response latencies, and other application metrics.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Beta<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}Metadata settings that are supplied to this version to enable beta runtime features.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Default<wbr>Expiration</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Duration that static files should be cached by web proxies and browsers. Only applicable if the corresponding
StaticFilesHandler does not specify its own expiration time.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Delete<wbr>Service<wbr>On<wbr>Destroy</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}If set to `true`, the service will be deleted if it is the last version.    
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Deployment</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversiondeployment">Flexible<wbr>App<wbr>Version<wbr>Deployment<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Code and application artifacts that make up this version.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Endpoints<wbr>Api<wbr>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionendpointsapiservice">Flexible<wbr>App<wbr>Version<wbr>Endpoints<wbr>Api<wbr>Service<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Code and application artifacts that make up this version.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Entrypoint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionentrypoint">Flexible<wbr>App<wbr>Version<wbr>Entrypoint<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}The entrypoint for the application.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Env<wbr>Variables</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}Environment variables available to the application. As these are not returned in the API request, Terraform will not
detect any changes made outside of the Terraform config.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Inbound<wbr>Services</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Before an application can receive email or XMPP messages, the application must be configured to enable the service.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Instance<wbr>Class</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Instance class that is used to run this version. Valid values are AutomaticScaling: F1, F2, F4, F4_1G ManualScaling: B1,
B2, B4, B8, B4_1G Defaults to F1 for AutomaticScaling and B1 for ManualScaling.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Liveness<wbr>Check</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionlivenesscheck">Flexible<wbr>App<wbr>Version<wbr>Liveness<wbr>Check<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}Health checking configuration for VM instances. Unhealthy instances are killed and replaced with new instances.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Manual<wbr>Scaling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionmanualscaling">Flexible<wbr>App<wbr>Version<wbr>Manual<wbr>Scaling<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A service with manual scaling runs continuously, allowing you to perform complex initialization and rely on the state of
its memory over time.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Network</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionnetwork">Flexible<wbr>App<wbr>Version<wbr>Network<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Extra network settings
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Nobuild<wbr>Files<wbr>Regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Files that match this pattern will not be built into this version. Only applicable for Go runtimes.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Noop<wbr>On<wbr>Destroy</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}If set to `true`, the application version will not be deleted.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Readiness<wbr>Check</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionreadinesscheck">Flexible<wbr>App<wbr>Version<wbr>Readiness<wbr>Check<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}Configures readiness health checking for instances. Unhealthy instances are not put into the backend traffic rotation.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resources</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionresources">Flexible<wbr>App<wbr>Version<wbr>Resources<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Machine resources for a version.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Runtime</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Desired runtime. Example python27.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Runtime<wbr>Api<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The version of the API in the given runtime environment. Please see the app.yaml reference for valid values at
https://cloud.google.com/appengine/docs/standard//config/appref
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Runtime<wbr>Channel</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The channel of the runtime to use. Only available for some runtimes.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Runtime<wbr>Main<wbr>Executable<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The path or name of the app's main executable.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}AppEngine service resource
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Serving<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Current serving status of this version. Only the versions with a SERVING status create instances and can be billed.
Defaults to SERVING.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Version<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Relative name of the version within the service. For example, 'v1'. Version names can contain only lowercase letters,
numbers, or hyphens. Reserved names,"default", "latest", and any name with the prefix "ah-".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vpc<wbr>Access<wbr>Connector</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionvpcaccessconnector">Flexible<wbr>App<wbr>Version<wbr>Vpc<wbr>Access<wbr>Connector<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Enables VPC connectivity for standard apps.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Api<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionapiconfig">*Flexible<wbr>App<wbr>Version<wbr>Api<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Serving configuration for Google Cloud Endpoints.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Automatic<wbr>Scaling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionautomaticscaling">*Flexible<wbr>App<wbr>Version<wbr>Automatic<wbr>Scaling</a></span>
    </dt>
    <dd>{{% md %}}Automatic scaling is based on request rate, response latencies, and other application metrics.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Beta<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}Metadata settings that are supplied to this version to enable beta runtime features.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Default<wbr>Expiration</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Duration that static files should be cached by web proxies and browsers. Only applicable if the corresponding
StaticFilesHandler does not specify its own expiration time.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Delete<wbr>Service<wbr>On<wbr>Destroy</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}If set to `true`, the service will be deleted if it is the last version.    
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Deployment</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversiondeployment">*Flexible<wbr>App<wbr>Version<wbr>Deployment</a></span>
    </dt>
    <dd>{{% md %}}Code and application artifacts that make up this version.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Endpoints<wbr>Api<wbr>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionendpointsapiservice">*Flexible<wbr>App<wbr>Version<wbr>Endpoints<wbr>Api<wbr>Service</a></span>
    </dt>
    <dd>{{% md %}}Code and application artifacts that make up this version.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Entrypoint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionentrypoint">*Flexible<wbr>App<wbr>Version<wbr>Entrypoint</a></span>
    </dt>
    <dd>{{% md %}}The entrypoint for the application.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Env<wbr>Variables</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}Environment variables available to the application. As these are not returned in the API request, Terraform will not
detect any changes made outside of the Terraform config.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Inbound<wbr>Services</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Before an application can receive email or XMPP messages, the application must be configured to enable the service.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Instance<wbr>Class</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Instance class that is used to run this version. Valid values are AutomaticScaling: F1, F2, F4, F4_1G ManualScaling: B1,
B2, B4, B8, B4_1G Defaults to F1 for AutomaticScaling and B1 for ManualScaling.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Liveness<wbr>Check</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionlivenesscheck">Flexible<wbr>App<wbr>Version<wbr>Liveness<wbr>Check</a></span>
    </dt>
    <dd>{{% md %}}Health checking configuration for VM instances. Unhealthy instances are killed and replaced with new instances.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Manual<wbr>Scaling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionmanualscaling">*Flexible<wbr>App<wbr>Version<wbr>Manual<wbr>Scaling</a></span>
    </dt>
    <dd>{{% md %}}A service with manual scaling runs continuously, allowing you to perform complex initialization and rely on the state of
its memory over time.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Network</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionnetwork">*Flexible<wbr>App<wbr>Version<wbr>Network</a></span>
    </dt>
    <dd>{{% md %}}Extra network settings
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Nobuild<wbr>Files<wbr>Regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Files that match this pattern will not be built into this version. Only applicable for Go runtimes.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Noop<wbr>On<wbr>Destroy</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}If set to `true`, the application version will not be deleted.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Readiness<wbr>Check</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionreadinesscheck">Flexible<wbr>App<wbr>Version<wbr>Readiness<wbr>Check</a></span>
    </dt>
    <dd>{{% md %}}Configures readiness health checking for instances. Unhealthy instances are not put into the backend traffic rotation.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resources</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionresources">*Flexible<wbr>App<wbr>Version<wbr>Resources</a></span>
    </dt>
    <dd>{{% md %}}Machine resources for a version.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Runtime</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Desired runtime. Example python27.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Runtime<wbr>Api<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The version of the API in the given runtime environment. Please see the app.yaml reference for valid values at
https://cloud.google.com/appengine/docs/standard//config/appref
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Runtime<wbr>Channel</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The channel of the runtime to use. Only available for some runtimes.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Runtime<wbr>Main<wbr>Executable<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The path or name of the app's main executable.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}AppEngine service resource
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Serving<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Current serving status of this version. Only the versions with a SERVING status create instances and can be billed.
Defaults to SERVING.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Version<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Relative name of the version within the service. For example, 'v1'. Version names can contain only lowercase letters,
numbers, or hyphens. Reserved names,"default", "latest", and any name with the prefix "ah-".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vpc<wbr>Access<wbr>Connector</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionvpcaccessconnector">*Flexible<wbr>App<wbr>Version<wbr>Vpc<wbr>Access<wbr>Connector</a></span>
    </dt>
    <dd>{{% md %}}Enables VPC connectivity for standard apps.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>api<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionapiconfig">Flexible<wbr>App<wbr>Version<wbr>Api<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}Serving configuration for Google Cloud Endpoints.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>automatic<wbr>Scaling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionautomaticscaling">Flexible<wbr>App<wbr>Version<wbr>Automatic<wbr>Scaling?</a></span>
    </dt>
    <dd>{{% md %}}Automatic scaling is based on request rate, response latencies, and other application metrics.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>beta<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}Metadata settings that are supplied to this version to enable beta runtime features.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>default<wbr>Expiration</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Duration that static files should be cached by web proxies and browsers. Only applicable if the corresponding
StaticFilesHandler does not specify its own expiration time.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>delete<wbr>Service<wbr>On<wbr>Destroy</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}If set to `true`, the service will be deleted if it is the last version.    
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>deployment</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversiondeployment">Flexible<wbr>App<wbr>Version<wbr>Deployment?</a></span>
    </dt>
    <dd>{{% md %}}Code and application artifacts that make up this version.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>endpoints<wbr>Api<wbr>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionendpointsapiservice">Flexible<wbr>App<wbr>Version<wbr>Endpoints<wbr>Api<wbr>Service?</a></span>
    </dt>
    <dd>{{% md %}}Code and application artifacts that make up this version.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>entrypoint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionentrypoint">Flexible<wbr>App<wbr>Version<wbr>Entrypoint?</a></span>
    </dt>
    <dd>{{% md %}}The entrypoint for the application.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>env<wbr>Variables</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}Environment variables available to the application. As these are not returned in the API request, Terraform will not
detect any changes made outside of the Terraform config.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>inbound<wbr>Services</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Before an application can receive email or XMPP messages, the application must be configured to enable the service.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>instance<wbr>Class</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Instance class that is used to run this version. Valid values are AutomaticScaling: F1, F2, F4, F4_1G ManualScaling: B1,
B2, B4, B8, B4_1G Defaults to F1 for AutomaticScaling and B1 for ManualScaling.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>liveness<wbr>Check</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionlivenesscheck">Flexible<wbr>App<wbr>Version<wbr>Liveness<wbr>Check</a></span>
    </dt>
    <dd>{{% md %}}Health checking configuration for VM instances. Unhealthy instances are killed and replaced with new instances.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>manual<wbr>Scaling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionmanualscaling">Flexible<wbr>App<wbr>Version<wbr>Manual<wbr>Scaling?</a></span>
    </dt>
    <dd>{{% md %}}A service with manual scaling runs continuously, allowing you to perform complex initialization and rely on the state of
its memory over time.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>network</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionnetwork">Flexible<wbr>App<wbr>Version<wbr>Network?</a></span>
    </dt>
    <dd>{{% md %}}Extra network settings
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>nobuild<wbr>Files<wbr>Regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Files that match this pattern will not be built into this version. Only applicable for Go runtimes.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>noop<wbr>On<wbr>Destroy</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}If set to `true`, the application version will not be deleted.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>readiness<wbr>Check</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionreadinesscheck">Flexible<wbr>App<wbr>Version<wbr>Readiness<wbr>Check</a></span>
    </dt>
    <dd>{{% md %}}Configures readiness health checking for instances. Unhealthy instances are not put into the backend traffic rotation.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resources</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionresources">Flexible<wbr>App<wbr>Version<wbr>Resources?</a></span>
    </dt>
    <dd>{{% md %}}Machine resources for a version.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>runtime</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Desired runtime. Example python27.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>runtime<wbr>Api<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The version of the API in the given runtime environment. Please see the app.yaml reference for valid values at
https://cloud.google.com/appengine/docs/standard//config/appref
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>runtime<wbr>Channel</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The channel of the runtime to use. Only available for some runtimes.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>runtime<wbr>Main<wbr>Executable<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The path or name of the app's main executable.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>service</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}AppEngine service resource
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>serving<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Current serving status of this version. Only the versions with a SERVING status create instances and can be billed.
Defaults to SERVING.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>version<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Relative name of the version within the service. For example, 'v1'. Version names can contain only lowercase letters,
numbers, or hyphens. Reserved names,"default", "latest", and any name with the prefix "ah-".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vpc<wbr>Access<wbr>Connector</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionvpcaccessconnector">Flexible<wbr>App<wbr>Version<wbr>Vpc<wbr>Access<wbr>Connector?</a></span>
    </dt>
    <dd>{{% md %}}Enables VPC connectivity for standard apps.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>api_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionapiconfig">Dict[Flexible<wbr>App<wbr>Version<wbr>Api<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}Serving configuration for Google Cloud Endpoints.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>automatic_<wbr>scaling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionautomaticscaling">Dict[Flexible<wbr>App<wbr>Version<wbr>Automatic<wbr>Scaling]</a></span>
    </dt>
    <dd>{{% md %}}Automatic scaling is based on request rate, response latencies, and other application metrics.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>beta_<wbr>settings</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}Metadata settings that are supplied to this version to enable beta runtime features.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>default_<wbr>expiration</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Duration that static files should be cached by web proxies and browsers. Only applicable if the corresponding
StaticFilesHandler does not specify its own expiration time.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>delete_<wbr>service_<wbr>on_<wbr>destroy</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If set to `true`, the service will be deleted if it is the last version.    
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>deployment</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversiondeployment">Dict[Flexible<wbr>App<wbr>Version<wbr>Deployment]</a></span>
    </dt>
    <dd>{{% md %}}Code and application artifacts that make up this version.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>endpoints_<wbr>api_<wbr>service</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionendpointsapiservice">Dict[Flexible<wbr>App<wbr>Version<wbr>Endpoints<wbr>Api<wbr>Service]</a></span>
    </dt>
    <dd>{{% md %}}Code and application artifacts that make up this version.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>entrypoint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionentrypoint">Dict[Flexible<wbr>App<wbr>Version<wbr>Entrypoint]</a></span>
    </dt>
    <dd>{{% md %}}The entrypoint for the application.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>env_<wbr>variables</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}Environment variables available to the application. As these are not returned in the API request, Terraform will not
detect any changes made outside of the Terraform config.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>inbound_<wbr>services</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Before an application can receive email or XMPP messages, the application must be configured to enable the service.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>instance_<wbr>class</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Instance class that is used to run this version. Valid values are AutomaticScaling: F1, F2, F4, F4_1G ManualScaling: B1,
B2, B4, B8, B4_1G Defaults to F1 for AutomaticScaling and B1 for ManualScaling.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>liveness_<wbr>check</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionlivenesscheck">Dict[Flexible<wbr>App<wbr>Version<wbr>Liveness<wbr>Check]</a></span>
    </dt>
    <dd>{{% md %}}Health checking configuration for VM instances. Unhealthy instances are killed and replaced with new instances.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>manual_<wbr>scaling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionmanualscaling">Dict[Flexible<wbr>App<wbr>Version<wbr>Manual<wbr>Scaling]</a></span>
    </dt>
    <dd>{{% md %}}A service with manual scaling runs continuously, allowing you to perform complex initialization and rely on the state of
its memory over time.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>network</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionnetwork">Dict[Flexible<wbr>App<wbr>Version<wbr>Network]</a></span>
    </dt>
    <dd>{{% md %}}Extra network settings
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>nobuild_<wbr>files_<wbr>regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Files that match this pattern will not be built into this version. Only applicable for Go runtimes.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>noop_<wbr>on_<wbr>destroy</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If set to `true`, the application version will not be deleted.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>readiness_<wbr>check</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionreadinesscheck">Dict[Flexible<wbr>App<wbr>Version<wbr>Readiness<wbr>Check]</a></span>
    </dt>
    <dd>{{% md %}}Configures readiness health checking for instances. Unhealthy instances are not put into the backend traffic rotation.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resources</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionresources">Dict[Flexible<wbr>App<wbr>Version<wbr>Resources]</a></span>
    </dt>
    <dd>{{% md %}}Machine resources for a version.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>runtime</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Desired runtime. Example python27.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>runtime_<wbr>api_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The version of the API in the given runtime environment. Please see the app.yaml reference for valid values at
https://cloud.google.com/appengine/docs/standard//config/appref
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>runtime_<wbr>channel</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The channel of the runtime to use. Only available for some runtimes.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>runtime_<wbr>main_<wbr>executable_<wbr>path</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The path or name of the app's main executable.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>service</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}AppEngine service resource
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>serving_<wbr>status</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Current serving status of this version. Only the versions with a SERVING status create instances and can be billed.
Defaults to SERVING.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>version_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Relative name of the version within the service. For example, 'v1'. Version names can contain only lowercase letters,
numbers, or hyphens. Reserved names,"default", "latest", and any name with the prefix "ah-".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vpc_<wbr>access_<wbr>connector</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionvpcaccessconnector">Dict[Flexible<wbr>App<wbr>Version<wbr>Vpc<wbr>Access<wbr>Connector]</a></span>
    </dt>
    <dd>{{% md %}}Enables VPC connectivity for standard apps.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## FlexibleAppVersion Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Api<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionapiconfig">Flexible<wbr>App<wbr>Version<wbr>Api<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}Serving configuration for Google Cloud Endpoints.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Automatic<wbr>Scaling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionautomaticscaling">Flexible<wbr>App<wbr>Version<wbr>Automatic<wbr>Scaling?</a></span>
    </dt>
    <dd>{{% md %}}Automatic scaling is based on request rate, response latencies, and other application metrics.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Beta<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}Metadata settings that are supplied to this version to enable beta runtime features.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Default<wbr>Expiration</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Duration that static files should be cached by web proxies and browsers. Only applicable if the corresponding
StaticFilesHandler does not specify its own expiration time.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Delete<wbr>Service<wbr>On<wbr>Destroy</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}If set to `true`, the service will be deleted if it is the last version.    
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Deployment</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversiondeployment">Flexible<wbr>App<wbr>Version<wbr>Deployment?</a></span>
    </dt>
    <dd>{{% md %}}Code and application artifacts that make up this version.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Endpoints<wbr>Api<wbr>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionendpointsapiservice">Flexible<wbr>App<wbr>Version<wbr>Endpoints<wbr>Api<wbr>Service?</a></span>
    </dt>
    <dd>{{% md %}}Code and application artifacts that make up this version.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Entrypoint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionentrypoint">Flexible<wbr>App<wbr>Version<wbr>Entrypoint?</a></span>
    </dt>
    <dd>{{% md %}}The entrypoint for the application.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Env<wbr>Variables</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}Environment variables available to the application. As these are not returned in the API request, Terraform will not
detect any changes made outside of the Terraform config.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Inbound<wbr>Services</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Before an application can receive email or XMPP messages, the application must be configured to enable the service.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Instance<wbr>Class</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Instance class that is used to run this version. Valid values are AutomaticScaling: F1, F2, F4, F4_1G ManualScaling: B1,
B2, B4, B8, B4_1G Defaults to F1 for AutomaticScaling and B1 for ManualScaling.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Liveness<wbr>Check</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionlivenesscheck">Flexible<wbr>App<wbr>Version<wbr>Liveness<wbr>Check</a></span>
    </dt>
    <dd>{{% md %}}Health checking configuration for VM instances. Unhealthy instances are killed and replaced with new instances.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Manual<wbr>Scaling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionmanualscaling">Flexible<wbr>App<wbr>Version<wbr>Manual<wbr>Scaling?</a></span>
    </dt>
    <dd>{{% md %}}A service with manual scaling runs continuously, allowing you to perform complex initialization and rely on the state of
its memory over time.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The identifier for this object. Format specified above.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Network</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionnetwork">Flexible<wbr>App<wbr>Version<wbr>Network?</a></span>
    </dt>
    <dd>{{% md %}}Extra network settings
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Nobuild<wbr>Files<wbr>Regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Files that match this pattern will not be built into this version. Only applicable for Go runtimes.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Noop<wbr>On<wbr>Destroy</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}If set to `true`, the application version will not be deleted.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Readiness<wbr>Check</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionreadinesscheck">Flexible<wbr>App<wbr>Version<wbr>Readiness<wbr>Check</a></span>
    </dt>
    <dd>{{% md %}}Configures readiness health checking for instances. Unhealthy instances are not put into the backend traffic rotation.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Resources</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionresources">Flexible<wbr>App<wbr>Version<wbr>Resources?</a></span>
    </dt>
    <dd>{{% md %}}Machine resources for a version.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Runtime</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Desired runtime. Example python27.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Runtime<wbr>Api<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The version of the API in the given runtime environment. Please see the app.yaml reference for valid values at
https://cloud.google.com/appengine/docs/standard//config/appref
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Runtime<wbr>Channel</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The channel of the runtime to use. Only available for some runtimes.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Runtime<wbr>Main<wbr>Executable<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The path or name of the app's main executable.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}AppEngine service resource
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Serving<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Current serving status of this version. Only the versions with a SERVING status create instances and can be billed.
Defaults to SERVING.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Version<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Relative name of the version within the service. For example, 'v1'. Version names can contain only lowercase letters,
numbers, or hyphens. Reserved names,"default", "latest", and any name with the prefix "ah-".
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Vpc<wbr>Access<wbr>Connector</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionvpcaccessconnector">Flexible<wbr>App<wbr>Version<wbr>Vpc<wbr>Access<wbr>Connector?</a></span>
    </dt>
    <dd>{{% md %}}Enables VPC connectivity for standard apps.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Api<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionapiconfig">*Flexible<wbr>App<wbr>Version<wbr>Api<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Serving configuration for Google Cloud Endpoints.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Automatic<wbr>Scaling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionautomaticscaling">*Flexible<wbr>App<wbr>Version<wbr>Automatic<wbr>Scaling</a></span>
    </dt>
    <dd>{{% md %}}Automatic scaling is based on request rate, response latencies, and other application metrics.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Beta<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}Metadata settings that are supplied to this version to enable beta runtime features.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Default<wbr>Expiration</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Duration that static files should be cached by web proxies and browsers. Only applicable if the corresponding
StaticFilesHandler does not specify its own expiration time.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Delete<wbr>Service<wbr>On<wbr>Destroy</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}If set to `true`, the service will be deleted if it is the last version.    
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Deployment</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversiondeployment">*Flexible<wbr>App<wbr>Version<wbr>Deployment</a></span>
    </dt>
    <dd>{{% md %}}Code and application artifacts that make up this version.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Endpoints<wbr>Api<wbr>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionendpointsapiservice">*Flexible<wbr>App<wbr>Version<wbr>Endpoints<wbr>Api<wbr>Service</a></span>
    </dt>
    <dd>{{% md %}}Code and application artifacts that make up this version.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Entrypoint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionentrypoint">*Flexible<wbr>App<wbr>Version<wbr>Entrypoint</a></span>
    </dt>
    <dd>{{% md %}}The entrypoint for the application.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Env<wbr>Variables</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}Environment variables available to the application. As these are not returned in the API request, Terraform will not
detect any changes made outside of the Terraform config.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Inbound<wbr>Services</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Before an application can receive email or XMPP messages, the application must be configured to enable the service.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Instance<wbr>Class</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Instance class that is used to run this version. Valid values are AutomaticScaling: F1, F2, F4, F4_1G ManualScaling: B1,
B2, B4, B8, B4_1G Defaults to F1 for AutomaticScaling and B1 for ManualScaling.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Liveness<wbr>Check</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionlivenesscheck">Flexible<wbr>App<wbr>Version<wbr>Liveness<wbr>Check</a></span>
    </dt>
    <dd>{{% md %}}Health checking configuration for VM instances. Unhealthy instances are killed and replaced with new instances.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Manual<wbr>Scaling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionmanualscaling">*Flexible<wbr>App<wbr>Version<wbr>Manual<wbr>Scaling</a></span>
    </dt>
    <dd>{{% md %}}A service with manual scaling runs continuously, allowing you to perform complex initialization and rely on the state of
its memory over time.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The identifier for this object. Format specified above.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Network</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionnetwork">*Flexible<wbr>App<wbr>Version<wbr>Network</a></span>
    </dt>
    <dd>{{% md %}}Extra network settings
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Nobuild<wbr>Files<wbr>Regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Files that match this pattern will not be built into this version. Only applicable for Go runtimes.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Noop<wbr>On<wbr>Destroy</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}If set to `true`, the application version will not be deleted.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Readiness<wbr>Check</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionreadinesscheck">Flexible<wbr>App<wbr>Version<wbr>Readiness<wbr>Check</a></span>
    </dt>
    <dd>{{% md %}}Configures readiness health checking for instances. Unhealthy instances are not put into the backend traffic rotation.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Resources</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionresources">*Flexible<wbr>App<wbr>Version<wbr>Resources</a></span>
    </dt>
    <dd>{{% md %}}Machine resources for a version.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Runtime</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Desired runtime. Example python27.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Runtime<wbr>Api<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The version of the API in the given runtime environment. Please see the app.yaml reference for valid values at
https://cloud.google.com/appengine/docs/standard//config/appref
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Runtime<wbr>Channel</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The channel of the runtime to use. Only available for some runtimes.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Runtime<wbr>Main<wbr>Executable<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The path or name of the app's main executable.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}AppEngine service resource
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Serving<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Current serving status of this version. Only the versions with a SERVING status create instances and can be billed.
Defaults to SERVING.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Version<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Relative name of the version within the service. For example, 'v1'. Version names can contain only lowercase letters,
numbers, or hyphens. Reserved names,"default", "latest", and any name with the prefix "ah-".
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Vpc<wbr>Access<wbr>Connector</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionvpcaccessconnector">*Flexible<wbr>App<wbr>Version<wbr>Vpc<wbr>Access<wbr>Connector</a></span>
    </dt>
    <dd>{{% md %}}Enables VPC connectivity for standard apps.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>api<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionapiconfig">Flexible<wbr>App<wbr>Version<wbr>Api<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}Serving configuration for Google Cloud Endpoints.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>automatic<wbr>Scaling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionautomaticscaling">Flexible<wbr>App<wbr>Version<wbr>Automatic<wbr>Scaling?</a></span>
    </dt>
    <dd>{{% md %}}Automatic scaling is based on request rate, response latencies, and other application metrics.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>beta<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}Metadata settings that are supplied to this version to enable beta runtime features.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>default<wbr>Expiration</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Duration that static files should be cached by web proxies and browsers. Only applicable if the corresponding
StaticFilesHandler does not specify its own expiration time.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>delete<wbr>Service<wbr>On<wbr>Destroy</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}If set to `true`, the service will be deleted if it is the last version.    
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>deployment</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversiondeployment">Flexible<wbr>App<wbr>Version<wbr>Deployment?</a></span>
    </dt>
    <dd>{{% md %}}Code and application artifacts that make up this version.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>endpoints<wbr>Api<wbr>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionendpointsapiservice">Flexible<wbr>App<wbr>Version<wbr>Endpoints<wbr>Api<wbr>Service?</a></span>
    </dt>
    <dd>{{% md %}}Code and application artifacts that make up this version.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>entrypoint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionentrypoint">Flexible<wbr>App<wbr>Version<wbr>Entrypoint?</a></span>
    </dt>
    <dd>{{% md %}}The entrypoint for the application.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>env<wbr>Variables</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}Environment variables available to the application. As these are not returned in the API request, Terraform will not
detect any changes made outside of the Terraform config.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>inbound<wbr>Services</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Before an application can receive email or XMPP messages, the application must be configured to enable the service.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>instance<wbr>Class</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Instance class that is used to run this version. Valid values are AutomaticScaling: F1, F2, F4, F4_1G ManualScaling: B1,
B2, B4, B8, B4_1G Defaults to F1 for AutomaticScaling and B1 for ManualScaling.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>liveness<wbr>Check</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionlivenesscheck">Flexible<wbr>App<wbr>Version<wbr>Liveness<wbr>Check</a></span>
    </dt>
    <dd>{{% md %}}Health checking configuration for VM instances. Unhealthy instances are killed and replaced with new instances.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>manual<wbr>Scaling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionmanualscaling">Flexible<wbr>App<wbr>Version<wbr>Manual<wbr>Scaling?</a></span>
    </dt>
    <dd>{{% md %}}A service with manual scaling runs continuously, allowing you to perform complex initialization and rely on the state of
its memory over time.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The identifier for this object. Format specified above.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>network</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionnetwork">Flexible<wbr>App<wbr>Version<wbr>Network?</a></span>
    </dt>
    <dd>{{% md %}}Extra network settings
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>nobuild<wbr>Files<wbr>Regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Files that match this pattern will not be built into this version. Only applicable for Go runtimes.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>noop<wbr>On<wbr>Destroy</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}If set to `true`, the application version will not be deleted.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>readiness<wbr>Check</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionreadinesscheck">Flexible<wbr>App<wbr>Version<wbr>Readiness<wbr>Check</a></span>
    </dt>
    <dd>{{% md %}}Configures readiness health checking for instances. Unhealthy instances are not put into the backend traffic rotation.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>resources</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionresources">Flexible<wbr>App<wbr>Version<wbr>Resources?</a></span>
    </dt>
    <dd>{{% md %}}Machine resources for a version.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>runtime</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Desired runtime. Example python27.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>runtime<wbr>Api<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The version of the API in the given runtime environment. Please see the app.yaml reference for valid values at
https://cloud.google.com/appengine/docs/standard//config/appref
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>runtime<wbr>Channel</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The channel of the runtime to use. Only available for some runtimes.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>runtime<wbr>Main<wbr>Executable<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The path or name of the app's main executable.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>service</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}AppEngine service resource
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>serving<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Current serving status of this version. Only the versions with a SERVING status create instances and can be billed.
Defaults to SERVING.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>version<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Relative name of the version within the service. For example, 'v1'. Version names can contain only lowercase letters,
numbers, or hyphens. Reserved names,"default", "latest", and any name with the prefix "ah-".
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>vpc<wbr>Access<wbr>Connector</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionvpcaccessconnector">Flexible<wbr>App<wbr>Version<wbr>Vpc<wbr>Access<wbr>Connector?</a></span>
    </dt>
    <dd>{{% md %}}Enables VPC connectivity for standard apps.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>api_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionapiconfig">Dict[Flexible<wbr>App<wbr>Version<wbr>Api<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}Serving configuration for Google Cloud Endpoints.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>automatic_<wbr>scaling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionautomaticscaling">Dict[Flexible<wbr>App<wbr>Version<wbr>Automatic<wbr>Scaling]</a></span>
    </dt>
    <dd>{{% md %}}Automatic scaling is based on request rate, response latencies, and other application metrics.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>beta_<wbr>settings</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}Metadata settings that are supplied to this version to enable beta runtime features.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>default_<wbr>expiration</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Duration that static files should be cached by web proxies and browsers. Only applicable if the corresponding
StaticFilesHandler does not specify its own expiration time.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>delete_<wbr>service_<wbr>on_<wbr>destroy</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If set to `true`, the service will be deleted if it is the last version.    
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>deployment</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversiondeployment">Dict[Flexible<wbr>App<wbr>Version<wbr>Deployment]</a></span>
    </dt>
    <dd>{{% md %}}Code and application artifacts that make up this version.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>endpoints_<wbr>api_<wbr>service</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionendpointsapiservice">Dict[Flexible<wbr>App<wbr>Version<wbr>Endpoints<wbr>Api<wbr>Service]</a></span>
    </dt>
    <dd>{{% md %}}Code and application artifacts that make up this version.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>entrypoint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionentrypoint">Dict[Flexible<wbr>App<wbr>Version<wbr>Entrypoint]</a></span>
    </dt>
    <dd>{{% md %}}The entrypoint for the application.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>env_<wbr>variables</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}Environment variables available to the application. As these are not returned in the API request, Terraform will not
detect any changes made outside of the Terraform config.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>inbound_<wbr>services</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Before an application can receive email or XMPP messages, the application must be configured to enable the service.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>instance_<wbr>class</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Instance class that is used to run this version. Valid values are AutomaticScaling: F1, F2, F4, F4_1G ManualScaling: B1,
B2, B4, B8, B4_1G Defaults to F1 for AutomaticScaling and B1 for ManualScaling.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>liveness_<wbr>check</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionlivenesscheck">Dict[Flexible<wbr>App<wbr>Version<wbr>Liveness<wbr>Check]</a></span>
    </dt>
    <dd>{{% md %}}Health checking configuration for VM instances. Unhealthy instances are killed and replaced with new instances.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>manual_<wbr>scaling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionmanualscaling">Dict[Flexible<wbr>App<wbr>Version<wbr>Manual<wbr>Scaling]</a></span>
    </dt>
    <dd>{{% md %}}A service with manual scaling runs continuously, allowing you to perform complex initialization and rely on the state of
its memory over time.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The identifier for this object. Format specified above.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>network</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionnetwork">Dict[Flexible<wbr>App<wbr>Version<wbr>Network]</a></span>
    </dt>
    <dd>{{% md %}}Extra network settings
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>nobuild_<wbr>files_<wbr>regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Files that match this pattern will not be built into this version. Only applicable for Go runtimes.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>noop_<wbr>on_<wbr>destroy</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If set to `true`, the application version will not be deleted.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>readiness_<wbr>check</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionreadinesscheck">Dict[Flexible<wbr>App<wbr>Version<wbr>Readiness<wbr>Check]</a></span>
    </dt>
    <dd>{{% md %}}Configures readiness health checking for instances. Unhealthy instances are not put into the backend traffic rotation.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>resources</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionresources">Dict[Flexible<wbr>App<wbr>Version<wbr>Resources]</a></span>
    </dt>
    <dd>{{% md %}}Machine resources for a version.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>runtime</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Desired runtime. Example python27.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>runtime_<wbr>api_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The version of the API in the given runtime environment. Please see the app.yaml reference for valid values at
https://cloud.google.com/appengine/docs/standard//config/appref
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>runtime_<wbr>channel</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The channel of the runtime to use. Only available for some runtimes.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>runtime_<wbr>main_<wbr>executable_<wbr>path</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The path or name of the app's main executable.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>service</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}AppEngine service resource
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>serving_<wbr>status</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Current serving status of this version. Only the versions with a SERVING status create instances and can be billed.
Defaults to SERVING.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>version_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Relative name of the version within the service. For example, 'v1'. Version names can contain only lowercase letters,
numbers, or hyphens. Reserved names,"default", "latest", and any name with the prefix "ah-".
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>vpc_<wbr>access_<wbr>connector</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionvpcaccessconnector">Dict[Flexible<wbr>App<wbr>Version<wbr>Vpc<wbr>Access<wbr>Connector]</a></span>
    </dt>
    <dd>{{% md %}}Enables VPC connectivity for standard apps.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing FlexibleAppVersion Resource

Get an existing FlexibleAppVersion resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/appengine/#FlexibleAppVersionState">FlexibleAppVersionState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/appengine/#FlexibleAppVersion">FlexibleAppVersion</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>api_config=None<span class="p">, </span>automatic_scaling=None<span class="p">, </span>beta_settings=None<span class="p">, </span>default_expiration=None<span class="p">, </span>delete_service_on_destroy=None<span class="p">, </span>deployment=None<span class="p">, </span>endpoints_api_service=None<span class="p">, </span>entrypoint=None<span class="p">, </span>env_variables=None<span class="p">, </span>inbound_services=None<span class="p">, </span>instance_class=None<span class="p">, </span>liveness_check=None<span class="p">, </span>manual_scaling=None<span class="p">, </span>name=None<span class="p">, </span>network=None<span class="p">, </span>nobuild_files_regex=None<span class="p">, </span>noop_on_destroy=None<span class="p">, </span>project=None<span class="p">, </span>readiness_check=None<span class="p">, </span>resources=None<span class="p">, </span>runtime=None<span class="p">, </span>runtime_api_version=None<span class="p">, </span>runtime_channel=None<span class="p">, </span>runtime_main_executable_path=None<span class="p">, </span>service=None<span class="p">, </span>serving_status=None<span class="p">, </span>version_id=None<span class="p">, </span>vpc_access_connector=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetFlexibleAppVersion<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/appengine?tab=doc#FlexibleAppVersionState">FlexibleAppVersionState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/appengine?tab=doc#FlexibleAppVersion">FlexibleAppVersion</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Appengine.FlexibleAppVersion.html">FlexibleAppVersion</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Appengine.FlexibleAppVersionState.html">FlexibleAppVersionState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language nodejs %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resulting resource.</dd>
    <dt class="property-required" title="Required">
        <span>id</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The <em>unique</em> provider ID of the resource to lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>state</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>Any extra arguments used during the lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

{{% choosable language python %}}
<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>resource_name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resulting resource.</dd>
    <dt class="property-required" title="Optional">
        <span>id</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The <em>unique</em> provider ID of the resource to lookup.</dd>
</dl>
{{% /choosable %}}

{{% choosable language go %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resulting resource.</dd>
    <dt class="property-required" title="Required">
        <span>id</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The <em>unique</em> provider ID of the resource to lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>state</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>Any extra arguments used during the lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

{{% choosable language csharp %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resulting resource.</dd>
    <dt class="property-required" title="Required">
        <span>id</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The <em>unique</em> provider ID of the resource to lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>state</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>Any extra arguments used during the lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

The following state arguments are supported:



{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Api<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionapiconfig">Flexible<wbr>App<wbr>Version<wbr>Api<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Serving configuration for Google Cloud Endpoints.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Automatic<wbr>Scaling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionautomaticscaling">Flexible<wbr>App<wbr>Version<wbr>Automatic<wbr>Scaling<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Automatic scaling is based on request rate, response latencies, and other application metrics.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Beta<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}Metadata settings that are supplied to this version to enable beta runtime features.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Default<wbr>Expiration</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Duration that static files should be cached by web proxies and browsers. Only applicable if the corresponding
StaticFilesHandler does not specify its own expiration time.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Delete<wbr>Service<wbr>On<wbr>Destroy</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}If set to `true`, the service will be deleted if it is the last version.    
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Deployment</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversiondeployment">Flexible<wbr>App<wbr>Version<wbr>Deployment<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Code and application artifacts that make up this version.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Endpoints<wbr>Api<wbr>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionendpointsapiservice">Flexible<wbr>App<wbr>Version<wbr>Endpoints<wbr>Api<wbr>Service<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Code and application artifacts that make up this version.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Entrypoint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionentrypoint">Flexible<wbr>App<wbr>Version<wbr>Entrypoint<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}The entrypoint for the application.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Env<wbr>Variables</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}Environment variables available to the application. As these are not returned in the API request, Terraform will not
detect any changes made outside of the Terraform config.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Inbound<wbr>Services</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Before an application can receive email or XMPP messages, the application must be configured to enable the service.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Instance<wbr>Class</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Instance class that is used to run this version. Valid values are AutomaticScaling: F1, F2, F4, F4_1G ManualScaling: B1,
B2, B4, B8, B4_1G Defaults to F1 for AutomaticScaling and B1 for ManualScaling.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Liveness<wbr>Check</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionlivenesscheck">Flexible<wbr>App<wbr>Version<wbr>Liveness<wbr>Check<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Health checking configuration for VM instances. Unhealthy instances are killed and replaced with new instances.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Manual<wbr>Scaling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionmanualscaling">Flexible<wbr>App<wbr>Version<wbr>Manual<wbr>Scaling<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A service with manual scaling runs continuously, allowing you to perform complex initialization and rely on the state of
its memory over time.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The identifier for this object. Format specified above.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Network</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionnetwork">Flexible<wbr>App<wbr>Version<wbr>Network<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Extra network settings
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Nobuild<wbr>Files<wbr>Regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Files that match this pattern will not be built into this version. Only applicable for Go runtimes.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Noop<wbr>On<wbr>Destroy</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}If set to `true`, the application version will not be deleted.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Readiness<wbr>Check</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionreadinesscheck">Flexible<wbr>App<wbr>Version<wbr>Readiness<wbr>Check<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Configures readiness health checking for instances. Unhealthy instances are not put into the backend traffic rotation.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resources</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionresources">Flexible<wbr>App<wbr>Version<wbr>Resources<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Machine resources for a version.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Runtime</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Desired runtime. Example python27.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Runtime<wbr>Api<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The version of the API in the given runtime environment. Please see the app.yaml reference for valid values at
https://cloud.google.com/appengine/docs/standard//config/appref
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Runtime<wbr>Channel</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The channel of the runtime to use. Only available for some runtimes.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Runtime<wbr>Main<wbr>Executable<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The path or name of the app's main executable.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}AppEngine service resource
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Serving<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Current serving status of this version. Only the versions with a SERVING status create instances and can be billed.
Defaults to SERVING.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Version<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Relative name of the version within the service. For example, 'v1'. Version names can contain only lowercase letters,
numbers, or hyphens. Reserved names,"default", "latest", and any name with the prefix "ah-".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vpc<wbr>Access<wbr>Connector</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionvpcaccessconnector">Flexible<wbr>App<wbr>Version<wbr>Vpc<wbr>Access<wbr>Connector<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Enables VPC connectivity for standard apps.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Api<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionapiconfig">*Flexible<wbr>App<wbr>Version<wbr>Api<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Serving configuration for Google Cloud Endpoints.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Automatic<wbr>Scaling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionautomaticscaling">*Flexible<wbr>App<wbr>Version<wbr>Automatic<wbr>Scaling</a></span>
    </dt>
    <dd>{{% md %}}Automatic scaling is based on request rate, response latencies, and other application metrics.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Beta<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}Metadata settings that are supplied to this version to enable beta runtime features.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Default<wbr>Expiration</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Duration that static files should be cached by web proxies and browsers. Only applicable if the corresponding
StaticFilesHandler does not specify its own expiration time.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Delete<wbr>Service<wbr>On<wbr>Destroy</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}If set to `true`, the service will be deleted if it is the last version.    
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Deployment</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversiondeployment">*Flexible<wbr>App<wbr>Version<wbr>Deployment</a></span>
    </dt>
    <dd>{{% md %}}Code and application artifacts that make up this version.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Endpoints<wbr>Api<wbr>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionendpointsapiservice">*Flexible<wbr>App<wbr>Version<wbr>Endpoints<wbr>Api<wbr>Service</a></span>
    </dt>
    <dd>{{% md %}}Code and application artifacts that make up this version.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Entrypoint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionentrypoint">*Flexible<wbr>App<wbr>Version<wbr>Entrypoint</a></span>
    </dt>
    <dd>{{% md %}}The entrypoint for the application.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Env<wbr>Variables</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}Environment variables available to the application. As these are not returned in the API request, Terraform will not
detect any changes made outside of the Terraform config.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Inbound<wbr>Services</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Before an application can receive email or XMPP messages, the application must be configured to enable the service.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Instance<wbr>Class</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Instance class that is used to run this version. Valid values are AutomaticScaling: F1, F2, F4, F4_1G ManualScaling: B1,
B2, B4, B8, B4_1G Defaults to F1 for AutomaticScaling and B1 for ManualScaling.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Liveness<wbr>Check</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionlivenesscheck">*Flexible<wbr>App<wbr>Version<wbr>Liveness<wbr>Check</a></span>
    </dt>
    <dd>{{% md %}}Health checking configuration for VM instances. Unhealthy instances are killed and replaced with new instances.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Manual<wbr>Scaling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionmanualscaling">*Flexible<wbr>App<wbr>Version<wbr>Manual<wbr>Scaling</a></span>
    </dt>
    <dd>{{% md %}}A service with manual scaling runs continuously, allowing you to perform complex initialization and rely on the state of
its memory over time.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The identifier for this object. Format specified above.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Network</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionnetwork">*Flexible<wbr>App<wbr>Version<wbr>Network</a></span>
    </dt>
    <dd>{{% md %}}Extra network settings
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Nobuild<wbr>Files<wbr>Regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Files that match this pattern will not be built into this version. Only applicable for Go runtimes.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Noop<wbr>On<wbr>Destroy</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}If set to `true`, the application version will not be deleted.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Readiness<wbr>Check</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionreadinesscheck">*Flexible<wbr>App<wbr>Version<wbr>Readiness<wbr>Check</a></span>
    </dt>
    <dd>{{% md %}}Configures readiness health checking for instances. Unhealthy instances are not put into the backend traffic rotation.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resources</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionresources">*Flexible<wbr>App<wbr>Version<wbr>Resources</a></span>
    </dt>
    <dd>{{% md %}}Machine resources for a version.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Runtime</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Desired runtime. Example python27.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Runtime<wbr>Api<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The version of the API in the given runtime environment. Please see the app.yaml reference for valid values at
https://cloud.google.com/appengine/docs/standard//config/appref
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Runtime<wbr>Channel</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The channel of the runtime to use. Only available for some runtimes.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Runtime<wbr>Main<wbr>Executable<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The path or name of the app's main executable.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}AppEngine service resource
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Serving<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Current serving status of this version. Only the versions with a SERVING status create instances and can be billed.
Defaults to SERVING.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Version<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Relative name of the version within the service. For example, 'v1'. Version names can contain only lowercase letters,
numbers, or hyphens. Reserved names,"default", "latest", and any name with the prefix "ah-".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vpc<wbr>Access<wbr>Connector</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionvpcaccessconnector">*Flexible<wbr>App<wbr>Version<wbr>Vpc<wbr>Access<wbr>Connector</a></span>
    </dt>
    <dd>{{% md %}}Enables VPC connectivity for standard apps.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>api<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionapiconfig">Flexible<wbr>App<wbr>Version<wbr>Api<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}Serving configuration for Google Cloud Endpoints.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>automatic<wbr>Scaling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionautomaticscaling">Flexible<wbr>App<wbr>Version<wbr>Automatic<wbr>Scaling?</a></span>
    </dt>
    <dd>{{% md %}}Automatic scaling is based on request rate, response latencies, and other application metrics.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>beta<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}Metadata settings that are supplied to this version to enable beta runtime features.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>default<wbr>Expiration</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Duration that static files should be cached by web proxies and browsers. Only applicable if the corresponding
StaticFilesHandler does not specify its own expiration time.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>delete<wbr>Service<wbr>On<wbr>Destroy</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}If set to `true`, the service will be deleted if it is the last version.    
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>deployment</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversiondeployment">Flexible<wbr>App<wbr>Version<wbr>Deployment?</a></span>
    </dt>
    <dd>{{% md %}}Code and application artifacts that make up this version.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>endpoints<wbr>Api<wbr>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionendpointsapiservice">Flexible<wbr>App<wbr>Version<wbr>Endpoints<wbr>Api<wbr>Service?</a></span>
    </dt>
    <dd>{{% md %}}Code and application artifacts that make up this version.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>entrypoint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionentrypoint">Flexible<wbr>App<wbr>Version<wbr>Entrypoint?</a></span>
    </dt>
    <dd>{{% md %}}The entrypoint for the application.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>env<wbr>Variables</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}Environment variables available to the application. As these are not returned in the API request, Terraform will not
detect any changes made outside of the Terraform config.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>inbound<wbr>Services</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Before an application can receive email or XMPP messages, the application must be configured to enable the service.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>instance<wbr>Class</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Instance class that is used to run this version. Valid values are AutomaticScaling: F1, F2, F4, F4_1G ManualScaling: B1,
B2, B4, B8, B4_1G Defaults to F1 for AutomaticScaling and B1 for ManualScaling.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>liveness<wbr>Check</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionlivenesscheck">Flexible<wbr>App<wbr>Version<wbr>Liveness<wbr>Check?</a></span>
    </dt>
    <dd>{{% md %}}Health checking configuration for VM instances. Unhealthy instances are killed and replaced with new instances.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>manual<wbr>Scaling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionmanualscaling">Flexible<wbr>App<wbr>Version<wbr>Manual<wbr>Scaling?</a></span>
    </dt>
    <dd>{{% md %}}A service with manual scaling runs continuously, allowing you to perform complex initialization and rely on the state of
its memory over time.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The identifier for this object. Format specified above.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>network</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionnetwork">Flexible<wbr>App<wbr>Version<wbr>Network?</a></span>
    </dt>
    <dd>{{% md %}}Extra network settings
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>nobuild<wbr>Files<wbr>Regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Files that match this pattern will not be built into this version. Only applicable for Go runtimes.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>noop<wbr>On<wbr>Destroy</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}If set to `true`, the application version will not be deleted.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>readiness<wbr>Check</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionreadinesscheck">Flexible<wbr>App<wbr>Version<wbr>Readiness<wbr>Check?</a></span>
    </dt>
    <dd>{{% md %}}Configures readiness health checking for instances. Unhealthy instances are not put into the backend traffic rotation.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resources</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionresources">Flexible<wbr>App<wbr>Version<wbr>Resources?</a></span>
    </dt>
    <dd>{{% md %}}Machine resources for a version.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>runtime</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Desired runtime. Example python27.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>runtime<wbr>Api<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The version of the API in the given runtime environment. Please see the app.yaml reference for valid values at
https://cloud.google.com/appengine/docs/standard//config/appref
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>runtime<wbr>Channel</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The channel of the runtime to use. Only available for some runtimes.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>runtime<wbr>Main<wbr>Executable<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The path or name of the app's main executable.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>service</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}AppEngine service resource
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>serving<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Current serving status of this version. Only the versions with a SERVING status create instances and can be billed.
Defaults to SERVING.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>version<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Relative name of the version within the service. For example, 'v1'. Version names can contain only lowercase letters,
numbers, or hyphens. Reserved names,"default", "latest", and any name with the prefix "ah-".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vpc<wbr>Access<wbr>Connector</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionvpcaccessconnector">Flexible<wbr>App<wbr>Version<wbr>Vpc<wbr>Access<wbr>Connector?</a></span>
    </dt>
    <dd>{{% md %}}Enables VPC connectivity for standard apps.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>api_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionapiconfig">Dict[Flexible<wbr>App<wbr>Version<wbr>Api<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}Serving configuration for Google Cloud Endpoints.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>automatic_<wbr>scaling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionautomaticscaling">Dict[Flexible<wbr>App<wbr>Version<wbr>Automatic<wbr>Scaling]</a></span>
    </dt>
    <dd>{{% md %}}Automatic scaling is based on request rate, response latencies, and other application metrics.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>beta_<wbr>settings</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}Metadata settings that are supplied to this version to enable beta runtime features.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>default_<wbr>expiration</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Duration that static files should be cached by web proxies and browsers. Only applicable if the corresponding
StaticFilesHandler does not specify its own expiration time.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>delete_<wbr>service_<wbr>on_<wbr>destroy</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If set to `true`, the service will be deleted if it is the last version.    
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>deployment</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversiondeployment">Dict[Flexible<wbr>App<wbr>Version<wbr>Deployment]</a></span>
    </dt>
    <dd>{{% md %}}Code and application artifacts that make up this version.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>endpoints_<wbr>api_<wbr>service</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionendpointsapiservice">Dict[Flexible<wbr>App<wbr>Version<wbr>Endpoints<wbr>Api<wbr>Service]</a></span>
    </dt>
    <dd>{{% md %}}Code and application artifacts that make up this version.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>entrypoint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionentrypoint">Dict[Flexible<wbr>App<wbr>Version<wbr>Entrypoint]</a></span>
    </dt>
    <dd>{{% md %}}The entrypoint for the application.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>env_<wbr>variables</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}Environment variables available to the application. As these are not returned in the API request, Terraform will not
detect any changes made outside of the Terraform config.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>inbound_<wbr>services</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Before an application can receive email or XMPP messages, the application must be configured to enable the service.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>instance_<wbr>class</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Instance class that is used to run this version. Valid values are AutomaticScaling: F1, F2, F4, F4_1G ManualScaling: B1,
B2, B4, B8, B4_1G Defaults to F1 for AutomaticScaling and B1 for ManualScaling.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>liveness_<wbr>check</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionlivenesscheck">Dict[Flexible<wbr>App<wbr>Version<wbr>Liveness<wbr>Check]</a></span>
    </dt>
    <dd>{{% md %}}Health checking configuration for VM instances. Unhealthy instances are killed and replaced with new instances.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>manual_<wbr>scaling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionmanualscaling">Dict[Flexible<wbr>App<wbr>Version<wbr>Manual<wbr>Scaling]</a></span>
    </dt>
    <dd>{{% md %}}A service with manual scaling runs continuously, allowing you to perform complex initialization and rely on the state of
its memory over time.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The identifier for this object. Format specified above.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>network</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionnetwork">Dict[Flexible<wbr>App<wbr>Version<wbr>Network]</a></span>
    </dt>
    <dd>{{% md %}}Extra network settings
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>nobuild_<wbr>files_<wbr>regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Files that match this pattern will not be built into this version. Only applicable for Go runtimes.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>noop_<wbr>on_<wbr>destroy</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If set to `true`, the application version will not be deleted.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>readiness_<wbr>check</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionreadinesscheck">Dict[Flexible<wbr>App<wbr>Version<wbr>Readiness<wbr>Check]</a></span>
    </dt>
    <dd>{{% md %}}Configures readiness health checking for instances. Unhealthy instances are not put into the backend traffic rotation.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resources</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionresources">Dict[Flexible<wbr>App<wbr>Version<wbr>Resources]</a></span>
    </dt>
    <dd>{{% md %}}Machine resources for a version.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>runtime</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Desired runtime. Example python27.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>runtime_<wbr>api_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The version of the API in the given runtime environment. Please see the app.yaml reference for valid values at
https://cloud.google.com/appengine/docs/standard//config/appref
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>runtime_<wbr>channel</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The channel of the runtime to use. Only available for some runtimes.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>runtime_<wbr>main_<wbr>executable_<wbr>path</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The path or name of the app's main executable.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>service</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}AppEngine service resource
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>serving_<wbr>status</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Current serving status of this version. Only the versions with a SERVING status create instances and can be billed.
Defaults to SERVING.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>version_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Relative name of the version within the service. For example, 'v1'. Version names can contain only lowercase letters,
numbers, or hyphens. Reserved names,"default", "latest", and any name with the prefix "ah-".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vpc_<wbr>access_<wbr>connector</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionvpcaccessconnector">Dict[Flexible<wbr>App<wbr>Version<wbr>Vpc<wbr>Access<wbr>Connector]</a></span>
    </dt>
    <dd>{{% md %}}Enables VPC connectivity for standard apps.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Flexible<wbr>App<wbr>Version<wbr>Api<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#FlexibleAppVersionApiConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#FlexibleAppVersionApiConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/appengine?tab=doc#FlexibleAppVersionApiConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/appengine?tab=doc#FlexibleAppVersionApiConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Auth<wbr>Fail<wbr>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Login</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Script</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Security<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Auth<wbr>Fail<wbr>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Login</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Script</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Security<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>auth<wbr>Fail<wbr>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>login</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>script</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>security<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>auth<wbr>Fail<wbr>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>login</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>script</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>security<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>url</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Flexible<wbr>App<wbr>Version<wbr>Automatic<wbr>Scaling</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#FlexibleAppVersionAutomaticScaling">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#FlexibleAppVersionAutomaticScaling">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/appengine?tab=doc#FlexibleAppVersionAutomaticScalingArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/appengine?tab=doc#FlexibleAppVersionAutomaticScalingOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Cool<wbr>Down<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Cpu<wbr>Utilization</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionautomaticscalingcpuutilization">Flexible<wbr>App<wbr>Version<wbr>Automatic<wbr>Scaling<wbr>Cpu<wbr>Utilization<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disk<wbr>Utilization</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionautomaticscalingdiskutilization">Flexible<wbr>App<wbr>Version<wbr>Automatic<wbr>Scaling<wbr>Disk<wbr>Utilization<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Concurrent<wbr>Requests</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Idle<wbr>Instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Pending<wbr>Latency</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Total<wbr>Instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Min<wbr>Idle<wbr>Instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Min<wbr>Pending<wbr>Latency</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Min<wbr>Total<wbr>Instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Network<wbr>Utilization</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionautomaticscalingnetworkutilization">Flexible<wbr>App<wbr>Version<wbr>Automatic<wbr>Scaling<wbr>Network<wbr>Utilization<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Request<wbr>Utilization</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionautomaticscalingrequestutilization">Flexible<wbr>App<wbr>Version<wbr>Automatic<wbr>Scaling<wbr>Request<wbr>Utilization<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Cool<wbr>Down<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Cpu<wbr>Utilization</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionautomaticscalingcpuutilization">Flexible<wbr>App<wbr>Version<wbr>Automatic<wbr>Scaling<wbr>Cpu<wbr>Utilization</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disk<wbr>Utilization</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionautomaticscalingdiskutilization">*Flexible<wbr>App<wbr>Version<wbr>Automatic<wbr>Scaling<wbr>Disk<wbr>Utilization</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Concurrent<wbr>Requests</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Idle<wbr>Instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Pending<wbr>Latency</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Total<wbr>Instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Min<wbr>Idle<wbr>Instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Min<wbr>Pending<wbr>Latency</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Min<wbr>Total<wbr>Instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Network<wbr>Utilization</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionautomaticscalingnetworkutilization">*Flexible<wbr>App<wbr>Version<wbr>Automatic<wbr>Scaling<wbr>Network<wbr>Utilization</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Request<wbr>Utilization</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionautomaticscalingrequestutilization">*Flexible<wbr>App<wbr>Version<wbr>Automatic<wbr>Scaling<wbr>Request<wbr>Utilization</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>cool<wbr>Down<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>cpu<wbr>Utilization</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionautomaticscalingcpuutilization">Flexible<wbr>App<wbr>Version<wbr>Automatic<wbr>Scaling<wbr>Cpu<wbr>Utilization</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disk<wbr>Utilization</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionautomaticscalingdiskutilization">Flexible<wbr>App<wbr>Version<wbr>Automatic<wbr>Scaling<wbr>Disk<wbr>Utilization?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Concurrent<wbr>Requests</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Idle<wbr>Instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Pending<wbr>Latency</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Total<wbr>Instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>min<wbr>Idle<wbr>Instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>min<wbr>Pending<wbr>Latency</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>min<wbr>Total<wbr>Instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>network<wbr>Utilization</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionautomaticscalingnetworkutilization">Flexible<wbr>App<wbr>Version<wbr>Automatic<wbr>Scaling<wbr>Network<wbr>Utilization?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>request<wbr>Utilization</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionautomaticscalingrequestutilization">Flexible<wbr>App<wbr>Version<wbr>Automatic<wbr>Scaling<wbr>Request<wbr>Utilization?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>cool<wbr>Down<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>cpu<wbr>Utilization</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionautomaticscalingcpuutilization">Dict[Flexible<wbr>App<wbr>Version<wbr>Automatic<wbr>Scaling<wbr>Cpu<wbr>Utilization]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disk<wbr>Utilization</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionautomaticscalingdiskutilization">Dict[Flexible<wbr>App<wbr>Version<wbr>Automatic<wbr>Scaling<wbr>Disk<wbr>Utilization]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Concurrent<wbr>Requests</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Idle<wbr>Instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Pending<wbr>Latency</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Total<wbr>Instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>min<wbr>Idle<wbr>Instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>min<wbr>Pending<wbr>Latency</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>min<wbr>Total<wbr>Instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>network<wbr>Utilization</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionautomaticscalingnetworkutilization">Dict[Flexible<wbr>App<wbr>Version<wbr>Automatic<wbr>Scaling<wbr>Network<wbr>Utilization]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>request<wbr>Utilization</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionautomaticscalingrequestutilization">Dict[Flexible<wbr>App<wbr>Version<wbr>Automatic<wbr>Scaling<wbr>Request<wbr>Utilization]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Flexible<wbr>App<wbr>Version<wbr>Automatic<wbr>Scaling<wbr>Cpu<wbr>Utilization</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#FlexibleAppVersionAutomaticScalingCpuUtilization">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#FlexibleAppVersionAutomaticScalingCpuUtilization">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/appengine?tab=doc#FlexibleAppVersionAutomaticScalingCpuUtilizationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/appengine?tab=doc#FlexibleAppVersionAutomaticScalingCpuUtilizationOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Aggregation<wbr>Window<wbr>Length</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Target<wbr>Utilization</span>
        <span class="property-indicator"></span>
        <span class="property-type">double</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Aggregation<wbr>Window<wbr>Length</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Target<wbr>Utilization</span>
        <span class="property-indicator"></span>
        <span class="property-type">float64</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>aggregation<wbr>Window<wbr>Length</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>target<wbr>Utilization</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>aggregation<wbr>Window<wbr>Length</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>target<wbr>Utilization</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Flexible<wbr>App<wbr>Version<wbr>Automatic<wbr>Scaling<wbr>Disk<wbr>Utilization</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#FlexibleAppVersionAutomaticScalingDiskUtilization">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#FlexibleAppVersionAutomaticScalingDiskUtilization">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/appengine?tab=doc#FlexibleAppVersionAutomaticScalingDiskUtilizationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/appengine?tab=doc#FlexibleAppVersionAutomaticScalingDiskUtilizationOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Target<wbr>Read<wbr>Bytes<wbr>Per<wbr>Second</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Target<wbr>Read<wbr>Ops<wbr>Per<wbr>Second</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Target<wbr>Write<wbr>Bytes<wbr>Per<wbr>Second</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Target<wbr>Write<wbr>Ops<wbr>Per<wbr>Second</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Target<wbr>Read<wbr>Bytes<wbr>Per<wbr>Second</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Target<wbr>Read<wbr>Ops<wbr>Per<wbr>Second</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Target<wbr>Write<wbr>Bytes<wbr>Per<wbr>Second</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Target<wbr>Write<wbr>Ops<wbr>Per<wbr>Second</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>target<wbr>Read<wbr>Bytes<wbr>Per<wbr>Second</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>target<wbr>Read<wbr>Ops<wbr>Per<wbr>Second</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>target<wbr>Write<wbr>Bytes<wbr>Per<wbr>Second</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>target<wbr>Write<wbr>Ops<wbr>Per<wbr>Second</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>target<wbr>Read<wbr>Bytes<wbr>Per<wbr>Second</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>target<wbr>Read<wbr>Ops<wbr>Per<wbr>Second</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>target<wbr>Write<wbr>Bytes<wbr>Per<wbr>Second</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>target<wbr>Write<wbr>Ops<wbr>Per<wbr>Second</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Flexible<wbr>App<wbr>Version<wbr>Automatic<wbr>Scaling<wbr>Network<wbr>Utilization</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#FlexibleAppVersionAutomaticScalingNetworkUtilization">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#FlexibleAppVersionAutomaticScalingNetworkUtilization">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/appengine?tab=doc#FlexibleAppVersionAutomaticScalingNetworkUtilizationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/appengine?tab=doc#FlexibleAppVersionAutomaticScalingNetworkUtilizationOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Target<wbr>Received<wbr>Bytes<wbr>Per<wbr>Second</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Target<wbr>Received<wbr>Packets<wbr>Per<wbr>Second</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Target<wbr>Sent<wbr>Bytes<wbr>Per<wbr>Second</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Target<wbr>Sent<wbr>Packets<wbr>Per<wbr>Second</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Target<wbr>Received<wbr>Bytes<wbr>Per<wbr>Second</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Target<wbr>Received<wbr>Packets<wbr>Per<wbr>Second</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Target<wbr>Sent<wbr>Bytes<wbr>Per<wbr>Second</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Target<wbr>Sent<wbr>Packets<wbr>Per<wbr>Second</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>target<wbr>Received<wbr>Bytes<wbr>Per<wbr>Second</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>target<wbr>Received<wbr>Packets<wbr>Per<wbr>Second</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>target<wbr>Sent<wbr>Bytes<wbr>Per<wbr>Second</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>target<wbr>Sent<wbr>Packets<wbr>Per<wbr>Second</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>target<wbr>Received<wbr>Bytes<wbr>Per<wbr>Second</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>target<wbr>Received<wbr>Packets<wbr>Per<wbr>Second</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>target<wbr>Sent<wbr>Bytes<wbr>Per<wbr>Second</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>target<wbr>Sent<wbr>Packets<wbr>Per<wbr>Second</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Flexible<wbr>App<wbr>Version<wbr>Automatic<wbr>Scaling<wbr>Request<wbr>Utilization</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#FlexibleAppVersionAutomaticScalingRequestUtilization">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#FlexibleAppVersionAutomaticScalingRequestUtilization">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/appengine?tab=doc#FlexibleAppVersionAutomaticScalingRequestUtilizationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/appengine?tab=doc#FlexibleAppVersionAutomaticScalingRequestUtilizationOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Target<wbr>Concurrent<wbr>Requests</span>
        <span class="property-indicator"></span>
        <span class="property-type">double?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Target<wbr>Request<wbr>Count<wbr>Per<wbr>Second</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Target<wbr>Concurrent<wbr>Requests</span>
        <span class="property-indicator"></span>
        <span class="property-type">*float64</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Target<wbr>Request<wbr>Count<wbr>Per<wbr>Second</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>target<wbr>Concurrent<wbr>Requests</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>target<wbr>Request<wbr>Count<wbr>Per<wbr>Second</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>target<wbr>Concurrent<wbr>Requests</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>target<wbr>Request<wbr>Count<wbr>Per<wbr>Second</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Flexible<wbr>App<wbr>Version<wbr>Deployment</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#FlexibleAppVersionDeployment">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#FlexibleAppVersionDeployment">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/appengine?tab=doc#FlexibleAppVersionDeploymentArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/appengine?tab=doc#FlexibleAppVersionDeploymentOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Cloud<wbr>Build<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversiondeploymentcloudbuildoptions">Flexible<wbr>App<wbr>Version<wbr>Deployment<wbr>Cloud<wbr>Build<wbr>Options<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Container</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversiondeploymentcontainer">Flexible<wbr>App<wbr>Version<wbr>Deployment<wbr>Container<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Files</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversiondeploymentfile">List&lt;Flexible<wbr>App<wbr>Version<wbr>Deployment<wbr>File<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Zip</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversiondeploymentzip">Flexible<wbr>App<wbr>Version<wbr>Deployment<wbr>Zip<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Cloud<wbr>Build<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversiondeploymentcloudbuildoptions">*Flexible<wbr>App<wbr>Version<wbr>Deployment<wbr>Cloud<wbr>Build<wbr>Options</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Container</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversiondeploymentcontainer">*Flexible<wbr>App<wbr>Version<wbr>Deployment<wbr>Container</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Files</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversiondeploymentfile">[]Flexible<wbr>App<wbr>Version<wbr>Deployment<wbr>File</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Zip</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversiondeploymentzip">*Flexible<wbr>App<wbr>Version<wbr>Deployment<wbr>Zip</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>cloud<wbr>Build<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversiondeploymentcloudbuildoptions">Flexible<wbr>App<wbr>Version<wbr>Deployment<wbr>Cloud<wbr>Build<wbr>Options?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>container</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversiondeploymentcontainer">Flexible<wbr>App<wbr>Version<wbr>Deployment<wbr>Container?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>files</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversiondeploymentfile">Flexible<wbr>App<wbr>Version<wbr>Deployment<wbr>File[]?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>zip</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversiondeploymentzip">Flexible<wbr>App<wbr>Version<wbr>Deployment<wbr>Zip?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>cloud<wbr>Build<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversiondeploymentcloudbuildoptions">Dict[Flexible<wbr>App<wbr>Version<wbr>Deployment<wbr>Cloud<wbr>Build<wbr>Options]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>container</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversiondeploymentcontainer">Dict[Flexible<wbr>App<wbr>Version<wbr>Deployment<wbr>Container]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>files</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversiondeploymentfile">List[Flexible<wbr>App<wbr>Version<wbr>Deployment<wbr>File]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>zip</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversiondeploymentzip">Dict[Flexible<wbr>App<wbr>Version<wbr>Deployment<wbr>Zip]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Flexible<wbr>App<wbr>Version<wbr>Deployment<wbr>Cloud<wbr>Build<wbr>Options</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#FlexibleAppVersionDeploymentCloudBuildOptions">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#FlexibleAppVersionDeploymentCloudBuildOptions">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/appengine?tab=doc#FlexibleAppVersionDeploymentCloudBuildOptionsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/appengine?tab=doc#FlexibleAppVersionDeploymentCloudBuildOptionsOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>App<wbr>Yaml<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cloud<wbr>Build<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>App<wbr>Yaml<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cloud<wbr>Build<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>app<wbr>Yaml<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cloud<wbr>Build<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>app<wbr>Yaml<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cloud<wbr>Build<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Flexible<wbr>App<wbr>Version<wbr>Deployment<wbr>Container</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#FlexibleAppVersionDeploymentContainer">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#FlexibleAppVersionDeploymentContainer">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/appengine?tab=doc#FlexibleAppVersionDeploymentContainerArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/appengine?tab=doc#FlexibleAppVersionDeploymentContainerOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Image</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Image</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>image</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>image</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Flexible<wbr>App<wbr>Version<wbr>Deployment<wbr>File</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#FlexibleAppVersionDeploymentFile">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#FlexibleAppVersionDeploymentFile">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/appengine?tab=doc#FlexibleAppVersionDeploymentFileArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/appengine?tab=doc#FlexibleAppVersionDeploymentFileOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The identifier for this object. Format specified above.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sha1Sum</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Source<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The identifier for this object. Format specified above.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sha1Sum</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Source<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The identifier for this object. Format specified above.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sha1Sum</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>source<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The identifier for this object. Format specified above.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sha1Sum</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>source<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Flexible<wbr>App<wbr>Version<wbr>Deployment<wbr>Zip</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#FlexibleAppVersionDeploymentZip">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#FlexibleAppVersionDeploymentZip">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/appengine?tab=doc#FlexibleAppVersionDeploymentZipArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/appengine?tab=doc#FlexibleAppVersionDeploymentZipOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Files<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Source<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Files<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Source<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>files<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>source<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>files<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>source<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Flexible<wbr>App<wbr>Version<wbr>Endpoints<wbr>Api<wbr>Service</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#FlexibleAppVersionEndpointsApiService">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#FlexibleAppVersionEndpointsApiService">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/appengine?tab=doc#FlexibleAppVersionEndpointsApiServiceArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/appengine?tab=doc#FlexibleAppVersionEndpointsApiServiceOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Config<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disable<wbr>Trace<wbr>Sampling</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The identifier for this object. Format specified above.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Rollout<wbr>Strategy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Config<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disable<wbr>Trace<wbr>Sampling</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The identifier for this object. Format specified above.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Rollout<wbr>Strategy</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>config<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disable<wbr>Trace<wbr>Sampling</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The identifier for this object. Format specified above.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>rollout<wbr>Strategy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>config_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disable<wbr>Trace<wbr>Sampling</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The identifier for this object. Format specified above.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>rollout<wbr>Strategy</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Flexible<wbr>App<wbr>Version<wbr>Entrypoint</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#FlexibleAppVersionEntrypoint">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#FlexibleAppVersionEntrypoint">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/appengine?tab=doc#FlexibleAppVersionEntrypointArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/appengine?tab=doc#FlexibleAppVersionEntrypointOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Shell</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Shell</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>shell</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>shell</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Flexible<wbr>App<wbr>Version<wbr>Liveness<wbr>Check</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#FlexibleAppVersionLivenessCheck">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#FlexibleAppVersionLivenessCheck">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/appengine?tab=doc#FlexibleAppVersionLivenessCheckArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/appengine?tab=doc#FlexibleAppVersionLivenessCheckOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Check<wbr>Interval</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Failure<wbr>Threshold</span>
        <span class="property-indicator"></span>
        <span class="property-type">double?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Host</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Initial<wbr>Delay</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Success<wbr>Threshold</span>
        <span class="property-indicator"></span>
        <span class="property-type">double?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Check<wbr>Interval</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Failure<wbr>Threshold</span>
        <span class="property-indicator"></span>
        <span class="property-type">*float64</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Host</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Initial<wbr>Delay</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Success<wbr>Threshold</span>
        <span class="property-indicator"></span>
        <span class="property-type">*float64</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>check<wbr>Interval</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>failure<wbr>Threshold</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>host</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>initial<wbr>Delay</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>success<wbr>Threshold</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>check<wbr>Interval</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>failure<wbr>Threshold</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>host</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>initial<wbr>Delay</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>path</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>success<wbr>Threshold</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Flexible<wbr>App<wbr>Version<wbr>Manual<wbr>Scaling</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#FlexibleAppVersionManualScaling">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#FlexibleAppVersionManualScaling">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/appengine?tab=doc#FlexibleAppVersionManualScalingArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/appengine?tab=doc#FlexibleAppVersionManualScalingOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Flexible<wbr>App<wbr>Version<wbr>Network</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#FlexibleAppVersionNetwork">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#FlexibleAppVersionNetwork">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/appengine?tab=doc#FlexibleAppVersionNetworkArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/appengine?tab=doc#FlexibleAppVersionNetworkOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Forwarded<wbr>Ports</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Instance<wbr>Tag</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The identifier for this object. Format specified above.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Session<wbr>Affinity</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Subnetwork</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Forwarded<wbr>Ports</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Instance<wbr>Tag</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The identifier for this object. Format specified above.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Session<wbr>Affinity</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Subnetwork</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>forwarded<wbr>Ports</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>instance<wbr>Tag</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The identifier for this object. Format specified above.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>session<wbr>Affinity</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>subnetwork</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>forwarded<wbr>Ports</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>instance<wbr>Tag</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The identifier for this object. Format specified above.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>session_<wbr>affinity</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>subnetwork</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Flexible<wbr>App<wbr>Version<wbr>Readiness<wbr>Check</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#FlexibleAppVersionReadinessCheck">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#FlexibleAppVersionReadinessCheck">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/appengine?tab=doc#FlexibleAppVersionReadinessCheckArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/appengine?tab=doc#FlexibleAppVersionReadinessCheckOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>App<wbr>Start<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Check<wbr>Interval</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Failure<wbr>Threshold</span>
        <span class="property-indicator"></span>
        <span class="property-type">double?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Host</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Success<wbr>Threshold</span>
        <span class="property-indicator"></span>
        <span class="property-type">double?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>App<wbr>Start<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Check<wbr>Interval</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Failure<wbr>Threshold</span>
        <span class="property-indicator"></span>
        <span class="property-type">*float64</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Host</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Success<wbr>Threshold</span>
        <span class="property-indicator"></span>
        <span class="property-type">*float64</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>app<wbr>Start<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>check<wbr>Interval</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>failure<wbr>Threshold</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>host</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>success<wbr>Threshold</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>app<wbr>Start<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>check<wbr>Interval</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>failure<wbr>Threshold</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>host</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>path</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>success<wbr>Threshold</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Flexible<wbr>App<wbr>Version<wbr>Resources</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#FlexibleAppVersionResources">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#FlexibleAppVersionResources">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/appengine?tab=doc#FlexibleAppVersionResourcesArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/appengine?tab=doc#FlexibleAppVersionResourcesOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Cpu</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disk<wbr>Gb</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Memory<wbr>Gb</span>
        <span class="property-indicator"></span>
        <span class="property-type">double?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Volumes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionresourcesvolume">List&lt;Flexible<wbr>App<wbr>Version<wbr>Resources<wbr>Volume<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Cpu</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disk<wbr>Gb</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Memory<wbr>Gb</span>
        <span class="property-indicator"></span>
        <span class="property-type">*float64</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Volumes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionresourcesvolume">[]Flexible<wbr>App<wbr>Version<wbr>Resources<wbr>Volume</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>cpu</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disk<wbr>Gb</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>memory<wbr>Gb</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>volumes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionresourcesvolume">Flexible<wbr>App<wbr>Version<wbr>Resources<wbr>Volume[]?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>cpu</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disk<wbr>Gb</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>memory<wbr>Gb</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>volumes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#flexibleappversionresourcesvolume">List[Flexible<wbr>App<wbr>Version<wbr>Resources<wbr>Volume]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Flexible<wbr>App<wbr>Version<wbr>Resources<wbr>Volume</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#FlexibleAppVersionResourcesVolume">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#FlexibleAppVersionResourcesVolume">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/appengine?tab=doc#FlexibleAppVersionResourcesVolumeArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/appengine?tab=doc#FlexibleAppVersionResourcesVolumeOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The identifier for this object. Format specified above.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Size<wbr>Gb</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Volume<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The identifier for this object. Format specified above.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Size<wbr>Gb</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Volume<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The identifier for this object. Format specified above.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>size<wbr>Gb</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>volume<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The identifier for this object. Format specified above.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>size<wbr>Gb</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>volume<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Flexible<wbr>App<wbr>Version<wbr>Vpc<wbr>Access<wbr>Connector</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#FlexibleAppVersionVpcAccessConnector">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#FlexibleAppVersionVpcAccessConnector">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/appengine?tab=doc#FlexibleAppVersionVpcAccessConnectorArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/appengine?tab=doc#FlexibleAppVersionVpcAccessConnectorOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The identifier for this object. Format specified above.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The identifier for this object. Format specified above.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The identifier for this object. Format specified above.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The identifier for this object. Format specified above.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-gcp">https://github.com/pulumi/pulumi-gcp</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd></dl>
