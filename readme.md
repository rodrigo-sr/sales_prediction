### Projeto de Previsão de Vendas com Modelos de Machine Learning

Este projeto consiste na construção de uma API utilizando FastAPI para prever vendas com base em dados de entrada fornecidos pelo usuário. O modelo de machine learning é treinado com dados históricos e implementado em uma API para permitir previsões em tempo real.

---

## Estrutura do Projeto

```
project/
│
├── main.py
├── models/
│   ├── model_uk.pkl
│   ├── model_fr.pkl
│   ├── model_de.pkl
│   ├── model_eire.pkl
│   ├── model_others.pkl
├── notebook/
│   ├── Sales_Prediction_Notebook.ipynb
└── requirements.txt
```

### Descrição dos Arquivos

- **main.py**: Código fonte da API FastAPI.
- **models/**: Diretório contendo os modelos treinados salvos como arquivos pickle.
  - `model_uk.pkl`: Modelo treinado para o Reino Unido.
  - `model_fr.pkl`: Modelo treinado para a França.
  - `model_de.pkl`: Modelo treinado para a Alemanha.
  - `model_eire.pkl`: Modelo treinado para EIRE.
  - `model_others.pkl`: Modelo treinado para outros países.
- **notebook/**: Diretório contendo o Jupyter Notebook usado para explorar os dados e treinar os modelos.
  - `Sales_Prediction_Notebook.ipynb`: Notebook com a exploração dos dados, treinamento dos modelos e avaliação.
- **requirements.txt**: Arquivo de dependências do projeto.

---

## Executando a API

### Passo 1: Clone o repositório

```sh
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### Passo 2: Instale as dependências

```sh
pip install -r requirements.txt
```

### Passo 3: Inicie a API

```sh
uvicorn main:app --reload
```

A API estará disponível em `http://127.0.0.1:8000`.

### Passo 4: Teste a API

Você pode testar a API utilizando ferramentas como `curl`, Postman, ou diretamente via código Python.

#### Exemplo de Requisição com `curl`

```sh
curl -X POST "http://127.0.0.1:8000/predict/" -H "Content-Type: application/json" -d '{
    "country": "United Kingdom",
    "month": 6,
    "day_of_week_numeric": 2
}'
```

#### Exemplo de Requisição com Python

```python
import requests

url = "http://127.0.0.1:8000/predict/"
data = {
    "country": "United Kingdom",
    "month": 6,
    "day_of_week_numeric": 2
}

response = requests.post(url, json=data)
print(response.json())
```

---

## Uso do Jupyter Notebook

1. Navegue até o diretório `notebook/`.
2. Abra o Jupyter Notebook:

```sh
jupyter notebook Sales_Prediction_Notebook.ipynb
```

O notebook contém a exploração dos dados, o treinamento dos modelos, a avaliação e a geração dos arquivos pickle dos modelos treinados.

---

## Documentação da API

A documentação automática da API está disponível em:

- **Swagger UI**: `http://127.0.0.1:8000/docs`
- **ReDoc**: `http://127.0.0.1:8000/redoc`

### Endpoints da API

- **GET /**: Endpoint de saúde para verificar se a API está funcionando.
- **POST /predict/**: Endpoint para fazer previsões de vendas. Requer um JSON com os seguintes campos:
  - `country`: Nome do país (ex: "United Kingdom", "France", "Germany", "EIRE", "Others").
  - `month`: Número do mês (1 a 12).
  - `day_of_week_numeric`: Número do dia da semana (0 para segunda-feira, 6 para domingo).

### Exemplo de Requisição

```json
{
    "country": "United Kingdom",
    "month": 6,
    "day_of_week_numeric": 2
}
```

### Exemplo de Resposta

```json
{
    "country": "United Kingdom",
    "prediction": 12345.67
}
```

---

## Conclusão

Este projeto fornece uma solução completa para prever vendas usando modelos de machine learning, integrados em uma API rápida e eficiente com FastAPI. Você pode utilizar o Jupyter Notebook para explorar os dados e treinar novos modelos, e a API para realizar previsões em tempo real.