#!/bin/bash
# Script that automatically finds providers using tfgen for documentation, and makes each
# one generate example coverage statistics in the form of JSON files. These are then 
# concatenated, and uploaded to S3. 

set -euf -o pipefail

# Creating the directory and file into which all the coverage data will be copied.
MainDir=$PWD
echo $MainDir
mkdir -p $MainDir/data/coverage
echo -n "" > $MainDir/data/coverage/summary.json


# Finding providers that use terraform and export coverage, running tfgen, and copying 
# coverage data into summary.json.
for MakefilePath in $(find ../ -name Makefile); do 
    if grep -q "^tfgen:" $MakefilePath && grep -q "\--coverageOutputDir" $MakefilePath; then
        # Makefile seems to support coverage
        MakefileDir=$(dirname $MakefilePath)
        echo "$MakefileDir"
        pushd $MakefileDir  > /dev/null
        make tfgen
        cat ./bin/coverage-data/summary.json >> $MainDir/data/coverage/summary.json        
        popd  > /dev/null
    fi
done

# Uploading file to S3
currDateTime=$(date +"%Y-%m-%d_%H-%M-%S")

# Makes sure that each summary has a unique name in S3
newSummaryName="summary_${currDateTime}.json"
echo "New file to be uploaded: ${newSummaryName}"

# Sets up URI of S3 bucket and location to upload to
# Example URI: s3://arm2pulumi-coverage-results-c9610a2/summaries/summary_2021-05-11_19-44-12.json
s3BucketName="tfgen-coverage-results-36b7864"
s3KeyName="summaries/${newSummaryName}"
s3FullURI="s3://${s3BucketName}/${s3KeyName}"

cp $MainDir/data/coverage/summary.json $MainDir/data/coverage/$newSummaryName

aws s3 cp $MainDir/data/coverage/$newSummaryName $s3FullURI --acl bucket-owner-full-control



