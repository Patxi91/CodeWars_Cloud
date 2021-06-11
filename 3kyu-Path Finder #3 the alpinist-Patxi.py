import math


class priorityQueue:  # Min Heap
    def __init__(self):
        self.queue = []

    def enqueue(self, node, priority):
        self.queue.append({"node": node, "priority": priority})
        #print(f"Node Added to Priority Queue: {node}, priority: {priority}")
        self.upHeap()

    def dequeue(self):
        if len(self.queue) > 0:
            first = self.queue[0].copy()
            lastElement = self.queue.pop(-1)
            if len(self.queue) > 0:
                self.queue[0] = lastElement
                self.downHeap()
                return first
            else:
                return lastElement

    def upHeap(self):
        childInd = len(self.queue) - 1
        while childInd > 0:
            parentIdx = math.floor((childInd - 1) / 2)
            if self.queue[parentIdx]["priority"] > self.queue[childInd]["priority"]:
                self.queue[childInd], self.queue[parentIdx] = self.queue[parentIdx], self.queue[childInd]
                childInd = parentIdx
            else:
                break

    def downHeap(self):
        parentIdx = 0
        listLen = len(self.queue) - 1
        while True:
            swap = False
            leftChildIdx, leftChild = 2 * parentIdx + 1, float('inf')
            rightChildIdx, rightChild = 2 * parentIdx + 2, float('inf')
            if leftChildIdx <= listLen:
                leftChild = self.queue[leftChildIdx]["priority"]
                swap = True
            if rightChildIdx <= listLen:
                rightChild = self.queue[rightChildIdx]["priority"]
            if swap:
                if leftChild <= rightChild:
                    minChildIdx = leftChildIdx
                else:
                    minChildIdx = rightChildIdx
            else:
                break
            if self.queue[parentIdx]["priority"] > self.queue[minChildIdx]["priority"]:
                self.queue[minChildIdx], self.queue[parentIdx] = self.queue[parentIdx], self.queue[minChildIdx]
                parentIdx = minChildIdx
            else:
                break

class WeightedGraph:
    def __init__(self):
        self.adjacencyList = {}

    def getWeight(self, key, neighbor):
        for x in self.adjacencyList[key]:
            if x['adjV'] == neighbor:
                return x['w']

    def getNeighbors(self, key):
        neighbors = []
        for node in self.adjacencyList[key]:
            neighbors.append(node)
        return neighbors

    def addVertex(self, vertex):
        self.adjacencyList.update({vertex: []})

    def addEdge(self, vertex1, vertex2, weight):
        self.adjacencyList[vertex1].append({"adjV": vertex2, "w": weight})


def initialize():
    global alpineGraph, q, distanceDict, prevNode, visited
    alpineGraph = WeightedGraph()
    q = priorityQueue()
    distanceDict = {}
    prevNode = {}
    visited = {}


def encode(elem1, elem2):
    return str(elem1) + "-" + str(elem2)


def searchAdj(currNode, maze):  # [y, x]
    vertex1 = encode(currNode[0], currNode[1])
    alpineGraph.addVertex(vertex1)
    searchList = []
    left, right = [currNode[0], currNode[1] - 1], [currNode[0], currNode[1] + 1]
    up, down = [currNode[0] - 1, currNode[1]], [currNode[0] + 1, currNode[1]]
    searchList.extend((left, right, up, down))
    for x in searchList:
        if 0 <= x[0] < len(maze) and 0 <= x[1] < len(maze[0]):
            vertex2 = encode(x[0], x[1])
            weight = abs(int(maze[currNode[0]][currNode[1]]) - int(maze[x[0]][x[1]]))
            alpineGraph.addEdge(vertex1, vertex2, weight)


def dijkstras(end, maze):  # alpineGraph, q, distanceDict, prevNode, visited
    while q:
        searchNode = q.dequeue()
        searchNodeXY = searchNode['node'].split('-')
        y1, x1 = int(searchNodeXY[0]), int(searchNodeXY[1])
        searchAdj([y1, x1], maze)
        if searchNode['node'] == end:
            break
        neighbors = alpineGraph.getNeighbors(searchNode['node'])
        visited[searchNode['node']] = True
        for neighbor in neighbors:
            startWeight = alpineGraph.getWeight(searchNode['node'], neighbor['adjV'])
            distanceWeight = startWeight + distanceDict[searchNode['node']]
            if distanceWeight < distanceDict[neighbor['adjV']]:
                distanceDict[neighbor['adjV']] = distanceWeight
                if neighbor['adjV'] not in visited:
                    q.enqueue(neighbor['adjV'], distanceDict[neighbor['adjV']])
                prevNode.update({neighbor['adjV']: searchNode['node']})
    return prevNode


def path_finder(maze):
    maze = maze.splitlines()
    initialize()

    for a in range(len(maze)):
        for z in range(len(maze[a])):
            name = encode(a, z)
            distanceDict[name] = float('inf')
            prevNode[name] = None
    q.enqueue('0-0', 0)
    distanceDict['0-0'] = 0
    prevNode['0-0'] = '0-0'
    end = str(len(maze) - 1) + "-" + str(len(maze[-1]) - 1)
    dijkstras(end, maze)
    return distanceDict[end]

