#!/bin/bash

CYPRESS_BASE_URL="$1" yarn run cypress run --headless
