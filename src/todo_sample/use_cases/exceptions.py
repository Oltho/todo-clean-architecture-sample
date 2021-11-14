class CreateTodoException(Exception):
    """CreateTodoException"""


class CreateTodoAlreadyExistException(CreateTodoException):
    """CreateTodoAlreadyExistException"""


class GetTodoInvalidIdFormatException(Exception):
    """GetTodoInvalidIdFormatException"""


class GetTodoNotFoundException(Exception):
    """GetTodoNotFoundException"""
