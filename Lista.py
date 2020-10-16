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
        self.inserirAntesAtual(valor)

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
        elif k >= self.__elementos or k < 0:
            print('Posicao inexistente.')
        else:
            self.__cursor.avancarKPosicoes(k)
            self.inserirAntesAtual(valor)

    def excluirAtual(self):
        if self.vazia():
            print('Lista vazia.')
        elif self.__cursor.atual.ant is None:
            self.__cursor.atual.prox.ant = None
            self.__cursor.atual = self.__cursor.atual.prox
        elif self.__cursor.atual.prox is None:
            self.__cursor.atual.ant.prox = None
            self.__cursor.atual = self.__cursor.atual.ant
        else:
            self.__cursor.atual.ant.prox = self.__cursor.atual.prox
            self.__cursor.atual.prox.ant = self.__cursor.atual.ant
            self.__cursor.atual = self.__cursor.atual.prox
            self.__elementos -= 1

    def excluirPrim(self):
        self.__cursor.irParaPrimeiro()
        self.excluirAtual()

    def excluirUlt(self):
        self.__cursor.irParaUltimo()
        self.excluirAtual()

    def excluirElem(self, valor):
        self.__cursor.irParaPrimeiro()
        x = self.__cursor.atual

        while x.valor != valor:
            if self.__cursor.atual.prox is None:
                print('Elemento Inexistente')
                return None
            else:
                self.__cursor.avancarKPosicoes(2)
                x = self.__cursor.atual

        self.excluirAtual()

    def excluirDaPos(self, k):
        self.__cursor.irParaPrimeiro()

        if self.vazia():
            print('Lista Vazia.')
        elif k >= self.__elementos or k < 0:
            print('Posicao inexistente.')
        else:
            self.__cursor.avancarKPosicoes(k)
            self.excluirAtual()

    def vazia(self):
        return self.__elementos == 0

    def cheia(self):
        return self.__elementos == self.__limite

    def contem(self, valor):
        self.__cursor.irParaPrimeiro()
        x = self.__cursor.atual

        while x.valor != valor:
            if self.__cursor.atual.prox is None:
                print('False')
                return False
            else:
                self.__cursor.avancarKPosicoes(2)
                x = self.__cursor.atual
        print('True')
        return True

    def posicaoDe(self, valor):
        self.__cursor.irParaPrimeiro()
        x = self.__cursor.atual
        posicao = 1

        while x.valor != valor:
            if self.__cursor.atual.prox is None:
                print('Elemento Inexistente')
                return None
            else:
                self.__cursor.avancarKPosicoes(2)
                x = self.__cursor.atual
                posicao += 1
        print('Posicao')
        return posicao

    def Buscar(self, valor):
        self.__cursor.irParaPrimeiro()
        x = self.__cursor.atual

        while x.valor != valor:
            if self.__cursor.atual.prox is None:
                print('Elemento Inexistente')
                return False
            else:
                self.__cursor.avancarKPosicoes(2)
                x = self.__cursor.atual
        print('Achou Elemento')
        return True