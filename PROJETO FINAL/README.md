API Marmitaria de Comida Caseira

API REST em Flask + SQLite para gerenciamento de uma marmitaria.

Tema

Duas tabelas relacionadas:

 Tabela pai    Tabela filho 
  categorias    marmitas     

Uma categoria pode ter várias marmitas. Cada marmita pertence a uma categoria.

Estrutura das tabelas

categorias
- id (INTEGER, PK)
- nome (TEXT, UNIQUE)
- descricao (TEXT)

marmitas
- id (INTEGER, PK)
- nome (TEXT)
- descricao (TEXT)
- preco (REAL)
- categoria_id (INTEGER, FK para categorias.id)

Como rodar

```bash
pip install flask
python app.py