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
    m = [[None, None, 2],
         [None, 3, None],
         [None, None, None]]
    v = ([None, None, None], [None, None, None], [None, None, None], [None, None, None])
    print("in:")
    imprime(m, *v)
    print("out:")
    r = projeto(m, *v)
    imprime(r, *v)


if __name__ == '__main__':
    main()
