# complex from (custom repository)
# ARG DOCKER_REPOSITORY_PATH=docker.artifactory.my-org.com
# ARG DOCKER_IMAGE_NAME=base
# ARG DOCKER_IMAGE_VERSION=1.0.0

# FROM ${DOCKER_REPOSITORY_PATH}/${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_VERSION}

# simple from
FROM ubuntu:22.04

ARG NODEJS_VERSION=18.16.1

# Avoid warnings by switching to noninteractive
ENV DEBIAN_FRONTEND=noninteractive

# install essentials
RUN apt-get -y update \
    && apt-get -y install \
    curl \
    gpg \
    git \
    build-essential \
    make \
    #clean up
    && apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

# install nodejs
RUN curl -fsSL https://deb.nodesource.com/gpgkey/nodesource.gpg.key | gpg --dearmor -o /etc/apt/keyrings/nodesource.gpg \
    && echo "deb [signed-by=/etc/apt/keyrings/nodesource.gpg] https://deb.nodesource.com/node_18.x jammy main" > /etc/apt/sources.list.d/nodesource.list \
    && apt-get -y update \
    && apt-get -y install \
    nodejs \
    # only needed in case you need the `setup.py`
    # python3-pip \
    #clean up
    && apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

# RUN python3 -m pip install \
#     requests

# Install docker
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg \
    && echo "deb [signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu jammy stable" > /etc/apt/sources.list.d/docker.list \
    && apt-get -y update \
    && apt-get -y install \
    docker-ce-cli \
    docker-compose-plugin \
    #clean up
    && apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

# Install pnpm and nx
RUN npm install -g \
    pnpm \
    nx

ENV DEBIAN_FRONTEND=

COPY user.env /tmp/user.env

# within windows the docker group id is always 0 (=root)
# within mac the docker group id is always 1 (=daemon), but is mounted with group id 0
# within linux we adapt the groupid from the host
RUN useradd -ms /bin/bash dev \
    && . /tmp/user.env && rm /tmp/user.env && \
    if [ "$GROUP_GID" = "0" ]; \
    then \
        usermod -aG 0 dev; \
    elif [ "$GROUP_GID" = "1" ]; \
    then \
        usermod -aG 0 dev; \
    else \
        if getent group $GROUPNAME; then groupdel $GROUPNAME; fi && \
        groupadd --gid $GROUP_GID $GROUPNAME && \
        gpasswd -a dev $GROUPNAME; \
    fi \
    && apt-get -y update \
    && apt-get -y install sudo \
    #clean up
    && apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

USER dev

RUN echo 'source /usr/share/bash-completion/completions/git \n\
if [ -f ~/.env ]; then \n\
    . ~/.env \n\
fi'\
    >> ~/.bashrc \
    && pnpm config set store-dir /home/dev/.pnpm-store
