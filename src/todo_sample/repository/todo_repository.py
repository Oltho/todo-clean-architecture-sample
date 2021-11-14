import typing as _t
from abc import ABCMeta, abstractmethod
from uuid import UUID

from todo_sample.entities.todo import Todo


class TodoRepository(ABCMeta):
    @abstractmethod
    def save(self, todo: Todo, create_only: bool = True) -> Todo:
        """Create or update a Todo object in repository

        Args:
            todo (Todo): Todo object to save
            create_only (bool, optional):
                If True will raise `AlreadyExistError` if a Todo with same `id` already exist
                If false will either create a new object or update the one with the same `id`.
                Defaults to True.

        Raises:
            AlreadyExistError: raise when trying to save an Todo that already exist

        Returns:
            Todo: the object that has been saved
        """
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
