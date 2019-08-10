#!/bin/bash
set -e

mkdir -p bin/

# Install dependencies if they changed.
if [ ! -f "./bin/requirements.txt" ] || [ "$(diff requirements.txt ./bin/requirements.txt)" != "" ]; then
    echo "Requirements changed -- updating:"
    pip install --upgrade --target ./bin -r requirements.txt
fi

# Always unconditionally copy the sources.
echo "Copying program files:"
cp aws index.py requirements.txt bin/

echo "Done."
