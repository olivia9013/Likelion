from django.shortcuts import render, redirect
from .models import Post
from django.utils import timezone
from django.contrib.auth.decorators import login_required


# Create your views here.


def index(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'posts/index.html', context)


def detail(request, post_id):
    post = Post.objects.get(id=post_id)

    context = {'post': post}

    return render(request, 'posts/detail.html', context)


@login_required
def new(request):

    return render(request, 'posts/new.html')


@login_required
def create(request):

    user = request.user
    body = request.POST['body']
    post = Post(user=user, body=body, created_at=timezone.now())
    post.save()

    return redirect('posts:detail', post_id=post.id)


@login_required
def edit(request, post_id):
    try:
        post = Post.objects.get(id=post_id, user=request.user)
    except Post.DoesNotExist:
        return redirect('posts:index')

    context = {'post': post}
    return render(request, 'posts/edit.html', context)


@login_required
def update(request, post_id):
    try:
        post = Post.objects.get(id=post_id, user=request.user)
    except Post.DoesNotExist:
        return redirect('posts:index')

    post.body = request.POST['body']
    post.save()

    return redirect('posts:detail', post_id=post.id)


@login_required
def delete(request, post_id):
    try:
        post = Post.objects.get(id=post_id, user=request.user)
    except Post.DoesNotExist:
        return redirect('posts:index')

    post.delete()

    return redirect('posts:index')


@login_required
def like(request, post_id):

    if request.method == 'POST':
        try:
            post = Post.objects.get(id=post_id)

            if request.user in post.liked_users.all():
                post.liked_users.remove(request.user)
            else:
                post.liked_users.add(request.user)

            return redirect('posts:detail', post_id=post.id)

        except Post.DoesNotExist:
            pass

    return redirect('posts:index')




#from django.shortcuts import render
#from django.http import HttpResponse

#def index(request):
#    context={ 'post' : '나의 첫 #Django Project...'}
#    return render(request, 'posts/index.html', context)

#def new(request):
#    if not request.user.is_authenticated:
#        return redirect('accounts:login')
#        #redirect 하면 이하코드는 실행되지 않는다.

#def create(request):
#    if not request.user.is_authenticated:
#        return redirect('accounts:login')
#is_authenticate는 함수가 아니고, get_username은 함수라서()
#django template에서는 괄호 열고 닫으면 안된당~!~!~!