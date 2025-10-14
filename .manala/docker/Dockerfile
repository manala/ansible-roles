# syntax=docker/dockerfile:1

########
# Base #
########

FROM debian:trixie-slim

ARG DEBIAN_FRONTEND="noninteractive"

ARG MANALA_USER_ID="1000"
ARG MANALA_GROUP_ID="1000"

ARG GOMPLATE_VERSION="4.3.3"
ARG DIRENV_VERSION="2.37.1"
ARG JQ_VERSION="1.7.1"
ARG YQ_VERSION="4.47.2"
ARG STARSHIP_VERSION="1.23.0"
ARG FZF_VERSION="0.65.2"

# The 'container' environment variable tells systemd that it's running inside a
# Docker container environment.
# It's also internally used for checking we're running inside a container.
ENV container="docker"

# Starship
ENV STARSHIP_CONFIG=/etc/starship/starship.toml

SHELL ["/bin/bash", "-e", "-o", "pipefail", "-c"]

RUN <<EOF
# Packages
apt-get --quiet update
apt-get --quiet --yes --purge --autoremove upgrade
apt-get --quiet --yes --no-install-recommends --verbose-versions install \
    bzip2 \
    ca-certificates \
    curl \
    git \
    gnupg \
    gosu \
    less \
    libarchive-tools \
    make \
    rsync \
    s6 \
    socat \
    sudo \
    vim \
    zsh
# Locale
apt-get --quiet --yes --no-install-recommends --verbose-versions install \
    locales
sed -i "/^# *en_US.UTF-8\b/s/^# *//" /etc/locale.gen
dpkg-reconfigure locales
# User
addgroup --gid ${MANALA_GROUP_ID} lazy
adduser --home /home/lazy --shell /bin/zsh --uid ${MANALA_USER_ID} --gecos lazy --ingroup lazy --disabled-password lazy
install --verbose --mode 0755 --group lazy --owner lazy --directory /run/user/${MANALA_USER_ID}
echo "lazy ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/lazy
# Gomplate
curl -sSLf "https://github.com/hairyhenderson/gomplate/releases/download/v${GOMPLATE_VERSION}/gomplate_linux-$(case $(dpkg --print-architecture) in "amd64") echo "amd64" ;; "arm64") echo "arm64" ;; esac)" \
    --output /usr/local/bin/gomplate
chmod +x /usr/local/bin/gomplate
# Direnv
curl -sSLf "https://github.com/direnv/direnv/releases/download/v${DIRENV_VERSION}/direnv.linux-$(case $(dpkg --print-architecture) in "amd64") echo "amd64" ;; "arm64") echo "arm64" ;; esac)" \
    --output /usr/local/bin/direnv
chmod +x /usr/local/bin/direnv
# Jq
curl -sSLf "https://github.com/jqlang/jq/releases/download/jq-${JQ_VERSION}/jq-linux-$(case $(dpkg --print-architecture) in "amd64") echo "amd64" ;; "arm64") echo "arm64" ;; esac)" \
    --output /usr/local/bin/jq
chmod +x /usr/local/bin/jq
# Yq
curl -sSLf "https://github.com/mikefarah/yq/releases/download/v${YQ_VERSION}/yq_linux_$(case $(dpkg --print-architecture) in "amd64") echo "amd64" ;; "arm64") echo "arm64" ;; esac)" \
    --output /usr/local/bin/yq
chmod +x /usr/local/bin/yq
# Oh My Zsh
git clone https://github.com/ohmyzsh/ohmyzsh.git /usr/local/share/oh-my-zsh
# See: https://github.com/ohmyzsh/ohmyzsh/issues/11995
git clone https://github.com/zsh-users/zsh-autosuggestions.git /usr/local/share/oh-my-zsh/custom/plugins/zsh-autosuggestions
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git /usr/local/share/oh-my-zsh/custom/plugins/zsh-syntax-highlighting
echo "ZDOTDIR=/etc/zsh" > /etc/zsh/zshenv
# Starship
curl -sSLf "https://github.com/starship/starship/releases/download/v${STARSHIP_VERSION}/starship-$(case $(dpkg --print-architecture) in "amd64") echo "x86_64" ;; "arm64") echo "aarch64" ;; esac)-unknown-linux-musl.tar.gz" \
    | bsdtar -xvf - -C /usr/local/bin
echo "Defaults env_keep += STARSHIP_CONFIG" > /etc/sudoers.d/starship
# Fzf
curl -sSLf "https://github.com/junegunn/fzf/releases/download/v${FZF_VERSION}/fzf-${FZF_VERSION}-linux_$(case $(dpkg --print-architecture) in "amd64") echo "amd64" ;; "arm64") echo "arm64" ;; esac).tar.gz" \
    | bsdtar -xvf - -C /usr/local/bin
chmod +x /usr/local/bin/fzf
# Clean
rm -rf /var/lib/apt/lists/*
EOF

# Locale
ENV LANG="en_US.UTF-8"

##########
# System #
##########

ENV PIPX_HOME="/usr/local/pipx"
ENV PIPX_BIN_DIR="/usr/local/bin"

RUN <<EOF
apt-get --quiet update
apt-get --quiet --yes --no-install-recommends --verbose-versions install \
    openssh-client \
    pipx \
    python3 \
    shellcheck \
    sshpass \
    goss
# Sudo
echo "Defaults env_keep += \"PIPX_*\"" > /etc/sudoers.d/pipx
# Clean
rm -rf /var/lib/apt/lists/*
EOF

# Docker
RUN <<EOF
curl -sSLf https://download.docker.com/linux/debian/gpg \
    --output /etc/apt/keyrings/docker.asc
printf "\
Types: deb\n\
URIs: https://download.docker.com/linux/debian\n\
Suites: $(. /etc/os-release; echo "${VERSION_CODENAME}")\n\
Components: stable\n\
Signed-By: /etc/apt/keyrings/docker.asc\n\
" > /etc/apt/sources.list.d/docker.sources
apt-get --quiet update
apt-get --quiet --yes --no-install-recommends --verbose-versions install \
    docker-ce-cli
# Clean
rm -rf /var/lib/apt/lists/*
EOF

# Ansible
RUN <<EOF
pipx install --pip-args="--no-cache-dir" \
    ansible-core==2.18.9
pipx inject --pip-args="--no-cache-dir" ansible-core \
    docker==7.1.0
EOF

# Ansible Lint
RUN <<EOF
BUILD_PACKAGES=( \
    libpython3-dev gcc \
)
apt-get --quiet update
apt-get --quiet --yes --no-install-recommends --verbose-versions install \
    "${BUILD_PACKAGES[@]}"
pipx install --pip-args="--no-cache-dir" \
    ansible-lint[lock]==25.9.1
# Clean
apt-get --quiet --yes --autoremove purge \
    "${BUILD_PACKAGES[@]}"
rm -rf /var/lib/apt/lists/*
EOF

# Ansible Creator
RUN <<EOF
pipx install --pip-args="--no-cache-dir" \
    ansible-creator==25.9.0
EOF

# Molecule
RUN <<EOF
pipx install --pip-args="--no-cache-dir" \
    molecule==25.9.0
pipx inject --pip-args="--no-cache-dir" molecule \
    molecule-plugins[docker]==25.8.12
EOF

# Run
COPY docker/entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]
CMD ["zsh"]
