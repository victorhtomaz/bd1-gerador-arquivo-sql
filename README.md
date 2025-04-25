# bd1-gerador-arquivo-sql

Este programa em Python foi desenvolvido para gerar um arquivo .sql, para ser mportado para um banco de dados MySQL. Ele cria N dados definido pelo usúario para popular e criar o banco de uma loja com as tabelas: clientes, produtos, pedidos e itens de um pedido. 

## Como usar

### Requisitos

- [Python](https://www.python.org/downloads/)
- [MySQL](https://dev.mysql.com/downloads/)

### Clonar o repositorio

```bash
git clone https://github.com/victorhtomaz/bd1-gerador-arquivo-sql.git
```

### Acessar a pasta 

```bash
cd bd1-gerador-arquivo-sql
```

### Instalar os pacotes necessários

```bash
pip install pandas Faker
```

### Execute o arquivo python

```bash
python gerador.py
```

### Responder à quantidade de dados a ser gerada

- Quantidade de clientes
- Quantidade de produtos
- Quantidade de pedidos
- Quantidade de itens de um pedido

### Executar no MySQL o arquivo gerado

```sql
USE sys;
```

```sql
source lojaimport.sql
```