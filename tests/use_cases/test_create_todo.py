from todo_sample.entities.todo import Todo
from todo_sample.repository.exception import AlreadyExistError
from todo_sample.use_cases.create_todo import CreateTodo
from todo_sample.use_cases.exceptions import CreateTodoAlreadyExistException

MODULE = "todo_sample.use_cases.create_todo"


def test_create_todo(mocker):
    fake_todo = Todo(title="title", description="description")
    mocker.patch(f"{MODULE}.Todo", mocker.Mock(return_value=fake_todo))

    fake_todo_repository = mocker.Mock()

    create_todo_uc = CreateTodo(todo_repo=fake_todo_repository)

    created_todo = create_todo_uc.call(title="title", description="description")

    fake_todo_repository.save.assert_called_once_with(todo=fake_todo, create_only=True)
    assert created_todo == fake_todo


def test_create_todo_already_exist(mocker):
    fake_todo = Todo(title="title", description="description")
    mocker.patch(f"{MODULE}.Todo", mocker.Mock(return_value=fake_todo))

    fake_todo_repository = mocker.Mock()
    fake_todo_repository.save.side_effect = AlreadyExistError()

    create_todo_uc = CreateTodo(todo_repo=fake_todo_repository)

    try:
        create_todo_uc.call(title="title", description="description")
    except CreateTodoAlreadyExistException as exc:
        assert str(fake_todo.id) in str(exc)

    fake_todo_repository.save.assert_called_once_with(todo=fake_todo, create_only=True)
