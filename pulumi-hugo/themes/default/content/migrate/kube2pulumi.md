---
title: Upgrade Your Kubernetes YAML to a Modern Language
url: /kube2pulumi
layout: kube2pulumi
linktitle: Kubernetes YAML to Pulumi
menu:
  converters:
    identifier: kube2pulumi
    weight: 3
meta_desc: See what your Kubernetes YAML would look like in a modern language thanks to Pulumi.

examples:
    - name: Nginx Pod
      filename: kube.yaml
      description:
      code: |
        apiVersion: v1
        kind: Pod
        metadata:
          namespace: frontend
          name: nginx
        spec:
          containers:
            - name: nginx
              image: nginx:1.14-alpine
              resources:
                limits:
                  memory: 20Mi
                  cpu: 0.2

    - name: Operator Deployment
      filename: kube.yaml
      description:
      code: |
        apiVersion: apps/v1
        kind: Deployment
        metadata:
          name: pulumi-kubernetes-operator
        spec:
          replicas: 1
          selector:
            matchLabels:
              name: pulumi-kubernetes-operator
          template:
            metadata:
              labels:
                name: pulumi-kubernetes-operator
            spec:
              serviceAccountName: pulumi-kubernetes-operator
              imagePullSecrets:
                - name: pulumi-kubernetes-operator
              containers:
                - name: pulumi-kubernetes-operator
                  image: pulumi/pulumi-kubernetes-operator:v0.0.2
                  command:
                    - pulumi-kubernetes-operator
                args:
                  - "--zap-level=debug"
                imagePullPolicy: Always
                env:
                    - name: WATCH_NAMESPACE
                      valueFrom:
                        fieldRef:
                          fieldPath: metadata.namespace
                    - name: POD_NAME
                      valueFrom:
                        fieldRef:
                          fieldPath: metadata.name
                    - name: OPERATOR_NAME
                      value: "pulumi-kubernetes-operator"

    - name: Auth Roles
      filename: kube.yaml
      description:
      code: |
        apiVersion: rbac.authorization.k8s.io/v1
        kind: Role
        metadata:
          creationTimestamp: null
          name: pulumi-kubernetes-operator
        rules:
          - apiGroups:
              - ""
            resources:
              - pods
              - services
              - services/finalizers
              - endpoints
              - persistentvolumeclaims
              - events
              - configmaps
              - secrets
            verbs:
              - create
              - delete
              - get
              - list
              - patch
              - update
              - watch
        - apiGroups:
            - apps
          resources:
            - deployments
            - daemonsets
            - replicasets
            - statefulsets
          verbs:
            - create
            - delete
            - get
            - list
            - patch
            - update
            - watch
        - apiGroups:
            - monitoring.coreos.com
          resources:
            - servicemonitors
          verbs:
            - get
            - create
        - apiGroups:
            - apps
          resourceNames:
            - pulumi-kubernetes-operator
          resources:
            - deployments/finalizers
          verbs:
            - update
        - apiGroups:
            - ""
          resources:
            - pods
          verbs:
            - get
        - apiGroups:
            - apps
          resources:
            - replicasets
            - deployments
          verbs:
            - get
        - apiGroups:
            - pulumi.com
          resources:
            - '*'
          verbs:
            - create
            - delete
            - get
            - list
            - patch
            - update
            - watch

form:
    hubspot_form_id: 8381e562-5fdf-4736-bb10-86096705e4ee
---
