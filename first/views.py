from django.shortcuts import get_object_or_404, render, redirect
from .models import Blog, Comment
from .forms import BlogForm, CommentForm
from django.utils import timezone

# Create your views here.
def layout(request):
    return render(request, 'first/index.html')

def eat(request):
    return render(request, 'first/eat.html')

def home(request):
    blogs = Blog.objects.all()
    return render(request, 'first/home.html', {'blogs': blogs})

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/first/home/')

def blogform(request, blog=None):
    if request.method =='POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.pub_date=timezone.now()
            blog.save()
            return redirect('home')
    else:
        form = BlogForm(instance=blog)
        return render(request, 'first/new.html',{'form':form})

def edit(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    return blogform(request, blog)

def remove(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    blog.delete()
    return redirect('home')

def detail(request, blog_id):
        blog = get_object_or_404(Blog, pk=blog_id)
        if request.method == "POST":
                form = CommentForm(request.POST)
                if form.is_valid():
                        comment = form.save(commit=False)
                        comment.blog_id = blog
                        comment.comment_text = form.cleaned_data["comment_text"]
                        comment.save()
                        return redirect("detail", blog_id)
        else:
                form = CommentForm()
                return render(request, "first/detail.html", {"blog":blog, "form":form})

def comment_edit(request, blog_id, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        if request.method == "POST":
                form = CommentForm(request.POST, instance=comment)
                if form.is_valid():
                        comment = form.save(commit=False)
                        comment.comment_text = form.cleaned_data["comment_text"]
                        comment.save()
                        return redirect("detail", blog_id)
        else:
                form = CommentForm(instance=comment)
                return render(request, "first/comment_edit.html", {"form":form})

def comment_remove(request, blog_id, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        comment.delete()
        return redirect("detail", blog_id)