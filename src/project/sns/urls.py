from django.urls import path

from .views import signupfunc, loginfunc, IndexView


app_name = 'sns'

urlpatterns = [
    path(r'signup/', signupfunc, name='signup'),
    path(r'signin/', loginfunc, name='signin'),
    path(r'hoge/', IndexView.as_view(), name='index'),
]
