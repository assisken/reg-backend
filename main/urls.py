from django.urls import path
from main.views import auth, index, make_home, login, logout, profile

urlpatterns = [
    path('', index.index, name='index'),
    path('login/', login.login, name='login'),
    path('profile/', profile.profile, name='profile'),
    path('conf/', make_home.make_home, name='make_home'),
    path('logout/', logout.logout, name='logout'),
    path('oidc_callback', auth.auth, name='auth')
]
