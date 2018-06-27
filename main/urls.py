from django.urls import path
from .views import auth, index, login, logout

urlpatterns = [
    path('', index.Index.as_view(), name='index'),
    path('login/', login.Login.as_view(), name='login'),
    path('logout/', logout.Logout.as_view(), name='logout'),
    path('oidc_callback', auth.Auth.as_view(), name='auth'),
]
