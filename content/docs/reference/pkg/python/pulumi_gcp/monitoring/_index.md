---
title: Module monitoring
title_tag: Module monitoring | Package pulumi_gcp | Python SDK
linktitle: monitoring
notitle: true
---

<div class="section" id="monitoring">
<h1>monitoring<a class="headerlink" href="#monitoring" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-gcp/issues">pulumi/pulumi-gcp repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/issues">terraform-providers/terraform-provider-google repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_gcp.monitoring"></span><dl class="py class">
<dt id="pulumi_gcp.monitoring.AlertPolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.monitoring.</code><code class="sig-name descname">AlertPolicy</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">combiner</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">conditions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">documentation</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notification_channels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.AlertPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>A description of the conditions under which some aspect of your system is
considered to be “unhealthy” and the ways to notify people or services
about this state.</p>
<p>To get more information about AlertPolicy, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/monitoring/alerts/">Official Documentation</a></p></li>
</ul>
</li>
</ul>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gcp</span> <span class="k">as</span> <span class="nn">gcp</span>

<span class="n">alert_policy</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">monitoring</span><span class="o">.</span><span class="n">AlertPolicy</span><span class="p">(</span><span class="s2">&quot;alertPolicy&quot;</span><span class="p">,</span>
    <span class="n">combiner</span><span class="o">=</span><span class="s2">&quot;OR&quot;</span><span class="p">,</span>
    <span class="n">conditions</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;conditionThreshold&quot;</span><span class="p">:</span> <span class="p">{</span>
            <span class="s2">&quot;aggregations&quot;</span><span class="p">:</span> <span class="p">[{</span>
                <span class="s2">&quot;alignmentPeriod&quot;</span><span class="p">:</span> <span class="s2">&quot;60s&quot;</span><span class="p">,</span>
                <span class="s2">&quot;perSeriesAligner&quot;</span><span class="p">:</span> <span class="s2">&quot;ALIGN_RATE&quot;</span><span class="p">,</span>
            <span class="p">}],</span>
            <span class="s2">&quot;comparison&quot;</span><span class="p">:</span> <span class="s2">&quot;COMPARISON_GT&quot;</span><span class="p">,</span>
            <span class="s2">&quot;duration&quot;</span><span class="p">:</span> <span class="s2">&quot;60s&quot;</span><span class="p">,</span>
            <span class="s2">&quot;filter&quot;</span><span class="p">:</span> <span class="s2">&quot;metric.type=&quot;</span><span class="n">compute</span><span class="o">.</span><span class="n">googleapis</span><span class="o">.</span><span class="n">com</span><span class="o">/</span><span class="n">instance</span><span class="o">/</span><span class="n">disk</span><span class="o">/</span><span class="n">write_bytes_count</span><span class="s2">&quot; AND resource.type=&quot;</span><span class="n">gce_instance</span><span class="s2">&quot;&quot;</span><span class="p">,</span>
        <span class="p">},</span>
        <span class="s2">&quot;displayName&quot;</span><span class="p">:</span> <span class="s2">&quot;test condition&quot;</span><span class="p">,</span>
    <span class="p">}],</span>
    <span class="n">display_name</span><span class="o">=</span><span class="s2">&quot;My Alert Policy&quot;</span><span class="p">,</span>
    <span class="n">user_labels</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;foo&quot;</span><span class="p">:</span> <span class="s2">&quot;bar&quot;</span><span class="p">,</span>
    <span class="p">})</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>combiner</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – How to combine the results of multiple conditions to
