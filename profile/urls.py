from django.urls import path
from .views import index, control_panel
from .views.actions.linux_pass_reset import LinuxPassReset
from .views.actions.database_create import DatabaseCreate
from .views.actions.database_remove import DatabaseRemove

urlpatterns = [
    path('', index.ProfileInfo.as_view(), name='index'),
    path('instruction/', index.ProfileInstruction.as_view(), name='instruction'),
    path('panel/', control_panel.ProfileControlPanel.as_view(), name='panel'),
    path('linux-pass-reset', LinuxPassReset.as_view(), name='linux_pass_reset'),
    path('create-db/', DatabaseCreate.as_view(), name='create_db'),
    path('remove-db/', DatabaseRemove.as_view(), name='remove_db')
]
