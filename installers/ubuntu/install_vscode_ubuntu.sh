#!/usr/bin/env sh

#
# Based on https://code.visualstudio.com/docs/setup/linux#_debian-and-ubuntu-based-distributions
#
sudo echo "" && sudo apt-get update \
&& sudo apt-get install --yes apt-transport-https curl \
&& wget --quiet -O - https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg \
&& sudo install -o root -g root -m 644 packages.microsoft.gpg /usr/share/keyrings/ \
&& sudo sh -c 'echo "deb [arch=amd64 signed-by=/usr/share/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/vscode stable main" > /etc/apt/sources.list.d/vscode.list' \
&& sudo apt-get update \
&& sudo apt-get install --yes code
