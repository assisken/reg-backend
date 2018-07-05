from django.urls import path
from .views import Auth, Index, Logout, Login

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('oidc_callback', Auth.as_view(), name='auth'),
]
