from unittest import TestCase, mock

import pytest

from todo_sample.entities.todo import Todo
from todo_sample.use_cases.delete_todo import DeleteTodo
from todo_sample.use_cases.exceptions import TodoInvalidIdFormatException

MODULE = "todo_sample.use_cases.delete_todo"


class TestGetTodo(TestCase):
    @pytest.fixture(autouse=True)
    def _fake_todo_fixture(self, mocker):
        self.fake_todo = Todo(title="title", description="description")

    @pytest.fixture(autouse=True)
    def _fake_todo_repo_fixture(self, mocker):
        self.fake_todo_repository = mocker.Mock()
        self.delete_todo_uc = DeleteTodo(todo_repo=self.fake_todo_repository)

    @mock.patch(f"{MODULE}.get_todo.GetTodo")
    def test_delete_todo(self, mocked_gettodo):
        fake_gettodo = mock.Mock()
        fake_gettodo.call.return_value = self.fake_todo
        mocked_gettodo.return_value = fake_gettodo

        id_str = str(self.fake_todo.id)

        ret = self.delete_todo_uc.call(id=id_str)

        mocked_gettodo.assert_called_once_with(todo_repo=self.fake_todo_repository)
        fake_gettodo.call.assert_called_once_with(id=id_str)
        self.fake_todo_repository.delete.assert_called_once_with(id=self.fake_todo.id)
        assert ret is None

    def test_delete_todo_wrong_id_format(self):
        fake_id = "some-wrong-format-id"
        try:
            self.delete_todo_uc.call(id=fake_id)
        except TodoInvalidIdFormatException as exc:
            assert fake_id in str(exc)
