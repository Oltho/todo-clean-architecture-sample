from todo_sample.entities.todo import Todo
from todo_sample.repository.exception import AlreadyExistError
from todo_sample.repository.todo_repository import TodoRepository

from .exceptions import CreateTodoAlreadyExistException


class CreateTodo:
    def __init__(self, todo_repo: TodoRepository) -> None:
        self.todo_repo = todo_repo

    def call(self, title: str, description: str) -> Todo:
        todo = Todo(title=title, description=description)

        try:
            self.todo_repo.save(todo=todo, create_only=True)
        except AlreadyExistError as exc:
            raise CreateTodoAlreadyExistException(f"Todo with same id:{todo.id} already exist.") from exc

        return todo
