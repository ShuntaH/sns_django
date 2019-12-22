from django.urls import path
from .views import signupfunc, loginfunc, IndexView, listfunc, signoutfunc

app_name = 'sns'

urlpatterns = [
    path(r'signup/', signupfunc, name='signup'),
    path(r'signin/', loginfunc, name='signin'),
    path(r'signout/', signoutfunc, name='signout'),
    path(r'list/', listfunc, name='list'),
    path(r'hoge/', IndexView.as_view(), name='index'),
]
