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
<span class="target" id="module-pulumi_gcp.monitoring"></span><dl class="class">
<dt id="pulumi_gcp.monitoring.AlertPolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.monitoring.</code><code class="sig-name descname">AlertPolicy</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">combiner=None</em>, <em class="sig-param">conditions=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">documentation=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">notification_channels=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">user_labels=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.AlertPolicy" title="Permalink to this definition">¶</a></dt>
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
<dl class="attribute">
<dt id="pulumi_gcp.monitoring.AlertPolicy.combiner">
<code class="sig-name descname">combiner</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.AlertPolicy.combiner" title="Permalink to this definition">¶</a></dt>
<dd><p>How to combine the results of multiple conditions to
determine if an incident should be opened.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.monitoring.AlertPolicy.conditions">
<code class="sig-name descname">conditions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.AlertPolicy.conditions" title="Permalink to this definition">¶</a></dt>
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

<dl class="attribute">
<dt id="pulumi_gcp.monitoring.AlertPolicy.creation_record">
<code class="sig-name descname">creation_record</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.AlertPolicy.creation_record" title="Permalink to this definition">¶</a></dt>
<dd><p>A read-only record of the creation of the alerting policy. If provided in a call to create or update, this field will be
ignored.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">mutateTime</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mutatedBy</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.monitoring.AlertPolicy.display_name">
<code class="sig-name descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.AlertPolicy.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>A short name or phrase used to identify the
condition in dashboards, notifications, and
incidents. To avoid confusion, don’t use the same
display name for multiple conditions in the same
policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.monitoring.AlertPolicy.documentation">
<code class="sig-name descname">documentation</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.AlertPolicy.documentation" title="Permalink to this definition">¶</a></dt>
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

<dl class="attribute">
<dt id="pulumi_gcp.monitoring.AlertPolicy.enabled">
<code class="sig-name descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.AlertPolicy.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether or not the policy is enabled. The default is true.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.monitoring.AlertPolicy.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.AlertPolicy.name" title="Permalink to this definition">¶</a></dt>
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

<dl class="attribute">
<dt id="pulumi_gcp.monitoring.AlertPolicy.notification_channels">
<code class="sig-name descname">notification_channels</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.AlertPolicy.notification_channels" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifies the notification channels to which notifications should be
sent when incidents are opened or closed or when new violations occur
on an already opened incident. Each element of this array corresponds
to the name field in each of the NotificationChannel objects that are
returned from the notificationChannels.list method. The syntax of the
entries in this field is
<code class="docutils literal notranslate"><span class="pre">projects/[PROJECT_ID]/notificationChannels/[CHANNEL_ID]</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.monitoring.AlertPolicy.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.AlertPolicy.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.monitoring.AlertPolicy.user_labels">
<code class="sig-name descname">user_labels</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.AlertPolicy.user_labels" title="Permalink to this definition">¶</a></dt>
<dd><p>This field is intended to be used for organizing and identifying the AlertPolicy
objects.The field can contain up to 64 entries. Each key and value is limited
to 63 Unicode characters or 128 bytes, whichever is smaller. Labels and values
can contain only lowercase letters, numerals, underscores, and dashes. Keys
must begin with a letter.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.monitoring.AlertPolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">combiner=None</em>, <em class="sig-param">conditions=None</em>, <em class="sig-param">creation_record=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">documentation=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">notification_channels=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">user_labels=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.AlertPolicy.get" title="Permalink to this definition">¶</a></dt>
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

