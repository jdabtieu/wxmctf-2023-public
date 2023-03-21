#!/bin/bash

if [[ $(ps aux | grep -v grep | grep "python3 uploader.py" | wc -c) -eq 0 ]]; then
    cd /wxmhealthcheck && python3 uploader.py
fi
