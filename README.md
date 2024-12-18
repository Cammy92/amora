# **API de Imóveis e Negociações**

## **Sobre o Projeto**

Esta API permite criar negociações de compra de imóveis e avaliar o risco associado à transação com base em critérios predefinidos. A API também possibilita a consulta dos detalhes de uma negociação específica.

### **Tecnologias Utilizadas**

- **Linguagem:** Python
- **Framework:** FastAPI
- **Banco de Dados:** PostgreSQL
- **ORM:** SQLAlchemy

---

## **Como Executar o Projeto**

### **1. Configuração do Ambiente**

Certifique-se de ter instalado:

- Python 3.10+
- PostgreSQL

Clone este repositório e instale as dependências:

```bash
# Clone o repositório
git clone https://github.com/Cammy92/amora.git
cd imoveis_api

# Crie e ative o ambiente virtual
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt
```

### **2. Configure o Banco de Dados**

Crie um banco de dados PostgreSQL e atualize a string de conexão no arquivo `database.py`:

```python
DATABASE_URL = "postgresql://username:password@localhost/imoveis_db"
```

Substitua `username`, `password` e `imoveis_db` pelas credenciais corretas.

### **3. Execute as Migrações**

Use o Alembic para criar as tabelas no banco de dados:

```bash
alembic upgrade head
```

### **4. Inicie o Servidor**

Execute o servidor da aplicação:

```bash
uvicorn app.main:app --reload
```

Acesse a API em [http://localhost:8000](http://localhost:8000).

---

## **Documentação dos Endpoints**

### **1. Criar uma Negociação de Imóvel**

#### **POST /imoveis**

Cria uma nova negociação, avalia o risco e salva os dados no banco.

#### **Requisição**

- **Corpo (JSON):**

```json
{
  "comprador": "Cammy Lua",
  "renda_comprador": 15000.0,
  "pontuacao_credito": 700,
  "imovel": {
    "endereco": "Rua das Amoras, 426",
    "valor": 400000.0,
    "tipo": "Apartamento"
  }
}
```

#### **Resposta**

- **200 OK**:

```json
{
  "id": 1,
  "status": "Aprovada",
  "comprador": "João do Nascimento",
  "renda_comprador": 15000.0,
  "pontuacao_credito": 700,
  "imovel": {
    "endereco": "Rua Elíseos, 123",
    "valor": 400000.0,
    "tipo": "Apartamento"
  }
}
```

- **400 Bad Request**:

```json
{
  "detail": "Erro de validação. Verifique os dados enviados."
}
```

---

### **2. Consultar uma Negociação por ID**

#### **GET /imoveis/{id}**

Retorna os detalhes de uma negociação e a avaliação de risco.

#### **Parâmetros**

- **Path Parameter:**
  - `id` (integer): ID da negociação a ser consultada.

#### **Resposta**

- **200 OK**:

```json
{
  "id": 1,
  "status": "Aprovada",
  "comprador": "Pedro Silva",
  "renda_comprador": 15000.0,
  "pontuacao_credito": 700,
  "imovel": {
    "endereco": "Rua das Panelas, 123",
    "valor": 400000.0,
    "tipo": "Apartamento"
  }
}
```

- **404 Not Found**:

```json
{
  "detail": "Negociação não encontrada"
}
```

---

## **Critérios de Avaliação de Risco**

A avaliação de risco é calculada no momento da criação da negociação com base nas seguintes regras:

1. **Valor do imóvel**:
   - Reprovado se o valor for maior que **10 milhões** ou menor que **100 mil reais**.
2. **Pontuação de crédito**:
   - Reprovado se a pontuação for menor que **500** (escala de 0 a 1000).
3. **Renda do comprador**:
   - Reprovado se o valor do imóvel for maior que **30% da renda mensal do comprador**.

---

## **Testando a API**

### **Via Swagger UI**

Acesse a documentação interativa em:

```
http://localhost:8000/docs
```

Utilize a interface para testar os endpoints diretamente no navegador.

### **Via cURL**

1. **Criar uma Negociação**:

```bash
curl -X POST "http://localhost:8000/imoveis" \
-H "Content-Type: application/json" \
-d '{
  "comprador": "Paulo José Silva",
  "renda_comprador": 15000.0,
  "pontuacao_credito": 700,
  "imovel": {
    "endereco": "Rua Camélia, 12",
    "valor": 400000.0,
    "tipo": "Apartamento"
  }
}'
```

2. **Consultar uma Negociação**:

```bash
curl -X GET "http://localhost:8000/imoveis/1"
```

---

## **Autores**

- **Desenvolvedor:** Camila Ramos Araújo
- **Contato:** [contatocamilaramos@gmail.com](mailto:contatocamilaramos@gmail.com)
