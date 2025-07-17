from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView
from .models import Categoria, Produto

class HomePageView(TemplateView):
    template_name = 'homepage.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.filter(exibir_na_homepage=True)
        return context

class CategoriaProdutoView(ListView):
    model = Produto
    template_name = 'produtos_categorias.html'
    context_object_name = 'produtos'

    def get_queryset(self):
        category_slug = self.kwargs['category_slug']
        return Produto.objects.filter(categoria__slug=category_slug, ativo=True)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_slug = self.kwargs['category_slug']
        context['categoria'] = get_object_or_404(Categoria, slug=category_slug)
        return context