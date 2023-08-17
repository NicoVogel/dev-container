#!/bin/bash

set -e #stop on error
sudo chmod g+w /var/run/docker.sock

# in case you want to connect this template with artifactory, then copy the `scripts/setup.py` into the `.devcontainer/` directory 
# .devcontainer/setup.py
