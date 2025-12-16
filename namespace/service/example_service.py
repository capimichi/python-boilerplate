from injector import inject

from namespace.client.example_client import ExampleClient
from namespace.model.example_model import ExampleModel


class ExampleService:
    """Service layer that wraps ExampleClient."""

    @inject
    def __init__(self, example_client: ExampleClient):
        self.example_client = example_client

    def get_example(self) -> ExampleModel:
        """Return the boilerplate example payload."""
        message = self.example_client.fetch_message()
        return ExampleModel(title="Example", message=message)
