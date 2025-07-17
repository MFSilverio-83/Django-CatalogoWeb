from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'), # link para homepage do site
    path('<slug:category_slug>/', CategoriaProdutoView.as_view(), name='produtos_categorias'),

]