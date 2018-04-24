from django.urls import path
from main.views import auth, index, login, profile

urlpatterns = [
    path('', index.index, name='index'),
    path('login/', login.login, name='login'),
    path('profile/', profile.profile, name='profile'),
    path('oidc_callback/', auth.auth)
]
