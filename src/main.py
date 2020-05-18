##
# Main function of the Python program.
#
##

from src.projeto import projeto


def imprime(m, t, b, l, r):
    print('    ' + ' '.join(map(aux, t)))
    print('    ' + ' '.join(['v'] * len(m)))
    for i in range(len(m)):
        print(' '.join(map(aux, [l[i], '>'] + m[i] + ['<', r[i]])))
    print('    ' + ' '.join(['^'] * len(m)))
    print('    ' + ' '.join(map(aux, b)))


def aux(d):
    if d:
        return str(d)
    else:
        return '.'


def main():
    print("<h3>projeto</h3>")
    m = [[1, 2, 3, 4],
         [3, 4, 1, 2],
         [2, 3, 4, 1],
         [4, 1, 2, 3]]
    v = ([3, 2, 2, 1], [1, 3, 2, 2], [4, 2, 3, 1], [1, 2, 2, 2])
    print("in:")
    imprime(m, *v)
    print("out:")
    r = projeto(m, *v)
    # imprime(r, *v)
    print(r)


if __name__ == '__main__':
    main()
