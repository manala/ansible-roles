#!/bin/sh

set -e

# Ssh agent bridge
if [ -n "${SSH_AUTH_SOCK}" ]; then
  sh -c " \
    while true; do \
      rm -f /var/run/ssh-auth-bridge.sock ;
      socat \
        UNIX-LISTEN:/var/run/ssh-auth-bridge.sock,fork,mode=777 \
        UNIX-CONNECT:/var/run/ssh-auth.sock ; \
      sleep 1; \
    done \
  " &
fi

# Docker bridge
if [ -n "${DOCKER_HOST}" ]; then
  sh -c " \
    while true; do \
      rm -f /var/run/docker-bridge.sock ;
      socat -t 600 \
        UNIX-LISTEN:/var/run/docker-bridge.sock,fork,mode=777 \
        UNIX-CONNECT:/var/run/docker.sock ; \
      sleep 1; \
    done \
  " &
fi

# As a consequence of running the container as root user,
# tty is not writable by sued user
if [ -t 1 ]; then
  chmod 666 "$(tty)"
  GPG_TTY="$(tty)"
  export GPG_TTY
fi

# Home cache
if [ -n "${MANALA_CACHE_DIR}" ]; then
  HOME_DIR=${MANALA_CACHE_DIR}/home
  if [ ! -d "${HOME_DIR}" ]; then
    cp --archive /home/lazy/. "${HOME_DIR}"
  fi
  usermod --home "${HOME_DIR}" lazy 2>/dev/null
fi

# Templates
if [ -d ".manala/etc" ]; then
  GOMPLATE_LOG_FORMAT=simple gomplate --input-dir=.manala/etc --output-dir=/etc 2>/dev/null
fi

# Services
if [ $# -eq 0 ] && [ -d "/etc/services.d" ]; then
    exec s6-svscan /etc/services.d
fi

# Command
exec gosu lazy "$@"
