#!/usr/bin/env python3
"""Compare two versions of the self-hosted feature parity page.

Usage: status-changes.py OLD_PAGE NEW_PAGE

Prints one Markdown list item per row whose status changed, and exits 0.
When GITHUB_OUTPUT is set, also writes:

  needs_review=true|false  true if a changed row has hand-written Details,
                           which may no longer match its new status
  changes<<EOF ... EOF     the same list, for the PR body
"""

import os
import re
import sys

ROW = re.compile(r"^\| (?P<feature>.+?) \| (?P<status>[^|]+?) \| (?P<details>.*?) \|$")
LINK = re.compile(r"^\[(?P<name>.+?)\]\(.*\)$")


def read_rows(path):
    rows = {}
    try:
        with open(path, encoding="utf-8") as f:
            lines = f.read().splitlines()
    except FileNotFoundError:
        return rows
    for line in lines:
        # The feature table ends where the status key begins
        if line.startswith("## "):
            break
        m = ROW.match(line)
        if not m or m["feature"] in ("Feature", "---"):
            continue
        link = LINK.match(m["feature"])
        name = link["name"] if link else m["feature"]
        rows[name] = (m["status"].strip(), m["details"].strip())
    return rows


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    old, new = read_rows(sys.argv[1]), read_rows(sys.argv[2])

    changes = []
    needs_review = False
    for name in sorted(new, key=str.lower):
        status, details = new[name]
        before = old.get(name, ("(not listed)", ""))[0]
        if before == status:
            continue
        note = " (has Details text: check it still matches)" if details else ""
        changes.append(f"- **{name}**: {before} → {status}{note}")
        needs_review = needs_review or bool(details)
    for name in sorted(set(old) - set(new), key=str.lower):
        changes.append(f"- **{name}**: removed from the page")
        needs_review = True

    print("\n".join(changes) if changes else "No status changes.")

    output = os.environ.get("GITHUB_OUTPUT")
    if output:
        with open(output, "a", encoding="utf-8") as f:
            f.write(f"needs_review={'true' if needs_review else 'false'}\n")
            f.write("changes<<EOF\n" + ("\n".join(changes) or "No status changes.") + "\nEOF\n")


if __name__ == "__main__":
    main()
