---
title: "Import Pulumi into your Data Warehouse with tap-pulumi-cloud"
date: 2024-08-13T15:01:40-04:00
draft: false
meta_desc: Using the Meltano Singer SDK we have expanded the tap-pulumi-cloud connector to be able to export all the pulumi cloud data into your own Data Warehouse
meta_image: schema.png
authors:
    - pablo-seibelt
    - lucas-crespo

tags:
    - data-warehouse
    - meltano
    - api
    - data


social:
  twitter: "Your Pulumi Data in your Warehouse: See how the tap-pulumi-cloud extractor helps you export your Pulumi data into your own Data Warehouse. #DataWarehouse #Pulumi #Meltano #ELT"
  linkedin: |
    See how the tap-pulumi-cloud extractor helps you export your Pulumi data into your own Data Warehouse.
    We show how you can use this connector to download Pulumi Cloud data into any destination of your choice; helping you to track infrastructure metrics alongside the rest of your data.

---

The [Pulumi Cloud REST API](https://www.pulumi.com/docs/pulumi-cloud/cloud-rest-api) allows our users to read the same data available in the [Pulumi Cloud UI](https://app.pulumi.com) and this presents an opportunity for data teams trying to integrate metrics of their Pulumi usage, by accessing said API.

<!--more-->

However, manually integrating dozens of API endpoints into a data pipeline can be a time consuming effort, having to figure out the intricacies of each API, how each endpoint is structured, how to work with the api's paging method, etc.

This is where the [Meltano SDK shines](https://sdk.meltano.com/en/latest/index.html) - It allows anyone to build "Taps" and "Targets" that read and write data, respectively. This way, we can use [tap-pulumi-cloud](https://github.com/pulumi/tap-pulumi-cloud) with loaders such as [target-snowflake](https://hub.meltano.com/loaders/target-snowflake), [target-bigquery](https://hub.meltano.com/loaders/target-bigquery), [target-redshift](https://hub.meltano.com/loaders/target-redshift) or even [target-postgres](https://hub.meltano.com/loaders/target-postgres); allowing us to load the data into our own Data Warehouse easily.

## Set up

First of all set up your environment [by following Meltano's installation guide](https://docs.meltano.com/guide/installation-guide), when this is done, continue by adding tap-pulumi-cloud and your choice of loader into your environment, we'll use target-duckdb for this example:

```bash
meltano add extractor tap-pulumi-cloud
meltano add loader target-duckdb
```

Then switch your tap variant to use Pulumi's instead of the default, open meltano.yml and change the pip_url to `git+https://github.com/pulumi/tap-pulumi-cloud.git`

```yml
version: 1
default_environment: dev
project_id: be90b150-3e48-4ecd-be9d-161ef7417e3c
environments:
- name: dev
- name: staging
- name: prod
plugins:
  extractors:
  - name: tap-pulumi-cloud
    variant: meltanolabs
    pip_url: git+https://github.com/pulumi/tap-pulumi-cloud.git
  loaders:
  - name: target-duckdb
    variant: jwills
    pip_url: target-duckdb~=0.6
```

And run `meltano install` to make sure the right version is installed

## Configure

To configure all settings available for this tap, you can use Meltano's interactive config running:

```bash
meltano config tap-pulumi-cloud set --interactive
```

The required variables are the `token` [(Get one from the Pulumi Cloud)](https://app.pulumi.com/) and organizations needs to have the org/s you want to extract data from.

## Load data

When your configuration has been finished, you can run the data pipeline like so:

```bash
meltano run tap-pulumi-cloud target-duckdb
```

After the run finishes, you can access the exported tables and create whichever analytics you need on top of them

![Data loaded into DuckDB](schema.png)
