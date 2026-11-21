---
title_tag: "Infrastructure posture report | Pulumi Policies"
meta_desc: Get a monthly infrastructure posture report that checks every stack in your organization against the Pulumi Best Practices policy packs.
title: Infrastructure posture report
h1: Infrastructure posture report
menu:
  discovery-governance:
    name: Infrastructure posture report
    parent: dg-operations
    weight: 15
---

{{< pulumi-cloud >}}
The infrastructure posture report is available in the Pro and Enterprise editions.
{{< /pulumi-cloud >}}

The infrastructure posture report is a monthly snapshot of how your organization's stacks measure up against the [Pulumi Best Practices](/docs/discovery-governance/guides/pre-built-policy-packs/) policy packs. Once a month, Pulumi Cloud scans the latest state of every stack in your organization against those packs and summarizes what it found: how many resources were evaluated, how many have no findings, and which issues affect the most resources.

The scan is read-only. It changes nothing in your infrastructure or your stacks, and it uses no new credentials. You don't need to assign the packs to a policy group first.

The report summarizes policy findings. It is not a compliance audit.

## Who can see the report

The report counts findings across every stack and cloud account in your organization, so it's available to members who can read policy results, every stack, and every cloud account. Only members who can update the organization, such as organization admins, can turn the report on or off.

While the report is off, members don't see it. Admins still do, so they can turn it back on.

## Turn on the report

1. Navigate to your organization in Pulumi Cloud.
1. Navigate to **Governance** > **Posture report** in the left navigation.
1. Review the preview, which shows how many stacks the scan covers and which packs it checks them against.
1. Select **Turn on**.

The first scan starts right away, and the first report appears on the page when it finishes. After that, a new report is delivered by the 1st of every month. Turning on the report is recorded in the [audit log](/docs/administration/concepts/audit-logs/) with your name and the time.

If you select **Not now**, the report stays off and members don't see the page. An admin can turn it on at any time from the same page.

If the first scan ends without a report, the page says why:

- **Nothing to report yet:** your organization had no stacks to scan. The next monthly report covers any stacks you create.
- **Your first report couldn't be prepared:** the scan couldn't evaluate enough of your stacks. The next scan tries again ahead of the 1st.

## Read the report

The report opens with the scope of the scan:

- **Stacks evaluated:** the stacks whose latest state was checked, with any that failed to evaluate or weren't evaluated.
- **Resources evaluated:** the resources in those stacks.
- **Rules run:** the rules in the Pulumi Best Practices packs, and the pack versions the scan used.

### Summary and coverage

The summary counts findings. A finding is one resource failing one rule, so a resource that fails the same rule more than once counts as one finding.

Coverage is the percentage of evaluated resources with no findings. It's rounded down, so it shows 100% only when no resource has a finding.

The report covers resources managed in Pulumi stacks. It doesn't scan discovered resources from cloud accounts that Pulumi IaC doesn't manage yet.

### Top issues

Top issues group findings by rule and resource family, such as every `aws:s3` resource that fails the same rule. Groups are ranked by severity, then by how many resources they affect. Select **Show findings** on a group to see a sample of the affected resources, and open each finding in [Policy findings](/docs/discovery-governance/operations/policy-findings/), where you can assign and resolve it.

Each report is a snapshot. It doesn't change as you resolve findings; the next month's report reflects the change.

### Past reports

Use the report menu at the top of the page to open a past month's report. A past report shows each finding's resources as they were when it was delivered, so its findings may have changed since. Reports are kept for a year.

### Export the report

Select **Export** to download the report:

- **Download CSV:** the report's scope, finding counts by severity, and top issues as a spreadsheet.
- **Save as PDF:** a printable version of the report, with when it was exported and by whom.

## Enable continuous monitoring

The report is a monthly snapshot. To track and resolve findings as they happen, select **Enable monitoring** on the report. This creates a **Pulumi Best Practices Audit** [policy group](/docs/discovery-governance/concepts/policy-as-code/policy-groups/) that evaluates every stack against the Pulumi Best Practices packs in audit mode, so findings appear in [Policy findings](/docs/discovery-governance/operations/policy-findings/) as stacks are updated. Audit policy groups never block deployments.

Enabling monitoring requires permission to create policy groups.

## Turn off the report

To turn off the report, an admin opens the settings menu on the report page and selects **Turn off posture reports**. This hides the report for everyone in the organization. Policy findings stay available in [Policy findings](/docs/discovery-governance/operations/policy-findings/).

Past reports are kept for a year. When an admin turns the report back on, past reports show again right away and monthly reports resume: if this month's report hasn't run yet, it runs within a day; otherwise the next one arrives at the start of next month.

In-app and email notices for the report are managed separately in your notification settings.
