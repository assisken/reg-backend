from django.contrib import admin

from main.models.stud_group import StudGroup
from main.models.teacher import Teacher
from .models.user import User
from .models.user_group import UserGroup


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('sub', 'family_name', 'given_name', 'middle_name', 'email', 'email_verified',)
    ordering = ('sub',)
    list_filter = ('email_verified',)
    exclude = ('db_password',)


@admin.register(UserGroup)
class UserGroupAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(StudGroup)
class StudGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_users')

    def get_users(self, group: StudGroup):
        return ', '.join(['{surname} {name}'.format(
            surname=u.family_name, name=u.given_name
        ) for u in group.users.all()])

    get_users.allow_tags = True


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'get_groups')

    def get_groups(self, teacher: Teacher):
        return ', '.join([g.__str__() for g in teacher.groups.all()])
