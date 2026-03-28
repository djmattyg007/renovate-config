#!/usr/bin/env bash

set -euo pipefail

exec renovate-config-validator --strict --no-global *.json5
