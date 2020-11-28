from django.shortcuts import render, get_object_or_404
from .models import Blog_project


def all_blogs(request):
    projects_blog = Blog_project.objects.all()
    return render(request, 'blog/all_blogs.html', {'projects_blog':projects_blog})
def details(request, blog_id):
    blog = get_object_or_404(Blog_project, pk = blog_id)
    return render(request, 'blog/details.html', {'blog':blog})
