import typing as _t
from abc import ABCMeta, abstractmethod
from uuid import UUID

from todo_sample.entities.todo import Todo


class TodoRepository(ABCMeta):
    @abstractmethod
    def create(self, todo: Todo) -> Todo:
        raise NotImplementedError

    @abstractmethod
    def update(self, todo: Todo) -> Todo:
        raise NotImplementedError

    @abstractmethod
    def find_by_id(self, id: UUID) -> _t.Optional[Todo]:
        raise NotImplementedError

    @abstractmethod
    def delete(self, id: UUID) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_all(self) -> _t.Iterable[Todo]:
        raise NotImplementedError
