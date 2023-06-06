#!/bin/sh
cd $(dirname "$0")
pip install -r requirements.txt
exec python script.py $@