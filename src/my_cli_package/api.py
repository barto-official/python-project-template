from my_package.application.commands import ValidateCommand
from my_package.application.services import ValidationService


def validate(path: str):
    service = ValidationService()
    return service.validate(ValidateCommand(path=path))
