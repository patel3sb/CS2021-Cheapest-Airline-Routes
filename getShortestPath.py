from collections import defaultdict, deque

# basic graph class
class Graph(object):

    # initialize graph nodes, edges and distances
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    # add new node
    def addNode(self, value):
        self.nodes.add(value)

    # add new edges (undirected graph) and distances
    def addEdge(self, fromNode, toNode, distance):
        self.edges[fromNode].append(toNode)
        self.edges[toNode].append(fromNode)
        self.distances[(fromNode, toNode)] = distance
        self.distances[(toNode, fromNode)] = distance

# implementation of dijstra's algorithm for shortest paths
def dijkstra(graph, initial):

    # keep track of visited nodes
    visited = {initial: 0}
    path = {}

    nodes = set(graph.nodes)

    # loop through nodes and find minimum distance nodes
    while nodes:
        minNode = None
        for node in nodes:
            # check if node has been visited and address minNode
            if node in visited:
                if minNode is None:
                    minNode = node
                elif visited[node] < visited[minNode]:
                    minNode = node
        if minNode is None:
            break

        nodes.remove(minNode)
        currentWeight = visited[minNode]

        # iterate through edges in minNode
        for edge in graph.edges[minNode]:
            try:
                weight = currentWeight + graph.distances[(minNode, edge)]
            except:
                continue
            # address non-visited edges and lower weights
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = minNode

    return visited, path

# returns shortest path from origin to destination
def shortestPath(graph, origin, dest):
    # initialize basic variables
    visited, paths = dijkstra(graph, origin)
    fullPath = deque()
    destination = paths[dest]

    # iterate through nodes to get to destination
    while destination != origin:
        fullPath.appendleft(destination)
        destination = paths[destination]

    fullPath.appendleft(origin)
    fullPath.append(dest)

    # return path as well as path cost
    return visited[dest], list(fullPath)


graph = Graph()

# list of cities
cityList = ['Fairbanks', 'Winnipeg', 'Vancouver', 'San Francisco', 'Los Angeles', 'Ottawa', 'Chicago', 'Dallas', 'New York', 'Washington DC', 'Houston', 'Miami', 'Mexico', 'Panama', 'Bogota', 'Caracas', 'Georgetown', 'Quito', 'Lima', 'Rio de Janeiro', 'Sao Paulo', 'Buenos Aires', 'Santiago', 'Reykjavik', 'Lagos', 'Cairo', 'Kinshasa', 'Pretoria', 'Cape Town', 'Addis Ababa', 'Nairobi', 'Mombasa', 'Port Louis', 'Tehran', 'Kuwait', 'Dubai', 'Karachi', 'Aden', 'Mumbai', 'New Delhi', 'Kathmandu', 'Dhaka', 'Chennai', 'Colombo', 'Kolkata', 'Omsk', 'Irkutsk', 'Beijing', 'Shanghai', 'Hong Kong', 'Bangkok', 'Singapore', 'Jakarta', 'Manila', 'Tokyo', 'Seoul', 'Perth', 'Brisbane', 'Melbourne', 'Sydney', 'Auckland', 'Wellington', 'Christchurch', 'London', 'Lisbon', 'Paris', 'Berlin', 'Frankfurt', 'Rome', 'Athens', 'Oslo', 'Stockholm', 'Leningrad', 'Moscow', 'Perm']

# create nodes using cityList
for node in cityList:
    graph.addNode(node)

