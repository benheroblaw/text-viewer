#!/usr/bin/env bash
REQUIRED_PKGS=("python3"         )
green='\033[0;32m'
red='\033[0;31m'
white='\033[0;0;0m'

for i in "${REQUIRED_PKGS[@]}"
do
  if dpkg -s $i &> /dev/null; then
    printf '%b\n' "$green$i is installed!$white"
  else
    printf '%b\n' "$red$i is not installed!$white"
    printf '%b\n' "installing..."
    sudo apt install $i
    if dpkg -s $i &> /dev/null; then
      printf '%b\n' "$green$i is installed!$white"
    fi
  fi
done

printf '%b\n' $green "all dependencies are installed!$white"