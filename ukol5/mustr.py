import numpy

# Nacteni dat ze vstupniho souboru a vytvoreni matice sousednosti
def read_matrix(filename):
    file = open(filename)
    maxn = 0
    data = [] # Vytvoreni prazdneho listu
    for line in file:
        vertex1, vertex2, weight = map(int, line.split(";")) # Rozdeleni radku a pretypovani na int
        maxn = max(vertex1, maxn, vertex2)
        data.append((vertex1, vertex2, weight)) # Vlozeni trojice `(vertex1, vertex1, weight)` do listu `data`
    file.close()
    # Vytvoreni matice sousednosti
    matrix = numpy.zeros((maxn + 1, maxn + 1), dtype = "uint32") # Vytvoreni prazdne numpy matice
    ### BEGIN TODO ukol 1
	### Naplnte matici na zaklade trojic ulozenych v listu `data`
    ### END TODO ukol 1
    return matrix


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
        for to_v in range(distance_matrix.shape[0]): # snazime se najit nenavstivene sousedy vrcholu `from_v`
            ### BEGIN TODO 4
			### Doimplementujte BFS:
			###   - kontrola zda-li byl uzel `to_v` navstiven a zda-li je mezi `from_v` a `to_v` hrana
			###   - pokud ano, nastavte všechny datové struktury dle algoritmu
            ### END TODO 4

    return distances

karate = read_matrix("..\data\karate.csv") # nacteme karate graf, jelikoz ten je nevazeny 
distance_sum = 0
for start in range(karate.shape[0]):
    distance_sum = distance_sum + sum(bfs(karate, 1)) # provadime sumu nejkratsich vzdalenosti

print('Prumerna vzdalenost v grafu je {}'.format(float(distance_sum) / (karate.shape[0] * karate.shape[0])))

# Ocekavany vystup spravneho reseni je:
# Prumerna vzdalenost v grafu je 1.6571428571428573
