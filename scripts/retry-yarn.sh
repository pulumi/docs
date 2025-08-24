#!/bin/bash
# Script to run yarn commands with retry logic and exponential backoff
# Usage: ./retry-yarn.sh [yarn command args...]

set -o pipefail

# Configuration
MAX_ATTEMPTS=3
BASE_DELAY=10
MAX_DELAY=300

# Function to run yarn command with retry logic
retry_yarn() {
    local cmd="$*"
    local attempt=1
    local delay=$BASE_DELAY
    
    echo "Running: yarn $cmd"
    
    while [ $attempt -le $MAX_ATTEMPTS ]; do
        echo "Attempt $attempt of $MAX_ATTEMPTS"
        
        # Run yarn command with network timeout configuration
        if yarn --network-timeout 60000 --network-concurrency 1 $cmd; then
            echo "✓ yarn $cmd succeeded on attempt $attempt"
            return 0
        fi
        
        local exit_code=$?
        echo "✗ yarn $cmd failed on attempt $attempt (exit code: $exit_code)"
        
        if [ $attempt -eq $MAX_ATTEMPTS ]; then
            echo "All $MAX_ATTEMPTS attempts failed for: yarn $cmd"
            return $exit_code
        fi
        
        echo "Waiting $delay seconds before retry..."
        sleep $delay
        
        # Exponential backoff with jitter
        delay=$((delay * 2))
        if [ $delay -gt $MAX_DELAY ]; then
            delay=$MAX_DELAY
        fi
        # Add jitter (random 0-25% of delay)
        jitter=$((delay / 4))
        delay=$((delay + RANDOM % jitter))
        
        attempt=$((attempt + 1))
    done
}

# Check if yarn is available
if ! command -v yarn &> /dev/null; then
    echo "Error: yarn is not installed or not in PATH"
    exit 1
fi

# Run the yarn command with retry logic
retry_yarn "$@"