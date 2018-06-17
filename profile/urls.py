from django.urls import path
from .views import index, control_panel

urlpatterns = [
    path('', index.ProfileInfo.as_view(), name='index'),
    path('instruction/', index.ProfileInstruction.as_view(), name='instruction'),
    path('panel/', control_panel.ProfileControlPanel.as_view(), name='control_panel'),
]