determine if an incident should be opened.</p></li>
<li><p><strong>conditions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of conditions for the policy. The conditions are combined by
AND or OR according to the combiner field. If the combined conditions
evaluate to true, then an incident is created. A policy can have from
one to six conditions.  Structure is documented below.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A short name or phrase used to identify the
condition in dashboards, notifications, and
incidents. To avoid confusion, don’t use the same
display name for multiple conditions in the same
policy.</p></li>
<li><p><strong>documentation</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A short name or phrase used to identify the policy in dashboards,
notifications, and incidents. To avoid confusion, don’t use the same
display name for multiple policies in the same project. The name is
limited to 512 Unicode characters.  Structure is documented below.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether or not the policy is enabled. The default is true.</p></li>
<li><p><strong>notification_channels</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Identifies the notification channels to which notifications should be
sent when incidents are opened or closed or when new violations occur
on an already opened incident. Each element of this array corresponds
to the name field in each of the NotificationChannel objects that are
returned from the notificationChannels.list method. The syntax of the
entries in this field is
<code class="docutils literal notranslate"><span class="pre">projects/[PROJECT_ID]/notificationChannels/[CHANNEL_ID]</span></code></p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>user_labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – This field is intended to be used for organizing and identifying the AlertPolicy
objects.The field can contain up to 64 entries. Each key and value is limited
to 63 Unicode characters or 128 bytes, whichever is smaller. Labels and values
can contain only lowercase letters, numerals, underscores, and dashes. Keys
must begin with a letter.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>conditions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">conditionAbsent</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A condition that checks that a time series
continues to receive new data points.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">aggregations</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Specifies the alignment of data points in
individual time series as well as how to
combine the retrieved time series together
(such as when aggregating multiple streams
on each resource to a single stream for each
resource or when aggregating streams across
all members of a group of resources).
Multiple aggregations are applied in the
order specified.This field is similar to the
one in the MetricService.ListTimeSeries
request. It is advisable to use the
ListTimeSeries method when debugging this
field.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">alignmentPeriod</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The alignment period for per-time
series alignment. If present,
alignmentPeriod must be at least
60 seconds. After per-time series
alignment, each time series will
contain data points only on the
period boundaries. If
perSeriesAligner is not specified
or equals ALIGN_NONE, then this
field is ignored. If
perSeriesAligner is specified and
does not equal ALIGN_NONE, then
this field must be defined;
otherwise an error is returned.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">crossSeriesReducer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The approach to be used to combine
time series. Not all reducer
functions may be applied to all
time series, depending on the
metric type and the value type of
the original time series.
Reduction may change the metric
type of value type of the time
series.Time series data must be
aligned in order to perform cross-
time series reduction. If
crossSeriesReducer is specified,
then perSeriesAligner must be
specified and not equal ALIGN_NONE
and alignmentPeriod must be
specified; otherwise, an error is
returned.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">groupByFields</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The set of fields to preserve when
crossSeriesReducer is specified.
The groupByFields determine how
the time series are partitioned
into subsets prior to applying the
aggregation function. Each subset
contains time series that have the
same value for each of the
grouping fields. Each individual
time series is a member of exactly
one subset. The crossSeriesReducer
is applied to each subset of time
series. It is not possible to
reduce across different resource
types, so this field implicitly
contains resource.type. Fields not
specified in groupByFields are
aggregated away. If groupByFields
is not specified and all the time
series have the same resource
type, then the time series are
aggregated into a single output
time series. If crossSeriesReducer
is not defined, this field is
ignored.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">perSeriesAligner</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The approach to be used to align
individual time series. Not all
alignment functions may be applied
to all time series, depending on
the metric type and value type of
the original time series.
Alignment may change the metric
type or the value type of the time
series.Time series data must be
aligned in order to perform cross-
time series reduction. If
crossSeriesReducer is specified,
then perSeriesAligner must be
specified and not equal ALIGN_NONE
and alignmentPeriod must be
specified; otherwise, an error is
returned.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">duration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The amount of time that a time series must
violate the threshold to be considered
failing. Currently, only values that are a
multiple of a minute–e.g., 0, 60, 120, or
300 seconds–are supported. If an invalid
value is given, an error will be returned.
When choosing a duration, it is useful to
keep in mind the frequency of the underlying
time series data (which may also be affected
by any alignments specified in the
aggregations field); a good duration is long
enough so that a single outlier does not
generate spurious alerts, but short enough
that unhealthy states are detected and
alerted on quickly.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">filter</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A filter that identifies which time series
should be compared with the threshold.The
filter is similar to the one that is
specified in the
MetricService.ListTimeSeries request (that
call is useful to verify the time series
that will be retrieved / processed) and must
specify the metric type and optionally may
contain restrictions on resource type,
resource labels, and metric labels. This
field may not exceed 2048 Unicode characters
in length.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">trigger</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The number/percent of time series for which
the comparison must hold in order for the
condition to trigger. If unspecified, then
the condition will trigger if the comparison
is true for any of the time series that have
been identified by filter and aggregations,
or by the ratio, if denominator_filter and
denominator_aggregations are specified.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The absolute number of time series
that must fail the predicate for the
condition to be triggered.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">percent</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The percentage of time series that
must fail the predicate for the
condition to be triggered.</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">conditionThreshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A condition that compares a time series against a
threshold.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">aggregations</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Specifies the alignment of data points in
individual time series as well as how to
combine the retrieved time series together
(such as when aggregating multiple streams
on each resource to a single stream for each
resource or when aggregating streams across
all members of a group of resources).
Multiple aggregations are applied in the
order specified.This field is similar to the
one in the MetricService.ListTimeSeries
request. It is advisable to use the
ListTimeSeries method when debugging this
field.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">alignmentPeriod</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The alignment period for per-time
series alignment. If present,
alignmentPeriod must be at least
60 seconds. After per-time series
alignment, each time series will
contain data points only on the
period boundaries. If
perSeriesAligner is not specified
or equals ALIGN_NONE, then this
field is ignored. If
perSeriesAligner is specified and
does not equal ALIGN_NONE, then
this field must be defined;
otherwise an error is returned.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">crossSeriesReducer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The approach to be used to combine
time series. Not all reducer
functions may be applied to all
time series, depending on the
metric type and the value type of
the original time series.
Reduction may change the metric
type of value type of the time
series.Time series data must be
aligned in order to perform cross-
time series reduction. If
crossSeriesReducer is specified,
then perSeriesAligner must be
specified and not equal ALIGN_NONE
and alignmentPeriod must be
specified; otherwise, an error is
returned.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">groupByFields</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The set of fields to preserve when
crossSeriesReducer is specified.
The groupByFields determine how
the time series are partitioned
into subsets prior to applying the
aggregation function. Each subset
contains time series that have the
same value for each of the
grouping fields. Each individual
time series is a member of exactly
one subset. The crossSeriesReducer
is applied to each subset of time
series. It is not possible to
reduce across different resource
types, so this field implicitly
contains resource.type. Fields not
specified in groupByFields are
aggregated away. If groupByFields
is not specified and all the time
series have the same resource
type, then the time series are
aggregated into a single output
time series. If crossSeriesReducer
is not defined, this field is
ignored.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">perSeriesAligner</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The approach to be used to align
individual time series. Not all
alignment functions may be applied
to all time series, depending on
the metric type and value type of
the original time series.
Alignment may change the metric
type or the value type of the time
series.Time series data must be
aligned in order to perform cross-
time series reduction. If
crossSeriesReducer is specified,
then perSeriesAligner must be
specified and not equal ALIGN_NONE
and alignmentPeriod must be
specified; otherwise, an error is
returned.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">comparison</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The comparison to apply between the time
series (indicated by filter and aggregation)
and the threshold (indicated by
threshold_value). The comparison is applied
on each time series, with the time series on
the left-hand side and the threshold on the
right-hand side. Only COMPARISON_LT and
COMPARISON_GT are supported currently.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">denominatorAggregations</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Specifies the alignment of data points in
individual time series selected by
denominatorFilter as well as how to combine
the retrieved time series together (such as
when aggregating multiple streams on each
resource to a single stream for each
resource or when aggregating streams across
all members of a group of resources).When
computing ratios, the aggregations and
denominator_aggregations fields must use the
same alignment period and produce time
series that have the same periodicity and
labels.This field is similar to the one in
the MetricService.ListTimeSeries request. It
is advisable to use the ListTimeSeries
method when debugging this field.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">alignmentPeriod</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The alignment period for per-time
series alignment. If present,
alignmentPeriod must be at least
60 seconds. After per-time series
alignment, each time series will
contain data points only on the
period boundaries. If
perSeriesAligner is not specified
or equals ALIGN_NONE, then this
field is ignored. If
perSeriesAligner is specified and
does not equal ALIGN_NONE, then
this field must be defined;
otherwise an error is returned.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">crossSeriesReducer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The approach to be used to combine
time series. Not all reducer
functions may be applied to all
time series, depending on the
metric type and the value type of
the original time series.
Reduction may change the metric
type of value type of the time
series.Time series data must be
aligned in order to perform cross-
time series reduction. If
crossSeriesReducer is specified,
then perSeriesAligner must be
specified and not equal ALIGN_NONE
and alignmentPeriod must be
specified; otherwise, an error is
returned.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">groupByFields</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The set of fields to preserve when
crossSeriesReducer is specified.
The groupByFields determine how
the time series are partitioned
into subsets prior to applying the
aggregation function. Each subset
contains time series that have the
same value for each of the
grouping fields. Each individual
time series is a member of exactly
one subset. The crossSeriesReducer
is applied to each subset of time
series. It is not possible to
reduce across different resource
types, so this field implicitly
contains resource.type. Fields not
specified in groupByFields are
aggregated away. If groupByFields
is not specified and all the time
series have the same resource
type, then the time series are
aggregated into a single output
time series. If crossSeriesReducer
is not defined, this field is
ignored.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">perSeriesAligner</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The approach to be used to align
individual time series. Not all
alignment functions may be applied
to all time series, depending on
the metric type and value type of
the original time series.
Alignment may change the metric
type or the value type of the time
series.Time series data must be
aligned in order to perform cross-
time series reduction. If
crossSeriesReducer is specified,
then perSeriesAligner must be
specified and not equal ALIGN_NONE
and alignmentPeriod must be
specified; otherwise, an error is
returned.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">denominatorFilter</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A filter that identifies a time series that
should be used as the denominator of a ratio
that will be compared with the threshold. If
a denominator_filter is specified, the time
series specified by the filter field will be
used as the numerator.The filter is similar
to the one that is specified in the
MetricService.ListTimeSeries request (that
call is useful to verify the time series
that will be retrieved / processed) and must
specify the metric type and optionally may
contain restrictions on resource type,
resource labels, and metric labels. This
field may not exceed 2048 Unicode characters
in length.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">duration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The amount of time that a time series must
violate the threshold to be considered
failing. Currently, only values that are a
multiple of a minute–e.g., 0, 60, 120, or
300 seconds–are supported. If an invalid
value is given, an error will be returned.
When choosing a duration, it is useful to
keep in mind the frequency of the underlying
time series data (which may also be affected
by any alignments specified in the
aggregations field); a good duration is long
enough so that a single outlier does not
generate spurious alerts, but short enough
that unhealthy states are detected and
alerted on quickly.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">filter</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A filter that identifies which time series
should be compared with the threshold.The
filter is similar to the one that is
specified in the
MetricService.ListTimeSeries request (that
call is useful to verify the time series
that will be retrieved / processed) and must
specify the metric type and optionally may
contain restrictions on resource type,
resource labels, and metric labels. This
field may not exceed 2048 Unicode characters
in length.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">thresholdValue</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - A value against which to compare the time
series.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">trigger</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The number/percent of time series for which
the comparison must hold in order for the
condition to trigger. If unspecified, then
the condition will trigger if the comparison
is true for any of the time series that have
been identified by filter and aggregations,
or by the ratio, if denominator_filter and
denominator_aggregations are specified.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The absolute number of time series
that must fail the predicate for the
condition to be triggered.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">percent</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The percentage of time series that
must fail the predicate for the
condition to be triggered.</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">display_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A short name or phrase used to identify the
condition in dashboards, notifications, and
incidents. To avoid confusion, don’t use the same
display name for multiple conditions in the same
policy.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - -
The unique resource name for this condition.
Its syntax is:
projects/[PROJECT_ID]/alertPolicies/[POLICY_ID]/conditions/[CONDITION_ID]
[CONDITION_ID] is assigned by Stackdriver Monitoring when
the condition is created as part of a new or updated alerting
policy.</p></li>
</ul>
<p>The <strong>documentation</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">content</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The text of the documentation, interpreted according to mimeType.
The content may not exceed 8,192 Unicode characters and may not
exceed more than 10,240 bytes when encoded in UTF-8 format,
whichever is smaller.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mimeType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The format of the content field. Presently, only the value
“text/markdown” is supported.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_gcp.monitoring.AlertPolicy.combiner">
<code class="sig-name descname">combiner</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.AlertPolicy.combiner" title="Permalink to this definition">¶</a></dt>
<dd><p>How to combine the results of multiple conditions to
determine if an incident should be opened.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.monitoring.AlertPolicy.conditions">
<code class="sig-name descname">conditions</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.AlertPolicy.conditions" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of conditions for the policy. The conditions are combined by
AND or OR according to the combiner field. If the combined conditions
evaluate to true, then an incident is created. A policy can have from
one to six conditions.  Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">conditionAbsent</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A condition that checks that a time series
continues to receive new data points.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">aggregations</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Specifies the alignment of data points in
individual time series as well as how to
combine the retrieved time series together
(such as when aggregating multiple streams
on each resource to a single stream for each
resource or when aggregating streams across
all members of a group of resources).
Multiple aggregations are applied in the
order specified.This field is similar to the
one in the MetricService.ListTimeSeries
request. It is advisable to use the
ListTimeSeries method when debugging this
field.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">alignmentPeriod</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The alignment period for per-time
series alignment. If present,
alignmentPeriod must be at least
60 seconds. After per-time series
alignment, each time series will
contain data points only on the
period boundaries. If
perSeriesAligner is not specified
or equals ALIGN_NONE, then this
field is ignored. If
perSeriesAligner is specified and
does not equal ALIGN_NONE, then
this field must be defined;
otherwise an error is returned.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">crossSeriesReducer</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The approach to be used to combine
time series. Not all reducer
functions may be applied to all
time series, depending on the
metric type and the value type of
the original time series.
Reduction may change the metric
type of value type of the time
series.Time series data must be
aligned in order to perform cross-
time series reduction. If
crossSeriesReducer is specified,
then perSeriesAligner must be
specified and not equal ALIGN_NONE
and alignmentPeriod must be
specified; otherwise, an error is
returned.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">groupByFields</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The set of fields to preserve when
crossSeriesReducer is specified.
The groupByFields determine how
the time series are partitioned
into subsets prior to applying the
aggregation function. Each subset
contains time series that have the
same value for each of the
grouping fields. Each individual
time series is a member of exactly
one subset. The crossSeriesReducer
is applied to each subset of time
series. It is not possible to
reduce across different resource
types, so this field implicitly
contains resource.type. Fields not
specified in groupByFields are
aggregated away. If groupByFields
is not specified and all the time
series have the same resource
type, then the time series are
aggregated into a single output
time series. If crossSeriesReducer
is not defined, this field is
ignored.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">perSeriesAligner</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The approach to be used to align
individual time series. Not all
alignment functions may be applied
to all time series, depending on
the metric type and value type of
the original time series.
Alignment may change the metric
type or the value type of the time
series.Time series data must be
aligned in order to perform cross-
time series reduction. If
crossSeriesReducer is specified,
then perSeriesAligner must be
specified and not equal ALIGN_NONE
and alignmentPeriod must be
specified; otherwise, an error is
returned.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">duration</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The amount of time that a time series must
violate the threshold to be considered
failing. Currently, only values that are a
multiple of a minute–e.g., 0, 60, 120, or
300 seconds–are supported. If an invalid
value is given, an error will be returned.
When choosing a duration, it is useful to
keep in mind the frequency of the underlying
time series data (which may also be affected
by any alignments specified in the
aggregations field); a good duration is long
enough so that a single outlier does not
generate spurious alerts, but short enough
that unhealthy states are detected and
alerted on quickly.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">filter</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A filter that identifies which time series
should be compared with the threshold.The
filter is similar to the one that is
specified in the
MetricService.ListTimeSeries request (that
call is useful to verify the time series
that will be retrieved / processed) and must
specify the metric type and optionally may
contain restrictions on resource type,
resource labels, and metric labels. This
field may not exceed 2048 Unicode characters
in length.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">trigger</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The number/percent of time series for which
the comparison must hold in order for the
condition to trigger. If unspecified, then
the condition will trigger if the comparison
is true for any of the time series that have
been identified by filter and aggregations,
or by the ratio, if denominator_filter and
denominator_aggregations are specified.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The absolute number of time series
that must fail the predicate for the
condition to be triggered.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">percent</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The percentage of time series that
must fail the predicate for the
condition to be triggered.</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">conditionThreshold</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A condition that compares a time series against a
threshold.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">aggregations</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Specifies the alignment of data points in
individual time series as well as how to
combine the retrieved time series together
(such as when aggregating multiple streams
on each resource to a single stream for each
resource or when aggregating streams across
all members of a group of resources).
Multiple aggregations are applied in the
order specified.This field is similar to the
one in the MetricService.ListTimeSeries
request. It is advisable to use the
ListTimeSeries method when debugging this
field.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">alignmentPeriod</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The alignment period for per-time
series alignment. If present,
alignmentPeriod must be at least
60 seconds. After per-time series
alignment, each time series will
contain data points only on the
period boundaries. If
perSeriesAligner is not specified
or equals ALIGN_NONE, then this
field is ignored. If
perSeriesAligner is specified and
does not equal ALIGN_NONE, then
this field must be defined;
otherwise an error is returned.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">crossSeriesReducer</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The approach to be used to combine
time series. Not all reducer
functions may be applied to all
time series, depending on the
metric type and the value type of
the original time series.
Reduction may change the metric
type of value type of the time
series.Time series data must be
aligned in order to perform cross-
time series reduction. If
crossSeriesReducer is specified,
then perSeriesAligner must be
specified and not equal ALIGN_NONE
and alignmentPeriod must be
specified; otherwise, an error is
returned.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">groupByFields</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The set of fields to preserve when
crossSeriesReducer is specified.
The groupByFields determine how
the time series are partitioned
into subsets prior to applying the
aggregation function. Each subset
contains time series that have the
same value for each of the
grouping fields. Each individual
time series is a member of exactly
one subset. The crossSeriesReducer
is applied to each subset of time
series. It is not possible to
reduce across different resource
types, so this field implicitly
contains resource.type. Fields not
specified in groupByFields are
aggregated away. If groupByFields
is not specified and all the time
series have the same resource
type, then the time series are
aggregated into a single output
time series. If crossSeriesReducer
is not defined, this field is
ignored.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">perSeriesAligner</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The approach to be used to align
individual time series. Not all
alignment functions may be applied
to all time series, depending on
the metric type and value type of
the original time series.
Alignment may change the metric
type or the value type of the time
series.Time series data must be
aligned in order to perform cross-
time series reduction. If
crossSeriesReducer is specified,
then perSeriesAligner must be
specified and not equal ALIGN_NONE
and alignmentPeriod must be
specified; otherwise, an error is
returned.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">comparison</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The comparison to apply between the time
series (indicated by filter and aggregation)
and the threshold (indicated by
threshold_value). The comparison is applied
on each time series, with the time series on
the left-hand side and the threshold on the
right-hand side. Only COMPARISON_LT and
COMPARISON_GT are supported currently.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">denominatorAggregations</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Specifies the alignment of data points in
individual time series selected by
denominatorFilter as well as how to combine
the retrieved time series together (such as
when aggregating multiple streams on each
resource to a single stream for each
resource or when aggregating streams across
all members of a group of resources).When
computing ratios, the aggregations and
denominator_aggregations fields must use the
same alignment period and produce time
series that have the same periodicity and
labels.This field is similar to the one in
the MetricService.ListTimeSeries request. It
is advisable to use the ListTimeSeries
method when debugging this field.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">alignmentPeriod</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The alignment period for per-time
series alignment. If present,
alignmentPeriod must be at least
60 seconds. After per-time series
alignment, each time series will
contain data points only on the
period boundaries. If
perSeriesAligner is not specified
or equals ALIGN_NONE, then this
field is ignored. If
perSeriesAligner is specified and
does not equal ALIGN_NONE, then
this field must be defined;
otherwise an error is returned.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">crossSeriesReducer</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The approach to be used to combine
time series. Not all reducer
functions may be applied to all
time series, depending on the
metric type and the value type of
the original time series.
Reduction may change the metric
type of value type of the time
series.Time series data must be
aligned in order to perform cross-
time series reduction. If
crossSeriesReducer is specified,
then perSeriesAligner must be
specified and not equal ALIGN_NONE
and alignmentPeriod must be
specified; otherwise, an error is
returned.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">groupByFields</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The set of fields to preserve when
crossSeriesReducer is specified.
The groupByFields determine how
the time series are partitioned
into subsets prior to applying the
aggregation function. Each subset
contains time series that have the
same value for each of the
grouping fields. Each individual
time series is a member of exactly
one subset. The crossSeriesReducer
is applied to each subset of time
series. It is not possible to
reduce across different resource
types, so this field implicitly
contains resource.type. Fields not
specified in groupByFields are
aggregated away. If groupByFields
is not specified and all the time
series have the same resource
type, then the time series are
aggregated into a single output
time series. If crossSeriesReducer
is not defined, this field is
ignored.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">perSeriesAligner</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The approach to be used to align
individual time series. Not all
alignment functions may be applied
to all time series, depending on
the metric type and value type of
the original time series.
Alignment may change the metric
type or the value type of the time
series.Time series data must be
aligned in order to perform cross-
time series reduction. If
crossSeriesReducer is specified,
then perSeriesAligner must be
specified and not equal ALIGN_NONE
and alignmentPeriod must be
specified; otherwise, an error is
returned.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">denominatorFilter</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A filter that identifies a time series that
should be used as the denominator of a ratio
that will be compared with the threshold. If
a denominator_filter is specified, the time
series specified by the filter field will be
used as the numerator.The filter is similar
to the one that is specified in the
MetricService.ListTimeSeries request (that
call is useful to verify the time series
that will be retrieved / processed) and must
specify the metric type and optionally may
contain restrictions on resource type,
resource labels, and metric labels. This
field may not exceed 2048 Unicode characters
in length.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">duration</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The amount of time that a time series must
violate the threshold to be considered
failing. Currently, only values that are a
multiple of a minute–e.g., 0, 60, 120, or
300 seconds–are supported. If an invalid
value is given, an error will be returned.
When choosing a duration, it is useful to
keep in mind the frequency of the underlying
time series data (which may also be affected
by any alignments specified in the
aggregations field); a good duration is long
enough so that a single outlier does not
generate spurious alerts, but short enough
that unhealthy states are detected and
alerted on quickly.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">filter</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A filter that identifies which time series
should be compared with the threshold.The
filter is similar to the one that is
specified in the
MetricService.ListTimeSeries request (that
call is useful to verify the time series
that will be retrieved / processed) and must
specify the metric type and optionally may
contain restrictions on resource type,
resource labels, and metric labels. This
field may not exceed 2048 Unicode characters
in length.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">thresholdValue</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - A value against which to compare the time
series.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">trigger</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The number/percent of time series for which
the comparison must hold in order for the
condition to trigger. If unspecified, then
the condition will trigger if the comparison
is true for any of the time series that have
been identified by filter and aggregations,
or by the ratio, if denominator_filter and
denominator_aggregations are specified.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The absolute number of time series
that must fail the predicate for the
condition to be triggered.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">percent</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The percentage of time series that
must fail the predicate for the
condition to be triggered.</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">display_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A short name or phrase used to identify the
condition in dashboards, notifications, and
incidents. To avoid confusion, don’t use the same
display name for multiple conditions in the same
policy.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - -
The unique resource name for this condition.
Its syntax is:
projects/[PROJECT_ID]/alertPolicies/[POLICY_ID]/conditions/[CONDITION_ID]
[CONDITION_ID] is assigned by Stackdriver Monitoring when
the condition is created as part of a new or updated alerting
policy.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.monitoring.AlertPolicy.creation_record">
<code class="sig-name descname">creation_record</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.AlertPolicy.creation_record" title="Permalink to this definition">¶</a></dt>
<dd><p>A read-only record of the creation of the alerting policy. If provided in a call to create or update, this field will be
ignored.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">mutateTime</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mutatedBy</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.monitoring.AlertPolicy.display_name">
<code class="sig-name descname">display_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.AlertPolicy.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>A short name or phrase used to identify the
condition in dashboards, notifications, and
incidents. To avoid confusion, don’t use the same
display name for multiple conditions in the same
policy.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.monitoring.AlertPolicy.documentation">
<code class="sig-name descname">documentation</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.AlertPolicy.documentation" title="Permalink to this definition">¶</a></dt>
<dd><p>A short name or phrase used to identify the policy in dashboards,
notifications, and incidents. To avoid confusion, don’t use the same
display name for multiple policies in the same project. The name is
limited to 512 Unicode characters.  Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">content</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The text of the documentation, interpreted according to mimeType.
The content may not exceed 8,192 Unicode characters and may not
exceed more than 10,240 bytes when encoded in UTF-8 format,
whichever is smaller.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mimeType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The format of the content field. Presently, only the value
“text/markdown” is supported.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.monitoring.AlertPolicy.enabled">
<code class="sig-name descname">enabled</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.AlertPolicy.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether or not the policy is enabled. The default is true.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.monitoring.AlertPolicy.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.AlertPolicy.name" title="Permalink to this definition">¶</a></dt>
<dd><ul class="simple">
<li></li>
</ul>
<p>The unique resource name for this condition.
Its syntax is:
projects/[PROJECT_ID]/alertPolicies/[POLICY_ID]/conditions/[CONDITION_ID]
[CONDITION_ID] is assigned by Stackdriver Monitoring when
the condition is created as part of a new or updated alerting
policy.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.monitoring.AlertPolicy.notification_channels">
<code class="sig-name descname">notification_channels</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.AlertPolicy.notification_channels" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifies the notification channels to which notifications should be
sent when incidents are opened or closed or when new violations occur
on an already opened incident. Each element of this array corresponds
to the name field in each of the NotificationChannel objects that are
returned from the notificationChannels.list method. The syntax of the
entries in this field is
<code class="docutils literal notranslate"><span class="pre">projects/[PROJECT_ID]/notificationChannels/[CHANNEL_ID]</span></code></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.monitoring.AlertPolicy.project">
<code class="sig-name descname">project</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.AlertPolicy.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.monitoring.AlertPolicy.user_labels">
<code class="sig-name descname">user_labels</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.AlertPolicy.user_labels" title="Permalink to this definition">¶</a></dt>
<dd><p>This field is intended to be used for organizing and identifying the AlertPolicy
objects.The field can contain up to 64 entries. Each key and value is limited
to 63 Unicode characters or 128 bytes, whichever is smaller. Labels and values
can contain only lowercase letters, numerals, underscores, and dashes. Keys
must begin with a letter.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.monitoring.AlertPolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">combiner</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">conditions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">creation_record</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">documentation</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notification_channels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_labels</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.AlertPolicy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AlertPolicy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>combiner</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – How to combine the results of multiple conditions to
determine if an incident should be opened.</p></li>
<li><p><strong>conditions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of conditions for the policy. The conditions are combined by
AND or OR according to the combiner field. If the combined conditions
evaluate to true, then an incident is created. A policy can have from
one to six conditions.  Structure is documented below.</p></li>
<li><p><strong>creation_record</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A read-only record of the creation of the alerting policy. If provided in a call to create or update, this field will be
ignored.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A short name or phrase used to identify the
condition in dashboards, notifications, and
incidents. To avoid confusion, don’t use the same
display name for multiple conditions in the same
policy.</p></li>
<li><p><strong>documentation</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A short name or phrase used to identify the policy in dashboards,
notifications, and incidents. To avoid confusion, don’t use the same
display name for multiple policies in the same project. The name is
limited to 512 Unicode characters.  Structure is documented below.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether or not the policy is enabled. The default is true.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <ul>
<li></li>
</ul>
<p>The unique resource name for this condition.
Its syntax is:
projects/[PROJECT_ID]/alertPolicies/[POLICY_ID]/conditions/[CONDITION_ID]
[CONDITION_ID] is assigned by Stackdriver Monitoring when
the condition is created as part of a new or updated alerting
policy.</p>
</p></li>
<li><p><strong>notification_channels</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Identifies the notification channels to which notifications should be
sent when incidents are opened or closed or when new violations occur
on an already opened incident. Each element of this array corresponds
to the name field in each of the NotificationChannel objects that are
returned from the notificationChannels.list method. The syntax of the
entries in this field is
<code class="docutils literal notranslate"><span class="pre">projects/[PROJECT_ID]/notificationChannels/[CHANNEL_ID]</span></code></p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>user_labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – This field is intended to be used for organizing and identifying the AlertPolicy
objects.The field can contain up to 64 entries. Each key and value is limited
to 63 Unicode characters or 128 bytes, whichever is smaller. Labels and values
can contain only lowercase letters, numerals, underscores, and dashes. Keys
must begin with a letter.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>conditions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">conditionAbsent</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A condition that checks that a time series
continues to receive new data points.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">aggregations</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Specifies the alignment of data points in
individual time series as well as how to
combine the retrieved time series together
(such as when aggregating multiple streams
on each resource to a single stream for each
resource or when aggregating streams across
all members of a group of resources).
Multiple aggregations are applied in the
order specified.This field is similar to the
one in the MetricService.ListTimeSeries
request. It is advisable to use the
ListTimeSeries method when debugging this
field.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">alignmentPeriod</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The alignment period for per-time
series alignment. If present,
alignmentPeriod must be at least
60 seconds. After per-time series
alignment, each time series will
contain data points only on the
period boundaries. If
perSeriesAligner is not specified
or equals ALIGN_NONE, then this
field is ignored. If
perSeriesAligner is specified and
does not equal ALIGN_NONE, then
this field must be defined;
otherwise an error is returned.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">crossSeriesReducer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The approach to be used to combine
time series. Not all reducer
functions may be applied to all
time series, depending on the
metric type and the value type of
the original time series.
Reduction may change the metric
type of value type of the time
series.Time series data must be
aligned in order to perform cross-
time series reduction. If
crossSeriesReducer is specified,
then perSeriesAligner must be
specified and not equal ALIGN_NONE
and alignmentPeriod must be
specified; otherwise, an error is
returned.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">groupByFields</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The set of fields to preserve when
crossSeriesReducer is specified.
The groupByFields determine how
the time series are partitioned
into subsets prior to applying the
aggregation function. Each subset
contains time series that have the
same value for each of the
grouping fields. Each individual
time series is a member of exactly
one subset. The crossSeriesReducer
is applied to each subset of time
series. It is not possible to
reduce across different resource
types, so this field implicitly
contains resource.type. Fields not
specified in groupByFields are
aggregated away. If groupByFields
is not specified and all the time
series have the same resource
type, then the time series are
aggregated into a single output
time series. If crossSeriesReducer
is not defined, this field is
ignored.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">perSeriesAligner</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The approach to be used to align
individual time series. Not all
alignment functions may be applied
to all time series, depending on
the metric type and value type of
the original time series.
Alignment may change the metric
type or the value type of the time
series.Time series data must be
aligned in order to perform cross-
time series reduction. If
crossSeriesReducer is specified,
then perSeriesAligner must be
specified and not equal ALIGN_NONE
and alignmentPeriod must be
specified; otherwise, an error is
returned.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">duration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The amount of time that a time series must
violate the threshold to be considered
failing. Currently, only values that are a
multiple of a minute–e.g., 0, 60, 120, or
300 seconds–are supported. If an invalid
value is given, an error will be returned.
When choosing a duration, it is useful to
keep in mind the frequency of the underlying
time series data (which may also be affected
by any alignments specified in the
aggregations field); a good duration is long
enough so that a single outlier does not
generate spurious alerts, but short enough
that unhealthy states are detected and
alerted on quickly.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">filter</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A filter that identifies which time series
should be compared with the threshold.The
filter is similar to the one that is
specified in the
MetricService.ListTimeSeries request (that
call is useful to verify the time series
that will be retrieved / processed) and must
specify the metric type and optionally may
contain restrictions on resource type,
resource labels, and metric labels. This
field may not exceed 2048 Unicode characters
in length.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">trigger</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The number/percent of time series for which
the comparison must hold in order for the
condition to trigger. If unspecified, then
the condition will trigger if the comparison
is true for any of the time series that have
been identified by filter and aggregations,
or by the ratio, if denominator_filter and
denominator_aggregations are specified.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The absolute number of time series
that must fail the predicate for the
condition to be triggered.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">percent</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The percentage of time series that
must fail the predicate for the
condition to be triggered.</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">conditionThreshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A condition that compares a time series against a
threshold.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">aggregations</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Specifies the alignment of data points in
individual time series as well as how to
combine the retrieved time series together
(such as when aggregating multiple streams
on each resource to a single stream for each
resource or when aggregating streams across
all members of a group of resources).
Multiple aggregations are applied in the
order specified.This field is similar to the
one in the MetricService.ListTimeSeries
request. It is advisable to use the
ListTimeSeries method when debugging this
field.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">alignmentPeriod</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The alignment period for per-time
series alignment. If present,
alignmentPeriod must be at least
60 seconds. After per-time series
alignment, each time series will
contain data points only on the
period boundaries. If
perSeriesAligner is not specified
or equals ALIGN_NONE, then this
field is ignored. If
perSeriesAligner is specified and
does not equal ALIGN_NONE, then
this field must be defined;
otherwise an error is returned.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">crossSeriesReducer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The approach to be used to combine
time series. Not all reducer
functions may be applied to all
time series, depending on the
metric type and the value type of
the original time series.
Reduction may change the metric
type of value type of the time
series.Time series data must be
aligned in order to perform cross-
time series reduction. If
crossSeriesReducer is specified,
then perSeriesAligner must be
specified and not equal ALIGN_NONE
and alignmentPeriod must be
specified; otherwise, an error is
returned.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">groupByFields</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The set of fields to preserve when
crossSeriesReducer is specified.
The groupByFields determine how
the time series are partitioned
into subsets prior to applying the
aggregation function. Each subset
contains time series that have the
same value for each of the
grouping fields. Each individual
time series is a member of exactly
one subset. The crossSeriesReducer
is applied to each subset of time
series. It is not possible to
reduce across different resource
types, so this field implicitly
contains resource.type. Fields not
specified in groupByFields are
aggregated away. If groupByFields
is not specified and all the time
series have the same resource
type, then the time series are
aggregated into a single output
time series. If crossSeriesReducer
is not defined, this field is
ignored.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">perSeriesAligner</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The approach to be used to align
individual time series. Not all
alignment functions may be applied
to all time series, depending on
the metric type and value type of
the original time series.
Alignment may change the metric
type or the value type of the time
series.Time series data must be
aligned in order to perform cross-
time series reduction. If
crossSeriesReducer is specified,
then perSeriesAligner must be
specified and not equal ALIGN_NONE
and alignmentPeriod must be
specified; otherwise, an error is
returned.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">comparison</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The comparison to apply between the time
series (indicated by filter and aggregation)
and the threshold (indicated by
threshold_value). The comparison is applied
on each time series, with the time series on
the left-hand side and the threshold on the
right-hand side. Only COMPARISON_LT and
COMPARISON_GT are supported currently.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">denominatorAggregations</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Specifies the alignment of data points in
individual time series selected by
denominatorFilter as well as how to combine
the retrieved time series together (such as
when aggregating multiple streams on each
resource to a single stream for each
resource or when aggregating streams across
all members of a group of resources).When
computing ratios, the aggregations and
denominator_aggregations fields must use the
same alignment period and produce time
series that have the same periodicity and
labels.This field is similar to the one in
the MetricService.ListTimeSeries request. It
is advisable to use the ListTimeSeries
method when debugging this field.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">alignmentPeriod</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The alignment period for per-time
series alignment. If present,
alignmentPeriod must be at least
60 seconds. After per-time series
alignment, each time series will
contain data points only on the
period boundaries. If
perSeriesAligner is not specified
or equals ALIGN_NONE, then this
field is ignored. If
perSeriesAligner is specified and
does not equal ALIGN_NONE, then
this field must be defined;
otherwise an error is returned.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">crossSeriesReducer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The approach to be used to combine
time series. Not all reducer
functions may be applied to all
time series, depending on the
metric type and the value type of
the original time series.
Reduction may change the metric
type of value type of the time
series.Time series data must be
aligned in order to perform cross-
time series reduction. If
crossSeriesReducer is specified,
then perSeriesAligner must be
specified and not equal ALIGN_NONE
and alignmentPeriod must be
specified; otherwise, an error is
returned.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">groupByFields</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The set of fields to preserve when
crossSeriesReducer is specified.
The groupByFields determine how
the time series are partitioned
into subsets prior to applying the
aggregation function. Each subset
contains time series that have the
same value for each of the
grouping fields. Each individual
time series is a member of exactly
one subset. The crossSeriesReducer
is applied to each subset of time
series. It is not possible to
reduce across different resource
types, so this field implicitly
contains resource.type. Fields not
specified in groupByFields are
aggregated away. If groupByFields
is not specified and all the time
series have the same resource
type, then the time series are
aggregated into a single output
time series. If crossSeriesReducer
is not defined, this field is
ignored.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">perSeriesAligner</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The approach to be used to align
individual time series. Not all
alignment functions may be applied
to all time series, depending on
the metric type and value type of
the original time series.
Alignment may change the metric
type or the value type of the time
series.Time series data must be
aligned in order to perform cross-
time series reduction. If
crossSeriesReducer is specified,
then perSeriesAligner must be
specified and not equal ALIGN_NONE
and alignmentPeriod must be
specified; otherwise, an error is
returned.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">denominatorFilter</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A filter that identifies a time series that
should be used as the denominator of a ratio
that will be compared with the threshold. If
a denominator_filter is specified, the time
series specified by the filter field will be
used as the numerator.The filter is similar
to the one that is specified in the
MetricService.ListTimeSeries request (that
call is useful to verify the time series
that will be retrieved / processed) and must
specify the metric type and optionally may
contain restrictions on resource type,
resource labels, and metric labels. This
field may not exceed 2048 Unicode characters
in length.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">duration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The amount of time that a time series must
violate the threshold to be considered
failing. Currently, only values that are a
multiple of a minute–e.g., 0, 60, 120, or
300 seconds–are supported. If an invalid
value is given, an error will be returned.
When choosing a duration, it is useful to
keep in mind the frequency of the underlying
time series data (which may also be affected
by any alignments specified in the
aggregations field); a good duration is long
enough so that a single outlier does not
generate spurious alerts, but short enough
that unhealthy states are detected and
alerted on quickly.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">filter</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A filter that identifies which time series
should be compared with the threshold.The
filter is similar to the one that is
specified in the
MetricService.ListTimeSeries request (that
call is useful to verify the time series
that will be retrieved / processed) and must
specify the metric type and optionally may
contain restrictions on resource type,
resource labels, and metric labels. This
field may not exceed 2048 Unicode characters
in length.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">thresholdValue</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - A value against which to compare the time
series.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">trigger</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The number/percent of time series for which
the comparison must hold in order for the
condition to trigger. If unspecified, then
the condition will trigger if the comparison
is true for any of the time series that have
been identified by filter and aggregations,
or by the ratio, if denominator_filter and
denominator_aggregations are specified.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The absolute number of time series
that must fail the predicate for the
condition to be triggered.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">percent</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The percentage of time series that
must fail the predicate for the
condition to be triggered.</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">display_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A short name or phrase used to identify the
condition in dashboards, notifications, and
incidents. To avoid confusion, don’t use the same
display name for multiple conditions in the same
policy.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - -
The unique resource name for this condition.
Its syntax is:
projects/[PROJECT_ID]/alertPolicies/[POLICY_ID]/conditions/[CONDITION_ID]
[CONDITION_ID] is assigned by Stackdriver Monitoring when
the condition is created as part of a new or updated alerting
policy.</p></li>
</ul>
<p>The <strong>creation_record</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">mutateTime</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mutatedBy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>documentation</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">content</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The text of the documentation, interpreted according to mimeType.
The content may not exceed 8,192 Unicode characters and may not
exceed more than 10,240 bytes when encoded in UTF-8 format,
whichever is smaller.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mimeType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The format of the content field. Presently, only the value
“text/markdown” is supported.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.monitoring.AlertPolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.AlertPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>prop</strong> (<em>str</em>) – A property name.</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>A potentially transformed property name.</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>str</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.monitoring.AlertPolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.AlertPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>prop</strong> (<em>str</em>) – A property name.</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>A potentially transformed property name.</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>str</p>
</dd>
</dl>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_gcp.monitoring.AwaitableGetAppEngineServiceResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.monitoring.</code><code class="sig-name descname">AwaitableGetAppEngineServiceResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">display_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">module_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">telemetries</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.AwaitableGetAppEngineServiceResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_gcp.monitoring.AwaitableGetNotificationChannelResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.monitoring.</code><code class="sig-name descname">AwaitableGetNotificationChannelResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sensitive_labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">verification_status</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.AwaitableGetNotificationChannelResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_gcp.monitoring.AwaitableGetSecretVersionResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.monitoring.</code><code class="sig-name descname">AwaitableGetSecretVersionResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">create_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">destroy_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">secret</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">secret_data</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.AwaitableGetSecretVersionResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_gcp.monitoring.AwaitableGetUptimeCheckIPsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.monitoring.</code><code class="sig-name descname">AwaitableGetUptimeCheckIPsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">uptime_check_ips</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.AwaitableGetUptimeCheckIPsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_gcp.monitoring.CustomService">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.monitoring.</code><code class="sig-name descname">CustomService</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">telemetry</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.CustomService" title="Permalink to this definition">¶</a></dt>
<dd><p>A Service is a discrete, autonomous, and network-accessible unit,
designed to solve an individual concern (Wikipedia). In Cloud Monitoring,
a Service acts as the root resource under which operational aspects of
the service are accessible</p>
<p>To get more information about Service, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/monitoring/api/ref_v3/rest/v3/services">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/monitoring/service-monitoring">Service Monitoring</a></p></li>
<li><p><a class="reference external" href="https://cloud.google.com/monitoring/api/v3/">Monitoring API Documentation</a></p></li>
</ul>
</li>
</ul>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gcp</span> <span class="k">as</span> <span class="nn">gcp</span>

