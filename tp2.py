import sys


def ler_arquivo_em_itens():
    itens = []
    arquivo = open(sys.argv[1], 'r')
    conteudo = arquivo.readlines()

    for linha in conteudo:
        itens.append(linha)

    return itens


def isort(nlist):
    swaps, checks = 0, 0

    for i in range(len(nlist)):

        value = nlist[i]
        position = i
        checks += 1

        while position > 0 and nlist[position-1] > value:
            nlist[position] = nlist[position-1]
            position -= 1
            checks += 1
            swaps += 1

        nlist[position] = value

    return "[isort] {} trocas foram feitas. {} comparações foram feitas.".format(swaps, checks)


def bsort(nlist):
    swaps, checks = 0, 0

    for j in range(len(nlist)):

        for i in range(1, len(nlist)-j):
            checks += 1

            if nlist[i-1] > nlist[i]:
                swaps += 1
                nlist[i-1], nlist[i] = nlist[i], nlist[i-1]

    return "[bsort] {} trocas foram feitas. {} comparações foram feitas.".format(swaps, checks)


def qsort(nlist):
    swaps, checks = __qsort(nlist, 0, len(nlist) - 1)
    return "[qsort] {} trocas foram feitas. {} comparações foram feitas.".format(swaps, checks)


def __qsort(nlist, begin, end):
    i = begin
    j = end
    swaps, checks = 0, 0
    pivote = nlist[(begin + end)//2]

    while i <= j:
        while nlist[i] < pivote:
            i += 1
        while pivote < nlist[j]:
            j -= 1
        if i <= j:
            aux = nlist[i]
            nlist[i] = nlist[j]
            nlist[j] = aux
            swaps += 1
            i += 1
            j -= 1
        checks += 1

    if begin < j:
        other_swap, other_check = __qsort(nlist, begin, j)
        swaps += other_swap
        checks += other_check
    if i < end:
        other_swap, other_check = __qsort(nlist, i, end)
        swaps += other_swap
        checks += other_check

    return (swaps, checks)


print(isort(ler_arquivo_em_itens()))
print(bsort(ler_arquivo_em_itens()))
print(qsort(ler_arquivo_em_itens()))
