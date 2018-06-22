from django.urls import path
from .views import index, control_panel
from .views.actions.linux_pass_reset import LinuxPassReset

urlpatterns = [
    path('', index.ProfileInfo.as_view(), name='index'),
    path('instruction/', index.ProfileInstruction.as_view(), name='instruction'),
    path('panel/', control_panel.ProfileControlPanel.as_view(), name='control_panel'),
    path('linux-pass-reset', LinuxPassReset.as_view(), name='linux_pass_reset')
]