<span class="n">custom</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">monitoring</span><span class="o">.</span><span class="n">CustomService</span><span class="p">(</span><span class="s2">&quot;custom&quot;</span><span class="p">,</span>
    <span class="n">display_name</span><span class="o">=</span><span class="s2">&quot;My Custom Service custom-srv&quot;</span><span class="p">,</span>
    <span class="n">service_id</span><span class="o">=</span><span class="s2">&quot;custom-srv&quot;</span><span class="p">,</span>
    <span class="n">telemetry</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;resourceName&quot;</span><span class="p">:</span> <span class="s2">&quot;//product.googleapis.com/foo/foo/services/test&quot;</span><span class="p">,</span>
    <span class="p">})</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name used for UI elements listing this Service.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>service_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An optional service ID to use. If not given, the server will generate a
service ID.</p></li>
<li><p><strong>telemetry</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration for how to query telemetry on a Service.  Structure is documented below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>telemetry</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">resourceName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The full name of the resource that defines this service.
Formatted as described in
<a class="reference external" href="https://cloud.google.com/apis/design/resource_names">https://cloud.google.com/apis/design/resource_names</a>.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_gcp.monitoring.CustomService.display_name">
<code class="sig-name descname">display_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.CustomService.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name used for UI elements listing this Service.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.monitoring.CustomService.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.CustomService.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The full resource name for this service. The syntax is: projects/[PROJECT_ID]/services/[SERVICE_ID].</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.monitoring.CustomService.project">
<code class="sig-name descname">project</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.CustomService.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.monitoring.CustomService.service_id">
<code class="sig-name descname">service_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.CustomService.service_id" title="Permalink to this definition">¶</a></dt>
<dd><p>An optional service ID to use. If not given, the server will generate a
service ID.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.monitoring.CustomService.telemetry">
<code class="sig-name descname">telemetry</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.CustomService.telemetry" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration for how to query telemetry on a Service.  Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">resourceName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The full name of the resource that defines this service.
Formatted as described in
<a class="reference external" href="https://cloud.google.com/apis/design/resource_names">https://cloud.google.com/apis/design/resource_names</a>.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.monitoring.CustomService.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">telemetry</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.CustomService.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing CustomService resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name used for UI elements listing this Service.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The full resource name for this service. The syntax is: projects/[PROJECT_ID]/services/[SERVICE_ID].</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>service_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An optional service ID to use. If not given, the server will generate a
service ID.</p></li>
<li><p><strong>telemetry</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration for how to query telemetry on a Service.  Structure is documented below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>telemetry</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">resourceName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The full name of the resource that defines this service.
Formatted as described in
<a class="reference external" href="https://cloud.google.com/apis/design/resource_names">https://cloud.google.com/apis/design/resource_names</a>.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.monitoring.CustomService.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.CustomService.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>prop</strong> (<em>str</em>) – A property name.</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>A potentially transformed property name.</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>str</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.monitoring.CustomService.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.CustomService.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>prop</strong> (<em>str</em>) – A property name.</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>A potentially transformed property name.</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>str</p>
</dd>
</dl>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_gcp.monitoring.GetAppEngineServiceResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.monitoring.</code><code class="sig-name descname">GetAppEngineServiceResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">display_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">module_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">telemetries</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.GetAppEngineServiceResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAppEngineService.</p>
<dl class="py attribute">
<dt id="pulumi_gcp.monitoring.GetAppEngineServiceResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.GetAppEngineServiceResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_gcp.monitoring.GetNotificationChannelResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.monitoring.</code><code class="sig-name descname">GetNotificationChannelResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sensitive_labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">verification_status</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.GetNotificationChannelResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getNotificationChannel.</p>
<dl class="py attribute">
<dt id="pulumi_gcp.monitoring.GetNotificationChannelResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.GetNotificationChannelResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_gcp.monitoring.GetSecretVersionResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.monitoring.</code><code class="sig-name descname">GetSecretVersionResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">create_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">destroy_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">secret</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">secret_data</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.GetSecretVersionResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getSecretVersion.</p>
<dl class="py attribute">
<dt id="pulumi_gcp.monitoring.GetSecretVersionResult.create_time">
<code class="sig-name descname">create_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.GetSecretVersionResult.create_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The time at which the Secret was created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.monitoring.GetSecretVersionResult.destroy_time">
<code class="sig-name descname">destroy_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.GetSecretVersionResult.destroy_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The time at which the Secret was destroyed. Only present if state is DESTROYED.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.monitoring.GetSecretVersionResult.enabled">
<code class="sig-name descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.GetSecretVersionResult.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>True if the current state of the SecretVersion is enabled.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.monitoring.GetSecretVersionResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.GetSecretVersionResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.monitoring.GetSecretVersionResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.GetSecretVersionResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource name of the SecretVersion. Format:
<code class="docutils literal notranslate"><span class="pre">projects/{{project}}/secrets/{{secret_id}}/versions/{{version}}</span></code></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.monitoring.GetSecretVersionResult.secret_data">
<code class="sig-name descname">secret_data</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.GetSecretVersionResult.secret_data" title="Permalink to this definition">¶</a></dt>
<dd><p>The secret data. No larger than 64KiB.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_gcp.monitoring.GetUptimeCheckIPsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.monitoring.</code><code class="sig-name descname">GetUptimeCheckIPsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">uptime_check_ips</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.GetUptimeCheckIPsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getUptimeCheckIPs.</p>
<dl class="py attribute">
<dt id="pulumi_gcp.monitoring.GetUptimeCheckIPsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.GetUptimeCheckIPsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.monitoring.GetUptimeCheckIPsResult.uptime_check_ips">
<code class="sig-name descname">uptime_check_ips</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.GetUptimeCheckIPsResult.uptime_check_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of uptime check IPs used by Stackdriver Monitoring. Each <code class="docutils literal notranslate"><span class="pre">uptime_check_ip</span></code> contains:</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_gcp.monitoring.Group">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.monitoring.</code><code class="sig-name descname">Group</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_cluster</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parent_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.Group" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of a dynamic collection of monitored resources. Each group
has a filter that is matched against monitored resources and their
associated metadata. If a group’s filter matches an available monitored
resource, then that resource is a member of that group.</p>
<p>To get more information about Group, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.groups">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/monitoring/groups/">Official Documentation</a></p></li>
</ul>
</li>
</ul>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gcp</span> <span class="k">as</span> <span class="nn">gcp</span>

