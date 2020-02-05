#!/bin/bash

# Runs a script to generate event pages from the data
# in /data/events.toml. It will only generate pages for
# events that have a content type defined. Specifically these
# pages are for users to register for an event/talk/workshop
# on our website. If the event links to an external registration
# page then we should not generate an internal landing page.

go run ./tools/eventgen/*.go
