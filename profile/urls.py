from django.urls import path
from .views import index, control_panel
from api.views.linux_pass_reset import LinuxPassReset
from api.views.database_create import DatabaseCreate
from api.views.database_remove import DatabaseRemove
from api.views.db_user_create import DbUserCreate
from api.views.db_user_reset import DbUserReset

urlpatterns = [
    path('', index.ProfileInfo.as_view(), name='index'),
    path('instruction/', index.ProfileInstruction.as_view(), name='instruction'),
    path('panel/', control_panel.ProfileControlPanel.as_view(), name='panel'),
]
