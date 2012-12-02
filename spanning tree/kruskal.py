import heapq

class Forest(object):

    def __init__(self, elements):
        self._parents = {}
        self._ranks = {}
        for elem in elements:
            self.setParent(elem, elem)
            self.setRank(elem, 0)

    def getParent(self, x):
        return self._parents[x]

    def setParent(self, x, parent):
        self._parents[x] = parent

    def getRank(self, x):
        return self._ranks[x]

    def setRank(self, elem, rank):
        self._ranks[elem] = rank

    def union(self, x, y):
        xRoot = self.find(x)
        yRoot = self.find(y)
        if self.getRank(xRoot) > self.getRank(yRoot):
            self.setParent(yRoot, xRoot)
        elif self.getRank(xRoot) < self.getRank(yRoot):
            self.setParent(xRoot, yRoot)
        elif xRoot != yRoot:
            self.setParent(yRoot, xRoot)
            self.setRank(x, self.getRank(xRoot) + 1)

    def find(self, x):
        if self.getParent(x) == x:
            return x
        else:
            self.setParent(x, self.find(self.getParent(x)))
            return self.getParent(x)

class EdgeHeap(object):
    def __init__(self, edges, weights):
        self._data = [(weights(edge), edge) for edge in edges]
        self._weights = weights
        heapq.heapify(self._data)

    def pop(self):
        return heapq.heappop(self._data)[1]


class KruskalAlgorithm(object):

    def __init__(self, graph, weights):
        self._graph = graph
        self._edgeHeap = EdgeHeap(graph.edges(), weights)
        self._nodeForest = Forest(graph.nodes())
        self._spanningTreeEdges = []

    def isFinished(self):
        return len(self._graph.nodes()) <= len(self._spanningTreeEdges) + 1

    def getSelectedSpanningTreeEdges(self):
        return self._spanningTreeEdges

    def nextStep(self):
        if self.isFinished():
            return #raise Error?

        while True:
            try:
                candidateEdge = self._edgeHeap.pop()
                (u, v) = candidateEdge
                if self._nodeForest.find(u) != self._nodeForest.find(v):
                    self._nodeForest.union(u, v)
                    self._spanningTreeEdges.append(candidateEdge)
                    return
            except IndexError:
                raise ValueError("Graph is not connected.")


