import click
from namespace.command.example_command import example_command


@click.group()
def cli():
    """Command line entrypoint for the boilerplate."""
    pass


cli.add_command(example_command)

if __name__ == '__main__':
    cli()
