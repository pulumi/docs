---
# Term page for the `industry` taxonomy, rendered at
# /customers/industry/iot-transportation/ by layouts/taxonomy/industry.html. The stub
# exists so the term page is generated whether or not a case study is filed
# under it — /customers/ lists customers, and a customer needs no case study.
# `make lint` (checkIndustryTermStubs) keeps this directory's contents equal
# to the id set in data/customers_industries.yaml.
#
# `slug` pins the URL to the industry id: Hugo would otherwise derive the
# term's :slug permalink from the title below, quietly turning
# /customers/industry/iot-transportation/ into /customers/industry/transportation-logistics/.
# The display name and description still come from the data file (the term
# templates and head.html read it directly), so there is nothing to sync here.
slug: iot-transportation
title: "Transportation & logistics"

aliases:
    - /case-studies/industry/iot-transportation/
---
