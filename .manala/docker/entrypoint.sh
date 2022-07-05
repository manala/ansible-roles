#!/bin/sh

set -e

# If ssh-agent bind differs from sock, establish an unprivileged relay
if [ -n "${SSH_AUTH_SOCK}" ] && [ -n "${MANALA_SSH_AUTH_SOCK_BIND}" ] && [ "${SSH_AUTH_SOCK}" != "${MANALA_SSH_AUTH_SOCK_BIND}" ]; then
  socat \
    UNIX-LISTEN:"${SSH_AUTH_SOCK}",fork,mode=777 \
    UNIX-CONNECT:"${MANALA_SSH_AUTH_SOCK_BIND}" &
fi

# If docker bind differs from sock, establish an unprivileged relay
if [ -n "${MANALA_DOCKER_SOCK}" ] && [ -n "${MANALA_DOCKER_SOCK_BIND}" ] && [ "${MANALA_DOCKER_SOCK}" != "${MANALA_DOCKER_SOCK_BIND}" ]; then
  socat -t600 \
    UNIX-LISTEN:"${MANALA_DOCKER_SOCK}",fork,mode=777 \
    UNIX-CONNECT:"${MANALA_DOCKER_SOCK_BIND}" &
fi

# As a consequence of running the container as root user,
# tty is not writable by sued user
if [ -t 1 ]; then
  chmod 666 "$(tty)"
  GPG_TTY="$(tty)"
  export GPG_TTY
fi

# Home cache
HOME_DIR=${CACHE_DIR}/home
if [ ! -d "${HOME_DIR}" ]; then
    cp --archive /home/lazy/. "${HOME_DIR}"
fi
usermod --home "${HOME_DIR}" lazy 2>/dev/null

# Templates
GOMPLATE_LOG_FORMAT=simple gomplate --input-dir=.manala/templates --output-dir=/etc 2>/dev/null

# Services
if [ $# -eq 0 ] && [ -d "/etc/services" ]; then
    exec s6-svscan /etc/services
fi

# Command
exec gosu lazy "$@"
