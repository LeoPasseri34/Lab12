import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._nodes = []
        self._graph = nx.Graph()
        self._idMap = {}

    def getCountries(self):
        allCountries = DAO.getCountries()
        return allCountries

    def getYear(self):
        years = DAO.getYear()
        return years

    def BuildGraph(self, year, country):
        self._graph.clear()
        self._nodes = DAO.getNodes(country)
        for n in self._nodes:
            self._idMap[n.Retailer_code] = n
        self._graph.add_nodes_from(self._nodes)
        self.addEdges(year, country)
        return self._graph

    def addEdges(self, year, country):
        edges = DAO.getEdges(year, country)
        for edge in edges:
            u = self._idMap[edge.r1Code]
            v = self._idMap[edge.r2Code]
            self._graph.add_edge(u, v, weight=edge.peso)
    def getNodes(self):
        return self._graph.nodes()



    def getNumNodes(self):
        return self._graph.number_of_nodes()

    def getNumEdges(self):
        return self._graph.number_of_edges()

    def getVolume(self):
        self._nodiConnessi = []
        self._volumi = []
        for n in self.getNodes():
            volume = 0
            for e in self._graph.edges(n, data=True):
                volume += e[2]['weight']
            if volume > 0:
                self._nodiConnessi.append(n)
                self._volumi.append((n.Retailer_name, volume))
        self._volumi.sort(key=lambda x: x[1], reverse=True)
        return self._volumi


