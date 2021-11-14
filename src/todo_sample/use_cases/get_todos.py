from typing import Iterable

from todo_sample.entities.todo import Todo
from todo_sample.repository.todo_repository import TodoRepository


class GetTodos:
    def __init__(self, todo_repo: TodoRepository) -> None:
        self.todo_repo = todo_repo

    def call(self) -> Iterable[Todo]:
        todos = self.todo_repo.get_all()

        return todos
