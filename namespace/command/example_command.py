import click

from namespace.container.example_container import ExampleContainer
from namespace.service.example_service import ExampleService


@click.command(name="example")
def example_command():
    """Print the example payload produced by the service layer."""
    container: ExampleContainer = ExampleContainer.getInstance()
    example_service: ExampleService = container.get(ExampleService)

    example = example_service.get_example()
    click.echo(f"{example.title}: {example.message}")