<dl class="method">
<dt id="pulumi_gcp.monitoring.AlertPolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.AlertPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="method">
<dt id="pulumi_gcp.monitoring.AlertPolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.AlertPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="class">
<dt id="pulumi_gcp.monitoring.AwaitableGetAppEngineServiceResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.monitoring.</code><code class="sig-name descname">AwaitableGetAppEngineServiceResult</code><span class="sig-paren">(</span><em class="sig-param">display_name=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">module_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">service_id=None</em>, <em class="sig-param">telemetries=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.AwaitableGetAppEngineServiceResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_gcp.monitoring.AwaitableGetNotificationChannelResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.monitoring.</code><code class="sig-name descname">AwaitableGetNotificationChannelResult</code><span class="sig-paren">(</span><em class="sig-param">description=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">sensitive_labels=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">user_labels=None</em>, <em class="sig-param">verification_status=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.AwaitableGetNotificationChannelResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_gcp.monitoring.AwaitableGetSecretVersionResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.monitoring.</code><code class="sig-name descname">AwaitableGetSecretVersionResult</code><span class="sig-paren">(</span><em class="sig-param">create_time=None</em>, <em class="sig-param">destroy_time=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">secret=None</em>, <em class="sig-param">secret_data=None</em>, <em class="sig-param">version=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.AwaitableGetSecretVersionResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_gcp.monitoring.AwaitableGetUptimeCheckIPsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.monitoring.</code><code class="sig-name descname">AwaitableGetUptimeCheckIPsResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">uptime_check_ips=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.AwaitableGetUptimeCheckIPsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_gcp.monitoring.CustomService">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.monitoring.</code><code class="sig-name descname">CustomService</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">service_id=None</em>, <em class="sig-param">telemetry=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.CustomService" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a CustomService resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] display_name: Name used for UI elements listing this Service.
:param pulumi.Input[str] service_id: An optional service ID to use. If not given, the server will generate a service ID.
:param pulumi.Input[dict] telemetry: Configuration for how to query telemetry on a Service.</p>
<p>The <strong>telemetry</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">resourceName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_gcp.monitoring.CustomService.display_name">
<code class="sig-name descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.CustomService.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name used for UI elements listing this Service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.monitoring.CustomService.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.CustomService.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The full resource name for this service. The syntax is: projects/[PROJECT_ID]/services/[SERVICE_ID].</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.monitoring.CustomService.service_id">
<code class="sig-name descname">service_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.CustomService.service_id" title="Permalink to this definition">¶</a></dt>
<dd><p>An optional service ID to use. If not given, the server will generate a service ID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.monitoring.CustomService.telemetry">
<code class="sig-name descname">telemetry</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.CustomService.telemetry" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration for how to query telemetry on a Service.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">resourceName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.monitoring.CustomService.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">service_id=None</em>, <em class="sig-param">telemetry=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.CustomService.get" title="Permalink to this definition">¶</a></dt>
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
<li><p><strong>service_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An optional service ID to use. If not given, the server will generate a service ID.</p></li>
<li><p><strong>telemetry</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration for how to query telemetry on a Service.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>telemetry</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">resourceName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.monitoring.CustomService.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.CustomService.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="method">
<dt id="pulumi_gcp.monitoring.CustomService.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.CustomService.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="class">
<dt id="pulumi_gcp.monitoring.GetAppEngineServiceResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.monitoring.</code><code class="sig-name descname">GetAppEngineServiceResult</code><span class="sig-paren">(</span><em class="sig-param">display_name=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">module_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">service_id=None</em>, <em class="sig-param">telemetries=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.GetAppEngineServiceResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAppEngineService.</p>
<dl class="attribute">
<dt id="pulumi_gcp.monitoring.GetAppEngineServiceResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.GetAppEngineServiceResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.monitoring.GetNotificationChannelResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.monitoring.</code><code class="sig-name descname">GetNotificationChannelResult</code><span class="sig-paren">(</span><em class="sig-param">description=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">sensitive_labels=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">user_labels=None</em>, <em class="sig-param">verification_status=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.GetNotificationChannelResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getNotificationChannel.</p>
<dl class="attribute">
<dt id="pulumi_gcp.monitoring.GetNotificationChannelResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.GetNotificationChannelResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.monitoring.GetSecretVersionResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.monitoring.</code><code class="sig-name descname">GetSecretVersionResult</code><span class="sig-paren">(</span><em class="sig-param">create_time=None</em>, <em class="sig-param">destroy_time=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">secret=None</em>, <em class="sig-param">secret_data=None</em>, <em class="sig-param">version=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.GetSecretVersionResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getSecretVersion.</p>
<dl class="attribute">
<dt id="pulumi_gcp.monitoring.GetSecretVersionResult.create_time">
<code class="sig-name descname">create_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.GetSecretVersionResult.create_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The time at which the Secret was created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.monitoring.GetSecretVersionResult.destroy_time">
<code class="sig-name descname">destroy_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.GetSecretVersionResult.destroy_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The time at which the Secret was destroyed. Only present if state is DESTROYED.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.monitoring.GetSecretVersionResult.enabled">
<code class="sig-name descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.GetSecretVersionResult.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>True if the current state of the SecretVersion is enabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.monitoring.GetSecretVersionResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.GetSecretVersionResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.monitoring.GetSecretVersionResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.GetSecretVersionResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource name of the SecretVersion. Format:
<code class="docutils literal notranslate"><span class="pre">projects/{{project}}/secrets/{{secret_id}}/versions/{{version}}</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.monitoring.GetSecretVersionResult.secret_data">
<code class="sig-name descname">secret_data</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.GetSecretVersionResult.secret_data" title="Permalink to this definition">¶</a></dt>
<dd><p>The secret data. No larger than 64KiB.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.monitoring.GetUptimeCheckIPsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.monitoring.</code><code class="sig-name descname">GetUptimeCheckIPsResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">uptime_check_ips=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.GetUptimeCheckIPsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getUptimeCheckIPs.</p>
<dl class="attribute">
<dt id="pulumi_gcp.monitoring.GetUptimeCheckIPsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.GetUptimeCheckIPsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.monitoring.Group">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.monitoring.</code><code class="sig-name descname">Group</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">filter=None</em>, <em class="sig-param">is_cluster=None</em>, <em class="sig-param">parent_name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.Group" title="Permalink to this definition">¶</a></dt>
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
<dl class="attribute">
<dt id="pulumi_gcp.monitoring.Group.display_name">
<code class="sig-name descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.Group.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>A user-assigned name for this group, used only for display
purposes.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.monitoring.Group.filter">
<code class="sig-name descname">filter</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.Group.filter" title="Permalink to this definition">¶</a></dt>
<dd><p>The filter used to determine which monitored resources
belong to this group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.monitoring.Group.is_cluster">
<code class="sig-name descname">is_cluster</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.Group.is_cluster" title="Permalink to this definition">¶</a></dt>
<dd><p>If true, the members of this group are considered to be a
cluster. The system can perform additional analysis on
groups that are clusters.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.monitoring.Group.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.Group.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique identifier for this group. The format is “projects/{project_id_or_number}/groups/{group_id}”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.monitoring.Group.parent_name">
<code class="sig-name descname">parent_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.Group.parent_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the group’s parent, if it has one. The format is
“projects/{project_id_or_number}/groups/{group_id}”. For
groups with no parent, parentName is the empty string, “”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.monitoring.Group.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.Group.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.monitoring.Group.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">filter=None</em>, <em class="sig-param">is_cluster=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">parent_name=None</em>, <em class="sig-param">project=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.Group.get" title="Permalink to this definition">¶</a></dt>
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

