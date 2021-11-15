from unittest import TestCase

import pytest

from todo_sample.entities.todo import Todo
from todo_sample.repository.exception import AlreadyExistError
from todo_sample.use_cases.create_todo import CreateTodo
from todo_sample.use_cases.exceptions import TodoAlreadyExistException

MODULE = "todo_sample.use_cases.create_todo"


class TestCreateTodo(TestCase):
    @pytest.fixture(autouse=True)
    def _fake_todo_fixture(self, mocker):
        self.fake_todo = Todo(title="title", description="description")
        mocker.patch(f"{MODULE}.Todo", mocker.Mock(return_value=self.fake_todo))

    @pytest.fixture(autouse=True)
    def _fake_todo_repo_fixture(self, mocker):
        self.fake_todo_repository = mocker.Mock()
        self.create_todo_uc = CreateTodo(todo_repo=self.fake_todo_repository)

    def test_create_todo(self):
        created_todo = self.create_todo_uc.call(title="title", description="description")

        self.fake_todo_repository.save.assert_called_once_with(todo=self.fake_todo, create_only=True)
        assert self.fake_todo == created_todo

    def test_create_todo_already_exist(self):
        self.fake_todo_repository.save.side_effect = AlreadyExistError()

        try:
            self.create_todo_uc.call(title="title", description="description")
        except TodoAlreadyExistException as exc:
            assert exc.id == self.fake_todo.id

        self.fake_todo_repository.save.assert_called_once_with(todo=self.fake_todo, create_only=True)