# pre-processed lists with from, to, and cost information
fromNodes = ['San Francisco', 'San Francisco', 'San Francisco', 'Chicago', 'San Francisco', 'Chicago', 'Chicago', 'Ottawa', 'New York', 'Washington DC', 'Los Angeles', 'Los Angeles', 'Santiago', 'Houston', 'Mexico', 'Mexico', 'Panama', 'Bogota', 'Lima', 'Bogota', 'Rio de Janeiro', 'Rio de Janeiro', 'Bogota', 'Caracas', 'Washington DC', 'Vancouver', 'San Francisco', 'Chicago', 'Lisbon', 'London', 'Reykjavik', 'London', 'Paris', 'Lagos', 'Lagos', 'Nairobi', 'Nairobi', 'Rio de Janeiro', 'Kinshasa', 'Kinshasa', 'Port Louis', 'Port Louis', 'Mumbai', 'Mumbai', 'Aden', 'Nairobi', 'Nairobi', 'Rome', 'Rome', 'London', 'Frankfurt', 'Oslo', 'Moscow', 'Moscow', 'Moscow', 'Omsk', 'Moscow', 'New Delhi', 'New Delhi', 'Cairo', 'Kuwait', 'Moscow', 'Tehran', 'Moscow', 'Irkutsk', 'Kathmandu', 'Dhaka', 'Kolkata', 'Chennai', 'Colombo', 'New Delhi', 'Colombo', 'Jakarta', 'Bangkok', 'Hong Kong', 'Hong Kong', 'Hong Kong', 'New Delhi', 'Tokyo', 'Beijing', 'Beijing', 'Seoul', 'Seoul', 'Bangkok', 'Tokyo', 'Manila', 'Melbourne', 'Christchurch', 'Christchurch', 'Brisbane', 'Brisbane', 'New York', 'Buenos Aires', 'New York']
toNodes = ['Vancouver', 'Chicago', 'Dallas', 'Houston', 'Los Angeles', 'Ottawa', 'New York', 'New York', 'Washington DC', 'Dallas', 'Winnipeg', 'Santiago', 'Buenos Aires', 'Mexico', 'Panama', 'Quito', 'Bogota', 'Lima', 'Sao Paulo', 'Rio de Janeiro', 'Georgetown', 'Caracas', 'Miami', 'New York', 'Fairbanks', 'Tokyo', 'Tokyo', 'Lisbon', 'London', 'Reykjavik', 'Vancouver', 'Paris', 'Lagos', 'Cairo', 'Nairobi', 'Mombasa', 'Pretoria', 'Pretoria', 'Pretoria', 'Lagos', 'Pretoria', 'Mumbai', 'Pretoria', 'Aden', 'Addis Ababa', 'Addis Ababa', 'Athens', 'Athens', 'London', 'Berlin', 'Berlin', 'Stockholm', 'Stockholm', 'Leningrad', 'Perm', 'Perm', 'New Delhi', 'Mumbai', 'London', 'Kuwait', 'Dubai', 'Tehran', 'Karachi', 'Cairo', 'Omsk', 'New Delhi', 'Kolkata', 'Mumbai', 'Mumbai', 'Chennai', 'Chennai', 'Perth', 'Singapore', 'Singapore', 'Singapore', 'Seoul', 'Tokyo', 'Singapore', 'Singapore', 'Shanghai', 'Seoul', 'Irkutsk', 'Tokyo', 'New Delhi', 'Manila', 'Sydney', 'Sydney', 'Melbourne', 'Sydney', 'Aukland', 'Wellington', 'London', 'Cape Town', 'London']
costNodes = [450.0, 237.0, 237.0, 257.0, 237.0, 514.0, 255.0, 255.0, 256.0, 246.0, 400.0, 1418.0, 404.0, 218.0, 960.0, 572.0, 230.0, 172.0, 304.0, 444.0, 1973.0, 8357.0, 265.0, 570.0, 492.0, 1033.0, 1636.0, 718.0, 144.0, 380.0, 643.0, 113.0, 919.0, 573.0, 579.0, 105.0, 1410.0, 2914.0, 458.0, 980.0, 926.0, 296.0, 3128.0, 854.0, 458.0, 218.0, 663.0, 963.0, 106.0, 141.0, 367.0, 114.0, 204.0, 378.0, 425.0, 315.0, 361.0, 260.0, 370.0, 189.0, 206.0, 274.0, 623.0, 408.0, 722.0, 158.0, 100.0, 272.0, 36.0, 100.0, 81.0, 564.0, 387.0, 100.0, 173.0, 169.0, 604.0, 377.0, 552.0, 70.0, 203.0, 402.0, 587.0, 178.0, 1037.0, 439.0, 98.0, 430.0, 394.0, 87.0, 428.0, 686.0, 1000.0, 500.0]

# add edges to Graph
length = len(fromNodes)
for i in range(0, length):
    graph.addEdge(fromNodes[i], toNodes[i], costNodes[i])
    

