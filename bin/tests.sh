#!/bin/bash
set -ex

PYTHONPATH=src poetry run pytest "$@"