<span class="n">basic</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">monitoring</span><span class="o">.</span><span class="n">Group</span><span class="p">(</span><span class="s2">&quot;basic&quot;</span><span class="p">,</span>
    <span class="n">display_name</span><span class="o">=</span><span class="s2">&quot;tf-test MonitoringGroup&quot;</span><span class="p">,</span>
    <span class="nb">filter</span><span class="o">=</span><span class="s2">&quot;resource.metadata.region=&quot;</span><span class="n">europe</span><span class="o">-</span><span class="n">west2</span><span class="s2">&quot;&quot;</span><span class="p">)</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gcp</span> <span class="k">as</span> <span class="nn">gcp</span>

<span class="n">parent</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">monitoring</span><span class="o">.</span><span class="n">Group</span><span class="p">(</span><span class="s2">&quot;parent&quot;</span><span class="p">,</span>
    <span class="n">display_name</span><span class="o">=</span><span class="s2">&quot;tf-test MonitoringParentGroup&quot;</span><span class="p">,</span>
    <span class="nb">filter</span><span class="o">=</span><span class="s2">&quot;resource.metadata.region=&quot;</span><span class="n">europe</span><span class="o">-</span><span class="n">west2</span><span class="s2">&quot;&quot;</span><span class="p">)</span>
<span class="n">subgroup</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">monitoring</span><span class="o">.</span><span class="n">Group</span><span class="p">(</span><span class="s2">&quot;subgroup&quot;</span><span class="p">,</span>
    <span class="n">display_name</span><span class="o">=</span><span class="s2">&quot;tf-test MonitoringSubGroup&quot;</span><span class="p">,</span>
    <span class="nb">filter</span><span class="o">=</span><span class="s2">&quot;resource.metadata.region=&quot;</span><span class="n">europe</span><span class="o">-</span><span class="n">west2</span><span class="s2">&quot;&quot;</span><span class="p">,</span>
    <span class="n">parent_name</span><span class="o">=</span><span class="n">parent</span><span class="o">.</span><span class="n">name</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A user-assigned name for this group, used only for display
