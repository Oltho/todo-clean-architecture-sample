from datetime import datetime
from unittest import TestCase, mock

import pytest

from todo_sample.entities.todo import Todo, TodoUpdate
from todo_sample.use_cases.update_todo import UpdateTodo

MODULE = "todo_sample.use_cases.update_todo"


class TestUpdateTodo(TestCase):
    @pytest.fixture(autouse=True)
    def _fake_todo_fixture(self, mocker):
        self.fake_todo = Todo(title="title", description="description")

    @pytest.fixture(autouse=True)
    def _fake_todo_repo_fixture(self, mocker):
        self.fake_todo_repository = mocker.Mock()
        self.get_todo_uc = UpdateTodo(todo_repo=self.fake_todo_repository)

    def test_nothing_to_do_empty_payload(self):
        todo_update = TodoUpdate()

        updated_todo = self.get_todo_uc.call(id=str(self.fake_todo.id), todo_update=todo_update)

        assert updated_todo is None

    def test_nothing_to_do_same_value(self):
        todo_update = TodoUpdate(title=self.fake_todo.title)
        self.fake_todo_repository.find_by_id.return_value = self.fake_todo
        updated_todo = self.get_todo_uc.call(id=str(self.fake_todo.id), todo_update=todo_update)

        self.fake_todo_repository.find_by_id.assert_called_once_with(id=self.fake_todo.id)
        assert updated_todo is None

    def test_update_all(self):
        fake_now = datetime.utcnow()
        self.fake_todo_repository.find_by_id.return_value = self.fake_todo

        new_title = f"{self.fake_todo.title}-updated"
        new_description = f"{self.fake_todo.description}-updated"
        new_done = not self.fake_todo.done

        todo_update = TodoUpdate(title=new_title, description=new_description, done=new_done)
        expected_updated_todo = Todo(
            id=self.fake_todo.id,
            title=new_title,
            description=new_description,
            done=new_done,
            created_at=self.fake_todo.created_at,
            updated_at=fake_now,
        )

        with mock.patch(f"{MODULE}.datetime") as fake_datetime:
            fake_datetime.utcnow.return_value = fake_now

            updated_todo = self.get_todo_uc.call(id=str(self.fake_todo.id), todo_update=todo_update)

        self.fake_todo_repository.find_by_id.assert_called_once_with(id=self.fake_todo.id)
        self.fake_todo_repository.save.assert_called_once_with(todo=updated_todo, create_only=False)
        assert updated_todo == expected_updated_todo