<dl class="method">
<dt id="pulumi_gcp.monitoring.Group.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.Group.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="method">
<dt id="pulumi_gcp.monitoring.Group.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.Group.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="class">
<dt id="pulumi_gcp.monitoring.NotificationChannel">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.monitoring.</code><code class="sig-name descname">NotificationChannel</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">sensitive_labels=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">user_labels=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.NotificationChannel" title="Permalink to this definition">¶</a></dt>
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
<li><p><code class="docutils literal notranslate"><span class="pre">authToken</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An authorization token for a notification channel. Channel types that support this field include: slack</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An password for a notification channel. Channel types that support this field include: webhook_basicauth</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An servicekey token for a notification channel. Channel types that support this field include: pagerduty</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_gcp.monitoring.NotificationChannel.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.NotificationChannel.description" title="Permalink to this definition">¶</a></dt>
<dd><p>An optional human-readable description of this notification channel. This description may provide additional details, beyond the display name, for the channel. This may not exceed 1024 Unicode characters.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.monitoring.NotificationChannel.display_name">
<code class="sig-name descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.NotificationChannel.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>An optional human-readable name for this notification channel. It is recommended that you specify a non-empty and unique name in order to make it easier to identify the channels in your project, though this is not enforced. The display name is limited to 512 Unicode characters.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.monitoring.NotificationChannel.enabled">
<code class="sig-name descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.NotificationChannel.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether notifications are forwarded to the described channel. This makes it possible to disable delivery of notifications to a particular channel without removing the channel from all alerting policies that reference the channel. This is a more convenient approach when the change is temporary and you want to receive notifications from the same set of alerting policies on the channel at some point in the future.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.monitoring.NotificationChannel.labels">
<code class="sig-name descname">labels</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.NotificationChannel.labels" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration fields that define the channel and its behavior. The
permissible and required labels are specified in the
NotificationChannelDescriptor corresponding to the type field.
Labels with sensitive data are obfuscated by the API and therefore the provider cannot
determine if there are upstream changes to these fields. They can also be configured via
the sensitive_labels block, but cannot be configured in both places.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.monitoring.NotificationChannel.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.NotificationChannel.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The full REST resource name for this channel. The syntax is: projects/[PROJECT_ID]/notificationChannels/[CHANNEL_ID] The
[CHANNEL_ID] is automatically assigned by the server on creation.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.monitoring.NotificationChannel.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.NotificationChannel.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.monitoring.NotificationChannel.sensitive_labels">
<code class="sig-name descname">sensitive_labels</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.NotificationChannel.sensitive_labels" title="Permalink to this definition">¶</a></dt>
<dd><p>Different notification type behaviors are configured primarily using the the <code class="docutils literal notranslate"><span class="pre">labels</span></code> field on this
resource. This block contains the labels which contain secrets or passwords so that they can be marked
sensitive and hidden from plan output. The name of the field, eg: password, will be the key
in the <code class="docutils literal notranslate"><span class="pre">labels</span></code> map in the api request.
Credentials may not be specified in both locations and will cause an error. Changing from one location
to a different credential configuration in the config will require an apply to update state.  Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">authToken</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - An authorization token for a notification channel. Channel types that support this field include: slack</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - An password for a notification channel. Channel types that support this field include: webhook_basicauth</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - An servicekey token for a notification channel. Channel types that support this field include: pagerduty</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.monitoring.NotificationChannel.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.NotificationChannel.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the notification channel. This field matches the value of the NotificationChannelDescriptor.type field. See <a class="reference external" href="https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannelDescriptors/list">https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannelDescriptors/list</a> to get the list of valid values such as “email”, “slack”, etc…</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.monitoring.NotificationChannel.user_labels">
<code class="sig-name descname">user_labels</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.NotificationChannel.user_labels" title="Permalink to this definition">¶</a></dt>
<dd><p>User-supplied key/value data that does not need to conform to the corresponding NotificationChannelDescriptor’s schema, unlike the labels field. This field is intended to be used for organizing and identifying the NotificationChannel objects.The field can contain up to 64 entries. Each key and value is limited to 63 Unicode characters or 128 bytes, whichever is smaller. Labels and values can contain only lowercase letters, numerals, underscores, and dashes. Keys must begin with a letter.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.monitoring.NotificationChannel.verification_status">
<code class="sig-name descname">verification_status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.NotificationChannel.verification_status" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether this channel has been verified or not. On a ListNotificationChannels or GetNotificationChannel
operation, this field is expected to be populated.If the value is UNVERIFIED, then it indicates that the channel is
non-functioning (it both requires verification and lacks verification); otherwise, it is assumed that the channel
works.If the channel is neither VERIFIED nor UNVERIFIED, it implies that the channel is of a type that does not require
verification or that this specific channel has been exempted from verification because it was created prior to
verification being required for channels of this type.This field cannot be modified using a standard
UpdateNotificationChannel operation. To change the value of this field, you must call VerifyNotificationChannel.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.monitoring.NotificationChannel.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">sensitive_labels=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">user_labels=None</em>, <em class="sig-param">verification_status=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.NotificationChannel.get" title="Permalink to this definition">¶</a></dt>
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
<li><p><code class="docutils literal notranslate"><span class="pre">authToken</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An authorization token for a notification channel. Channel types that support this field include: slack</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An password for a notification channel. Channel types that support this field include: webhook_basicauth</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An servicekey token for a notification channel. Channel types that support this field include: pagerduty</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.monitoring.NotificationChannel.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.NotificationChannel.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="method">
<dt id="pulumi_gcp.monitoring.NotificationChannel.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.NotificationChannel.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="class">
<dt id="pulumi_gcp.monitoring.Slo">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.monitoring.</code><code class="sig-name descname">Slo</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">basic_sli=None</em>, <em class="sig-param">calendar_period=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">goal=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">rolling_period_days=None</em>, <em class="sig-param">service=None</em>, <em class="sig-param">slo_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.Slo" title="Permalink to this definition">¶</a></dt>
<dd><p>A Service-Level Objective (SLO) describes the level of desired good
service. It consists of a service-level indicator (SLI), a performance
goal, and a period over which the objective is to be evaluated against
that goal. The SLO can use SLIs defined in a number of different manners.
Typical SLOs might include “99% of requests in each rolling week have
latency below 200 milliseconds” or “99.5% of requests in each calendar
month return successfully.”</p>
<p>To get more information about Slo, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/monitoring/service-monitoring">Service Monitoring</a></p></li>
<li><p><a class="reference external" href="https://cloud.google.com/monitoring/api/v3/">Monitoring API Documentation</a></p></li>
</ul>
</li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
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
<dl class="attribute">
<dt id="pulumi_gcp.monitoring.Slo.basic_sli">
<code class="sig-name descname">basic_sli</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.Slo.basic_sli" title="Permalink to this definition">¶</a></dt>
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

