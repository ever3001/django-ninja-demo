#!/bin/bash
set -ex

PYTHONPATH=src mypy --config-file ./config/mypy.ini --cache-dir=/dev/null --show-error-codes "$@" src/
