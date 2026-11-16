#!/usr/bin/env python3
"""Builds data/rbac_scopes.json from three Pulumi Cloud API responses.

Usage: build-rbac-scopes.py SCOPES_JSON ROLES_JSON SETS_JSON SECTIONS_YAML OUTPUT

  SCOPES_JSON  GET /api/orgs/{org}/roles/scopes
  ROLES_JSON   GET /api/orgs/{org}/roles?uxPurpose=role
  SETS_JSON    GET /api/orgs/{org}/roles?uxPurpose=set

scripts/fetch-rbac-scopes.sh fetches those and runs this. It's a separate file
so the transformation can be rerun against saved responses without a token.

Everything the reference pages show is computed here, so the Hugo shortcodes
only render: each scope's section (from SECTIONS_YAML), the built-in roles that
grant each organization-level scope, the smallest built-in permission set that
grants each entity-level scope, and how each built-in permission set extends
the next smaller one.

When the API returns something SECTIONS_YAML doesn't cover (a scope no section
matches, or a built-in role, permission set, or entity type it doesn't list),
the build fails. If FIX_NOTICE_FILE is set, it first writes one sentence per
kind of gap there, saying what's missing and how to fix it, so the nightly
workflow can post that to Slack.
"""

import json
import os
import re
import sys

import yaml


def fail(message):
    sys.exit("error: " + message)


def load(path):
    with open(path) as f:
        return json.load(f)


def flatten(descriptor, owner):
    """Returns the permissions a built-in role or permission set grants.

    Built-ins use only Allow and Group descriptors today. Any other kind
    (a condition, a reference to another descriptor) would mean a grant that
    a flat list can't describe, so stop rather than publish a wrong one.
    """
    kind = descriptor.get("__type")
    if kind == "PermissionDescriptorAllow":
        return set(descriptor["permissions"])
    if kind == "PermissionDescriptorGroup":
        result = set()
        for entry in descriptor["entries"]:
            result |= flatten(entry, owner)
        return result
    fail("%s uses a %s permission descriptor, which this script can't flatten"
         % (owner, kind))


