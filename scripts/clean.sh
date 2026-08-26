#!/bin/bash

# Locally, this is a full reset: wiping node_modules and the Hugo caches is how
# you recover from a bad install or stale generated resources.
#
# CI is a different situation. The workspace is a fresh clone, so there is
# nothing stale to remove -- but actions/cache has just restored the yarn cache
# and Hugo's processed-image cache (resources/) into it. Deleting those here
# throws the restore away seconds after it happened, which forces Hugo to
# re-encode every blog feature image on every run. The caches still saved and
# restored cleanly, so the waste was invisible in the job log.
#
# Skip those paths under CI. `hugo mod clean` is in here too: it is a no-op on a
# fresh runner (no module cache has been downloaded yet at this point), and
# keeping it out of the CI path removes any question of it reaching into
# resources/_gen and undoing the guard above. The rest are no-ops on a fresh
# clone and are left alone so local behavior is unchanged.
if [ -z "${CI:-}" ]; then
    yarn cache clean
    rm -rf resources
    hugo mod clean
fi

rm -rf node_modules
rm -rf infrastructure/node_modules
rm -rf _vendor
rm -rf public
rm -rf cypress/screenshots
rm -rf cypress/videos
rm -f origin-bucket-metadata.json
rm -f redirects.txt