purposes.</p></li>
<li><p><strong>filter</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The filter used to determine which monitored resources
belong to this group.</p></li>
<li><p><strong>is_cluster</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, the members of this group are considered to be a
cluster. The system can perform additional analysis on
groups that are clusters.</p></li>
<li><p><strong>parent_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the group’s parent, if it has one. The format is
“projects/{project_id_or_number}/groups/{group_id}”. For
groups with no parent, parentName is the empty string, “”.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_gcp.monitoring.Group.display_name">
<code class="sig-name descname">display_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.Group.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>A user-assigned name for this group, used only for display
purposes.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.monitoring.Group.filter">
<code class="sig-name descname">filter</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.Group.filter" title="Permalink to this definition">¶</a></dt>
<dd><p>The filter used to determine which monitored resources
belong to this group.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.monitoring.Group.is_cluster">
<code class="sig-name descname">is_cluster</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.Group.is_cluster" title="Permalink to this definition">¶</a></dt>
<dd><p>If true, the members of this group are considered to be a
cluster. The system can perform additional analysis on
groups that are clusters.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.monitoring.Group.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.Group.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique identifier for this group. The format is “projects/{project_id_or_number}/groups/{group_id}”.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.monitoring.Group.parent_name">
<code class="sig-name descname">parent_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.Group.parent_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the group’s parent, if it has one. The format is
“projects/{project_id_or_number}/groups/{group_id}”. For
groups with no parent, parentName is the empty string, “”.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.monitoring.Group.project">
<code class="sig-name descname">project</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.Group.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.monitoring.Group.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_cluster</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parent_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.Group.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Group resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A user-assigned name for this group, used only for display
purposes.</p></li>
<li><p><strong>filter</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The filter used to determine which monitored resources
belong to this group.</p></li>
<li><p><strong>is_cluster</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, the members of this group are considered to be a
cluster. The system can perform additional analysis on
groups that are clusters.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique identifier for this group. The format is “projects/{project_id_or_number}/groups/{group_id}”.</p></li>
<li><p><strong>parent_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the group’s parent, if it has one. The format is
“projects/{project_id_or_number}/groups/{group_id}”. For
groups with no parent, parentName is the empty string, “”.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.monitoring.Group.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.Group.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>prop</strong> (<em>str</em>) – A property name.</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>A potentially transformed property name.</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>str</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.monitoring.Group.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.Group.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>prop</strong> (<em>str</em>) – A property name.</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>A potentially transformed property name.</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>str</p>
</dd>
</dl>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_gcp.monitoring.NotificationChannel">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.monitoring.</code><code class="sig-name descname">NotificationChannel</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sensitive_labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.NotificationChannel" title="Permalink to this definition">¶</a></dt>
<dd><p>A NotificationChannel is a medium through which an alert is delivered
when a policy violation is detected. Examples of channels include email, SMS,
and third-party messaging applications. Fields containing sensitive information
like authentication tokens or contact info are only partially populated on retrieval.</p>
<p>Notification Channels are designed to be flexible and are made up of a supported <code class="docutils literal notranslate"><span class="pre">type</span></code>
and labels to configure that channel. Each <code class="docutils literal notranslate"><span class="pre">type</span></code> has specific labels that need to be
present for that channel to be correctly configured. The labels that are required to be
present for one channel <code class="docutils literal notranslate"><span class="pre">type</span></code> are often different than those required for another.
Due to these loose constraints it’s often best to set up a channel through the UI
and import it to the provider when setting up a brand new channel type to determine which
labels are required.</p>
<p>A list of supported channels per project the <code class="docutils literal notranslate"><span class="pre">list</span></code> endpoint can be
accessed programmatically or through the api explorer at  <a class="reference external" href="https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannelDescriptors/list">https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannelDescriptors/list</a> .
This provides the channel type and all of the required labels that must be passed.</p>
<p>To get more information about NotificationChannel, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannels">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/monitoring/support/notification-options">Notification Options</a></p></li>
<li><p><a class="reference external" href="https://cloud.google.com/monitoring/api/v3/">Monitoring API Documentation</a></p></li>
</ul>
</li>
</ul>
<blockquote>
<div><p><strong>Warning:</strong> All arguments including <code class="docutils literal notranslate"><span class="pre">sensitive_labels.auth_token</span></code>, <code class="docutils literal notranslate"><span class="pre">sensitive_labels.password</span></code>, and <code class="docutils literal notranslate"><span class="pre">sensitive_labels.service_key</span></code> will be stored in the raw
state as plain-text. <a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">Read more about sensitive data in state</a>.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gcp</span> <span class="k">as</span> <span class="nn">gcp</span>

<span class="n">basic</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">monitoring</span><span class="o">.</span><span class="n">NotificationChannel</span><span class="p">(</span><span class="s2">&quot;basic&quot;</span><span class="p">,</span>
    <span class="n">display_name</span><span class="o">=</span><span class="s2">&quot;Test Notification Channel&quot;</span><span class="p">,</span>
    <span class="n">labels</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;email_address&quot;</span><span class="p">:</span> <span class="s2">&quot;fake_email@blahblah.com&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;email&quot;</span><span class="p">)</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gcp</span> <span class="k">as</span> <span class="nn">gcp</span>

