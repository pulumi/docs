---
title: Kubernetes Checklist
---

## Identity

* Set up cloud provider IAM roles, groups for service accounts, team.
* Set up audit logs
* Create password policies and >2-factor authentication

## Infrastructure

* Provision some kind of container registry
* Configure hard drives
* Deploy production-grade datastores
* Configure backup, x-account backup
* Test your backup mechanisms
* Set up loadbalancing
* Set up load testing/chaos testing
* Set up a container registry

## Containers

* Build Docker images
* Configure CPU, memory (+ GC?) settings.

## CI/CD

* Set up VCS/build system
* Set up environments

## Security

* Configure encryption-in-transit and configure-at-rest
* Set up secrets management

## Metrics

* Track availability metrics. Set up R53 health checks, etc.
* Track app metrics like QPS, _e.g._, through CloudWatch
* Track server metrics like CPU utilization, _e.g._, through CloudWatch
