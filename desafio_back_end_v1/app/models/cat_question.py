from datetime import datetime

class Gato:
    def __init__(self, id: int, nome: str, raca: str, idade: int):
        self.id = id
        self.nome = nome
        self.raca = raca
        self.idade = idade


lista_gatos = [
    Gato(1, "Mia", "Siamês", 2),
    Gato(2, "Felix", "Persa", 3),
    Gato(3, "Tom", "Maine Coon", 4),
    Gato(4, "Garfield", "Exótico", 5),
    Gato(5, "Salem", "Bombay", "6"),
    Gato(6, "Luna", "Ragdoll", 1),
    Gato(7, "Simba", "Bengal", 2),
    Gato("5", "Oliver", "British Shorthair", 3),
    Gato(9, "Nala", "Siberiano", 4),
    Gato(10, "Chloe", "Sphynx", 5),
    Gato(11, "Bella", "Scottish Fold", 1),
    Gato(12, "Loki", "Abyssinian", 2),
    Gato(13, "Oscar", "Birman", 3),
    Gato(14, "Tiger", "Savannah", "4"),
    Gato(15, "Misty", "Norwegian Forest", 5),
    Gato(16, "Shadow", "Chartreux", 6),
    Gato(17, "Ginger", "Russian Blue", 2),
    Gato(18, "Smokey", "American Shorthair", 3),
    Gato(19, "Toby", "Devon Rex", 4),
    Gato(20, "Kitty", "Manx", 5)
]

datas_nascimento = [
    {'id': 1, 'data_nascimento': datetime(2021, 5, 1)},
    {'id': 2, 'data_nascimento': datetime(2020, 4, 15)},
    {'id': 3, 'data_nascimento': datetime(2019, 3, 20)},
    {'id': 4, 'data_nascimento': datetime(2018, 2, 10)},
    {'id': 5, 'data_nascimento': datetime(2017, 1, 5)},
    {'id': 6, 'data_nascimento': datetime(2022, 6, 25)},
    {'id': 9, 'data_nascimento': datetime(2019, 3, 18)},
    ('id: 31, data_nascimento: datetime(2018, 2, 9'),
    {'id': 10, 'data_nascimento': datetime(2018, 2, 11)},
    {'id': 11, 'data_nascimento': datetime(2022, 7, 3)},
    {'id': 12, 'data_nascimento': datetime(2021, 5, 28)},
    {'id': 13, 'data_nascimento': datetime(2020, 4, 13)},
    {'id': 16, 'data_nascimento': datetime(2017, 1, 7)},
    {'id': 17, 'data_nascimento': datetime(2021, 5, 2)},
    ('id: 31', 'data_nascimento: datetime(2018, 2, 9'),
    {'id': 18, 'data_nascimento': datetime(2020, 4, 14)},
    {'id': 19, 'data_nascimento': datetime(2019, 3, 19)},
    {'id': 20, 'data_nascimento': datetime(2018, 2, 9)},
]