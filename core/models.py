from django.db import models
from django.utils.text import slugify
from cloudinary_storage.storage import MediaCloudinaryStorage

class Categoria(models.Model):
    nome = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=150, unique=True, blank=True)
    imagem = models.ImageField(upload_to='fotos_categorias/', null= True, blank=True, storage=MediaCloudinaryStorage())
    exibir_na_homepage = models.BooleanField(default=False, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nome)
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.nome)
    
class Produto(models.Model):
    nome = models.CharField(max_length=250, null= True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null= True, blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2, blank=True)   
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return str (self.nome)
    
    
    # MÉTODO NOVO ADICIONADO AQUI
    def preco_formatado(self):
        """Formata o preço para o padrão brasileiro R$ 1.234,56"""
        # Formata o número para ter 2 casas decimais e troca o ponto por vírgula.
        preco_str = f'R$ {self.preco:.2f}'.replace('.', ',')
        return preco_str

    def link_whatsapp(self):
        # 📱 Coloque aqui o número de telefone da loja no formato internacional
        numero = '5535998102172'
        mensagem = f'Olá! Tenho interesse no produto: {self.nome}'
        return f'https://wa.me/{numero}?text={mensagem}'
    
class ImagemProduto(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='imagens')
    imagem = models.ImageField(upload_to='fotos_produtos/', storage=MediaCloudinaryStorage())

    def __str__(self):
        return f"Imagem de {self.produto.nome}"
