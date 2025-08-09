from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'), # link para homepage do site
    path('<slug:category_slug>/', CategoriaProdutoView.as_view(), name='produtos_categorias'),
    path('produto/<int:pk>/upload-imagens/', MultiImageUploadView.as_view(), name='upload_multiplas_imagens'),
]
