from todo_sample.repository.todo_repository import TodoRepository

from . import get_todo


class DeleteTodo:
    def __init__(self, todo_repo: TodoRepository) -> None:
        self.todo_repo = todo_repo

    def call(self, id: str) -> None:
        """Delete a Todo by its ID

        Args:
            id (str): UUID4 format ID

        Raises:
            TodoInvalidIdFormatException: when the `id` parameter does not respect UUID4 format
            TodoNotFoundException: when no Todo matching id has been found

        Returns:

        """
        todo = get_todo.GetTodo(todo_repo=self.todo_repo).call(id=id)

        self.todo_repo.delete(id=todo.id)

        return None
