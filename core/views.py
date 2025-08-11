from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, View
from .models import Categoria, Produto, ImagemProduto
from .forms import MultiImageUploadForm # Importe o formulário

class HomePageView(TemplateView):
    template_name = 'homepage.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.filter(exibir_na_homepage=True).order_by('id')
        return context

class CategoriaProdutoView(ListView):
    model = Produto
    template_name = 'produtos_categorias.html'
    context_object_name = 'produtos'

    def get_queryset(self):
        category_slug = self.kwargs['category_slug']
        return Produto.objects.filter(categoria__slug=category_slug, ativo=True).order_by('id')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_slug = self.kwargs['category_slug']
        context['categoria'] = get_object_or_404(Categoria, slug=category_slug)
        return context
    
# Nova view para o upload de múltiplas imagens
class MultiImageUploadView(View):
    def get(self, request, pk):
        produto = get_object_or_404(Produto, pk=pk)
        form = MultiImageUploadForm()
        return render(request, 'multi_image_upload.html', {'form': form, 'produto': produto})
    
    def post(self, request, pk):
        produto = get_object_or_404(Produto, pk=pk)
        form = MultiImageUploadForm(request.POST, request.FILES)
        
        if form.is_valid():
            images = request.FILES.getlist('images')
            for f in images:
                ImagemProduto.objects.create(produto=produto, imagem=f)
            
            # Redireciona de volta para o admin do produto após o sucesso
            from django.urls import reverse
            return redirect(reverse('admin:core_produto_change', args=[produto.pk]))
        
        return render(request, 'multi_image_upload.html', {'form': form, 'produto': produto})
