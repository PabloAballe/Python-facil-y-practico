

#improtamos las librerias que vamos a estar utilizando
from django.shortcuts import render, get_object_or_404



#importamos el modelo de post y el timezone
from .models import Post
from django.utils import timezone


#definimos nuestra vista como si fuese una funcion y le decimos donde estará
def index(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'index.html', {'posts': posts})

#vista para ver los detalles de cualquier post
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})
