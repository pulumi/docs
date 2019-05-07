#!/bin/bash

# Runs travisqueue to ensure that only one `push` job is running
# concurrently for a given branch. This is how we can avoid conflicts
# when running `pulumi update` in response to any push.

# Travis doesn't make secret config available on forks, so we skip
# it when TRAVIS_TOKEN is not set.
if [ -z ${TRAVIS_TOKEN:-} ]; then
    echo "Skipping travisqueue, TRAVIS_TOKEN is not set."
    exit 0
fi

case ${1:-} in
    install)
        # We cannot run `go get` to install it because the Go runtime on
        # the ruby VM is too old. So instead we get it from get.pulumi.com.
        # (Which is neither recommended nor supported).
        mkdir -p ~/.bin/
        curl https://get.pulumi.com/internal/travisqueue > ~/.bin/travisqueue
        chmod +x ~/.bin/travisqueue
        ;;
    start)
        ~/.bin/travisqueue start
        ;;
    finish)
        ~/.bin/travisqueue finish
        ;;
    *)
        echo "Unknown command '${1:-}'."
        ;;
esac
