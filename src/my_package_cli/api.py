from my_package.application.services import ValidationService
from my_package.application.commands import ValidateCommand


def validate(path: str):
    service = ValidationService()
    return service.validate(ValidateCommand(path=path))

