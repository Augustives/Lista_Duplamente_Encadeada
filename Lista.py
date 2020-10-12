from Cursor import Cursor
from Nodo import Nodo

class ListaDE:
    def __init__(self):
        self.__cursor = Cursor()
        self.__limite = 10
        self.__elementos = 0

    def acessarAtual(self):
        return self.__cursor.atual

    def inserirAntesAtual(self, valor):
        novo = Nodo(valor)

        if self.cheia():
            print('Lista Cheia.')
        elif self.vazia():
            self.__cursor.atual = novo
            self.__elementos += 1
        elif self.__cursor.atual.ant is None:
            self.__cursor.atual.ant = novo
            novo.prox = self.__cursor.atual
        else:
            self.__cursor.atual.ant.prox = novo
            novo.ant = self.__cursor.atual.ant
            self.__cursor.atual.ant = novo
            novo.prox = self.__cursor.atual
            self.__elementos += 1


    def inserirPosAtual(self, valor):
        novo = Nodo(valor)

        if self.cheia():
            print('Lista Cheia.')
        elif self.vazia():
            self.__cursor.atual = novo
            self.__elementos += 1
        elif self.__cursor.atual.prox is None:
            self.__cursor.atual.prox = novo
            novo.ant = self.__cursor.atual
        else:
            self.__cursor.atual.prox.ant = novo
            novo.prox = self.__cursor.atual.prox
            self.__cursor.atual.prox = novo
            novo.ant = self.__cursor.atual
            self.__elementos += 1

    def inserirFim(self, valor):
        novo = Nodo(valor)

        if self.cheia():
            print('Lista Cheia.')
        elif self.vazia():
            self.__cursor.atual = novo
            self.__elementos += 1
        else:
            self.__cursor.irParaUltimo()
            novo.ant = self.__cursor.atual
            self.__cursor.atual.prox = novo
            self.__elementos += 1

    def inserirFrente(self, valor):
        novo = Nodo(valor)

        if self.cheia():
            print('Lista Cheia.')
        elif self.vazia():
            self.__cursor.atual = novo
            self.__elementos += 1
        else:
            self.__cursor.irParaPrimeiro()
            novo.prox = self.__cursor.atual
            self.__cursor.atual.ant = novo
            self.__elementos += 1

    def inserirNaPosicao(self, k, valor):
        self.__cursor.irParaPrimeiro()

        if self.cheia():
            print('Lista Cheia.')
        elif k >= self.__elementos:
            print('Posicao inexistente.')
        else:
            self.__cursor.avancarKPosicoes(k)
            self.inserirPosAtual(valor)

    def excluirAtual(self):


    def excluirPrim(self):
        pass

    def excluirUlt(self):
        pass

    def excluirElem(self, valor):
        pass

    def excluirDaPos(self):
        pass

    def vazia(self):
        return self.__elementos == 0

    def cheia(self):
        return self.__elementos == self.__limite

    def contem(self, valor):
        pass

    def posicaoDe(self, valor):
        pass