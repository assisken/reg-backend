from django.urls import path
from .views import LinuxPassReset, DatabaseCreate, DatabaseRemove, DbUserCreate, DbUserReset

urlpatterns = [
    path('linux-pass-reset', LinuxPassReset.as_view(), name='linux_pass_reset'),
    path('create-db/', DatabaseCreate.as_view(), name='create_db'),
    path('remove-db/', DatabaseRemove.as_view(), name='remove_db'),
    path('db-user-create/', DbUserCreate.as_view(), name='db_user_create'),
    path('db-user-reset/', DbUserReset.as_view(), name='db_user_reset')
]
