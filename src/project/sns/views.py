from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.views import generic
from .models import Post

User = get_user_model()
# Create your views here.


class IndexView(generic.TemplateView):
    """
    ダミーページ
    """
    template_name = 'hoge.html'


def signupfunc(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username, '', password)
        except Exception as e:
            return render(request, 'signup.html', {'error': e})
        return render(request, 'signup.html', {'msg': 'successfully'})
    return render(request, 'signup.html', {'msg': ''})


def loginfunc(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('sns:list')
        else:
            return render(request, 'signin.html', {'error': 'no such a user'})
    return render(request, 'signin.html')  # ifじゃなかった時、つまりgetだったときはそのページの見た目だけを返す


def signoutfunc(request):
    logout(request)
    return redirect('sns:signin')


@login_required
def listfunc(request):
    posts = Post.objects.all()
    user = request.user
    return render(request, 'list.html', {'posts': posts, 'user': user})
