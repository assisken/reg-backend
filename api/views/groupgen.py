import json

from django.db import IntegrityError
from django.http import HttpRequest, HttpResponse
from django.views import View

from main.models.stud_group import StudGroup
from main.models.teacher import Teacher
from main.models.user import User
from profile.forms import GenGroupByFileForm
from profile.mixins import UserRequired
from utils import Notification


class Groupgen(UserRequired, View):
    def post(self, request: HttpRequest, user: User) -> HttpResponse:
        form = GenGroupByFileForm(request.POST, request.FILES)
        if not form.is_valid():
            message = str(form.errors.as_data())
            return HttpResponse(message)

        byte_data: bytes = request.FILES['file'].read()
        data = byte_data.decode('utf-8')
        norm_data = json.loads(data)

        teacher = Teacher.objects.get(user=user)

        try:
            for group_data in norm_data:
                try:
                    group = StudGroup.objects.create(name=group_data['group'])
                except IntegrityError:
                    group = StudGroup.objects.get(name=group_data['group'])

                users_list: list = group_data['users']
                for user_str in users_list:
                    try:
                        surname, name, middlename = user_str.split(' ')
                    except ValueError:
                        return Notification.error('Опечатка в {}'.format(user_str))
                    try:
                        user = User.objects.get(family_name=surname, given_name=name, middle_name=middlename)
                    except User.DoesNotExist:
                        return Notification.error('Пользователь {} не найден'.format(user_str))
                    group.users.add(user)

                group.save()
                teacher.groups.add(group)
                teacher.save()
        except Exception as e:
            raise e
            return Notification.error(str(e))

        return Notification.success('Группа успешно создана и прикреплена к вам!')
