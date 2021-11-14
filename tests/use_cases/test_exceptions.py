from uuid import uuid4

from todo_sample.use_cases.exceptions import TodoNotFoundException


def test_todonotfoundexception():
    fake_id = uuid4()
    exc = TodoNotFoundException(id=fake_id)

    assert exc.id == fake_id
    assert f"Todo with id:{fake_id} not found." == str(exc)
