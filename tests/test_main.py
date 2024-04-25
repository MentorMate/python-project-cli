import re
import pytest
from typer.testing import CliRunner

from src.python_project_cli.main import (
    Frameworks,
    app,
    REPO_URLS,
    generate_framework,
    __version__,
)

runner = CliRunner()


@pytest.mark.parametrize(
    'user_input',
    [
        Frameworks.django,
        Frameworks.fast_api,
    ],
)
def test_generate_option(user_input):
    result = runner.invoke(app, ['generate'], input=user_input)
    assert (
        f'Please select a framework (Django, FastAPI): {user_input}\n'
        in result.stdout
    )
    assert result.exit_code == 0


@pytest.mark.parametrize(
    'incorrect_user_input',
    [
        'django',
        'fastapi',
        'wrong input',
    ],
)
def test_generate_option_fail_incorrect_input(
    mock_subprocess_run, incorrect_user_input
):
    # NOTE: This is a hack to bypass the choice: Annotated[...], because it hangs,
    #       expecting correct input. That way we can test the first wrong input, while the second one
    #       succedes - freeing the input()
    result = runner.invoke(
        app, ['generate'], input=incorrect_user_input + '\nDjango\n'
    )
    assert (
        f"Error: '{incorrect_user_input}' is not one of 'Django', 'FastAPI'."
        in result.stdout
    )
    assert mock_subprocess_run.call_count < 2


@pytest.mark.parametrize(
    'generate_options',
    [
        (Frameworks.django, REPO_URLS[Frameworks.django]),
        (Frameworks.fast_api, REPO_URLS[Frameworks.fast_api]),
    ],
)
def test_generate_framework(capfd, mock_subprocess_run, generate_options):
    framework_name, repo_url = generate_options
    generate_framework(framework_name)
    stdout, err = capfd.readouterr()
    assert stdout.strip() == f'Generating {framework_name} framework...'
    mock_subprocess_run.assert_called_once_with(['cookiecutter', repo_url])


def test_status():
    result = runner.invoke(app, ['status'])
    rendered_table = """
    ┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┓\n
    ┃ Framework ┃ Repo URL                                                ┃ Status ┃\n
    ┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━┩\n
    │ Django    │ https://github.com/MentorMate/mentormate-django-cookie… │ ✅     │\n
    │ FastAPI   │ https://github.com/gp-mentormate/fastapi-cookiecutter-… │ ❌     │\n
    └───────────┴─────────────────────────────────────────────────────────┴────────┘\n
    """
    assert result.exit_code == 0
    assert re.sub(r'\s+', ' ', result.stdout.strip()) == re.sub(
        r'\s+', ' ', rendered_table.strip()
    )


def test_version():
    result = runner.invoke(app, ['version'])
    assert result.exit_code == 0
    assert result.stdout.strip() == f'CLI Version: {__version__}'
