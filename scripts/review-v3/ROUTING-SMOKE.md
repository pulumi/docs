# Routing smoke test

Throwaway file used to confirm that the v3 reviewer-routing step resolves the
approval matrix from live paths and actually requests the lane team. Nothing
reads this file, and it must never be merged.

The routing step lives in `.github/workflows/claude-triage.yml` and shells out
to `scripts/review-v3/route-pr.py`, which wires the mechanical bar into the
lane matrix in `.github/review-routing.yml`.

Expected resolution for this path: subject `other`, change type `substantive`,
role `tools` -> `pulumi/docs-tools`, no staging evidence.

Delete this file and close the pull request once the request has landed.
