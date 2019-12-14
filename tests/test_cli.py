from click.testing import CliRunner
from referencer import cli


# Tests

def test_cli():
    runner = CliRunner()
    result = runner.invoke(cli, ['referencer', 'README.md'])
    assert result.exit_code == 0
    assert result.output.startswith('# referencer-py')


def test_cli_version():
    runner = CliRunner()
    result = runner.invoke(cli, ['--version'])
    assert result.exit_code == 0
    assert len(result.output.split('.')) == 3
