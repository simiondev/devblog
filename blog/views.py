from django.shortcuts import render, get_object_or_404
from .models import Post, Comentario
from .forms import ComentarioForm

def lista_posts(request):
    posts = Post.objects.all().order_by('-fecha_publicacion')
    return render(request, 'blog/lista_posts.html', {'posts': posts})

def detalle_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comentarios = post.comentarios.all().order_by('-fecha_creacion')

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            nuevo_comentario = form.save(commit=False)
            nuevo_comentario.post = post
            nuevo_comentario.save()
            form = ComentarioForm()  # limpia el formulario
    else:
        form = ComentarioForm()

    return render(request, 'blog/detalle_post.html', {
        'post': post,
        'comentarios': comentarios,
        'form': form
    })