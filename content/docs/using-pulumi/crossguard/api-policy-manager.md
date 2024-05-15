---
title_tag: "Compliance Ready Policies (Policy Manager) | CrossGuard"
meta_desc: This page contains the API reference for Policy Manager.
title: Policy Manager
h1: Policy Manager
weight: 1
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  usingpulumi:
    parent: crossguard-compliance-ready-policies
    weight: 1
---
## Classes

<a name="PolicyManager"></a>

## PolicyManager

Class to manage policies.

**Kind**: global class

<a name="PolicyManager+getSelectionStats"></a>

### policyManager.getSelectionStats() ⇒

The function `getSelectionStats()` returns statistics about the number of registered
policies as well as the names and count of already selected policies and the number
of policies that haven't been selected yet.

**Kind**: instance method of [`PolicyManager`](#PolicyManager)
**Returns**: Returns a populated `PolicyManagerStats`.
<a name="PolicyManager+displaySelectionStats"></a>

### policyManager.displaySelectionStats() ⇒

This function `displaySelectionStats()` displays general statistics about policies
that have been returned by `selectPolicies()` and how many remain in the pool.
Additional information about registered policy modules are displayed too.

**Kind**: instance method of [`PolicyManager`](#PolicyManager)
**Returns**: No value is returned.
<a name="PolicyManager+resetPolicySelector"></a>

### policyManager.resetPolicySelector()

When executing the policy selector, it's crucial for the function to return each policy
exactly once. This ensures that the Pulumi service doesn't return an error related to
duplicated policies when a Policy Pack is published.
The purpose of this function is to reset the policy filter, enabling a fresh start.
Consequently, when you invoke `selectPolicies()`, it will take into account all the
registered policies including the ones previously selected. This may add previously
selected policies to your Policy Pack.
This function for unit tests purpose and most users/developers shouldn't use it.

**Kind**: instance method of [`PolicyManager`](#PolicyManager)
<a name="PolicyManager+getPolicyByName"></a>

### policyManager.getPolicyByName(name) ⇒

This function returns a resource policy information by providing the policy
name.
This function for unit tests purpose and most users/developers shouldn't use it.
**Note**: The returned policy is not removed from the pool of available policies.
If you want to select an individual policy, then you should be using
`selectPolicyByName()` instead.

**Kind**: instance method of [`PolicyManager`](#PolicyManager)
**Returns**: The PolicyInfo if found, otherwise `undefined`.

| Param | Description |
| --- | --- |
| name | The policy name to search for and return. |

<a name="PolicyManager+selectPolicyByName"></a>

### policyManager.selectPolicyByName(name, enforcementLevel) ⇒

This function searches for a policy based on the provided `name`. If the
policy is found, then it is removed from the pool of available policies
and the policy is returned. If not found, the `undefined` is returned.

**Kind**: instance method of [`PolicyManager`](#PolicyManager)
**Returns**: A `ResourceValidationPolicy` policy that matched the supplied `name` or `undefined` if the policy wasn't found in the pool of `remainingPolicies`.

| Param | Description |
| --- | --- |
| name | The policy name to search for and return. |
| enforcementLevel | The desired policy enforcement Level. Valid values are `advisory`, `mandatory` and `disabled`. |

<a name="PolicyManager+selectPoliciesByName"></a>

### policyManager.selectPoliciesByName(names, enforcementLevel) ⇒

Takes an array of policy names and set the desired enforcement level on each policy.
If a provided policy name has alread been selected, then the matching policy is not
returned as part of the result.

**Kind**: instance method of [`PolicyManager`](#PolicyManager)
**Returns**: An array of policies.

| Param | Description |
| --- | --- |
| names | An array of policy names. |
| enforcementLevel | The desired enforcement level for those policies. |

<a name="PolicyManager+selectPolicies"></a>

### policyManager.selectPolicies(args, enforcementLevel) ⇒

Select policies based on criterias provided as arguments. The selectiopn filter only
returns policies that match selection criterias. Effectively, this function performs
an `or` operation within each selection criteria, and an `and` operation between
selection criterias.
You may also provide an array of cherry-picked polcies. The function takes care of
removing duplicates as well as ignoring already selected policies from previous calls.
Note: Criterias are all case-insensitive.
Note: Call `resetPolicyfilter()` to reset the selection filter and consider all
policies again.

**Kind**: instance method of [`PolicyManager`](#PolicyManager)
**Returns**: An array of ResourceValidationPolicy policies that matched with the selection criterias.

| Param | Description |
| --- | --- |
| args | A bag of options containing the selection criterias, or an array of cherry-picked policies. |
| enforcementLevel | The desired policy enforcement Level. Valid values are `advisory`, `mandatory` and `disabled`. |

<a name="PolicyManager+registerPolicy"></a>

### policyManager.registerPolicy(args) ⇒

Register a new policy into the pool of policies. The policy name must be
unique to the pool of policies already registered or an exception is thrown.
This function is used if you are authoring your own Compliance Ready Policies.

**Kind**: instance method of [`PolicyManager`](#PolicyManager)
**Returns**: a `ResourceValidationPolicy` object.

| Param | Description |
| --- | --- |
| args | An object containing the policy to register as well as its additional attributes. |

<a name="PolicyManager+registerPolicyModule"></a>

### policyManager.registerPolicyModule(name, version) ⇒

This function is used by policy module to register information about themselves.
This can be later used to display statistics about included packages as part of
a policy-pack.
This function is to be used if you are authoring your own Compliance Ready Policies.

**Kind**: instance method of [`PolicyManager`](#PolicyManager)
**Returns**: returns the package version as a string

| Param | Description |
| --- | --- |
| name | Name of the policy module as stored in `package.json` |
| version | The module version as stored in `package.json` |

<a name="valToBoolean"></a>

## valToBoolean ⇒

The function `valToBoolean()` is a helper because some boolean properties
require a string type instead of a boolean type.
The idea for this function is to allow compatibility across multiple versions
of the same provider in case a property type changes from string to boolean.

**Kind**: global variable
**Returns**: The boolean value, or `undefined` is the conversion isn't possible.
**Link**: <https://github.com/pulumi/pulumi-aws/issues/2257>

| Param | Description |
| --- | --- |
| val | A value to convert into a boolean. |

<a name="policyManager"></a>

## policyManager

An instance of the `PolicyManager` class.
Use this instance to manipulate (register, select...) policies.

**Kind**: global constant

<a name="loadPlugins"></a>

## loadPlugins(globPatterns) ⇒

`loadPlugins()` loads NPM policy packages that are present in the `package.json` which
names are matching the `globPatterns`.
this function is typically used when you've authored a policy package and you want to
load and register the policies it contains.
A common pattern example is `["@pulumi/*-compliance-policies"]` for Pulumi Compliance
Ready Policies.

**Kind**: global function
**Returns**: No value is returned. Exceptions are thrown on error with a descriptive message.

| Param | Description |
| --- | --- |
| globPatterns | An array of patterns as used by `micromatch`. |
