# Blogging Platform API

## API documentation

A documentação da API está disponível nos seguintes links:

- [Swagger UI](http://localhost:8000/swagger/) - Explore e teste a API.
- [Redoc](http://localhost:8000/redoc/) - Visualize a documentação da API em um formato de documento.

Certifique-se de que o servidor da API esteja em execução para acessar a documentação localmente.


#### `GET /api/items/`

- **Descrição:** Retorna uma lista de itens.
- **Parâmetros:**
  - `limit` (opcional): Número máximo de itens a retornar.
- **Respostas:**
  - `200 OK`: Lista de itens.
  - `400 Bad Request`: Solicitação inválida.

#### `POST /api/items/`

- **Descrição:** Cria um novo item.
- **Parâmetros:**
  - `name`: Nome do item (requerido).
  - `description`: Descrição do item (opcional).
- **Corpo da Requisição:**
  ```json
  {
    "name": "Item1",
    "description": "Descrição do Item1"
  }
