# Desafio Estágio Projex Consulting

Desafio Estágio de Desenvolvimento Projex Consulting 2024.

## Dica

Para visualizar os endpoints acesse este link no seu navegador após rodar o projeto

```sh
localhost:8000/docs
```

## Observações relacionadas a construção das funções/métodos

Assumi que não deveria retornar nenhuma mensagem de erro ou aviso, assim sendo,
preferi sempre retornar o corpo esperado na ausência de informação, seja informação total ou parcial,
como com datas de nascimento inexistentes.

Também assumi que tipos incorretos também deveriam ser desconsiderados, como ids e idades em str.

### Questão 2 e 3:

Questão 2: Assumi que o método retornava uma lista de gatos sem data de nascimento e sem idade, para um gato não ter idade assumi que seria no caso de a idade estar com o tipo incorreto (str -> int), então o método retornará sempre os gatos sem data de nascimento definida e com idade incorreta.

Questão 3: Assim como o método anterior, decidi que os gatos com idade diferente do tipo int não deveriam ser considerados.

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
(Após retirar dúvidas o correto seria esse corpo)

```sh
[
    {
        "id": 0,
        "nome": "Qualquer",
        "raca": "Qualquer",
    },
    {
        "id": 0,
        "nome": "Qualquer",
        "raca": "Qualquer",
    },
]
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
