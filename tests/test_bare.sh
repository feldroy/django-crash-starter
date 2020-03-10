#!/bin/sh
# this is a very simple script that tests the docker configuration for cookiecutter-django
# it is meant to be run from the root directory of the repository, eg:
# sh tests/test_docker.sh

set -o errexit

# install test requirements
pip install -r requirements.txt

# create a cache directory
mkdir -p .cache/bare
cd .cache/bare

# create the project using the default settings in cookiecutter.json
cookiecutter ../../ --no-input --overwrite-if-exists $@
cd everycheese


# Install Python deps
pip install -r requirements/local.txt

# run the project's tests
echo "Running pytest:"
pytest || { echo "ERROR: Pytest report some issues"; exit 1; }

echo "Checking missing migrations:"
# return non-zero status code if there are migrations that have not been created
python manage.py makemigrations --dry-run --check || { echo "ERROR: there were changes in the models, but migration listed above have not been created and are not saved in version control"; exit 1; }
