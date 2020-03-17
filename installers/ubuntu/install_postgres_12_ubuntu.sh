#!/usr/bin/env sh

#
# Based on https://www.postgresql.org/download/linux/ubuntu/
#

sudo echo "" && wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add - \
&& sudo sh -c 'echo "deb [arch=amd64] http://apt.postgresql.org/pub/repos/apt/ $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list' \
&& sudo apt-get update \
&& sudo apt-get install --yes postgresql-12 libpq-dev
