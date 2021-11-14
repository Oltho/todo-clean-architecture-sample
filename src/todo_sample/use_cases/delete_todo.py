from uuid import UUID

from todo_sample.entities.todo import Todo
from todo_sample.repository.todo_repository import TodoRepository

from .exceptions import GetTodoInvalidIdFormatException, GetTodoNotFoundException


class DeleteTodo:
    def __init__(self, todo_repo: TodoRepository) -> None:
        self.todo_repo = todo_repo

    def call(self, id: str) -> Todo:
        """Delete a Todo by its ID

        Args:
            id (str): UUID4 format ID

        Raises:
            GetTodoInvalidIdFormatException: when the `id` parameter does not respect UUID4 format
            GetTodoNotFoundException: when no Todo matching id has been found

        Returns:

        """
        try:
            id_uuid = UUID(id)
        except ValueError as exc:
            raise GetTodoInvalidIdFormatException(f"{id} is not a valid UUID4 format.") from exc

        todo = self.todo_repo.find_by_id(id=id_uuid)

        if not todo:
            raise GetTodoNotFoundException(f"Todo with id:{id} not found.")

        self.todo_repo.delete(id=id_uuid)

        return None
