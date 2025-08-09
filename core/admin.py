from django.contrib import admin
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.html import format_html
from .models import Categoria, Produto, ImagemProduto

# Esta classe permite adicionar imagens DIRETAMENTE na página de cadastro do produto
class ImagemProdutoInline(admin.TabularInline):
    model = ImagemProduto
    # 'extra' define quantos campos de upload de imagem vazios aparecerão
    extra = 1

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    # Campos que aparecerão na listagem de categorias
    list_display = ('nome', 'slug', 'exibir_na_homepage')
    # Adiciona uma barra de busca que procura pelo nome
    search_fields = ('nome',)
    # Cria o 'slug' automaticamente a partir do campo 'nome' (muito útil!)
    prepopulated_fields = {'slug': ('nome',)}

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    # Campos que aparecerão na listagem de produtos
    list_display = ('nome', 'categoria', 'preco_formatado', 'ativo', 'link_upload_imagens')
    # Permite editar o campo 'ativo' diretamente na listagem (muito prático!)
    list_editable = ('ativo',)
    # Adiciona filtros na lateral direita para facilitar a busca
    list_filter = ('categoria', 'ativo')
    # Adiciona uma barra de busca
    search_fields = ('nome', 'categoria__nome')
    # Adiciona o formulário de Imagens (que criamos acima) dentro da página do produto
    inlines = [ImagemProdutoInline]

    # Campo para exibir o link no formulário de edição do produto
    readonly_fields = ('link_upload_imagens',)

    def link_upload_imagens(self, obj):
        if obj.pk:
            url = reverse('upload_multiplas_imagens', args=[obj.pk])
            return format_html('<a class="button" href="{}">Adicionar várias fotos</a>', url)
        return ""

    link_upload_imagens.short_description = "Adicionar Fotos"

    # NOVO MÉTODO ADICIONADO AQUI
    def response_add(self, request, obj, post_response_object=None):
        """Redireciona para a página de edição do objeto após a criação."""
        # Cria a URL para a página de edição do produto recém-criado
        url = reverse('admin:core_produto_change', args=[obj.pk])
        # Redireciona para essa URL
        return redirect(url)
