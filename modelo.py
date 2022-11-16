class Programa:
    def __init__(self, nome, ano):
        self.__nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def like(self):
        return self._like

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novoNome):
        self._nome = novoNome

    def  __str__imprime(self):
        return f'{self._nome} - {self.ano} - {self._like}'

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def  __str__(self):
        return f'{self._nome} - {self.ano} - {self.duracao} - {self._like}'

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas
    def __str__(self):
         return f'{self._nome} - {self.ano} - {self.temporadas} - {self._like}'

class PlayList(list):
    def __init__(self, nome, programas):
        self.nome = nome
        super().__init__(programas)

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
tmep = Filme('Todo mundo em pânico', 1999, 100)
demolidor = Serie('Demolidor', 2016, 2)

vingadores.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
demolidor.dar_like()
demolidor.dar_like()
atlanta.dar_like()
atlanta.dar_like()
atlanta.dar_like()

filmes_e_series = [vingadores, atlanta, demolidor, tmep]
playlist_fim_de_semana = PlayList('fim de semana', filmes_e_series)

for programa in playlist_fim_de_semana:
    print(programa)