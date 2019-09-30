from django.shortcuts import render, redirect
from .models import Post
from django.utils import timezone
from .forms import PostForm


def post_list(request):
	context = {}
	posts = Post.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')
	context['posts'] = posts
	return render(request, 'blog/post_list.html', context)

def post_new(request):
	if request.method =="POST":
		form= PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit = False)
			post.author = request.user
			post.publish_date = timezone.now()
			post.save()
			return redirect('post_list')
	else:
		form = PostForm()
		return render(request,'blog/post_new.html', {'form':form})

