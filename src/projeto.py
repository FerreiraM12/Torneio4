"""

Neste torneio pretende-se que implemente um programa que ajude um arquiteto a
planear os prédios a construir num bairro.

Um bairro de dimensão N é uma matriz quadrada com N x N lotes de iguais dimensões.
Em cada lote deve ser construído um prédio. As alturas dos prédios variam entre
1 e N, sendo que em cada linha e coluna do bairro as alturas dos prédios devem ser
todas diferentes. Alguns lotes podem já ter um prédio previamente construído.

Para além destas retrições, o arquiteto tem que respeitar algumas regras de
visibilidade: para cada coluna e para cada linha podem ser indicados quantos
prédios devem ser visíveis em cada uma das direcções.

Considere por exemplo o seguinte esquema para um bairro de dimensão N = 4.

    3 . . 1
    v v v v
. > . . . . < .
. > . 4 . . < 2
. > . . . . < .
1 > . . . 3 < .
    ^ ^ ^ ^
    . . 2 .

Dois dos lotes deste bairro já têm prédios constuídos (de alturas 4 e 3). Na primeira
coluna só podem estar visíveis 3 prédios quando olhando de Norte para Sul. Na terceira
coluna só podem estar visíveis 2 prédios quando olhando de Sul para Norte. Na quarta
coluna só pode estar visível um prédio quando olhando de Norte para Sul. Na segunda
linha só podem estar visíveis 2 prédios quando olhando de Este para Oeste. Finalmente,
na quarta linha só pode estar visível um prédio quando olhando de Oeste para Este.

O programa deve calcular um possível projeto para o bairro, nomeadamente as alturas dos
prédios a construir em cada lote, que respeite todas as restrições dadas. Só serão dados
problemas onde tal é possível. Pode existir mais do que um projeto que satisfaz todas as
restrições, podendo neste caso ser devolvido qualquer um deles.

A função a implementar recebe 5 parâmetros:
- m é uma matriz quadrada (representada por uma lista de listas) que descreve quais os
  prédios já existentes. Se um lote estiver vazio a lista irá conter um None na posição
  respectiva.
- t é uma lista com as restrições de visibilidade para as colunas, quando olhando de Norte
  para Sul. Se não existir restrição para uma determinada coluna existirá um None na
  posição respectiva.
- b é uma lista com as restrições de visibilidade para as colunas, quando olhando de Sul
  para Norte. Se não existir restrição para uma determinada coluna existirá um None na
  posição respectiva.
- l é uma lista com as restrições de visibilidade para as linhas, quando olhando de Oeste
  para Este. Se não existir restrição para uma determinada linha existirá um None na
  posição respectiva.
- r é uma lista com as restrições de visibilidade para as linhas, quando olhando de Este
  para Oeste. Se não existir restrição para uma determinada linha existirá um None na
  posição respectiva.

A função deverá devolver uma matriz quadrada (representada por uma lista de listas) com as
alturas projetadas para todos os lotes.

"""

import copy


# Funcao chamada pela main
def projeto(m, t, b, l, r):
    objBairro = bairro(m, t, b, l, r)
    objBairro.solve()
    m = objBairro.listaSol[0]  # Devolve uma das possiveis solucoes
    return m


#  Substitui o None por 0
def noneToZeroM(m):
    for row in m:
        noneToZeroL(row)
    return m


def noneToZeroL(m):
    for i, elem in enumerate(m):
        if elem is None:
            m[i] = 0
    return m


class bairro:

    #  Construtor
    def __init__(self, m, t, b, l, r):
        self.m = noneToZeroM(m)
        self.t = noneToZeroL(t)
        self.b = noneToZeroL(b)
        self.l = noneToZeroL(l)
        self.r = noneToZeroL(r)
        self.listaSol = []

    #  Verifica se o bairro cumpre as condicoes de de visibilidade
    # 1  t: N -> S       t
    # 2  b: S -> N     l m r
    # 3  l: O -> E       b
    # 4  r: E -> O
    def __isValidAux(self, n, d):  # n -> (t, b, l, ou r) d -> (1-4)

        if d == 1 or d == 3:
            inicio = 0
            fim = len(n)
            sinal = 1
        else:
            inicio = len(n) - 1
            fim = -1
            sinal = -1

        for i, vis in enumerate(n):
            if vis == 0:
                continue
            tallest = 0
            for j in range(inicio, fim, sinal):
                if (d == 1 or d == 2) and self.m[j][i] > tallest:
                    tallest = self.m[j][i]
                    vis -= 1
                elif self.m[i][j] > tallest:
                    tallest = self.m[i][j]
                    vis -= 1
            if vis != 0:
                return False
        return True

    def isValid(self):
        return self.__isValidAux(self.t, 1) and self.__isValidAux(self.b, 2) and \
               self.__isValidAux(self.l, 3) and self.__isValidAux(self.r, 4)

    #  Confirma se um dado predio cumpre a regra de altura unica na sua linha e coluna
    def isPossible(self, y, x, n):
        for i in range(len(self.m)):
            if self.m[y][i] == n or self.m[i][x] == n:
                return False
        return True

    #  Utiliza o isPossible com backtracking para gerar possiveis configuracoes que cumprem as alturas unicas
    def solve(self):
        for y in range(len(self.m)):
            for x in range(len(self.m)):
                if self.m[y][x] == 0:
                    for n in range(1, len(self.m) + 1):
                        if self.isPossible(y, x, n):
                            self.m[y][x] = n
                            self.solve()
                            self.m[y][x] = 0
                    return
        if self.isValid():
            self.listaSol.append(copy.deepcopy(self.m))
