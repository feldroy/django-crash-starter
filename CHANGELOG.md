# Change Log
All enhancements and patches to Cookiecutter Django will be documented in this file.

## [2020-09-28]
### Changed
- Updated pytest to 6.1.0 - [@luzfcb](https://github.com/luzfcb)

## [2020-09-24]
### Changed
- Added a small script to install Postgresql 13 on Ubuntu - [@luzfcb](https://github.com/luzfcb)

## [2020-09-22]
### Changed
- Updated django-debug-toolbar to 3.1 - [@luzfcb](https://github.com/luzfcb)
- Updated django-extensions to 3.0.9 - [@luzfcb](https://github.com/luzfcb)


## [2020-09-16]
### Changed
- Updated coverage to 5.3 - [@luzfcb](https://github.com/luzfcb)
- Removed the coverage workaround on config/settings/test.py. The coverage 5.3 fixed the issue - [@luzfcb](https://github.com/luzfcb)
- Updated pytest-django to 3.10.0 - [@luzfcb](https://github.com/luzfcb)
- Updated django-redis to 4.12.1 - [@luzfcb](https://github.com/luzfcb)

## [2020-09-15]
### Changed
- Updated django-anymail to 8.0 - [@luzfcb](https://github.com/luzfcb)
- Updated pytest to 6.0.2 - [@luzfcb](https://github.com/luzfcb)

## [2020-09-11]
### Changed
- Updated factory-boy to 3.0.1 - [@luzfcb](https://github.com/luzfcb)
- Updated project compatibility with factory-boy v3.0.1 - [@luzfcb](https://github.com/luzfcb)
- Updated black to 20.8b1 - [@luzfcb](https://github.com/luzfcb)
- Updated ipdb to 0.13.3 - [@luzfcb](https://github.com/luzfcb)
- Updated psycopg2-binary to 2.8.6 - [@luzfcb](https://github.com/luzfcb)
- Updated pytest to 6.0.1 - [@luzfcb](https://github.com/luzfcb)
- Updated pytest-sugar to 0.9.4 - [@luzfcb](https://github.com/luzfcb)
- Updated flake8 to 3.8.3 - [@luzfcb](https://github.com/luzfcb)
- Updated coverage to 5.2.1 - [@luzfcb](https://github.com/luzfcb)
- Updated pylint-django to 2.3.0 - [@luzfcb](https://github.com/luzfcb)
- Updated pre-commit to 2.7.1 - [@luzfcb](https://github.com/luzfcb)
- Updated django-extensions to 3.0.8 - [@luzfcb](https://github.com/luzfcb)

## [2020-09-10]
### Changed
- Added a workaround on config/settings/test.py to fix the coverage.py + django_coverage_plugin "Can't add file tracer data for unmeasured file" warning message (https://github.com/feldroy/django-crash-course/issues/329) - [@luzfcb](https://github.com/luzfcb)

## [2020-09-09]
### Changed
- Removed env.sample file - [@luzfcb](https://github.com/luzfcb)
- Updated basic instructions on the README.md - [@luzfcb](https://github.com/luzfcb)
- Updated project to Django 3.1 - [@luzfcb](https://github.com/luzfcb)
- Synced contrib/sites app 0001_initial migration to follow Django 3.1 changes - [@luzfcb](https://github.com/luzfcb)
- Synced users app 0001_initial migration to follow Django 3.1 changes - [@luzfcb](https://github.com/luzfcb)
- Updated black to 20.8b1 - [@luzfcb](https://github.com/luzfcb)
- Updated project compatibility with black v20.8b1 - [@luzfcb](https://github.com/luzfcb)
- Updated tox to 3.20.0 - [@luzfcb](https://github.com/luzfcb)
- Updated pytest-xdist to 2.1.0 - [@luzfcb](https://github.com/luzfcb)
- Updated pytest to 6.0.1 - [@luzfcb](https://github.com/luzfcb)
- Updated psycopg2 to 2.8.6 - [@luzfcb](https://github.com/luzfcb)
- Updated sh to 1.14.0 - [@luzfcb](https://github.com/luzfcb)


## [2020-09-08]
### Changed
- Added env.sample.mac_or_linux and env.sample.windows files - [@pydanny](https://github.com/pydanny)
- Added .env file on gitignore - [@pydanny](https://github.com/pydanny)

## [2020-08-28]
### Changed
- Added basic instructions on the README.md - [@luzfcb](https://github.com/luzfcb)

## [2020-08-10]
### Changed
- Updated whitenoise to 5.2.0 - [@luzfcb](https://github.com/luzfcb)
- Updated tox to 3.19.0 - [@luzfcb](https://github.com/luzfcb)
- Updated django-anymail to 7.2.1 - [@luzfcb](https://github.com/luzfcb)


## [2020-08-03]
### Changed
- Updated Django to 3.0.9 - [@luzfcb](https://github.com/luzfcb)
- Updated tox to 3.18.1 - [@luzfcb](https://github.com/luzfcb)
- Updated pytest-xdist to 1.34.0 - [@luzfcb](https://github.com/luzfcb)

## [2020-07-27]
### Changed
- Updated django-autoslug to 1.9.8 - [@luzfcb](https://github.com/luzfcb)
- Updated tox to 3.18.0 - [@luzfcb](https://github.com/luzfcb)
- Updated django-anymail to 7.2 - [@luzfcb](https://github.com/luzfcb)
- Updated django-autoslug to 1.9.8 - [@luzfcb](https://github.com/luzfcb)

## [2020-07-17]
### Changed
- Ignore sqlite database on git - [@luzfcb](https://github.com/luzfcb)

## [2020-07-09]
### Changed
- Fix the Sqlite database filename when generate the project with `windows=y` - [@luzfcb](https://github.com/luzfcb)

## [2020-07-08]
### Changed
- Explicitly define which settings variables should be included in the template context - [@pydanny](https://github.com/pydanny)

## [2020-07-06]
### Changed
- Automatically read an .env file, if it exists in the project's root path - [@luzfcb](https://github.com/luzfcb)
- Updated tox to 3.16.1 - [@luzfcb](https://github.com/luzfcb)
- Updated pillow to 7.2.0 - [@luzfcb](https://github.com/luzfcb)
- Updated python-slugify to 4.0.1 - [@luzfcb](https://github.com/luzfcb)
- Updated Django to 3.0.8 - [@luzfcb](https://github.com/luzfcb)

## [2020-07-02]
### Changed
- Migrate to pathlib - [@luzfcb](https://github.com/luzfcb)

## [2020-06-29]
### Changed
- Updated tox to 3.16.0 - [@luzfcb](https://github.com/luzfcb)

## [2020-06-22]
### Changed
- Switch to dark navbar - [@pydanny](https://github.com/pydanny)

## [2020-06-18]
### Changed
- Updated flake8 to 3.8.3 - [@luzfcb](https://github.com/luzfcb)
- Updated pytest to 5.4.3 - [@luzfcb](https://github.com/luzfcb)

## [2020-06-12]
### Changed
- Small fixes in the .coveragerc file - [@pydanny](https://github.com/pydanny)


## [2020-06-01]
### Changed
- Fixed the project generation when select database=SQLite and windows=n - [@luzfcb](https://github.com/luzfcb)
- Applyed black formatting on production.py - [@luzfcb](https://github.com/luzfcb)
- Small fixes in the project generation tests - [@luzfcb](https://github.com/luzfcb)
- Updated pytest to 5.4.2 - [@luzfcb](https://github.com/luzfcb)
- Updated flake8 to 3.8.2 - [@luzfcb](https://github.com/luzfcb)
- Updated pylint-django to 2.0.15 - [@luzfcb](https://github.com/luzfcb)
- Updated pre-commit to 2.4.0 - [@luzfcb](https://github.com/luzfcb)

## [2020-05-09]
### Changed
- Windows must use Sqlite - [@pydanny](https://github.com/pydanny)

## [2020-04-29]
### Changed
- Added a small batch script to install Chocolatey on Windows - [@luzfcb](https://github.com/luzfcb)
- Fixed a small code style issue on UserDetailView [@luzfcb](https://github.com/luzfcb)
- Added comments about slug_field and slug_url_kwarg usage on UserDetailView class - [@pydanny](https://github.com/pydanny)
- Updated mypy to 0.770 [@luzfcb](https://github.com/luzfcb)
- Removed django-compressor to due install problems on Windows 10 [@luzfcb](https://github.com/luzfcb)

## [2020-04-03]
### Changed
- Added a small script to install Visual Studio Code on Ubuntu [@luzfcb](https://github.com/luzfcb)
- Added a small script to install Postgresql 12 on Ubuntu [@luzfcb](https://github.com/luzfcb)
- Explained the behavior when DATABASE_URL is not found [@luzfcb](https://github.com/luzfcb)
- Renamed ROOT_DIR to BASE_DIR to follow the django `startproject` nomenclature [@luzfcb](https://github.com/luzfcb)
- Replaced the usage of ugettext_lazy by gettext_lazy  [@luzfcb](https://github.com/luzfcb)
- Added Django 3.0 asgi.py file [@luzfcb](https://github.com/luzfcb)
- Added pyproject.toml to configure black [@luzfcb](https://github.com/luzfcb)
- Formatted the code with black following the rules defined on pyproject.toml [@luzfcb](https://github.com/luzfcb)
- Fixed some flake8 formatting issues [@luzfcb](https://github.com/luzfcb)
- Fixed and improve the test suite [@luzfcb](https://github.com/luzfcb) 
- Updated .travis.yml to follow the new Travis cfg standard [@luzfcb](https://github.com/luzfcb)
- Configured travis-ci to use Ubuntu 18.04 instead of 16.04 [@luzfcb](https://github.com/luzfcb)
- Fixed formatting issues on DATABASES section to be able to generate project compliant with pep8 [@luzfcb](https://github.com/luzfcb)
- Added Travis-ci Badge [@luzfcb](https://github.com/luzfcb)
- Updated project configurations to use Python 3.8 [@luzfcb](https://github.com/luzfcb)
- Updated django 3.0.4 [@luzfcb](https://github.com/luzfcb)
- Updated pre-commit to 2.2.0 [@luzfcb](https://github.com/luzfcb)
- Updated mypy to 0.661 [@luzfcb](https://github.com/luzfcb)
- Updated werkzeug to 1.0.0 [@luzfcb](https://github.com/luzfcb)
- Updated django-debug-toolbar to 2.2 [@luzfcb](https://github.com/luzfcb)
- Updated pytest to 5.3.5 [@luzfcb](https://github.com/luzfcb)
- Updated pylint-django to 2.0.14 [@luzfcb](https://github.com/luzfcb)
- Updated django-crispy-forms to 1.9.0 [@luzfcb](https://github.com/luzfcb)
- Updated django-debug-toolbar to 2.2 [@luzfcb](https://github.com/luzfcb)
- Updated django-extensions to 2.2.8 [@luzfcb](https://github.com/luzfcb)
- Updated ipdb to 0.13.2 [@luzfcb](https://github.com/luzfcb)
- Updated collectfast to 2.1.0 [@luzfcb](https://github.com/luzfcb)

## [2020-03-05]
### Changed
- Fixed misformatted unidecode version number - [@luzfcb](https://github.com/luzfcb)
- Added a link to django-autoslug repository on the base.txt - [@luzfcb](https://github.com/luzfcb)
- Added dependabot configuration file - [@luzfcb](https://github.com/luzfcb)
- Removed PyUP configuration file - [@luzfcb](https://github.com/luzfcb)

## [2020-02-18]
### Changed
- Fixed UserUpdateView - [@quique](https://github.com/quique)

## [2020-01-30]
### Changed
- Added missing imports, and got SQLite to run - [@pydanny](https://github.com/pydanny)
- Converted CONTRIBUTORS.rst to markdown - [@pydanny](https://github.com/pydanny)
- Removed bio from models - [@edvm](https://github.com)

## [2020-01-28]
### Changed
- Hard fork of Cookiecutter-Django project - [@pydanny](https://github.com/pydanny)

## Before Hard Fork of CookiecutterDjango

[Cookiecutter Django Changelog](https://github.com/pydanny/cookiecutter-django/blob/master/CHANGELOG.md)
