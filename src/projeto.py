'''

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

'''

# Funcao chamada pela main
def projeto(m, t, b, l, r):
    objeto = bairro(m, t, b, l, r)
    res = objeto.isValid()
    print(res)
    return m


#  Substitui o None por 0
def noneToZeroM(m):
    for i, row in enumerate(m):
        for j, elem in enumerate(row):
            if elem is None:
                m[i][j] = 0
    return m


def noneToZeroL(m):
    for i, row in enumerate(m):
        if row is None:
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

    #  Getter
    def getBairro(self):
        return self.m

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
        elif d == 2 or d == 4:
            inicio = len(n) - 1
            fim = -1
            sinal = -1

        for i, vis in enumerate(n):
            tallest = 0
            for j in range(inicio, fim, sinal):
                if d == 1 or d == 2:
                    if self.m[j][i] > tallest:
                        tallest = self.m[j][i]
                        vis -= 1
                else:
                    if self.m[i][j] > tallest:
                        tallest = self.m[i][j]
                        vis -= 1
            if vis != 0:
                return False
        return True

    def isValid(self):
        return self.__isValidAux(self.t, 1) and self.__isValidAux(self.b, 2) and \
               self.__isValidAux(self.l, 3) and self.__isValidAux(self.r, 4)
