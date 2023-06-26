ARG DOCKER_REPOSITORY_PATH=docker.artifactory.my-org.com
ARG DOCKER_IMAGE_NAME=base
ARG DOCKER_IMAGE_VERSION=1.0.0

FROM ${DOCKER_REPOSITORY_PATH}/${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_VERSION}

ARG NODEJS_VERSION=18.16.1

# Avoid warnings by switching to noninteractive
ENV DEBIAN_FRONTEND=noninteractive

# install nodejs and google-chrome
RUN curl -fsSL https://deb.nodesource.com/gpgkey/nodesource.gpg.key | gpg --dearmor -o /etc/apt/keyrings/nodesource.gpg \
    && echo "deb [signed-by=/etc/apt/keyrings/nodesource.gpg] https://deb.nodesource.com/node_18.x jammy main" > /etc/apt/sources.list.d/nodesource.list \
    && apt-get -y update \
    && apt-get -y install \
    build-essential \
    make \
    nodejs \
    python3-pip

# Install pnpm
RUN npm install -g \
    pnpm@8.6.5 \
    nx

RUN python3 -m pip install \
    requests

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

ENV DEBIAN_FRONTEND=

COPY user.env /tmp/user.env

# within windows the docker group id is always 0 (=root)
# within mac the docker group id is always 1 (=daemon), but is mounted with group id 0
# within linux we adapt the groupid from the host
RUN . /tmp/user.env && rm /tmp/user.env && \
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
    fi

USER dev

RUN echo 'alias pnx="pnpm exec nx" \n\
source /usr/share/bash-completion/completions/git \n\
if [ -f ~/.env ]; then \n\
    . ~/.env \n\
fi'\
    >> ~/.bashrc \
    && pnpm config set store-dir /home/dev/.pnpm-store
