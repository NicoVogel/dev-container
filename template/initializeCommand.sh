#!/bin/bash

echo "GROUPNAME=docker" > .devcontainer/user.env
echo "GROUP_GID=$(if [ "$(uname)" = "Darwin" ]; then stat -f "%g" /var/run/docker.sock; else stat -c %g /var/run/docker.sock; fi)" >> .devcontainer/user.env