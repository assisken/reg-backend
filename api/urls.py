from django.urls import path
from api.views.linux_pass_reset import LinuxPassReset
from api.views.database_create import DatabaseCreate
from api.views.database_remove import DatabaseRemove
from api.views.db_user_create import DbUserCreate
from api.views.db_user_reset import DbUserReset

urlpatterns = [
    path('linux-pass-reset', LinuxPassReset.as_view(), name='linux_pass_reset'),
    path('create-db/', DatabaseCreate.as_view(), name='create_db'),
    path('remove-db/', DatabaseRemove.as_view(), name='remove_db'),
    path('db-user-create/', DbUserCreate.as_view(), name='db_user_create'),
    path('db-user-reset/', DbUserReset.as_view(), name='db_user_reset')
]
