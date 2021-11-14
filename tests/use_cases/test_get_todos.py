from todo_sample.use_cases.get_todos import GetTodos

MODULE = "todo_sample.use_cases.get_todos"


def test_get_todos(mocker):
    fake_todo_repository = mocker.Mock()
    get_todos_uc = GetTodos(todo_repo=fake_todo_repository)

    todos = get_todos_uc.call()

    assert fake_todo_repository.get_all.return_value == todos
    fake_todo_repository.get_all.assert_called_once()
