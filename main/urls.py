from django.urls import path
from .views import auth, index, login, logout

urlpatterns = [
    path('', index.index, name='index'),
    path('login/', login.login, name='login'),
    # path('conf/', make_home.make_home, name='make_home'),
    path('logout/', logout.logout, name='logout'),
    path('oidc_callback', auth.auth, name='auth')
]
