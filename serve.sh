#!/usr/bin/env bash

unset TECHIES_RUNTIME
export TECHIES_RUNTIME="$(techies get_runtime_path):`pwd`"

$PYTHON -u server.py


