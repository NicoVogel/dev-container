#!/bin/bash

set -e #stop on error

PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD=true pnpm install
pnpx playwright@1.28.1 install --with-deps webkit
