from typing import List

from namespace.entity.example_entity import ExampleEntity
from namespace.repository.abstract_example_repository import AbstractExampleRepository


class ExampleManager:
    """Coordinates repository actions for ExampleEntity objects."""

    def __init__(self, repository: AbstractExampleRepository):
        self.repository = repository

    def create(self, entity: ExampleEntity) -> ExampleEntity:
        return self.repository.save(entity)

    def list_examples(self) -> List[ExampleEntity]:
        return self.repository.list_all()
