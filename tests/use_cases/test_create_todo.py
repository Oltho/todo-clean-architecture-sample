from unittest import TestCase

import pytest

from todo_sample.entities.todo import Todo
from todo_sample.repository.exception import AlreadyExistError
from todo_sample.use_cases.create_todo import CreateTodo
from todo_sample.use_cases.exceptions import CreateTodoAlreadyExistException

MODULE = "todo_sample.use_cases.create_todo"


class TestCreateTodo(TestCase):
    @pytest.fixture(autouse=True)
    def _fake_todo_fixture(self, mocker):
        self.fake_todo = Todo(title="title", description="description")
        mocker.patch(f"{MODULE}.Todo", mocker.Mock(return_value=self.fake_todo))

    @pytest.fixture(autouse=True)
    def _fake_todo_repo_fixture(self, mocker):
        self.fake_todo_repository = mocker.Mock()

    def test_create_todo(self):
        create_todo_uc = CreateTodo(todo_repo=self.fake_todo_repository)

        created_todo = create_todo_uc.call(title="title", description="description")

        self.fake_todo_repository.save.assert_called_once_with(todo=self.fake_todo, create_only=True)
        assert created_todo == self.fake_todo

    def test_create_todo_already_exist(self):
        self.fake_todo_repository.save.side_effect = AlreadyExistError()

        create_todo_uc = CreateTodo(todo_repo=self.fake_todo_repository)

        try:
            create_todo_uc.call(title="title", description="description")
        except CreateTodoAlreadyExistException as exc:
            assert str(self.fake_todo.id) in str(exc)

        self.fake_todo_repository.save.assert_called_once_with(todo=self.fake_todo, create_only=True)
