import typing as _t
from datetime import datetime

from deepdiff import DeepDiff

from todo_sample.entities.todo import Todo, TodoUpdate
from todo_sample.repository.todo_repository import TodoRepository

from . import get_todo


class UpdateTodo:
    INCLUDE_FILTER = set(TodoUpdate().dict().keys())

    def __init__(self, todo_repo: TodoRepository) -> None:
        self.todo_repo = todo_repo

    def call(self, id: str, todo_update: TodoUpdate) -> _t.Optional[Todo]:
        """Update a Todo given its ID

        Args:
            id (str): ID of the Todo to update
            todo (Todo): new object to update

        Raises:
            TodoInvalidIdFormatException: when the `id` parameter does not respect UUID4 format
            TodoNotFoundException: when no Todo matching id has been found

        Returns:
            Todo: update Todo
        """
        data_to_update = todo_update.dict(exclude_unset=True)
        if data_to_update == {}:
            # nothing to do
            return None

        todo = get_todo.GetTodo(todo_repo=self.todo_repo).call(id=id)

        todo_updatable_field = todo.dict(include=self.INCLUDE_FILTER)
        if DeepDiff(data_to_update, todo_updatable_field).get("values_changed") is None:
            # nothing to do
            return None

        updated_todo = todo.copy(update=data_to_update)
        updated_todo.updated_at = datetime.utcnow()

        self.todo_repo.save(todo=updated_todo, create_only=False)

        return updated_todo
