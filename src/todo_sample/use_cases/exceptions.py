class CreateTodoException(Exception):
    """CreateTodoException"""

    pass


class CreateTodoAlreadyExistException(CreateTodoException):
    """CreateTodoAlreadyExistException"""

    pass


class TodoException(Exception):
    """TodoException"""

    pass


class TodoInvalidIdFormatException(TodoException):
    """TodoInvalidIdFormatException"""

    pass


class TodoNotFoundException(TodoException):
    """TodoNotFoundException"""

    pass
