eval "$(direnv hook bash)"

# Config directory
export DIRENV_CONFIG=/etc/direnv

# Faint output
# See: https://github.com/direnv/direnv/wiki/Quiet-or-Silence-direnv
export DIRENV_LOG_FORMAT=$'\033[2mdirenv: %s\033[0m'
