from unittest import TestCase

import pytest

from todo_sample.entities.todo import Todo
from todo_sample.use_cases.delete_todo import DeleteTodo
from todo_sample.use_cases.exceptions import TodoInvalidIdFormatException, TodoNotFoundException

MODULE = "todo_sample.use_cases.delete_todo"


class TestGetTodo(TestCase):
    @pytest.fixture(autouse=True)
    def _fake_todo_fixture(self, mocker):
        self.fake_todo = Todo(title="title", description="description")

    @pytest.fixture(autouse=True)
    def _fake_todo_repo_fixture(self, mocker):
        self.fake_todo_repository = mocker.Mock()
        self.delete_todo_uc = DeleteTodo(todo_repo=self.fake_todo_repository)

    def test_delete_todo(self):
        """we could mock GetTodo, but lets try to avoid to much mock (1662232f61aa9a1fe449f66fec97bf63042e5a47)"""
        self.fake_todo_repository.find_by_id.return_value = self.fake_todo

        ret = self.delete_todo_uc.call(id=str(self.fake_todo.id))

        self.fake_todo_repository.find_by_id.assert_called_once_with(id=self.fake_todo.id)
        self.fake_todo_repository.delete.assert_called_once_with(id=self.fake_todo.id)
        assert ret is None

    def test_delete_todo_wrong_id_format(self):
        """Keeping the test but this is already tested in test_get_todo_wrong_id_format"""
        fake_id = "some-wrong-format-id"
        try:
            self.delete_todo_uc.call(id=fake_id)
        except TodoInvalidIdFormatException as exc:
            assert fake_id in str(exc)

    def test_get_todo_not_found(self):
        """Keeping the test but this is already tested in test_get_todo_not_found"""
        self.fake_todo_repository.find_by_id.return_value = None

        try:
            self.delete_todo_uc.call(id=str(self.fake_todo.id))
        except TodoNotFoundException as exc:
            assert exc.id == self.fake_todo.id

        self.fake_todo_repository.find_by_id.assert_called_once_with(id=self.fake_todo.id)
        self.fake_todo_repository.delete.assert_not_called()
