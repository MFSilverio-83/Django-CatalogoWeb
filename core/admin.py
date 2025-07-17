from django.contrib import admin
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
    list_display = ('nome', 'categoria', 'preco_formatado', 'ativo')
    # Permite editar o campo 'ativo' diretamente na listagem (muito prático!)
    list_editable = ('ativo',)
    # Adiciona filtros na lateral direita para facilitar a busca
    list_filter = ('categoria', 'ativo')
    # Adiciona uma barra de busca
    search_fields = ('nome', 'categoria__nome')
    # Adiciona o formulário de Imagens (que criamos acima) dentro da página do produto
    inlines = [ImagemProdutoInline]

# Não precisamos registrar ImagemProduto separadamente, pois já está como 'inline'
# admin.site.register(ImagemProduto)
