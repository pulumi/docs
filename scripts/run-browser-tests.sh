#!/bin/bash

MAX_RETRIES=3
RETRY_COUNT=0

# Retry on errors up to `MAX_RETRIES` with a 10 second sleep in between.
run_tests() {
    while true; do
        CYPRESS_BASE_URL="$1" yarn run cypress run --headless
        exit_code=$?
        if [ $exit_code -ne 0 ]; then
            RETRY_COUNT=$((RETRY_COUNT+1))
            if [ $RETRY_COUNT -eq $MAX_RETRIES ]; then
                echo "Error: Browser tests failed after ${MAX_RETRIES} retries"
                exit $exit_code
            else
                echo "Error: Retrying browser tests in 10 seconds..."
                sleep 10
            fi
        else
            break
        fi
    done
}

trap 'run_tests $1' EXIT