<span class="n">default</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">monitoring</span><span class="o">.</span><span class="n">NotificationChannel</span><span class="p">(</span><span class="s2">&quot;default&quot;</span><span class="p">,</span>
    <span class="n">display_name</span><span class="o">=</span><span class="s2">&quot;Test Slack Channel&quot;</span><span class="p">,</span>
    <span class="n">labels</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;channel_name&quot;</span><span class="p">:</span> <span class="s2">&quot;#foobar&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">sensitive_labels</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;authToken&quot;</span><span class="p">:</span> <span class="s2">&quot;one&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;slack&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An optional human-readable description of this notification channel. This description may provide additional details, beyond the display name, for the channel. This may not exceed 1024 Unicode characters.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An optional human-readable name for this notification channel. It is recommended that you specify a non-empty and unique name in order to make it easier to identify the channels in your project, though this is not enforced. The display name is limited to 512 Unicode characters.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether notifications are forwarded to the described channel. This makes it possible to disable delivery of notifications to a particular channel without removing the channel from all alerting policies that reference the channel. This is a more convenient approach when the change is temporary and you want to receive notifications from the same set of alerting policies on the channel at some point in the future.</p></li>
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration fields that define the channel and its behavior. The
permissible and required labels are specified in the
NotificationChannelDescriptor corresponding to the type field.
Labels with sensitive data are obfuscated by the API and therefore the provider cannot
determine if there are upstream changes to these fields. They can also be configured via
the sensitive_labels block, but cannot be configured in both places.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>sensitive_labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Different notification type behaviors are configured primarily using the the <code class="docutils literal notranslate"><span class="pre">labels</span></code> field on this
resource. This block contains the labels which contain secrets or passwords so that they can be marked
sensitive and hidden from plan output. The name of the field, eg: password, will be the key
in the <code class="docutils literal notranslate"><span class="pre">labels</span></code> map in the api request.
Credentials may not be specified in both locations and will cause an error. Changing from one location
to a different credential configuration in the config will require an apply to update state.  Structure is documented below.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the notification channel. This field matches the value of the NotificationChannelDescriptor.type field. See <a class="reference external" href="https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannelDescriptors/list">https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannelDescriptors/list</a> to get the list of valid values such as “email”, “slack”, etc…</p></li>
<li><p><strong>user_labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – User-supplied key/value data that does not need to conform to the corresponding NotificationChannelDescriptor’s schema, unlike the labels field. This field is intended to be used for organizing and identifying the NotificationChannel objects.The field can contain up to 64 entries. Each key and value is limited to 63 Unicode characters or 128 bytes, whichever is smaller. Labels and values can contain only lowercase letters, numerals, underscores, and dashes. Keys must begin with a letter.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>sensitive_labels</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">authToken</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An authorization token for a notification channel. Channel types that support this field include: slack  <strong>Note</strong>: This property is sensitive and will not be displayed in the plan.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An password for a notification channel. Channel types that support this field include: webhook_basicauth  <strong>Note</strong>: This property is sensitive and will not be displayed in the plan.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An servicekey token for a notification channel. Channel types that support this field include: pagerduty  <strong>Note</strong>: This property is sensitive and will not be displayed in the plan.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_gcp.monitoring.NotificationChannel.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.NotificationChannel.description" title="Permalink to this definition">¶</a></dt>
<dd><p>An optional human-readable description of this notification channel. This description may provide additional details, beyond the display name, for the channel. This may not exceed 1024 Unicode characters.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.monitoring.NotificationChannel.display_name">
<code class="sig-name descname">display_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.NotificationChannel.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>An optional human-readable name for this notification channel. It is recommended that you specify a non-empty and unique name in order to make it easier to identify the channels in your project, though this is not enforced. The display name is limited to 512 Unicode characters.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.monitoring.NotificationChannel.enabled">
<code class="sig-name descname">enabled</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.NotificationChannel.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether notifications are forwarded to the described channel. This makes it possible to disable delivery of notifications to a particular channel without removing the channel from all alerting policies that reference the channel. This is a more convenient approach when the change is temporary and you want to receive notifications from the same set of alerting policies on the channel at some point in the future.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.monitoring.NotificationChannel.labels">
<code class="sig-name descname">labels</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.NotificationChannel.labels" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration fields that define the channel and its behavior. The
permissible and required labels are specified in the
NotificationChannelDescriptor corresponding to the type field.
Labels with sensitive data are obfuscated by the API and therefore the provider cannot
determine if there are upstream changes to these fields. They can also be configured via
the sensitive_labels block, but cannot be configured in both places.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.monitoring.NotificationChannel.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.NotificationChannel.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The full REST resource name for this channel. The syntax is: projects/[PROJECT_ID]/notificationChannels/[CHANNEL_ID] The
[CHANNEL_ID] is automatically assigned by the server on creation.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.monitoring.NotificationChannel.project">
<code class="sig-name descname">project</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.NotificationChannel.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.monitoring.NotificationChannel.sensitive_labels">
<code class="sig-name descname">sensitive_labels</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.NotificationChannel.sensitive_labels" title="Permalink to this definition">¶</a></dt>
<dd><p>Different notification type behaviors are configured primarily using the the <code class="docutils literal notranslate"><span class="pre">labels</span></code> field on this
resource. This block contains the labels which contain secrets or passwords so that they can be marked
sensitive and hidden from plan output. The name of the field, eg: password, will be the key
in the <code class="docutils literal notranslate"><span class="pre">labels</span></code> map in the api request.
Credentials may not be specified in both locations and will cause an error. Changing from one location
to a different credential configuration in the config will require an apply to update state.  Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">authToken</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - An authorization token for a notification channel. Channel types that support this field include: slack  <strong>Note</strong>: This property is sensitive and will not be displayed in the plan.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - An password for a notification channel. Channel types that support this field include: webhook_basicauth  <strong>Note</strong>: This property is sensitive and will not be displayed in the plan.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - An servicekey token for a notification channel. Channel types that support this field include: pagerduty  <strong>Note</strong>: This property is sensitive and will not be displayed in the plan.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.monitoring.NotificationChannel.type">
<code class="sig-name descname">type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.NotificationChannel.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the notification channel. This field matches the value of the NotificationChannelDescriptor.type field. See <a class="reference external" href="https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannelDescriptors/list">https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannelDescriptors/list</a> to get the list of valid values such as “email”, “slack”, etc…</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.monitoring.NotificationChannel.user_labels">
<code class="sig-name descname">user_labels</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.NotificationChannel.user_labels" title="Permalink to this definition">¶</a></dt>
<dd><p>User-supplied key/value data that does not need to conform to the corresponding NotificationChannelDescriptor’s schema, unlike the labels field. This field is intended to be used for organizing and identifying the NotificationChannel objects.The field can contain up to 64 entries. Each key and value is limited to 63 Unicode characters or 128 bytes, whichever is smaller. Labels and values can contain only lowercase letters, numerals, underscores, and dashes. Keys must begin with a letter.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.monitoring.NotificationChannel.verification_status">
<code class="sig-name descname">verification_status</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.NotificationChannel.verification_status" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether this channel has been verified or not. On a ListNotificationChannels or GetNotificationChannel
operation, this field is expected to be populated.If the value is UNVERIFIED, then it indicates that the channel is
non-functioning (it both requires verification and lacks verification); otherwise, it is assumed that the channel
works.If the channel is neither VERIFIED nor UNVERIFIED, it implies that the channel is of a type that does not require
verification or that this specific channel has been exempted from verification because it was created prior to
verification being required for channels of this type.This field cannot be modified using a standard
UpdateNotificationChannel operation. To change the value of this field, you must call VerifyNotificationChannel.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.monitoring.NotificationChannel.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sensitive_labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">verification_status</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.NotificationChannel.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing NotificationChannel resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An optional human-readable description of this notification channel. This description may provide additional details, beyond the display name, for the channel. This may not exceed 1024 Unicode characters.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An optional human-readable name for this notification channel. It is recommended that you specify a non-empty and unique name in order to make it easier to identify the channels in your project, though this is not enforced. The display name is limited to 512 Unicode characters.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether notifications are forwarded to the described channel. This makes it possible to disable delivery of notifications to a particular channel without removing the channel from all alerting policies that reference the channel. This is a more convenient approach when the change is temporary and you want to receive notifications from the same set of alerting policies on the channel at some point in the future.</p></li>
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration fields that define the channel and its behavior. The
permissible and required labels are specified in the
NotificationChannelDescriptor corresponding to the type field.
Labels with sensitive data are obfuscated by the API and therefore the provider cannot
determine if there are upstream changes to these fields. They can also be configured via
the sensitive_labels block, but cannot be configured in both places.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The full REST resource name for this channel. The syntax is: projects/[PROJECT_ID]/notificationChannels/[CHANNEL_ID] The
[CHANNEL_ID] is automatically assigned by the server on creation.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>sensitive_labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Different notification type behaviors are configured primarily using the the <code class="docutils literal notranslate"><span class="pre">labels</span></code> field on this
resource. This block contains the labels which contain secrets or passwords so that they can be marked
sensitive and hidden from plan output. The name of the field, eg: password, will be the key
in the <code class="docutils literal notranslate"><span class="pre">labels</span></code> map in the api request.
Credentials may not be specified in both locations and will cause an error. Changing from one location
to a different credential configuration in the config will require an apply to update state.  Structure is documented below.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the notification channel. This field matches the value of the NotificationChannelDescriptor.type field. See <a class="reference external" href="https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannelDescriptors/list">https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannelDescriptors/list</a> to get the list of valid values such as “email”, “slack”, etc…</p></li>
<li><p><strong>user_labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – User-supplied key/value data that does not need to conform to the corresponding NotificationChannelDescriptor’s schema, unlike the labels field. This field is intended to be used for organizing and identifying the NotificationChannel objects.The field can contain up to 64 entries. Each key and value is limited to 63 Unicode characters or 128 bytes, whichever is smaller. Labels and values can contain only lowercase letters, numerals, underscores, and dashes. Keys must begin with a letter.</p></li>
<li><p><strong>verification_status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Indicates whether this channel has been verified or not. On a ListNotificationChannels or GetNotificationChannel
operation, this field is expected to be populated.If the value is UNVERIFIED, then it indicates that the channel is
non-functioning (it both requires verification and lacks verification); otherwise, it is assumed that the channel
works.If the channel is neither VERIFIED nor UNVERIFIED, it implies that the channel is of a type that does not require
verification or that this specific channel has been exempted from verification because it was created prior to
verification being required for channels of this type.This field cannot be modified using a standard
UpdateNotificationChannel operation. To change the value of this field, you must call VerifyNotificationChannel.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>sensitive_labels</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">authToken</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An authorization token for a notification channel. Channel types that support this field include: slack  <strong>Note</strong>: This property is sensitive and will not be displayed in the plan.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An password for a notification channel. Channel types that support this field include: webhook_basicauth  <strong>Note</strong>: This property is sensitive and will not be displayed in the plan.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An servicekey token for a notification channel. Channel types that support this field include: pagerduty  <strong>Note</strong>: This property is sensitive and will not be displayed in the plan.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.monitoring.NotificationChannel.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.NotificationChannel.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>prop</strong> (<em>str</em>) – A property name.</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>A potentially transformed property name.</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>str</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.monitoring.NotificationChannel.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.NotificationChannel.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>prop</strong> (<em>str</em>) – A property name.</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>A potentially transformed property name.</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>str</p>
</dd>
</dl>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_gcp.monitoring.Slo">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.monitoring.</code><code class="sig-name descname">Slo</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">basic_sli</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">calendar_period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">goal</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rolling_period_days</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">slo_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.Slo" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Slo resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[dict] basic_sli: Basic Service-Level Indicator (SLI) on a well-known service type.</p>
<blockquote>
<div><p>Performance will be computed on the basis of pre-defined metrics.
SLIs are used to measure and calculate the quality of the Service’s
performance with respect to a single aspect of service quality.  Structure is documented below.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>calendar_period</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A calendar period, semantically “since the start of the current
<span class="raw-html-m2r"><calendarPeriod></span>”.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name used for UI elements listing this SLO.</p></li>
<li><p><strong>goal</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The fraction of service that must be good in order for this objective
to be met. 0 &lt; goal &lt;= 0.999</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>rolling_period_days</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – A rolling time period, semantically “in the past X days”.
Must be between 1 to 30 days, inclusive.</p></li>
<li><p><strong>service</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the service to which this SLO belongs.</p></li>
<li><p><strong>slo_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id to use for this ServiceLevelObjective. If omitted, an id will be generated instead.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>basic_sli</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">latency</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Parameters for a latency threshold SLI.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">threshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A duration string, e.g. 10s.
Good service is defined to be the count of requests made to
this service that return in no more than threshold.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">locations</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - An optional set of locations to which this SLI is relevant.
Telemetry from other locations will not be used to calculate
performance for this SLI. If omitted, this SLI applies to all
locations in which the Service has activity. For service types
that don’t support breaking down by location, setting this
field will result in an error.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">methods</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - An optional set of RPCs to which this SLI is relevant.
Telemetry from other methods will not be used to calculate
performance for this SLI. If omitted, this SLI applies to all
the Service’s methods. For service types that don’t support
breaking down by method, setting this field will result in an
error.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">versions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The set of API versions to which this SLI is relevant.
Telemetry from other API versions will not be used to
calculate performance for this SLI. If omitted,
this SLI applies to all API versions. For service types
that don’t support breaking down by version, setting this
field will result in an error.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_gcp.monitoring.Slo.basic_sli">
<code class="sig-name descname">basic_sli</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.Slo.basic_sli" title="Permalink to this definition">¶</a></dt>
<dd><p>Basic Service-Level Indicator (SLI) on a well-known service type.
Performance will be computed on the basis of pre-defined metrics.
SLIs are used to measure and calculate the quality of the Service’s
performance with respect to a single aspect of service quality.  Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">latency</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Parameters for a latency threshold SLI.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">threshold</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A duration string, e.g. 10s.
Good service is defined to be the count of requests made to
this service that return in no more than threshold.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">locations</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - An optional set of locations to which this SLI is relevant.
Telemetry from other locations will not be used to calculate
performance for this SLI. If omitted, this SLI applies to all
locations in which the Service has activity. For service types
that don’t support breaking down by location, setting this
field will result in an error.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">methods</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - An optional set of RPCs to which this SLI is relevant.
Telemetry from other methods will not be used to calculate
performance for this SLI. If omitted, this SLI applies to all
the Service’s methods. For service types that don’t support
breaking down by method, setting this field will result in an
error.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">versions</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The set of API versions to which this SLI is relevant.
Telemetry from other API versions will not be used to
calculate performance for this SLI. If omitted,
this SLI applies to all API versions. For service types
that don’t support breaking down by version, setting this
field will result in an error.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.monitoring.Slo.calendar_period">
<code class="sig-name descname">calendar_period</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.Slo.calendar_period" title="Permalink to this definition">¶</a></dt>
<dd><p>A calendar period, semantically “since the start of the current</p>
<p><span class="raw-html-m2r"><calendarPeriod></span>”.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.monitoring.Slo.display_name">
<code class="sig-name descname">display_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.Slo.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name used for UI elements listing this SLO.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.monitoring.Slo.goal">
<code class="sig-name descname">goal</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.Slo.goal" title="Permalink to this definition">¶</a></dt>
<dd><p>The fraction of service that must be good in order for this objective
to be met. 0 &lt; goal &lt;= 0.999</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.monitoring.Slo.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.Slo.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The full resource name for this service. The syntax is:
projects/[PROJECT_ID_OR_NUMBER]/services/[SERVICE_ID]/serviceLevelObjectives/[SLO_NAME]</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.monitoring.Slo.project">
<code class="sig-name descname">project</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.Slo.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.monitoring.Slo.rolling_period_days">
<code class="sig-name descname">rolling_period_days</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.Slo.rolling_period_days" title="Permalink to this definition">¶</a></dt>
<dd><p>A rolling time period, semantically “in the past X days”.
Must be between 1 to 30 days, inclusive.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.monitoring.Slo.service">
<code class="sig-name descname">service</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.Slo.service" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the service to which this SLO belongs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.monitoring.Slo.slo_id">
<code class="sig-name descname">slo_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.Slo.slo_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id to use for this ServiceLevelObjective. If omitted, an id will be generated instead.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.monitoring.Slo.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">basic_sli</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">calendar_period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">goal</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rolling_period_days</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">slo_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.Slo.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Slo resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>basic_sli</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Basic Service-Level Indicator (SLI) on a well-known service type.
Performance will be computed on the basis of pre-defined metrics.
SLIs are used to measure and calculate the quality of the Service’s
performance with respect to a single aspect of service quality.  Structure is documented below.</p></li>
<li><p><strong>calendar_period</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A calendar period, semantically “since the start of the current
<span class="raw-html-m2r"><calendarPeriod></span>”.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name used for UI elements listing this SLO.</p></li>
<li><p><strong>goal</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The fraction of service that must be good in order for this objective
to be met. 0 &lt; goal &lt;= 0.999</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The full resource name for this service. The syntax is:
projects/[PROJECT_ID_OR_NUMBER]/services/[SERVICE_ID]/serviceLevelObjectives/[SLO_NAME]</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>rolling_period_days</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – A rolling time period, semantically “in the past X days”.
Must be between 1 to 30 days, inclusive.</p></li>
<li><p><strong>service</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the service to which this SLO belongs.</p></li>
<li><p><strong>slo_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id to use for this ServiceLevelObjective. If omitted, an id will be generated instead.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>basic_sli</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">latency</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Parameters for a latency threshold SLI.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">threshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A duration string, e.g. 10s.
Good service is defined to be the count of requests made to
this service that return in no more than threshold.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">locations</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - An optional set of locations to which this SLI is relevant.
Telemetry from other locations will not be used to calculate
performance for this SLI. If omitted, this SLI applies to all
locations in which the Service has activity. For service types
that don’t support breaking down by location, setting this
field will result in an error.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">methods</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - An optional set of RPCs to which this SLI is relevant.
Telemetry from other methods will not be used to calculate
performance for this SLI. If omitted, this SLI applies to all
the Service’s methods. For service types that don’t support
breaking down by method, setting this field will result in an
error.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">versions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The set of API versions to which this SLI is relevant.
Telemetry from other API versions will not be used to
calculate performance for this SLI. If omitted,
this SLI applies to all API versions. For service types
that don’t support breaking down by version, setting this
field will result in an error.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.monitoring.Slo.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.Slo.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>prop</strong> (<em>str</em>) – A property name.</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>A potentially transformed property name.</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>str</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.monitoring.Slo.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.Slo.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>prop</strong> (<em>str</em>) – A property name.</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>A potentially transformed property name.</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>str</p>
</dd>
</dl>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_gcp.monitoring.UptimeCheckConfig">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.monitoring.</code><code class="sig-name descname">UptimeCheckConfig</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">content_matchers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">http_check</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">monitored_resource</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">selected_regions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tcp_check</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.UptimeCheckConfig" title="Permalink to this definition">¶</a></dt>
<dd><p>This message configures which resources and services to monitor for availability.</p>
<p>To get more information about UptimeCheckConfig, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/monitoring/uptime-checks/">Official Documentation</a></p></li>
</ul>
</li>
</ul>
<blockquote>
<div><p><strong>Warning:</strong> All arguments including <code class="docutils literal notranslate"><span class="pre">http_check.auth_info.password</span></code> will be stored in the raw
state as plain-text. <a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">Read more about sensitive data in state</a>.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gcp</span> <span class="k">as</span> <span class="nn">gcp</span>

<span class="n">http</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">monitoring</span><span class="o">.</span><span class="n">UptimeCheckConfig</span><span class="p">(</span><span class="s2">&quot;http&quot;</span><span class="p">,</span>
    <span class="n">content_matchers</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;content&quot;</span><span class="p">:</span> <span class="s2">&quot;example&quot;</span><span class="p">,</span>
    <span class="p">}],</span>
    <span class="n">display_name</span><span class="o">=</span><span class="s2">&quot;http-uptime-check&quot;</span><span class="p">,</span>
    <span class="n">http_check</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;path&quot;</span><span class="p">:</span> <span class="s2">&quot;/some-path&quot;</span><span class="p">,</span>
        <span class="s2">&quot;port&quot;</span><span class="p">:</span> <span class="s2">&quot;8010&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">monitored_resource</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;labels&quot;</span><span class="p">:</span> <span class="p">{</span>
            <span class="s2">&quot;host&quot;</span><span class="p">:</span> <span class="s2">&quot;192.168.1.1&quot;</span><span class="p">,</span>
            <span class="s2">&quot;project_id&quot;</span><span class="p">:</span> <span class="s2">&quot;my-project-name&quot;</span><span class="p">,</span>
        <span class="p">},</span>
        <span class="s2">&quot;type&quot;</span><span class="p">:</span> <span class="s2">&quot;uptime_url&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">timeout</span><span class="o">=</span><span class="s2">&quot;60s&quot;</span><span class="p">)</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gcp</span> <span class="k">as</span> <span class="nn">gcp</span>

<span class="n">https</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">monitoring</span><span class="o">.</span><span class="n">UptimeCheckConfig</span><span class="p">(</span><span class="s2">&quot;https&quot;</span><span class="p">,</span>
    <span class="n">content_matchers</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;content&quot;</span><span class="p">:</span> <span class="s2">&quot;example&quot;</span><span class="p">,</span>
    <span class="p">}],</span>
    <span class="n">display_name</span><span class="o">=</span><span class="s2">&quot;https-uptime-check&quot;</span><span class="p">,</span>
    <span class="n">http_check</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;path&quot;</span><span class="p">:</span> <span class="s2">&quot;/some-path&quot;</span><span class="p">,</span>
        <span class="s2">&quot;port&quot;</span><span class="p">:</span> <span class="s2">&quot;443&quot;</span><span class="p">,</span>
        <span class="s2">&quot;useSsl&quot;</span><span class="p">:</span> <span class="kc">True</span><span class="p">,</span>
        <span class="s2">&quot;validateSsl&quot;</span><span class="p">:</span> <span class="kc">True</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">monitored_resource</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;labels&quot;</span><span class="p">:</span> <span class="p">{</span>
            <span class="s2">&quot;host&quot;</span><span class="p">:</span> <span class="s2">&quot;192.168.1.1&quot;</span><span class="p">,</span>
            <span class="s2">&quot;project_id&quot;</span><span class="p">:</span> <span class="s2">&quot;my-project-name&quot;</span><span class="p">,</span>
        <span class="p">},</span>
        <span class="s2">&quot;type&quot;</span><span class="p">:</span> <span class="s2">&quot;uptime_url&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">timeout</span><span class="o">=</span><span class="s2">&quot;60s&quot;</span><span class="p">)</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gcp</span> <span class="k">as</span> <span class="nn">gcp</span>

