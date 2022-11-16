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

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

     def imprime(self):
         print(f'{self._nome} - {self.ano} - {self.duracao} - {self._like}')

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

     def imprime(self):
         print(f'{self._nome} - {self.ano} - {self.temporadas} - {self._like}')

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
vingadores.dar_like()

atlanta = Serie('atlanta', 2018, 2)
atlanta.dar_like()
atlanta.dar_like()

filmeSerie = [vingadores, atlanta]

for programa in filmeSerie:
    programa.imprime
