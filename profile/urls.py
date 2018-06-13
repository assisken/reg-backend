from django.urls import path
from .views import index, control_panel

urlpatterns = [
    path('', index.info, name='index'),
    path('instruction/', index.instruction, name='instruction'),
    path('panel/', control_panel.control_panel, name='control_panel'),
]