def main(scopes_path, roles_path, sets_path, sections_path, output):
    catalog = load(scopes_path)
    with open(sections_path) as f:
        config = yaml.safe_load(f)

    replacements = [
        (re.compile(re.escape(r["from"]), re.IGNORECASE), r["to"])
        for r in config.get("replacements") or []
    ]

    def clean(text):
        text = (text or "").strip()
        for pattern, replacement in replacements:
            text = pattern.sub(replacement, text)
        # The API's labels have no final period; the docs append notes after
        # them, which would otherwise run on ("Create stack The same...").
        if text and text[-1] not in ".!?":
            text += "."
        return text

    builtin = lambda r: r.get("defaultIdentifier")
    roles = [r for r in load(roles_path)["roles"] if builtin(r)]
    sets = [r for r in load(sets_path)["roles"] if builtin(r)]
    if not catalog or not roles or not sets:
        # An empty or reshaped response would publish empty reference tables.
        fail("an API response was empty; refusing to overwrite %s" % output)

    # Every gap is collected rather than failing on the first, so one failed
    # run names everything the sections file needs.
    problems = []

    def order_key(order):
        # Sorts anything the sections file doesn't list last, so the rest of
        # the build can still run and report every gap at once.
        return lambda item: (order.index(item["defaultIdentifier"])
                             if item["defaultIdentifier"] in order else len(order))

    role_order = config["roles"]
    unknown = sorted(r["defaultIdentifier"] for r in roles
                     if r["defaultIdentifier"] not in role_order)
    if unknown:
        problems.append(
            "Pulumi Cloud returned built-in roles that `roles` in %s doesn't list: %s. "
            "Add each one there, in the order the docs should list roles."
            % (sections_path, ", ".join(unknown)))
    roles.sort(key=order_key(role_order))
    role_grants = [(r["name"], flatten(r["details"], r["name"])) for r in roles]

    entity_ids = [e["id"] for e in config["entities"]]
    unknown = sorted(set(catalog) - set(entity_ids))
    if unknown:
        problems.append(
            "Pulumi Cloud returned RBAC entity types that `entities` in %s doesn't list: %s. "
            "Add each one there with its sections, and add a reference page under "
            "content/docs/administration/reference/rbac-scopes/ that renders it with "
            "the rbac-scopes shortcode."
            % (sections_path, ", ".join(unknown)))

    set_order = config["permission_sets"]
    unknown = sorted(s["defaultIdentifier"] for s in sets
                     if s["defaultIdentifier"] not in set_order)
    if unknown:
        problems.append(
            "Pulumi Cloud returned built-in permission sets that `permission_sets` in %s "
            "doesn't list: %s. Add each one there, smallest first within its entity type, "
            "since each set renders as the one before it plus its additions."
            % (sections_path, ", ".join(unknown)))

    permission_sets = []
    for entity in entity_ids:
        members = [(s, flatten(s["details"], s["name"])) for s in sets
                   if s.get("resourceType") == entity]
        members.sort(key=lambda pair: order_key(set_order)(pair[0]))
        previous = None
        for s, permissions in members:
            # Show a set as "<smaller set>, + <additions>" only when it really
            # contains the smaller one; Billing doesn't contain Standard.
            inherits = previous if previous and previous[1] <= permissions else None
            permission_sets.append({
                "id": s["defaultIdentifier"],
                "name": s["name"],
                "entity": entity,
                "description": clean(s.get("description")),
                "permissions": sorted(permissions),
                "inherits": inherits[0]["name"] if inherits else None,
                "added": sorted(permissions - inherits[1]) if inherits else None,
                "_set": permissions,
            })
            previous = (s, permissions)

    entities = []
    unmapped = []
    for entity_config in config["entities"]:
        entity = entity_config["id"]
        exact, prefixes, groups = {}, [], {}
        for index, section in enumerate(entity_config["sections"]):
            match = section.get("match") or {}
            for scope in match.get("scopes") or []:
                exact[scope] = index
            for prefix in match.get("prefixes") or []:
                prefixes.append((prefix, index))
            for group in match.get("groups") or []:
                groups[group] = index
        prefixes.sort(key=lambda pair: len(pair[0]), reverse=True)

        def place(scope, group):
            if scope in exact:
                return exact[scope]
            for prefix, index in prefixes:
                if scope.startswith(prefix):
                    return index
            return groups.get(group)

        sections = [{"name": s["name"], "scopes": []} for s in entity_config["sections"]]
        entity_sets = [s for s in permission_sets if s["entity"] == entity]
        for group in catalog.get(entity, []):
            for scope in group["scopes"]:
                name = scope["name"]
                index = place(name, group["name"])
                if index is None:
                    unmapped.append("%s: %s (API group %r)" % (entity, name, group["name"]))
                    continue
                row = {"name": name,
                       "description": clean(scope["metadata"]["description"])}
                if entity == "global":
                    row["defaultRoles"] = [n for n, grants in role_grants if name in grants]
                else:
                    # The smallest set that grants the scope is the least
                    # access a reader needs to give someone for it.
                    granting = [s for s in entity_sets if name in s["_set"]]
                    granting.sort(key=lambda s: len(s["_set"]))
                    row["defaultPermissionSet"] = granting[0]["name"] if granting else None
                sections[index]["scopes"].append(row)

        for section in sections:
            section["scopes"].sort(key=lambda row: row["name"])
        empty = [s["name"] for s in sections if not s["scopes"]]
        if empty and catalog.get(entity):
            print("warning: %s section(s) with no scopes: %s" % (entity, ", ".join(empty)))
        entities.append({"id": entity,
                         "sections": [s for s in sections if s["scopes"]]})

    if unmapped:
        # Deliberately fatal, like the audit log events job: a new scope must
        # be filed under a real section, not dropped or lumped into "Other".
        problems.append(
            "Pulumi Cloud returned scopes that match no section: %s. Add each one to "
            "the right section's `match` block in %s (an exact scope, a prefix, or an "
            "API group; see the file's header comment)."
            % (", ".join(sorted(unmapped)), sections_path))

    if problems:
        notice_file = os.environ.get("FIX_NOTICE_FILE")
        if notice_file:
            with open(notice_file, "w") as f:
                f.write("\n".join(problems) + "\n")
        fail("\n  ".join(["%s doesn't cover what the API returned:" % sections_path]
                         + problems))

    for s in permission_sets:
        del s["_set"]

    with open(output, "w") as f:
        json.dump({"entities": entities, "permissionSets": permission_sets},
                  f, indent=2, sort_keys=True)
        f.write("\n")

    count = sum(len(s["scopes"]) for e in entities for s in e["sections"])
    print("Wrote %d scopes and %d permission sets to %s"
          % (count, len(permission_sets), output))


if __name__ == "__main__":
    if len(sys.argv) != 6:
        sys.exit(__doc__)
    main(*sys.argv[1:])
