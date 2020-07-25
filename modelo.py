
class Filme:
    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes

    def give_like(self):
        self.__like += 1

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

class Serie:
    def __init__(self, nome, ano, temporadas):
        self.__nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes

    def give_like(self):
        self.__like += 1

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

vingadores = Filme("vingadores - guerra infinita", 2018, 160)
print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duração: {vingadores.duracao} minutos - Likes {vingadores.likes}.')

atlanta = Serie("atlanta", 2018, 2)
print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} - Temporadas: {atlanta.temporadas} - Likes: {atlanta.likes}.')
