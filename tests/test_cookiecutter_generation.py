import os
import re
import pathlib

import pytest
from cookiecutter.exceptions import FailedHookException
import sh
import yaml
from binaryornot.check import is_binary

PATTERN = r"{{(\s?cookiecutter)[.](.*?)}}"
RE_OBJ = re.compile(PATTERN)

PROJECT_DIR = pathlib.Path(__file__).resolve().parent.parent
PYPROJECT_TOML = PROJECT_DIR / "pyproject.toml"


@pytest.fixture
def context():
    return {
        "project_name": "My Test Project",
        "project_slug": "my_test_project",
        "description": "A short description of the project.",
        "author_name": "Test Author",
        "domain_name": "example.com",
        "email": "test@example.com",
        "timezone": "UTC",
    }


SUPPORTED_COMBINATIONS = [
    {"windows": "y", "database": "PostgreSQL"},
    {"windows": "y", "database": "SQLite"},
    {"windows": "n", "database": "PostgreSQL"},
    {"windows": "n", "database": "SQLite"},
]


def _fixture_id(ctx):
    """Helper to get a user friendly test name from the parametrized context."""
    return "-".join(f"{key}:{value}" for key, value in ctx.items())


def build_files_list(base_dir):
    """Build a list containing absolute paths to the generated files."""
    return [
        os.path.join(dirpath, file_path)
        for dirpath, subdirs, files in os.walk(base_dir)
        for file_path in files
    ]


def check_paths(paths):
    """Method to check all paths have correct substitutions."""
    # Assert that no match is found in any of the files
    for path in paths:
        if is_binary(path):
            continue

        for line in open(path, "r"):
            match = RE_OBJ.search(line)
            msg = "cookiecutter variable not replaced in {}"
            assert match is None, msg.format(path)


@pytest.mark.parametrize(
    "context_override", SUPPORTED_COMBINATIONS, ids=_fixture_id
)
def test_project_generation(cookies, context, context_override):
    """Test that project is generated and fully rendered."""
    result = cookies.bake(
        extra_context={**context, **context_override}
    )
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == context["project_slug"]
    assert result.project.isdir()

    paths = build_files_list(str(result.project))
    assert paths
    check_paths(paths)


@pytest.mark.parametrize(
    "context_override", SUPPORTED_COMBINATIONS, ids=_fixture_id
)
def test_flake8_passes(cookies, context_override):
    """Generated project should pass flake8."""
    result = cookies.bake(extra_context=context_override)
    result_project_dir = f"{result._project_dir}"

    try:
        sh.flake8(str(result.project), _cwd=result_project_dir)
    except sh.ErrorReturnCode as e:
        pytest.fail(e.stdout.decode())


@pytest.mark.parametrize(
    "context_override", SUPPORTED_COMBINATIONS, ids=_fixture_id
)
def test_black_passes(cookies, context_override):
    """Generated project should pass black."""
    result = cookies.bake(extra_context=context_override)
    result_project_dir = f"{result._project_dir}"
    try:
        sh.black(
            "--config",
            str(PYPROJECT_TOML),
            "--check",
            "--diff",
            "--exclude",
            "migrations",
            f"{result.project}/",
            _cwd=result_project_dir,
        )
    except sh.ErrorReturnCode as e:
        pytest.fail(e.stdout.decode())


def test_travis_invokes_pytest(cookies, context):
    result = cookies.bake(extra_context=context)

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == context["project_slug"]
    assert result.project.isdir()

    with open(f"{result.project}/.travis.yml", "r") as travis_yml:
        try:
            assert yaml.safe_load(travis_yml)["script"] == [
                "pytest"
            ]
        except yaml.YAMLError as e:
            pytest.fail(e)


def test_gitlab_invokes_flake8_and_pytest(cookies, context):
    result = cookies.bake(extra_context=context)

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == context["project_slug"]
    assert result.project.isdir()

    with open(
        f"{result.project}/.gitlab-ci.yml", "r"
    ) as gitlab_yml:
        try:
            gitlab_config = yaml.safe_load(gitlab_yml)
            assert gitlab_config["flake8"]["script"] == ["flake8"]
            assert gitlab_config["pytest"]["script"] == ["pytest"]
        except yaml.YAMLError as e:
            pytest.fail(e)


@pytest.mark.parametrize("slug", ["project slug", "Project_Slug"])
def test_invalid_slug(cookies, context, slug):
    """Invalid slug should failed pre-generation hook."""
    context.update({"project_slug": slug})

    result = cookies.bake(extra_context=context)

    assert result.exit_code != 0
    assert isinstance(result.exception, FailedHookException)
