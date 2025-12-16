from injector import Injector

from namespace.client.example_client import ExampleClient
from namespace.controller.example_controller import ExampleController
from namespace.service.example_service import ExampleService


class ExampleContainer:
    injector = None
    instance = None

    @staticmethod
    def getInstance():
        if ExampleContainer.instance is None:
            ExampleContainer.instance = ExampleContainer()
        return ExampleContainer.instance

    def __init__(self):
        self.injector = Injector()
        self._init_bindings()

    def get(self, key):
        return self.injector.get(key)

    def _init_bindings(self):
        example_client = ExampleClient()
        self.injector.binder.bind(ExampleClient, to=example_client)

        example_service = ExampleService(example_client)
        self.injector.binder.bind(ExampleService, to=example_service)

        example_controller = ExampleController(example_service)
        self.injector.binder.bind(ExampleController, to=example_controller)
