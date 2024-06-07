# Desafio Estágio Projex Consulting
![Python](https://img.shields.io/badge/python-%233776AB.svg?style=for-the-badge&logo=python&logoColor=white)&nbsp;
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)&nbsp;

Desafio Estágio de Desenvolvimento Projex Consulting 2024.

## Sobre o desafio

Parabéns, você foi selecionado(a) para a etapa de desafio de programação.\
Por favor leia atentamente as instruções a seguir:

- O desafio terá 1 semana de duração
- Serão avaliadas suas habilidades de resolução de problemas, raciocínio lógico e conhecimentos da linguagem Python e FastAPI

## Objetivo

Você recebeu um BackEnd simples de API de gatos, seu objetivo é consertar o código de forma a fazer com que ele rode sem erros, para testar a API use o Postman, ThunderClient ou qualquer outra ferramenta para fazer chamadas de API.

## Dependências

- Python 3.10 ou superior
- PIP (Preferred Installer Program)
- FastAPI

## Preparação de ambiente

Instale as dependências em [requirements](requirements.txt) com:

```sh
pip install -r requirements.txt
```

Rode o projeto com:

```sh
py run.py
```

## Dica

Para visualizar os endpoints acesse este link no seu navegador após rodar o projeto

```sh
localhost:8000/docs
```

## Respostas esperadas

### Questão 1 e 3
Deve retornar um corpo semelhante a esse:

```sh
{
    "id": 0,
    "nome": "Qualquer",
    "raca": "Qualquer",
    "idade": 0,
    "data_nascimento": "0000-00-00"
}
```

### Questão 2
Deve retornar um corpo semelhante a esse:

```sh
{
    "id": 0,
    "nome": "Qualquer",
    "raca": "Qualquer",
}
```

### Questão 4 e 5
Deve retornar um corpo semelhante a esse:

```sh
[
    {
        "id": 0,
        "nome": "Qualquer",
        "raca": "Qualquer",
        "idade": 0,
        "data_nascimento": "0000-00-00"
    },
    {
        "id": 0,
        "nome": "Qualquer",
        "raca": "Qualquer",
        "idade": 0,
        "data_nascimento": "0000-00-00"
    }
]
```