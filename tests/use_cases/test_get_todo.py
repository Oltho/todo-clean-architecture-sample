from unittest import TestCase

import pytest

from todo_sample.entities.todo import Todo
from todo_sample.use_cases.exceptions import TodoInvalidIdFormatException, TodoNotFoundException
from todo_sample.use_cases.get_todo import GetTodo

MODULE = "todo_sample.use_cases.get_todo"


class TestGetTodo(TestCase):
    @pytest.fixture(autouse=True)
    def _fake_todo_fixture(self, mocker):
        self.fake_todo = Todo(title="title", description="description")

    @pytest.fixture(autouse=True)
    def _fake_todo_repo_fixture(self, mocker):
        self.fake_todo_repository = mocker.Mock()
        self.get_todo_uc = GetTodo(todo_repo=self.fake_todo_repository)

    def test_get_todo(self):
        self.fake_todo_repository.find_by_id.return_value = self.fake_todo

        todo = self.get_todo_uc.call(id=str(self.fake_todo.id))

        self.fake_todo_repository.find_by_id.assert_called_once_with(id=self.fake_todo.id)
        assert self.fake_todo == todo

    def test_get_todo_wrong_id_format(self):
        fake_id = "some-wrong-format-id"
        try:
            self.get_todo_uc.call(id=fake_id)
        except TodoInvalidIdFormatException as exc:
            assert fake_id in str(exc)

    def test_get_todo_not_found(self):
        self.fake_todo_repository.find_by_id.return_value = None

        try:
            self.get_todo_uc.call(id=str(self.fake_todo.id))
        except TodoNotFoundException as exc:
            assert str(self.fake_todo.id) in str(exc)

        self.fake_todo_repository.find_by_id.assert_called_once_with(id=self.fake_todo.id)
