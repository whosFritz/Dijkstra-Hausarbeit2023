import sys

# Alle Funktionen und Klassen


class Graph(object):
    def __init__(self, knoten, roh_graph):
        self.knoten = knoten
        self.graph = self.konstruiere_graph(knoten, roh_graph)

    def konstruiere_graph(self, knoten, roh_graph):
        '''
        Diese Methode stellt sicher, dass der Graph symetrisch ist.
        Wenn ein weg von A nach B mit der Gewichtung W führt,
        dann führt auch ein Weg von B nach A mit der Gewichtung W.
        '''
        graph = {}
        for knotenx in knoten:
            graph[knotenx] = {}

        graph.update(roh_graph)

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

    pfad.append(start_knoten)

    print("Der kürzeste Pfad von {} zu {} hat die Länge/Gewichtung {} und sieht wie folgt aus.".format(start_knoten, ziel_knoten,
                                                                                                       kuerzester_pfad[ziel_knoten]))
    print(" -> ".join(reversed(pfad)))


def dijkstra(graph, start_knoten):
    unbesuchte_knoten = list(graph.get_knoten())

    # Mittels diesem dictionary spart man sich die Kosten, jeden Knoten zu besuchen und ihn upzudaten.
    kuerzester_pfad = {}

    # Mittels diesem dictionary, um den bisher bekanntesten kürzesten Pfad um zu einem Knoten zu kommen zu speichern.
    vorheriger_pfad = {}

    # Um die Gewichtung der Pfade zu vergleichen muss man einen "infinity-like" Wert für die unbesuchten Knoten festlegen.
    # Dadurch wird jeder unbesuchte Knoten erstmal als "super schlecht" angesehen.
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
        nachbarn = graph.get_ausgehende_nachbarn(aktueller_min_knoten)
        for nachbar in nachbarn:
            bisherversuchte_wichtung = kuerzester_pfad[aktueller_min_knoten] + \
                graph.wichtung(aktueller_min_knoten, nachbar)
            if bisherversuchte_wichtung < kuerzester_pfad[nachbar]:
                kuerzester_pfad[nachbar] = bisherversuchte_wichtung
                # Außerdem wird der beste Pfad zum aktuellen Knoten geupdated
                vorheriger_pfad[nachbar] = aktueller_min_knoten

        # Nach dem jeder Nachbar besucht wurde, wird der Knoten als "besucht" markiert, indem er aus der Liste der "unbesuchten Knoten" entfernt wird
        unbesuchte_knoten.remove(aktueller_min_knoten)

    return vorheriger_pfad, kuerzester_pfad


# Programmstart:
# Leere Set-Initalisierung für die Liste der Knoten (0 bis 9), es darf keine Dopplung geben, deswegen ein Set.
knoten = set()
while (True):
    print("Dateien:")
    dateilisten = {"1": "Graph_Dijk2_1.txt",
                   "2": "Graph_Dijk2_2.txt (enthält negative Gewichtung)"}
    for x in dateilisten:
        print("Für", dateilisten[x], "drücken Sie die Taste", x)
    auswahl = input("Welche Datei lesen: ")

    roh_graph = {}
    if auswahl == "1":
        dateizulesen = dateilisten["1"][0:17]
        break
    if auswahl == "2":
        dateizulesen = dateilisten["2"][0:17]
        break
    else:
        print("Ungültige Eingabe!")


# Einlesen der Datei.
with open(dateizulesen, "r") as datei:
    # für jede Zeile in der Datei, aufspalten und in das Set packen.
    for zeile in datei:
        knoten1, knoten2, gewicht = zeile.strip().split()
        knoten.add(knoten1)
        knoten.add(knoten2)
        # Knoten falls noch nicht im Graphen-Dictionary in das Dictionary packen,
        if knoten1 not in roh_graph:
            roh_graph[knoten1] = {}
        # falls doch, dann die Gewichtung anpassen
        roh_graph[knoten1][knoten2] = int(gewicht)
# Set wird umgewandelt zu einer Liste, damit datentypbezogene Operationen möglich sind.
knoten = list(knoten)
knoten.sort()  # Knoten sortieren in aufsteigender Reihenfolge.
graph = Graph(knoten, roh_graph)  # Erstellung des Graphen
while True:
    # Ausgabe aller kürzesten Pfade von Null oder Manuelle Eingabe
    print("1: Vollständige Ausgabe kürzester Pfade von 0 zu allen Knoten?\n2: Manuelle Eingabe? ")
    entscheidung = input("Warte auf Eingabe: ")
    if entscheidung == "1":
        start_knoten = "0"
        for knt in knoten:
            vorheriger_pfad, kuerzester_pfad = dijkstra(
                graph, start_knoten)
            print_ergebnis(vorheriger_pfad, kuerzester_pfad,
                           start_knoten, knt)
        break

    if entscheidung == "2":
        try:
            # Eingabe des Startknotens und des Zielknotens über die Kommandozeile.
            while True:
                start_knoten = input("Startknoten[0-9]: ")
                ziel_knoten = input("Zielknoten[0-9]: ")
                if start_knoten in knoten and ziel_knoten in knoten:
                    break
                else:
                    # Falls die Eingabe Falsch ist, wird die Eingabe wiederholt. Wenn nicht, gehts weiter.
                    print("Ungültige Eingabe!")

        except KeyError:
            print("Ungültige Eingabe!")

        vorheriger_pfad, kuerzester_pfad = dijkstra(
            graph, start_knoten)  # Funktion des Algorithmus ausführen
        print_ergebnis(vorheriger_pfad, kuerzester_pfad,
                       start_knoten, ziel_knoten)  # Ausgabe des Ergebnis
        break
    else:
        print("Ungültige Eingabe!")
