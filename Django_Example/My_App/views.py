from django.shortcuts import render, HttpResponseRedirect
from .models import Post
from .forms import PostForm

def index(request): # request can be GET or POST for example
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(request.get_full_path())
	else:
		posts = Post.objects.all()
		form = PostForm()
		context = {'posts': posts, 'form': form}
	return render(request, 'index.html', context)

def about(request):
	return render(request, 'about.html', context={})