<dl class="attribute">
<dt id="pulumi_gcp.monitoring.Slo.calendar_period">
<code class="sig-name descname">calendar_period</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.Slo.calendar_period" title="Permalink to this definition">¶</a></dt>
<dd><p>A calendar period, semantically “since the start of the current</p>
<p><span class="raw-html-m2r"><calendarPeriod></span>”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.monitoring.Slo.display_name">
<code class="sig-name descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.Slo.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name used for UI elements listing this SLO.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.monitoring.Slo.goal">
<code class="sig-name descname">goal</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.Slo.goal" title="Permalink to this definition">¶</a></dt>
<dd><p>The fraction of service that must be good in order for this objective
to be met. 0 &lt; goal &lt;= 0.999</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.monitoring.Slo.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.Slo.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The full resource name for this service. The syntax is:
projects/[PROJECT_ID_OR_NUMBER]/services/[SERVICE_ID]/serviceLevelObjectives/[SLO_NAME]</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.monitoring.Slo.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.Slo.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.monitoring.Slo.rolling_period_days">
<code class="sig-name descname">rolling_period_days</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.Slo.rolling_period_days" title="Permalink to this definition">¶</a></dt>
<dd><p>A rolling time period, semantically “in the past X days”.
Must be between 1 to 30 days, inclusive.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.monitoring.Slo.service">
<code class="sig-name descname">service</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.Slo.service" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the service to which this SLO belongs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.monitoring.Slo.slo_id">
<code class="sig-name descname">slo_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.Slo.slo_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id to use for this ServiceLevelObjective. If omitted, an id will be generated instead.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.monitoring.Slo.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">basic_sli=None</em>, <em class="sig-param">calendar_period=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">goal=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">rolling_period_days=None</em>, <em class="sig-param">service=None</em>, <em class="sig-param">slo_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.Slo.get" title="Permalink to this definition">¶</a></dt>
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

