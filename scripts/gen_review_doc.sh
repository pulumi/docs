#!/bin/bash

# Generates a doc which can be pasted into Google Docs or Word for offline copy-editing review.

set -o nounset -o errexit -o pipefail

# Generate a review doc for the reference docs TOC
DOC_TOC="_data/reference.yaml"


# Collect all files referenced in the TOC
FILES=$(ruby -ryaml -e "puts YAML::load(open(ARGV.first).read)['toc'][1]['section']" ${DOC_TOC})

# Write out the TOC and then each file name and contents
cat $DOC_TOC
for FILE in ${FILES}
do
    printf "\n\n###############\n"
    printf "# %s\n" $FILE
    printf "###############\n\n"
    cat $FILE
done
