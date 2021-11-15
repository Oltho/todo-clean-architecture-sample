from uuid import uuid4

from todo_sample.use_cases.exceptions import TodoAlreadyExistException, TodoNotFoundException


def test_todonotfoundexception():
    fake_id = uuid4()
    exc = TodoNotFoundException(id=fake_id)

    assert exc.id == fake_id
    assert f"Todo with id:{fake_id} not found." == str(exc)


def test_todoalreadyexistexception():
    fake_id = uuid4()
    exc = TodoAlreadyExistException(id=fake_id)

    assert exc.id == fake_id
    assert f"Todo with id:{fake_id} already exist." == str(exc)
