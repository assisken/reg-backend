import json
from enum import Enum, auto

from django.http import HttpResponse, JsonResponse


class NotificationType(Enum):
    error = auto()
    warning = auto()
    success = auto()

    danger = error


class Notification:
    __slots__ = ('__type', 'content')

    def __init__(self, type: NotificationType, content):
        self.__type = type
        self.content = content

    def __str__(self):
        return self.to_json()

    @property
    def type(self) -> str:
        return {
            NotificationType.error: 'danger',
            NotificationType.danger: 'danger',
            NotificationType.warning: 'warning',
            NotificationType.success: 'success'
        }[self.__type]

    def to_json(self) -> str:
        return str(json.dumps(
            {'type': self.type, 'message': self.content},
            ensure_ascii=False
        ))

    def as_response(self):
        return JsonResponse({'type': self.type, 'message': self.content})

    @classmethod
    def error(cls, content):
        return Notification(type=NotificationType.error, content=content).as_response()

    @classmethod
    def danger(cls, content):
        return Notification(type=NotificationType.error, content=content).as_response()

    @classmethod
    def warning(cls, content):
        return Notification(type=NotificationType.error, content=content).as_response()

    @classmethod
    def success(cls, content):
        return Notification(type=NotificationType.error, content=content).as_response()
