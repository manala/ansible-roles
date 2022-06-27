ARG DEBIAN=bullseye

########
# Base #
########

FROM debian:${DEBIAN}-slim as base

ARG DEBIAN
ARG USER_ID=1000
ARG GROUP_ID=1000
ARG GOSU_VERSION=1.14
ARG GOMPLATE_VERSION=3.11.1

# The 'container' environment variable tells systemd that it's running inside a
# Docker container environment.
# It's also internally used for checking we're running inside a container.
ENV container="docker"

RUN \
    # Backports
    printf "deb http://deb.debian.org/debian ${DEBIAN}-backports main" > /etc/apt/sources.list.d/backports.list \
    && apt-get update \
    && apt-get install --yes --no-install-recommends \
        s6 \
        sudo \
        curl \
        ca-certificates \
        gnupg \
        libarchive-tools bzip2 \
        bash-completion \
        git \
        make \
        less \
        vim \
        socat \
    # User
    && addgroup --gid ${GROUP_ID} lazy \
    && adduser --home /home/lazy --shell /bin/bash --uid ${USER_ID} --gecos lazy --ingroup lazy --disabled-password lazy \
    && mkdir -p /run/user/${USER_ID} && chown lazy:lazy /run/user/${USER_ID} \
    && printf "lazy ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/lazy \
    # Gosu
    && curl -sSL https://github.com/tianon/gosu/releases/download/${GOSU_VERSION}/gosu-$(case $(dpkg --print-architecture) in "amd64") echo "amd64" ;; "arm64") echo "arm64" ;; esac) \
        -o /usr/local/bin/gosu \
    && chmod +x /usr/local/bin/gosu \
    # Gomplate
    && curl -sSL https://github.com/hairyhenderson/gomplate/releases/download/v${GOMPLATE_VERSION}/gomplate_linux-$(case $(dpkg --print-architecture) in "amd64") echo "amd64" ;; "arm64") echo "arm64" ;; esac) \
        -o /usr/local/bin/gomplate \
    && chmod +x /usr/local/bin/gomplate \
    # Bash completion
    && mkdir -p /etc/bash_completion.d \
    # Oh My Bash
    && git clone https://github.com/ohmybash/oh-my-bash.git /usr/local/share/oh-my-bash

##########
# System #
##########

FROM base AS system

ARG DEBIAN

RUN \
    apt-get install --yes --no-install-recommends \
      openssh-client \
      sshpass \
      python3 python3-pip \
      python3-argcomplete \
      python3-apt python3-docker \
      shellcheck \
    # Bash completion
    && activate-global-python-argcomplete3 --dest /etc/bash_completion.d

# Docker
RUN \
    printf "deb https://download.docker.com/linux/debian ${DEBIAN} stable" > /etc/apt/sources.list.d/docker.list \
    && curl -sSL https://download.docker.com/linux/debian/gpg \
        | apt-key add - \
    && apt-get update \
    && apt-get install --yes --no-install-recommends \
        docker-ce-cli

# Ansible
RUN \
    pip3 install ansible-core==2.11.12

RUN \
    BUILD_PACKAGES="pipx python3-dev gcc" \
    export PIPX_HOME="/usr/local" \
    export PIPX_BIN_DIR="/usr/local/bin" \
    && apt-get install --yes --no-install-recommends \
      ${BUILD_PACKAGES} \
    # Ansible Lint
    && pipx install ansible-lint==6.3.0 \
    # Molecule
    && pipx install molecule==4.0.0 \
    && _MOLECULE_COMPLETE=bash_source molecule > /etc/bash_completion.d/molecule \
    && pipx inject molecule molecule-docker==1.1.0 \
    && apt-get purge --yes --autoremove ${BUILD_PACKAGES}

