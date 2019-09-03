import numpy

# budeme pouzivat reprezentaci, ze pokud je vzdalenost mezi vrcholy neznama, pak ma v matici hodnotu 2^30
def FloydWarshall(filename):
    distance = read_matrix(filename)
    # inicializace distance matice
    for i in range(distance.shape[0]): # distance.shape[0] vrati pocet prvku v ose x matice
        for j in range(distance.shape[0]):
            if distance[i][j] == 0 and i != j:
                distance[i][j] = pow(2,30) # nastaveni hodnoty 2^30

    ### BEGIN TODO 5
    ### Implementujte Floyd-Warshall algoritmus
    ### END TODO 5
    return distance

matrix = FloydWarshall("..\data\karate.csv")
pocet_hran = (matrix.shape[0] - 1) * (matrix.shape[0] - 1) - (matrix.shape[0] - 1) # viz. predchozi ukol
print("Prumerna nejkratsi vzdalenost v karate klubu je {}".format(matrix.sum() / pocet_hran))

matrix = FloydWarshall("..\data\lesmis.csv")
pocet_hran = matrix.shape[0] * matrix.shape[0] - matrix.shape[0] # v tomto pripade jsou vrcholy indexovany od nuly!
print("Průměrná nejkratší vzdalenost mezi Bidniky je {}".format(matrix.sum() / pocet_hran))


# Ocekavany vystup spravneho reseni je:
# Prumerna nejkratsi vzdalenost v karate klubu je 2.408199643493761
# Průměrná nejkratší vzdalenost mezi Bidniky je 4.861244019138756
