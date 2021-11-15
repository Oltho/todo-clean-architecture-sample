from uuid import UUID


class TodoException(Exception):
    """TodoException"""

    pass


class CreateTodoAlreadyExistException(TodoException):
    """CreateTodoAlreadyExistException"""

    pass


class TodoInvalidIdFormatException(TodoException):
    """TodoInvalidIdFormatException"""

    pass


class TodoNotFoundException(TodoException):
    """TodoNotFoundException"""

    def __init__(self, id: UUID) -> None:
        self.id = id

    def __str__(self) -> str:
        return f"Todo with id:{self.id} not found."
