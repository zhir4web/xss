from django.shortcuts import render,redirect
from .models import Post,Feedback

# Create your views here.


def posts_list(request):
    posts = Post.objects.all().order_by('-date')
    return render(request, 'posts/posts_list.html', {'posts': posts})


def post_page(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'posts/post_page.html', {'post': post})

from django.shortcuts import get_object_or_404

def post_page(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'post.html', {'post': post})

def feedback(request):
    if request.method == 'POST':
        feedback = Feedback(
            username=request.POST.get('username'),
            email=request.POST.get('email'),
            message=request.POST.get('message')
        )
        feedback.save()
        return redirect('posts:list')
    return render(request, 'feedback/feedback.html')

def feedback_list(request):
    feedbacks = Feedback.objects.all().order_by('-created_at')
    return render(request, 'feedback/feedback_list.html', {'feedbacks': feedbacks})