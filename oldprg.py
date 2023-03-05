while (True):
    print("Dateien:")
    dateilisten = {"1": "Graph_Dijk1_1.txt", "2": "Graph_Dijk1_2.txt",
                   "3": "Graph_Dijk2_1.txt", "4": "Graph_Dijk2_2.txt"}
    for x in dateilisten:
        print("Für", dateilisten[x], "drücke die Taste", x)
    auswahl = input("Welche Datei lesen: ")

    graph = {}
    if auswahl == "1":
        dateizulesen = dateilisten["1"]
        break
    if auswahl == "2":
        dateizulesen = dateilisten["2"]
        break
    if auswahl == "3":
        dateizulesen = dateilisten["3"]
        break
    if auswahl == "4":
        dateizulesen = dateilisten["4"]
        break
    else:
        print("falsche eingabe")

with open(dateizulesen, "r") as datei:
    for zeile in datei:
        knoten1, knoten2, gewicht = zeile.strip().split()
        if knoten1 not in graph:
            graph[knoten1] = {}
        graph[knoten1][knoten2] = int(gewicht)
    print(graph)


def dijkstra(graph, start, ziel):
    kuerzeste_distanz = {}
    vorfahren = {}
    versteckteknoten = graph
    infinity = float("inf")
    pfad = []
    for node in versteckteknoten:
        kuerzeste_distanz[node] = infinity
    kuerzeste_distanz[start] = 0

    while versteckteknoten:
        minKnoten = None
        for node in versteckteknoten:
            if minKnoten is None:
                minKnoten = node
            elif kuerzeste_distanz[node] < kuerzeste_distanz[minKnoten]:
                minKnoten = node

        for kindknoten, gewicht in graph[minKnoten].items():
            if gewicht + kuerzeste_distanz[minKnoten] < kuerzeste_distanz[kindknoten]:
                kuerzeste_distanz[kindknoten] = gewicht + \
                    kuerzeste_distanz[minKnoten]
                vorfahren[kindknoten] = minKnoten
        versteckteknoten.pop(minKnoten)

    aktuellerKnoten = ziel
    while aktuellerKnoten != start:
        try:
            pfad.insert(0, aktuellerKnoten)
            aktuellerKnoten = vorfahren[aktuellerKnoten]
        except KeyError:
            print("Pfad nicht erreichbar")
            break
    pfad.insert(0, start)
    if kuerzeste_distanz[ziel] != infinity:
        print("Die kürzeste Distanz von", start, "bis",
              ziel, "ist: " + str(kuerzeste_distanz[ziel]))
        print("Der Pfad ist: " + str(pfad))


try:
    start = input("Startknoten[0-9]: ")
    zielknoten = input("Zielknoten[0-9]: ")
except KeyError:
    print("Ungültige Eingabe")
dijkstra(graph, start, zielknoten)
