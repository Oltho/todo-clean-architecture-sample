from uuid import UUID

from todo_sample.entities.todo import Todo
from todo_sample.repository.todo_repository import TodoRepository

from .exceptions import TodoInvalidIdFormatException, TodoNotFoundException


class GetTodo:
    def __init__(self, todo_repo: TodoRepository) -> None:
        self.todo_repo = todo_repo

    def call(self, id: str) -> Todo:
        """Retreive a Todo by its ID

        Args:
            id (str): UUID4 format ID

        Raises:
            TodoInvalidIdFormatException: when the `id` parameter does not respect UUID4 format
            TodoNotFoundException: when no Todo matching id has been found

        Returns:
            Todo: Todo that match the `id`
        """
        try:
            id_uuid = UUID(id)
        except ValueError as exc:
            raise TodoInvalidIdFormatException(f"{id} is not a valid UUID4 format.") from exc

        todo = self.todo_repo.find_by_id(id=id_uuid)

        if not todo:
            raise TodoNotFoundException(f"Todo with id:{id} not found.")

        return todo