<dl class="method">
<dt id="pulumi_gcp.monitoring.Slo.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.Slo.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="method">
<dt id="pulumi_gcp.monitoring.Slo.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.Slo.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="class">
<dt id="pulumi_gcp.monitoring.UptimeCheckConfig">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.monitoring.</code><code class="sig-name descname">UptimeCheckConfig</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">content_matchers=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">http_check=None</em>, <em class="sig-param">monitored_resource=None</em>, <em class="sig-param">period=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">resource_group=None</em>, <em class="sig-param">selected_regions=None</em>, <em class="sig-param">tcp_check=None</em>, <em class="sig-param">timeout=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.UptimeCheckConfig" title="Permalink to this definition">¶</a></dt>
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
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The password to authenticate.</p></li>
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
<dl class="attribute">
<dt id="pulumi_gcp.monitoring.UptimeCheckConfig.content_matchers">
<code class="sig-name descname">content_matchers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.UptimeCheckConfig.content_matchers" title="Permalink to this definition">¶</a></dt>
<dd><p>The expected content on the page the check is run against. Currently, only the first entry in the list is supported, and other entries will be ignored. The server will look for an exact match of the string in the page response’s content. This field is optional and should only be specified if a content match is required.  Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">content</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - String or regex content to match (max 1024 bytes)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.monitoring.UptimeCheckConfig.display_name">
<code class="sig-name descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.UptimeCheckConfig.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>A human-friendly name for the uptime check configuration. The display name should be unique within a Stackdriver Workspace in order to make it easier to identify; however, uniqueness is not enforced.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.monitoring.UptimeCheckConfig.http_check">
<code class="sig-name descname">http_check</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.UptimeCheckConfig.http_check" title="Permalink to this definition">¶</a></dt>
<dd><p>Contains information needed to make an HTTP or HTTPS check.  Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">authInfo</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The authentication information. Optional when creating an HTTP check; defaults to empty.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The password to authenticate.</p></li>
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

