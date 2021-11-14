class CreateTodoException(Exception):
    """CreateTodoException"""


class CreateTodoAlreadyExistException(CreateTodoException):
    """CreateTodoAlreadyExistException"""


class GetTodoException(Exception):
    """GetTodoException"""


class GetTodoInvalidIdFormatException(GetTodoException):
    """GetTodoInvalidIdFormatException"""


class GetTodoNotFoundException(GetTodoException):
    """GetTodoNotFoundException"""