<span class="n">check</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">monitoring</span><span class="o">.</span><span class="n">Group</span><span class="p">(</span><span class="s2">&quot;check&quot;</span><span class="p">,</span>
    <span class="n">display_name</span><span class="o">=</span><span class="s2">&quot;uptime-check-group&quot;</span><span class="p">,</span>
    <span class="nb">filter</span><span class="o">=</span><span class="s2">&quot;resource.metadata.name=has_substring(&quot;</span><span class="n">foo</span><span class="s2">&quot;)&quot;</span><span class="p">)</span>
<span class="n">tcp_group</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">monitoring</span><span class="o">.</span><span class="n">UptimeCheckConfig</span><span class="p">(</span><span class="s2">&quot;tcpGroup&quot;</span><span class="p">,</span>
    <span class="n">display_name</span><span class="o">=</span><span class="s2">&quot;tcp-uptime-check&quot;</span><span class="p">,</span>
    <span class="n">timeout</span><span class="o">=</span><span class="s2">&quot;60s&quot;</span><span class="p">,</span>
    <span class="n">tcp_check</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;port&quot;</span><span class="p">:</span> <span class="mi">888</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">resource_group</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;resourceType&quot;</span><span class="p">:</span> <span class="s2">&quot;INSTANCE&quot;</span><span class="p">,</span>
        <span class="s2">&quot;groupId&quot;</span><span class="p">:</span> <span class="n">check</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="p">})</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>content_matchers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The expected content on the page the check is run against. Currently, only the first entry in the list is supported, and other entries will be ignored. The server will look for an exact match of the string in the page response’s content. This field is optional and should only be specified if a content match is required.  Structure is documented below.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-friendly name for the uptime check configuration. The display name should be unique within a Stackdriver Workspace in order to make it easier to identify; however, uniqueness is not enforced.</p></li>
<li><p><strong>http_check</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Contains information needed to make an HTTP or HTTPS check.  Structure is documented below.</p></li>
<li><p><strong>monitored_resource</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The monitored resource (<a class="reference external" href="https://cloud.google.com/monitoring/api/resources">https://cloud.google.com/monitoring/api/resources</a>) associated with the configuration. The following monitored resource types are supported for uptime checks:  uptime_url  gce_instance  gae_app  aws_ec2_instance  aws_elb_load_balancer  Structure is documented below.</p></li>
<li><p><strong>period</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – How often, in seconds, the uptime check is performed. Currently, the only supported values are 60s (1 minute), 300s (5 minutes), 600s (10 minutes), and 900s (15 minutes). Optional, defaults to 300s.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>resource_group</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The group resource associated with the configuration.  Structure is documented below.</p></li>
<li><p><strong>selected_regions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of regions from which the check will be run. Some regions contain one location, and others contain more than one. If this field is specified, enough regions to include a minimum of 3 locations must be provided, or an error message is returned. Not specifying this field will result in uptime checks running from all regions.</p></li>
<li><p><strong>tcp_check</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Contains information needed to make a TCP check.  Structure is documented below.</p></li>
<li><p><strong>timeout</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The maximum amount of time to wait for the request to complete (must be between 1 and 60 seconds). Accepted formats <a class="reference external" href="https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration">https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration</a></p></li>
</ul>
</dd>
</dl>
<p>The <strong>content_matchers</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">content</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String or regex content to match (max 1024 bytes)</p></li>
</ul>
<p>The <strong>http_check</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">authInfo</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The authentication information. Optional when creating an HTTP check; defaults to empty.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The password to authenticate.  <strong>Note</strong>: This property is sensitive and will not be displayed in the plan.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The username to authenticate.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">headers</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The list of headers to send as part of the uptime check request. If two headers have the same key and different values, they should be entered as a single header, with the value being a comma-separated list of all the desired values as described at <a class="reference external" href="https://www.w3.org/Protocols/rfc2616/rfc2616.txt">https://www.w3.org/Protocols/rfc2616/rfc2616.txt</a> (page 31). Entering two separate headers with the same key in a Create call will cause the first to be overwritten by the second. The maximum number of headers allowed is 100.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maskHeaders</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean specifying whether to encrypt the header information. Encryption should be specified for any headers related to authentication that you do not wish to be seen when retrieving the configuration. The server will be responsible for encrypting the headers. On Get/List calls, if mask_headers is set to True then the headers will be obscured with <strong>**</strong>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path to the page to run the check against. Will be combined with the host (specified within the MonitoredResource) and port to construct the full URL. Optional (defaults to “/”).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The port to the page to run the check against. Will be combined with host (specified within the MonitoredResource) to construct the full URL.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useSsl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - If true, use HTTPS instead of HTTP to run the check.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">validateSsl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean specifying whether to include SSL certificate validation as a part of the Uptime check. Only applies to checks where monitoredResource is set to uptime_url. If useSsl is false, setting validateSsl to true has no effect.</p></li>
</ul>
<p>The <strong>monitored_resource</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">labels</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Values for all of the labels listed in the associated monitored resource descriptor. For example, Compute Engine VM instances use the labels “project_id”, “instance_id”, and “zone”.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The monitored resource type. This field must match the type field of a MonitoredResourceDescriptor (<a class="reference external" href="https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.monitoredResourceDescriptors#MonitoredResourceDescriptor">https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.monitoredResourceDescriptors#MonitoredResourceDescriptor</a>) object. For example, the type of a Compute Engine VM instance is gce_instance. For a list of types, see Monitoring resource types (<a class="reference external" href="https://cloud.google.com/monitoring/api/resources">https://cloud.google.com/monitoring/api/resources</a>) and Logging resource types (<a class="reference external" href="https://cloud.google.com/logging/docs/api/v2/resource-list">https://cloud.google.com/logging/docs/api/v2/resource-list</a>).</p></li>
</ul>
<p>The <strong>resource_group</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">groupId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The group of resources being monitored. Should be the <code class="docutils literal notranslate"><span class="pre">name</span></code> of a group</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resourceType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The resource type of the group members.</p></li>
</ul>
<p>The <strong>tcp_check</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The port to the page to run the check against. Will be combined with host (specified within the MonitoredResource) to construct the full URL.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_gcp.monitoring.UptimeCheckConfig.content_matchers">
<code class="sig-name descname">content_matchers</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.UptimeCheckConfig.content_matchers" title="Permalink to this definition">¶</a></dt>
<dd><p>The expected content on the page the check is run against. Currently, only the first entry in the list is supported, and other entries will be ignored. The server will look for an exact match of the string in the page response’s content. This field is optional and should only be specified if a content match is required.  Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">content</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - String or regex content to match (max 1024 bytes)</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.monitoring.UptimeCheckConfig.display_name">
<code class="sig-name descname">display_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.UptimeCheckConfig.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>A human-friendly name for the uptime check configuration. The display name should be unique within a Stackdriver Workspace in order to make it easier to identify; however, uniqueness is not enforced.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.monitoring.UptimeCheckConfig.http_check">
<code class="sig-name descname">http_check</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.UptimeCheckConfig.http_check" title="Permalink to this definition">¶</a></dt>
<dd><p>Contains information needed to make an HTTP or HTTPS check.  Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">authInfo</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The authentication information. Optional when creating an HTTP check; defaults to empty.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The password to authenticate.  <strong>Note</strong>: This property is sensitive and will not be displayed in the plan.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The username to authenticate.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">headers</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The list of headers to send as part of the uptime check request. If two headers have the same key and different values, they should be entered as a single header, with the value being a comma-separated list of all the desired values as described at <a class="reference external" href="https://www.w3.org/Protocols/rfc2616/rfc2616.txt">https://www.w3.org/Protocols/rfc2616/rfc2616.txt</a> (page 31). Entering two separate headers with the same key in a Create call will cause the first to be overwritten by the second. The maximum number of headers allowed is 100.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maskHeaders</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Boolean specifying whether to encrypt the header information. Encryption should be specified for any headers related to authentication that you do not wish to be seen when retrieving the configuration. The server will be responsible for encrypting the headers. On Get/List calls, if mask_headers is set to True then the headers will be obscured with <strong>**</strong>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The path to the page to run the check against. Will be combined with the host (specified within the MonitoredResource) and port to construct the full URL. Optional (defaults to “/”).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The port to the page to run the check against. Will be combined with host (specified within the MonitoredResource) to construct the full URL.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useSsl</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - If true, use HTTPS instead of HTTP to run the check.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">validateSsl</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Boolean specifying whether to include SSL certificate validation as a part of the Uptime check. Only applies to checks where monitoredResource is set to uptime_url. If useSsl is false, setting validateSsl to true has no effect.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.monitoring.UptimeCheckConfig.monitored_resource">
<code class="sig-name descname">monitored_resource</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.UptimeCheckConfig.monitored_resource" title="Permalink to this definition">¶</a></dt>
<dd><p>The monitored resource (<a class="reference external" href="https://cloud.google.com/monitoring/api/resources">https://cloud.google.com/monitoring/api/resources</a>) associated with the configuration. The following monitored resource types are supported for uptime checks:  uptime_url  gce_instance  gae_app  aws_ec2_instance  aws_elb_load_balancer  Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">labels</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Values for all of the labels listed in the associated monitored resource descriptor. For example, Compute Engine VM instances use the labels “project_id”, “instance_id”, and “zone”.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The monitored resource type. This field must match the type field of a MonitoredResourceDescriptor (<a class="reference external" href="https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.monitoredResourceDescriptors#MonitoredResourceDescriptor">https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.monitoredResourceDescriptors#MonitoredResourceDescriptor</a>) object. For example, the type of a Compute Engine VM instance is gce_instance. For a list of types, see Monitoring resource types (<a class="reference external" href="https://cloud.google.com/monitoring/api/resources">https://cloud.google.com/monitoring/api/resources</a>) and Logging resource types (<a class="reference external" href="https://cloud.google.com/logging/docs/api/v2/resource-list">https://cloud.google.com/logging/docs/api/v2/resource-list</a>).</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.monitoring.UptimeCheckConfig.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.UptimeCheckConfig.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique resource name for this UptimeCheckConfig. The format is
projects/[PROJECT_ID]/uptimeCheckConfigs/[UPTIME_CHECK_ID].</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.monitoring.UptimeCheckConfig.period">
<code class="sig-name descname">period</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.UptimeCheckConfig.period" title="Permalink to this definition">¶</a></dt>
<dd><p>How often, in seconds, the uptime check is performed. Currently, the only supported values are 60s (1 minute), 300s (5 minutes), 600s (10 minutes), and 900s (15 minutes). Optional, defaults to 300s.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.monitoring.UptimeCheckConfig.project">
<code class="sig-name descname">project</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.UptimeCheckConfig.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.monitoring.UptimeCheckConfig.resource_group">
<code class="sig-name descname">resource_group</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.UptimeCheckConfig.resource_group" title="Permalink to this definition">¶</a></dt>
<dd><p>The group resource associated with the configuration.  Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">groupId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The group of resources being monitored. Should be the <code class="docutils literal notranslate"><span class="pre">name</span></code> of a group</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resourceType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The resource type of the group members.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.monitoring.UptimeCheckConfig.selected_regions">
<code class="sig-name descname">selected_regions</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.UptimeCheckConfig.selected_regions" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of regions from which the check will be run. Some regions contain one location, and others contain more than one. If this field is specified, enough regions to include a minimum of 3 locations must be provided, or an error message is returned. Not specifying this field will result in uptime checks running from all regions.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.monitoring.UptimeCheckConfig.tcp_check">
<code class="sig-name descname">tcp_check</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.UptimeCheckConfig.tcp_check" title="Permalink to this definition">¶</a></dt>
<dd><p>Contains information needed to make a TCP check.  Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The port to the page to run the check against. Will be combined with host (specified within the MonitoredResource) to construct the full URL.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.monitoring.UptimeCheckConfig.timeout">
<code class="sig-name descname">timeout</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.UptimeCheckConfig.timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum amount of time to wait for the request to complete (must be between 1 and 60 seconds). Accepted formats <a class="reference external" href="https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration">https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration</a></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.monitoring.UptimeCheckConfig.uptime_check_id">
<code class="sig-name descname">uptime_check_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.UptimeCheckConfig.uptime_check_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the uptime check</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.monitoring.UptimeCheckConfig.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">content_matchers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">http_check</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">monitored_resource</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">selected_regions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tcp_check</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">uptime_check_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.UptimeCheckConfig.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing UptimeCheckConfig resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>content_matchers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The expected content on the page the check is run against. Currently, only the first entry in the list is supported, and other entries will be ignored. The server will look for an exact match of the string in the page response’s content. This field is optional and should only be specified if a content match is required.  Structure is documented below.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-friendly name for the uptime check configuration. The display name should be unique within a Stackdriver Workspace in order to make it easier to identify; however, uniqueness is not enforced.</p></li>
<li><p><strong>http_check</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Contains information needed to make an HTTP or HTTPS check.  Structure is documented below.</p></li>
<li><p><strong>monitored_resource</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The monitored resource (<a class="reference external" href="https://cloud.google.com/monitoring/api/resources">https://cloud.google.com/monitoring/api/resources</a>) associated with the configuration. The following monitored resource types are supported for uptime checks:  uptime_url  gce_instance  gae_app  aws_ec2_instance  aws_elb_load_balancer  Structure is documented below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique resource name for this UptimeCheckConfig. The format is
projects/[PROJECT_ID]/uptimeCheckConfigs/[UPTIME_CHECK_ID].</p></li>
<li><p><strong>period</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – How often, in seconds, the uptime check is performed. Currently, the only supported values are 60s (1 minute), 300s (5 minutes), 600s (10 minutes), and 900s (15 minutes). Optional, defaults to 300s.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>resource_group</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The group resource associated with the configuration.  Structure is documented below.</p></li>
<li><p><strong>selected_regions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of regions from which the check will be run. Some regions contain one location, and others contain more than one. If this field is specified, enough regions to include a minimum of 3 locations must be provided, or an error message is returned. Not specifying this field will result in uptime checks running from all regions.</p></li>
<li><p><strong>tcp_check</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Contains information needed to make a TCP check.  Structure is documented below.</p></li>
<li><p><strong>timeout</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The maximum amount of time to wait for the request to complete (must be between 1 and 60 seconds). Accepted formats <a class="reference external" href="https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration">https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration</a></p></li>
<li><p><strong>uptime_check_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the uptime check</p></li>
</ul>
</dd>
</dl>
<p>The <strong>content_matchers</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">content</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String or regex content to match (max 1024 bytes)</p></li>
</ul>
<p>The <strong>http_check</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">authInfo</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The authentication information. Optional when creating an HTTP check; defaults to empty.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The password to authenticate.  <strong>Note</strong>: This property is sensitive and will not be displayed in the plan.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The username to authenticate.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">headers</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The list of headers to send as part of the uptime check request. If two headers have the same key and different values, they should be entered as a single header, with the value being a comma-separated list of all the desired values as described at <a class="reference external" href="https://www.w3.org/Protocols/rfc2616/rfc2616.txt">https://www.w3.org/Protocols/rfc2616/rfc2616.txt</a> (page 31). Entering two separate headers with the same key in a Create call will cause the first to be overwritten by the second. The maximum number of headers allowed is 100.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maskHeaders</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean specifying whether to encrypt the header information. Encryption should be specified for any headers related to authentication that you do not wish to be seen when retrieving the configuration. The server will be responsible for encrypting the headers. On Get/List calls, if mask_headers is set to True then the headers will be obscured with <strong>**</strong>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path to the page to run the check against. Will be combined with the host (specified within the MonitoredResource) and port to construct the full URL. Optional (defaults to “/”).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The port to the page to run the check against. Will be combined with host (specified within the MonitoredResource) to construct the full URL.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useSsl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - If true, use HTTPS instead of HTTP to run the check.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">validateSsl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean specifying whether to include SSL certificate validation as a part of the Uptime check. Only applies to checks where monitoredResource is set to uptime_url. If useSsl is false, setting validateSsl to true has no effect.</p></li>
</ul>
<p>The <strong>monitored_resource</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">labels</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Values for all of the labels listed in the associated monitored resource descriptor. For example, Compute Engine VM instances use the labels “project_id”, “instance_id”, and “zone”.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The monitored resource type. This field must match the type field of a MonitoredResourceDescriptor (<a class="reference external" href="https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.monitoredResourceDescriptors#MonitoredResourceDescriptor">https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.monitoredResourceDescriptors#MonitoredResourceDescriptor</a>) object. For example, the type of a Compute Engine VM instance is gce_instance. For a list of types, see Monitoring resource types (<a class="reference external" href="https://cloud.google.com/monitoring/api/resources">https://cloud.google.com/monitoring/api/resources</a>) and Logging resource types (<a class="reference external" href="https://cloud.google.com/logging/docs/api/v2/resource-list">https://cloud.google.com/logging/docs/api/v2/resource-list</a>).</p></li>
</ul>
<p>The <strong>resource_group</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">groupId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The group of resources being monitored. Should be the <code class="docutils literal notranslate"><span class="pre">name</span></code> of a group</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resourceType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The resource type of the group members.</p></li>
</ul>
<p>The <strong>tcp_check</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The port to the page to run the check against. Will be combined with host (specified within the MonitoredResource) to construct the full URL.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.monitoring.UptimeCheckConfig.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.UptimeCheckConfig.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>prop</strong> (<em>str</em>) – A property name.</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>A potentially transformed property name.</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>str</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.monitoring.UptimeCheckConfig.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.UptimeCheckConfig.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>prop</strong> (<em>str</em>) – A property name.</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>A potentially transformed property name.</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>str</p>
</dd>
</dl>
</dd></dl>

</dd></dl>

<dl class="py function">
<dt id="pulumi_gcp.monitoring.get_app_engine_service">
<code class="sig-prename descclassname">pulumi_gcp.monitoring.</code><code class="sig-name descname">get_app_engine_service</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">module_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.get_app_engine_service" title="Permalink to this definition">¶</a></dt>
<dd><p>A Monitoring Service is the root resource under which operational aspects of a
generic service are accessible. A service is some discrete, autonomous, and
network-accessible unit, designed to solve an individual concern</p>
<p>An App Engine monitoring service is automatically created by GCP to monitor
App Engine services.</p>
<p>To get more information about Service, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/monitoring/api/ref_v3/rest/v3/services">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/monitoring/service-monitoring">Service Monitoring</a></p></li>
<li><p><a class="reference external" href="https://cloud.google.com/monitoring/api/v3/">Monitoring API Documentation</a></p></li>
</ul>
</li>
</ul>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gcp</span> <span class="k">as</span> <span class="nn">gcp</span>

<span class="n">bucket</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">storage</span><span class="o">.</span><span class="n">Bucket</span><span class="p">(</span><span class="s2">&quot;bucket&quot;</span><span class="p">)</span>
<span class="nb">object</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">storage</span><span class="o">.</span><span class="n">BucketObject</span><span class="p">(</span><span class="s2">&quot;object&quot;</span><span class="p">,</span>
    <span class="n">bucket</span><span class="o">=</span><span class="n">bucket</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">source</span><span class="o">=</span><span class="n">pulumi</span><span class="o">.</span><span class="n">FileAsset</span><span class="p">(</span><span class="s2">&quot;./test-fixtures/appengine/hello-world.zip&quot;</span><span class="p">))</span>
<span class="n">myapp</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">appengine</span><span class="o">.</span><span class="n">StandardAppVersion</span><span class="p">(</span><span class="s2">&quot;myapp&quot;</span><span class="p">,</span>
    <span class="n">version_id</span><span class="o">=</span><span class="s2">&quot;v1&quot;</span><span class="p">,</span>
    <span class="n">service</span><span class="o">=</span><span class="s2">&quot;myapp&quot;</span><span class="p">,</span>
    <span class="n">runtime</span><span class="o">=</span><span class="s2">&quot;nodejs10&quot;</span><span class="p">,</span>
    <span class="n">entrypoint</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;shell&quot;</span><span class="p">:</span> <span class="s2">&quot;node ./app.js&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">deployment</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;zip&quot;</span><span class="p">:</span> <span class="p">{</span>
            <span class="s2">&quot;sourceUrl&quot;</span><span class="p">:</span> <span class="n">pulumi</span><span class="o">.</span><span class="n">Output</span><span class="o">.</span><span class="n">all</span><span class="p">(</span><span class="n">bucket</span><span class="o">.</span><span class="n">name</span><span class="p">,</span> <span class="nb">object</span><span class="o">.</span><span class="n">name</span><span class="p">)</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="n">bucketName</span><span class="p">,</span> <span class="n">objectName</span><span class="p">:</span> <span class="sa">f</span><span class="s2">&quot;https://storage.googleapis.com/</span><span class="si">{</span><span class="n">bucket_name</span><span class="si">}</span><span class="s2">/</span><span class="si">{</span><span class="n">object_name</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">),</span>
        <span class="p">},</span>
    <span class="p">},</span>
    <span class="n">env_variables</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;port&quot;</span><span class="p">:</span> <span class="s2">&quot;8080&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">delete_service_on_destroy</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
<span class="n">srv</span> <span class="o">=</span> <span class="n">myapp</span><span class="o">.</span><span class="n">service</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="n">service</span><span class="p">:</span> <span class="n">gcp</span><span class="o">.</span><span class="n">monitoring</span><span class="o">.</span><span class="n">get_app_engine_service</span><span class="p">(</span><span class="n">module_id</span><span class="o">=</span><span class="n">service</span><span class="p">))</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>module_id</strong> (<em>str</em>) – The ID of the App Engine module underlying this
service. Corresponds to the moduleId resource label in the <a class="reference external" href="https://cloud.google.com/monitoring/api/resources#tag_gae_app">gae_app</a> monitored resource, or the service/module name.</p></li>
<li><p><strong>project</strong> (<em>str</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_gcp.monitoring.get_notification_channel">
<code class="sig-prename descclassname">pulumi_gcp.monitoring.</code><code class="sig-name descname">get_notification_channel</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">display_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.get_notification_channel" title="Permalink to this definition">¶</a></dt>
<dd><p>A NotificationChannel is a medium through which an alert is delivered
when a policy violation is detected. Examples of channels include email, SMS,
and third-party messaging applications. Fields containing sensitive information
like authentication tokens or contact info are only partially populated on retrieval.</p>
<p>To get more information about NotificationChannel, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannels">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/monitoring/support/notification-options">Notification Options</a></p></li>
<li><p><a class="reference external" href="https://cloud.google.com/monitoring/api/v3/">Monitoring API Documentation</a></p></li>
</ul>
</li>
</ul>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gcp</span> <span class="k">as</span> <span class="nn">gcp</span>

<span class="n">basic</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">monitoring</span><span class="o">.</span><span class="n">get_notification_channel</span><span class="p">(</span><span class="n">display_name</span><span class="o">=</span><span class="s2">&quot;Test Notification Channel&quot;</span><span class="p">)</span>
<span class="n">alert_policy</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">monitoring</span><span class="o">.</span><span class="n">AlertPolicy</span><span class="p">(</span><span class="s2">&quot;alertPolicy&quot;</span><span class="p">,</span>
    <span class="n">display_name</span><span class="o">=</span><span class="s2">&quot;My Alert Policy&quot;</span><span class="p">,</span>
    <span class="n">notification_channels</span><span class="o">=</span><span class="p">[</span><span class="n">basic</span><span class="o">.</span><span class="n">name</span><span class="p">],</span>
    <span class="n">combiner</span><span class="o">=</span><span class="s2">&quot;OR&quot;</span><span class="p">,</span>
    <span class="n">conditions</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;displayName&quot;</span><span class="p">:</span> <span class="s2">&quot;test condition&quot;</span><span class="p">,</span>
        <span class="s2">&quot;condition_threshold&quot;</span><span class="p">:</span> <span class="p">{</span>
            <span class="s2">&quot;filter&quot;</span><span class="p">:</span> <span class="s2">&quot;metric.type=&quot;</span><span class="n">compute</span><span class="o">.</span><span class="n">googleapis</span><span class="o">.</span><span class="n">com</span><span class="o">/</span><span class="n">instance</span><span class="o">/</span><span class="n">disk</span><span class="o">/</span><span class="n">write_bytes_count</span><span class="s2">&quot; AND resource.type=&quot;</span><span class="n">gce_instance</span><span class="s2">&quot;&quot;</span><span class="p">,</span>
            <span class="s2">&quot;duration&quot;</span><span class="p">:</span> <span class="s2">&quot;60s&quot;</span><span class="p">,</span>
            <span class="s2">&quot;comparison&quot;</span><span class="p">:</span> <span class="s2">&quot;COMPARISON_GT&quot;</span><span class="p">,</span>
            <span class="s2">&quot;aggregations&quot;</span><span class="p">:</span> <span class="p">[{</span>
                <span class="s2">&quot;alignmentPeriod&quot;</span><span class="p">:</span> <span class="s2">&quot;60s&quot;</span><span class="p">,</span>
                <span class="s2">&quot;perSeriesAligner&quot;</span><span class="p">:</span> <span class="s2">&quot;ALIGN_RATE&quot;</span><span class="p">,</span>
            <span class="p">}],</span>
        <span class="p">},</span>
    <span class="p">}])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>display_name</strong> (<em>str</em>) – The display name for this notification channel.</p></li>
