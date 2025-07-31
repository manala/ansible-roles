printf "\n"
printf "          \033[33m|\033[0m\n"
printf "        \033[33m\ _ /\033[0m     Lazy - Ansible\n"
printf "      \033[33m-= (_) =-\033[0m\n"
printf "        \033[33m/   \ \033[0m        \033[32m_\/_\033[0m\n"
printf "          \033[33m|\033[0m           \033[32m//o\ \033[0m \033[32m_\/_\033[0m\n"
printf "\033[34m   _____ _ __ __ ____ _ \033[32m| \033[34m__\033[32m/o\ \033[34m_\033[0m\n"
printf "\033[34m =-=-_-__=_-= _=_=-=_,-'\033[32m|\033[34m\"'\"\"-\033[32m|\033[34m-,_\033[0m\n"
printf "\033[34m  =- _=-=- -_=-=_,-\"          \033[32m|\033[34m\"\033[0m\n"
printf "\033[34m    =- =- -=.--\"\033[0m\n"
printf "\n"
printf " \033[36m‣ ansible \033[35m2.15.12\033[0m\n"
printf "    \033[36m· docker==7.1.0\033[0m\n"
printf " \033[36m‣ ansible-lint \033[35m24.7.0\033[0m\n"
printf " \033[36m‣ molecule \033[35m24.12.0\033[0m\n"
printf "    \033[36m· molecule-plugins[docker]==23.5.3\033[0m\n"
printf "\n"
cat << EOF
## Containerd ##
Build of test containers with Molecule is incompatible with Containerd on Mac ARM
Turn it off in Docker Desktop in order to launch your tests in local
EOF
