#!/usr/bin/env bash



python "./completed_flow/Extract/extract.py"

python "./completed_flow/Transform/transform.py"

python "./completed_flow/Load/load.py"

echo $?
