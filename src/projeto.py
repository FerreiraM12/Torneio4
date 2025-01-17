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


# Funcao chamada pela main
def projeto(m, t, b, l, r):
    ex = bairro(m, t, b, l, r)
    casosImediatos(ex)
    m = solve(ex, 0, 0)
    return m


class bairro:
    def __init__(self, mapa, ns, sn, oe, eo):
        self.mapa = mapa
        self.ns = ns
        self.sn = sn
        self.oe = oe
        self.eo = eo
        self.dim = len(self.mapa)
        self.possiveis = matrizAlturasPossiveis(self)

    def col(self, x):
        return [row[x] for row in self.mapa]

    def row(self, y):
        return self.mapa[y]

    def setCol(self, lista, x):
        for i, row in enumerate(self.mapa):
            row[x] = lista[i]

    def setRow(self, row, y):
        self.mapa[y] = row


def casosImediatos(ex):
    for i, v in enumerate(ex.ns):
        if v == ex.dim:
            ex.setCol(list(range(1, ex.dim + 1)), i)
        elif v == 1:
            ex.mapa[0][i] = ex.dim
    for i, v in enumerate(ex.sn):
        if v == ex.dim:
            ex.setCol(list(range(ex.dim, 0, -1)), i)
        elif v == 1:
            ex.mapa[ex.dim - 1][i] = ex.dim
    for i, v in enumerate(ex.oe):
        if v == ex.dim:
            ex.setRow(list(range(1, ex.dim + 1)), i)
        elif v == 1:
            ex.mapa[i][0] = ex.dim
    for i, v in enumerate(ex.eo):
        if v == ex.dim:
            ex.setRow(list(range(ex.dim, 0, -1)), i)
        elif v == 1:
            ex.mapa[i][ex.dim - 1] = ex.dim


def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))


def matrizAlturasPossiveis(ex):
    n = ex.dim
    matriz = []
    for y in range(ex.dim):
        matriz.append([])
        for x in range(ex.dim):
            alturasPossiveisNS = []
            c = ex.ns[x]
            if c is None:
                alturasPossiveisNS = list(range(1, n + 1))
            else:
                d = y
                ap = n - c + 1 + d
                for i in range(1, ap + 1):
                    alturasPossiveisNS.append(i)

            alturasPossiveisSN = []
            c = ex.sn[x]
            if c is None:
                alturasPossiveisSN = list(range(1, n + 1))
            else:
                d = n - y - 1
                ap = n - c + 1 + d
                if ap > n:
                    ap = n
                for i in range(1, ap + 1):
                    alturasPossiveisSN.append(i)

            alturasPossiveisOE = []
            c = ex.oe[y]
            if c is None:
                alturasPossiveisOE = list(range(1, n + 1))
            else:
                d = x
                ap = n - c + 1 + d
                for i in range(1, ap + 1):
                    alturasPossiveisOE.append(i)

            alturasPossiveisEO = []
            c = ex.eo[y]
            if c is None:
                alturasPossiveisEO = list(range(1, n + 1))
            else:
                d = n - x - 1
                ap = n - c + 1 + d
                if ap > n:
                    ap = n
                for i in range(1, ap + 1):
                    alturasPossiveisEO.append(i)

            alturasPossiveis = intersection(intersection(alturasPossiveisNS, alturasPossiveisSN),
                                            intersection(alturasPossiveisOE, alturasPossiveisEO))
            matriz[y].append(alturasPossiveis)
    return matriz


def ultrapassaVis(ex, line, c, f):
    if f == 0:
        vis1 = ex.oe[c]
        vis2 = ex.eo[c]
    else:
        vis1 = ex.ns[c]
        vis2 = ex.sn[c]
    tallest = 0
    if vis1 is not None and vis1 > 1:
        for i in line:
            if i is None:
                break
            if tallest < i:
                tallest = i
                vis1 -= 1
        if vis1 < 0:
            return True
    if vis2 is not None and vis2 > 1:
        tallest = 0
        line = line[::-1]
        for i in line:
            if i is None:
                break
            if tallest < i:
                tallest = i
                vis2 -= 1
        if vis2 < 0:
            return True
    return False


def isPossible(ex, y, x, n):
    for i in range(ex.dim):
        if ex.mapa[y][i] == n or ex.mapa[i][x] == n:
            return False
    #  row
    row = list(ex.row(y))
    row[x] = n
    if ultrapassaVis(ex, row, y, 0):
        return False
    #  col
    col = list(ex.col(x))
    col[y] = n
    if ultrapassaVis(ex, col, x, 1):
        return False
    return True


def isValidAux(ex, n, d):  # n -> (t, b, l, ou r) d -> (1-4)

    if d == 1 or d == 3:
        inicio = 0
        fim = len(n)
        sinal = 1
    else:
        inicio = len(n) - 1
        fim = -1
        sinal = -1

    for i, vis in enumerate(n):
        if vis is None:
            continue
        tallest = 0
        for j in range(inicio, fim, sinal):
            if (d == 1 or d == 2) and ex.mapa[j][i] > tallest:
                tallest = ex.mapa[j][i]
                vis -= 1
            elif (d == 3 or d == 4) and ex.mapa[i][j] > tallest:
                tallest = ex.mapa[i][j]
                vis -= 1
        if vis != 0:
            return False
    return True


def isValid(ex):
    return isValidAux(ex, ex.ns, 1) and isValidAux(ex, ex.sn, 2) and \
           isValidAux(ex, ex.oe, 3) and isValidAux(ex, ex.eo, 4)


def solve(ex, y, x):
    flag = True
    dim = ex.dim
    if x >= dim:
        x = 0
        y += 1
    if y >= dim:
        y -= 1
    for y in range(y, dim):
        if not flag:
            x = 0
        for x in range(x, dim):
            if ex.mapa[y][x] is None:
                for n in ex.possiveis[y][x]:
                    if isPossible(ex, y, x, n):
                        ex.mapa[y][x] = n
                        sol = solve(ex, y, x + 1)
                        if sol is not None:
                            return sol
                        ex.mapa[y][x] = None
                return
            flag = False
    if isValid(ex):
        return ex.mapa
