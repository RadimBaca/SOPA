import numpy

# Nacteni dat ze vstupniho souboru a vytvoreni matice sousednosti
def read_matrix(filename):
    with open(filename) as file:
        maxn = 0
        data = [] # Vytvoreni prazdneho listu
        for line in file:
            vertex1, vertex2, weight = map(int, line.split(";")) # Rozdeleni radku a pretypovani na int
            maxn = max(vertex1, maxn, vertex2)
            data.append((vertex1, vertex2, weight)) # Vlozeni trojice `(vertex1, vertex1, weight)` do listu `data`
        # Vytvoreni matice sousednosti
        matrix = numpy.zeros((maxn + 1, maxn + 1), dtype = "uint32") # Vytvoreni prazdne numpy matice
        ### BEGIN TODO 1
        ### Naplnte matici na zaklade trojic ulozenych v listu `data`
        ### END TODO 1
        return matrix

# Nacteni jmen ze souboru a ulozeni v map
# TODO 2 - tato funkce obsahuje trivialni chybu, zkuste opravit
def read_names(filename):
    with open(filename) as file:
        names = {} # Vytvoreni prazdne mapy
        file.readline()
        for line in file:
            order, name = line.split(",") # Rozdeleni radku nacteneho ze souboru
            order = int(order)
            name = name.rstrip()
            names[order] = name # Ulozeni v mape `names`, pro dany klic `order` ulozime hodnotu `name`
        return names

# Volani predchozich funkci
matrix = read_matrix("../data/lesmis.csv")
names = read_names("../data/lesmis_names.csv")
print(matrix)
print(names)

# Ocekavany vystup spravneho reseni je
# [[0 1 8 ... 0 0 0]
 # [1 0 0 ... 0 0 0]
 # [8 0 0 ... 0 0 0]
 # ...
 # [0 0 0 ... 0 0 0]
 # [0 0 0 ... 0 0 0]
 # [0 0 0 ... 0 0 0]]
# {0: 'Myriel', 1: 'Napoleon', 2: 'MlleBaptistine', 3: 'MmeMagloire', 4: 'CountessDeLo', 5: 'Geborand', 6: 'Champtercier', 7: 'Cravatte', 8: 'Count', 9: 'OldMan', 10: 'Labarre', 11: 'Valjean', 12: 'Marguerite', 13: 'MmeDeR', 14: 'Isabeau', 15: 'Gervais', 16: 'Tholomyes', 17: 'Listolier', 18: 'Fameuil', 19: 'Blacheville', 20: 'Favourite', 21: 'Dahlia', 22: 'Zephine', 23: 'Fantine', 24: 'MmeThenardier', 25: 'Thenardier', 26: 'Cosette', 27: 'Javert', 28: 'Fauchelevent', 29: 'Bamatabois', 30: 'Perpetue', 31: 'Simplice', 32: 'Scaufflaire', 33: 'Woman1', 34: 'Judge', 35: 'Champmathieu', 36: 'Brevet', 37: 'Chenildieu', 38: 'Cochepaille', 39: 'Pontmercy', 40: 'Boulatruelle', 41: 'Eponine', 42: 'Anzelma', 43: 'Woman2', 44: 'MotherInnocent', 45: 'Gribier', 46: 'Jondrette', 47: 'MmeBurgon', 48: 'Gavroche', 49: 'Gillenormand', 50: 'Magnon', 51: 'MlleGillenormand', 52: 'MmePontmercy', 53: 'MlleVaubois', 54: 'LtGillenormand', 55: 'Marius', 56: 'BaronessT', 57: 'Mabeuf', 58: 'Enjolras', 59: 'Combeferre', 60: 'Prouvaire', 61: 'Feuilly', 62: 'Courfeyrac', 63: 'Bahorel', 64: 'Bossuet', 65: 'Joly', 66: 'Grantaire', 67: 'MotherPlutarch', 68: 'Gueulemer', 69: 'Babet', 70: 'Claquesous', 71: 'Montparnasse', 72: 'Toussaint', 73: 'Child1', 74: 'Child2', 75: 'Brujon', 76: 'MmeHucheloup'}
