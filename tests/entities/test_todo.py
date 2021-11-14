from pydantic import ValidationError

from todo_sample.entities import todo


def test_required_field():
    try:
        todo.Todo()
    except ValidationError as e:
        assert "title" in str(e)
        assert "description" in str(e)


def test_default_field():
    todo_obj = todo.Todo(title="title", description="description")

    # todo: mock datetime to assert fake_now
    assert todo_obj.created_at == todo_obj.updated_at
    assert not todo_obj.done
