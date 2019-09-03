import numpy


### `Breath-first search` algoritmus (dále jen BFS) pro hledani prumeru nevazeneho grafu. 
### Vstupem je matice sousednosti a vychozi uzel.
def bfs(distance_matrix, start):
    distances = [0] * distance_matrix.shape[0] # list vzdalenosti vsech vrcholu od vrcholu `start`
    visited = [False] * distance_matrix.shape[0] # list priznaku urcujici zda-li byl vrchol navstiven
    visited[start] = True # pruchod zaciname od vrcholu start, takze jej oznacime za navstiveny
    queue = [(start, 0)] # do fronty ukladame id vrcholu spolu s aktualni vzdalenosti
    queue_start = 0
    while len(queue) - queue_start > 0:
        from_v, distance = queue[queue_start]
        queue_start = queue_start + 1
        for to_v in range(distance_matrix.shape[0]): # snazime se najit nenavstivene sousedy vrcholu `from_to`
            raise NotImplementedError
            ### BEGIN TODO 4
            ### Doimplementujte BFS:
            ###   - kontrola zda-li byl uzel `to_v` navstiven a zda-li je mezi `from_v` a `to_v` hrana
            ###   - pokud ano, nastavte všechny datové struktury dle algoritmu
            ### END TODO 4

    return distances

karate = read_matrix("..\data\karate.csv") # nacteme karate graf, jelikoz ten je nevazeny 
distance_sum = 0
for start in range(1,karate.shape[0]): # vsimnete si, ze zde provadime pruchod az od cisla jedna
    distance_sum = distance_sum + sum(bfs(karate, start)) # provadime sumu nejkratsich vzdalenosti

pocet_hran = (karate.shape[0] - 1) * (karate.shape[0] - 1) - (karate.shape[0] - 1) # nulty radek matice neodpovida zadne osobe, proto minus jedna. Do prumerne vzdalenosti v grafu se pak nezapocitavaji ani vzdalenosti mezi stejnym vrcholem.
print('Prumerna nejkratsi vzdalenost v grafu je {}'.format(float(distance_sum) / pocet_hran))


# Ocekavany vystup spravneho reseni je
# Prumerna nejkratsi vzdalenost v grafu je 2.408199643493761