<li><p><strong>labels</strong> (<em>dict</em>) – Labels (corresponding to the
NotificationChannelDescriptor schema) to filter the notification channels by.</p></li>
<li><p><strong>project</strong> (<em>str</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>type</strong> (<em>str</em>) – The type of the notification channel.</p></li>
<li><p><strong>user_labels</strong> (<em>dict</em>) – User-provided key-value labels to filter by.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_gcp.monitoring.get_secret_version">
<code class="sig-prename descclassname">pulumi_gcp.monitoring.</code><code class="sig-name descname">get_secret_version</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">secret</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.get_secret_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Get a Secret Manager secret’s version. For more information see the <a class="reference external" href="https://cloud.google.com/secret-manager/docs/">official documentation</a> and <a class="reference external" href="https://cloud.google.com/secret-manager/docs/reference/rest/v1beta1/projects.secrets.versions">API</a>.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gcp</span> <span class="k">as</span> <span class="nn">gcp</span>

<span class="n">basic</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">secretmanager</span><span class="o">.</span><span class="n">get_secret_version</span><span class="p">(</span><span class="n">secret</span><span class="o">=</span><span class="s2">&quot;my-secret&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>Deprecated: gcp.monitoring.getSecretVersion has been deprecated in favour of gcp.secretmanager.getSecretVersion</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>project</strong> (<em>str</em>) – The project to get the secret version for. If it
is not provided, the provider project is used.</p></li>
<li><p><strong>secret</strong> (<em>str</em>) – The secret to get the secret version for.</p></li>
<li><p><strong>version</strong> (<em>str</em>) – The version of the secret to get. If it
is not provided, the latest version is retrieved.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_gcp.monitoring.get_uptime_check_i_ps">
<code class="sig-prename descclassname">pulumi_gcp.monitoring.</code><code class="sig-name descname">get_uptime_check_i_ps</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.get_uptime_check_i_ps" title="Permalink to this definition">¶</a></dt>
<dd><p>Returns the list of IP addresses that checkers run from. For more information see
the <a class="reference external" href="https://cloud.google.com/monitoring/uptime-checks#get-ips">official documentation</a>.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gcp</span> <span class="k">as</span> <span class="nn">gcp</span>

<span class="n">ips</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">monitoring</span><span class="o">.</span><span class="n">get_uptime_check_i_ps</span><span class="p">()</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;ipList&quot;</span><span class="p">,</span> <span class="n">ips</span><span class="o">.</span><span class="n">uptime_check_ips</span><span class="p">)</span>
</pre></div>
</div>
</dd></dl>

</div>
