#!/usr/bin/env sh
git clone https://github.com/rgrannell1/password123
cd password123
echo alias password123=\"python3 \'$(pwd -P)/password123-docopt.py\'\" >> ~/.bashrc && . ~/.bashrc