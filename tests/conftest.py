import pytest
from unittest.mock import patch


@pytest.fixture()
def mock_subprocess_run():
    with patch('src.python_project_cli.main.run') as mocked_function:
        yield mocked_function
