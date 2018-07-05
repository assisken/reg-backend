from django.urls import path

from .views import ProfileInfo, ProfileInstruction, ProfileControlPanel, TeacherView

urlpatterns = [
    path('', ProfileInfo.as_view(), name='index'),
    path('instruction/', ProfileInstruction.as_view(), name='instruction'),
    path('panel/', ProfileControlPanel.as_view(), name='panel'),
    path('teacher/', TeacherView.as_view(), name='teacher')
]
