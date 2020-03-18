#!/bin/bash

# Prints a heartbeat to STDOUT while the script is still running.
# Used to prevent Travis from killing long-running jobs, even if
# there is no output for 10+ minutes at a time.
#
# It is assumed the caller will launch the script on a background
# process and kill it once it is no longer needed.

if [ -z ${2} ]; then
    echo "Usage: ${0} <seconds-between-heartbeat> <max-seconds>"
    exit 1
fi

TIME_BETWEEN_HEARTBEATS="${1}"
MAX_TIMEOUT=${2}

ELAPSED=0
while [ $ELAPSED -lt $MAX_TIMEOUT ]; do
    sleep ${TIME_BETWEEN_HEARTBEATS}
    echo "... still working ..."
    ELAPSED=$((${ELAPSED} + ${TIME_BETWEEN_HEARTBEATS}))
done

echo "ERROR: Max Timeout occurred. Terminating heartbeat."
exit 1
