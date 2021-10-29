import pytest

from todo_sample.hello import hello_name


@pytest.mark.parametrize(
    ("name", "expected"),
    [
        ("Jeanette", "Hello Jeanette !"),
        ("Raven", "Hello Raven !"),
        ("Maxine", "Hello Maxine !"),
        ("Matteo", "Hello Matteo !"),
        ("Destinee", "Hello Destinee !"),
        ("Alden", "Hello Alden !"),
        ("Mariah", "Hello Mariah !"),
        ("Anika", "Hello Anika !"),
        ("Isabella", "Hello Isabella !"),
    ],
)
def test_hello(name, expected):
    """Example test with parametrization."""
    assert hello_name(name) == expected
