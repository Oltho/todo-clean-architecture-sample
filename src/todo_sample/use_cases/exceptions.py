class CreateTodoException(Exception):
    """CreateTodoException"""

    pass


class CreateTodoAlreadyExistException(CreateTodoException):
    """CreateTodoAlreadyExistException"""

    pass


class GetTodoException(Exception):
    """GetTodoException"""

    pass


class GetTodoInvalidIdFormatException(GetTodoException):
    """GetTodoInvalidIdFormatException"""

    pass


class GetTodoNotFoundException(GetTodoException):
    """GetTodoNotFoundException"""

    pass
