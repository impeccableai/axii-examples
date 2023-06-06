#!/usr/bin/env sh

source=$1
shift 1

pip install -r $source/requirements.txt
exec python $source/script.py  $@
