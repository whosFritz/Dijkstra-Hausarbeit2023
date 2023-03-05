import sys

# Alle Funktionen und Klassen


class Graph(object):
    def __init__(self, knoten, origin_graph):
        self.knoten = knoten
        self.graph = self.konstruiere_graph(knoten, origin_graph)

    def konstruiere_graph(self, knoten, origin_graph):
        '''
        Diese Methode stellt sicher, dass der Graph symetrisch ist. 
        Wenn ein weg von A nach B mit der Gewichtung W führt, 
        dann führt auch ein Weg von B nach A mit der Gewichtung W.
        '''
        graph = {}
        for knotenx in knoten:
            graph[knotenx] = {}

        graph.update(origin_graph)

        for knotenx, verbindung in graph.items():
            for nachbar_knoten, wichtung in verbindung.items():
                if graph[nachbar_knoten].get(knotenx, False) == False:
                    graph[nachbar_knoten][knotenx] = wichtung

        return graph

    def get_knoten(self):
        """Gibt Knoten des Graphen zurück.

        Returns:
            list: alle knoten des Graphen
        """
        return self.knoten

    def get_ausgehende_nachbarn(self, node):
        """Gibt die Nachbarn eines Graphen zurück.

        Returns:
            list: Verbindungen des jeweiligen Knotens
        """

        verbindungen = []
        for out_knotenx in self.knoten:
            if self.graph[node].get(out_knotenx, False) != False:
                verbindungen.append(out_knotenx)
        return verbindungen

    def wichtung(self, node1, node2):
        """Gibt das Gewicht einer Verbindung zwischen zwei Knoten zurück.

        Returns:
            int: Gewichtung
        """
        return self.graph[node1][node2]


def print_ergebnis(vorheriger_pfad, kuerzester_pfad, start_knoten, ziel_knoten):
    pfad = []
    knoten = ziel_knoten

    while knoten != start_knoten:
        pfad.append(knoten)
        knoten = vorheriger_pfad[knoten]

    # Add the start node manually
    pfad.append(start_knoten)

    print("Der kürzeste Pfad hat die Länge/Gewichtung: {} und sieht wie folgt aus.".format(
        kuerzester_pfad[ziel_knoten]))
    print(" -> ".join(reversed(pfad)))


def dijkstra(graph, start_knoten):
    unbesuchte_knoten = list(graph.get_knoten())

    # Mittels diesem dictionary spart man sich die Kosten, jeden Knoten zu besuchen und ihn upzudaten.
    kuerzester_pfad = {}

    # Mittels diesem dictionary,um den bisher bekanntestens kürzesten Pfad zu speicher um zu einem Knoten zu kommen.
    vorheriger_pfad = {}

    # Um die Gewichtung der Pfade zu vergleichen muss man einen "infinity-like" Werte festlegen für die unbesuchten Knoten
    max_wichtung = sys.maxsize
    for node in unbesuchte_knoten:
        kuerzester_pfad[node] = max_wichtung

    # Startknoten hat die Gewichtung 0
    kuerzester_pfad[start_knoten] = 0

    # Der Algorithmus läuft bis alle Knoten besucht wurden.
    while unbesuchte_knoten:
        # Dieser Code findet den Knoten mit der geringsten Gewichtung.
        aktueller_min_knoten = None
        for node in unbesuchte_knoten:  # Über die Knoten iterieren
            if aktueller_min_knoten == None:
                aktueller_min_knoten = node
            elif kuerzester_pfad[node] < kuerzester_pfad[aktueller_min_knoten]:
                aktueller_min_knoten = node

        # Dieser Code holt sich die Nachbarn des Knotens und updated deren Distanzen
        neighbors = graph.get_ausgehende_nachbarn(aktueller_min_knoten)
        for neighbor in neighbors:
            tentative_wichtung = kuerzester_pfad[aktueller_min_knoten] + \
                graph.wichtung(aktueller_min_knoten, neighbor)
            if tentative_wichtung < kuerzester_pfad[neighbor]:
                kuerzester_pfad[neighbor] = tentative_wichtung
                # We also update the best pfad to the current node
                vorheriger_pfad[neighbor] = aktueller_min_knoten

        # Nach dem jeder Nachbar besucht wurde, wird der Knoten als "besucht" markiert, indem er aus der Liste der "unbesuchten Knoten" entfernt wird
        unbesuchte_knoten.remove(aktueller_min_knoten)

    return vorheriger_pfad, kuerzester_pfad


# Programmstart:
while (True):
    print("Dateien:")
    dateilisten = {"1": "Graph_Dijk1_1.txt", "2": "Graph_Dijk1_2.txt",
                   "3": "Graph_Dijk2_1.txt", "4": "Graph_Dijk2_2.txt"}
    for x in dateilisten:
        print("Für", dateilisten[x], "drücke die Taste", x)
    auswahl = input("Welche Datei lesen: ")

    origin_graph = {}
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
        print("Ungültige Eingabe")

# Leere Set-Initalisierung für die Liste der Knoten (0 bis 9), es darf keine Dopplung geben, deswegen ein Set.
knoten = set()

# Einlesen der Datei.
with open(dateizulesen, "r") as datei:
    # für jede Zeile in der Datei, aufspalten und in das Set packen.
    for zeile in datei:
        knoten1, knoten2, gewicht = zeile.strip().split()
        knoten.add(knoten1)
        knoten.add(knoten2)
        # Knoten falls noch nicht im Graphen-Dictionary in das Dictionary packen,
        if knoten1 not in origin_graph:
            origin_graph[knoten1] = {}
        # falls doch, dann die Gewichtung anpassen
        origin_graph[knoten1][knoten2] = int(gewicht)

# Set wird umgewandelt zu einer Liste, damit datentypbezogene Operationen möglich sind.
knoten = list(knoten)
knoten.sort()  # Knoten sortieren in aufsteigender Reihenfolge.

try:
    # Eingabe des Startknotens und des Zielknotens über die Kommandozeile.
    while True:
        start = input("Startknoten[0-9]: ")
        zielknoten = input("Zielknoten[0-9]: ")
        if start in knoten and zielknoten in knoten:
            break
        else:
            # Falls die Eingabe Falsch ist, wird die Eingabe wiederholt. Wenn nicht, gehts weiter.
            print("Falsche eingabe")

except KeyError:
    print("Ungültige Eingabe")


graph = Graph(knoten, origin_graph)  # Erstellung des Graphen
vorheriger_pfad, kuerzester_pfad = dijkstra(
    graph=graph, start_knoten=start)  # Funktion des Algorithmus ausführen
print_ergebnis(vorheriger_pfad, kuerzester_pfad,
               start_knoten=start, ziel_knoten=zielknoten)  # Ausgabe des Ergebnis