<dl class="attribute">
<dt id="pulumi_gcp.monitoring.UptimeCheckConfig.monitored_resource">
<code class="sig-name descname">monitored_resource</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.UptimeCheckConfig.monitored_resource" title="Permalink to this definition">¶</a></dt>
<dd><p>The monitored resource (<a class="reference external" href="https://cloud.google.com/monitoring/api/resources">https://cloud.google.com/monitoring/api/resources</a>) associated with the configuration. The following monitored resource types are supported for uptime checks:  uptime_url  gce_instance  gae_app  aws_ec2_instance  aws_elb_load_balancer  Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">labels</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Values for all of the labels listed in the associated monitored resource descriptor. For example, Compute Engine VM instances use the labels “project_id”, “instance_id”, and “zone”.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The monitored resource type. This field must match the type field of a MonitoredResourceDescriptor (<a class="reference external" href="https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.monitoredResourceDescriptors#MonitoredResourceDescriptor">https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.monitoredResourceDescriptors#MonitoredResourceDescriptor</a>) object. For example, the type of a Compute Engine VM instance is gce_instance. For a list of types, see Monitoring resource types (<a class="reference external" href="https://cloud.google.com/monitoring/api/resources">https://cloud.google.com/monitoring/api/resources</a>) and Logging resource types (<a class="reference external" href="https://cloud.google.com/logging/docs/api/v2/resource-list">https://cloud.google.com/logging/docs/api/v2/resource-list</a>).</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.monitoring.UptimeCheckConfig.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.UptimeCheckConfig.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique resource name for this UptimeCheckConfig. The format is
projects/[PROJECT_ID]/uptimeCheckConfigs/[UPTIME_CHECK_ID].</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.monitoring.UptimeCheckConfig.period">
<code class="sig-name descname">period</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.UptimeCheckConfig.period" title="Permalink to this definition">¶</a></dt>
<dd><p>How often, in seconds, the uptime check is performed. Currently, the only supported values are 60s (1 minute), 300s (5 minutes), 600s (10 minutes), and 900s (15 minutes). Optional, defaults to 300s.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.monitoring.UptimeCheckConfig.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.UptimeCheckConfig.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.monitoring.UptimeCheckConfig.resource_group">
<code class="sig-name descname">resource_group</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.UptimeCheckConfig.resource_group" title="Permalink to this definition">¶</a></dt>
<dd><p>The group resource associated with the configuration.  Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">groupId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The group of resources being monitored. Should be the <code class="docutils literal notranslate"><span class="pre">name</span></code> of a group</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resourceType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The resource type of the group members.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.monitoring.UptimeCheckConfig.selected_regions">
<code class="sig-name descname">selected_regions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.UptimeCheckConfig.selected_regions" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of regions from which the check will be run. Some regions contain one location, and others contain more than one. If this field is specified, enough regions to include a minimum of 3 locations must be provided, or an error message is returned. Not specifying this field will result in uptime checks running from all regions.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.monitoring.UptimeCheckConfig.tcp_check">
<code class="sig-name descname">tcp_check</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.UptimeCheckConfig.tcp_check" title="Permalink to this definition">¶</a></dt>
<dd><p>Contains information needed to make a TCP check.  Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The port to the page to run the check against. Will be combined with host (specified within the MonitoredResource) to construct the full URL.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.monitoring.UptimeCheckConfig.timeout">
<code class="sig-name descname">timeout</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.UptimeCheckConfig.timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum amount of time to wait for the request to complete (must be between 1 and 60 seconds). Accepted formats <a class="reference external" href="https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration">https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.monitoring.UptimeCheckConfig.uptime_check_id">
<code class="sig-name descname">uptime_check_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.UptimeCheckConfig.uptime_check_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the uptime check</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.monitoring.UptimeCheckConfig.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">content_matchers=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">http_check=None</em>, <em class="sig-param">monitored_resource=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">period=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">resource_group=None</em>, <em class="sig-param">selected_regions=None</em>, <em class="sig-param">tcp_check=None</em>, <em class="sig-param">timeout=None</em>, <em class="sig-param">uptime_check_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.UptimeCheckConfig.get" title="Permalink to this definition">¶</a></dt>
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
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The password to authenticate.</p></li>
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

<dl class="method">
<dt id="pulumi_gcp.monitoring.UptimeCheckConfig.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.UptimeCheckConfig.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="method">
<dt id="pulumi_gcp.monitoring.UptimeCheckConfig.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.UptimeCheckConfig.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="function">
<dt id="pulumi_gcp.monitoring.get_app_engine_service">
<code class="sig-prename descclassname">pulumi_gcp.monitoring.</code><code class="sig-name descname">get_app_engine_service</code><span class="sig-paren">(</span><em class="sig-param">module_id=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.get_app_engine_service" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_gcp.monitoring.get_notification_channel">
<code class="sig-prename descclassname">pulumi_gcp.monitoring.</code><code class="sig-name descname">get_notification_channel</code><span class="sig-paren">(</span><em class="sig-param">display_name=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">user_labels=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.get_notification_channel" title="Permalink to this definition">¶</a></dt>
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

<dl class="function">
<dt id="pulumi_gcp.monitoring.get_secret_version">
<code class="sig-prename descclassname">pulumi_gcp.monitoring.</code><code class="sig-name descname">get_secret_version</code><span class="sig-paren">(</span><em class="sig-param">project=None</em>, <em class="sig-param">secret=None</em>, <em class="sig-param">version=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.get_secret_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Get a Secret Manager secret’s version. For more information see the <a class="reference external" href="https://cloud.google.com/secret-manager/docs/">official documentation</a> and <a class="reference external" href="https://cloud.google.com/secret-manager/docs/reference/rest/v1beta1/projects.secrets.versions">API</a>.</p>
<p>Deprecated: gcp.getSecretVersion has been deprecated in favour of gcp.getSecretVersion</p>
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

<dl class="function">
<dt id="pulumi_gcp.monitoring.get_uptime_check_i_ps">
<code class="sig-prename descclassname">pulumi_gcp.monitoring.</code><code class="sig-name descname">get_uptime_check_i_ps</code><span class="sig-paren">(</span><em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.get_uptime_check_i_ps" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
</dd></dl>

</div>
