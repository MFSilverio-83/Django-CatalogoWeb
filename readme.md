🛍️ Catálogo Online com Django

Este é um projeto de um catálogo online desenvolvido com Python e o framework Django. A aplicação permite a exibição de produtos organizados por categorias (setores), com uma página inicial destacando as categorias principais e páginas dedicadas para listar os produtos de cada categoria.

✨ Funcionalidades Principais

Gestão de Categorias: Crie e gerencie categorias de produtos.

Gestão de Produtos: Adicione produtos com nome, preço, link externo e associe-os a uma categoria.

Múltiplas Imagens: Suporte para upload de múltiplas imagens por produto.

Homepage Dinâmica: Exibe apenas as categorias marcadas como "destaque" na página inicial.

Navegação por Categoria: Páginas dedicadas que listam todos os produtos de uma categoria específica.

Carrossel de Imagens: Cada produto na lista de categoria possui seu próprio carrossel de imagens.

Design Responsivo: Interface adaptável para diferentes tamanhos de tela utilizando Bootstrap.

🛠️ Tecnologias Utilizadas

- 🐍 Python
- 🎭 Django
- 🌐 HTML5
- 🎨 CSS3
- 🅱️ Bootstrap

⚙️ Estrutura do Projeto

O código-fonte está organizado da seguinte forma, destacando os principais componentes:

models.py: Define a estrutura do banco de dados com três modelos principais:

Categoria: Armazena o nome, slug e imagem da categoria. Gera o slug automaticamente a partir do nome.

Produto: Contém os detalhes do produto, como nome, preço, link externo e a qual Categoria pertence.

ImagemProduto: Permite associar múltiplas imagens a um Produto.

views.py: Controla a lógica da aplicação usando Class-Based Views (CBVs) do Django.

HomePageView: Renderiza a página inicial, enviando para o template apenas as categorias que devem ser exibidas.

CategoriaProdutoView: Filtra e exibe os produtos que pertencem à categoria selecionada através do slug na URL.

templates/: Contém os arquivos HTML que renderizam o front-end.

homepage.html: Página inicial que mostra as categorias em destaque.

produtos_categorias.html: Página que lista os produtos de uma categoria, utilizando um carrossel Bootstrap para as imagens de cada produto.

🖼️ Painel Administrativo com django-jazzmin

📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

Desenvolvido com ❤️ por Marcio Freire Silverio
