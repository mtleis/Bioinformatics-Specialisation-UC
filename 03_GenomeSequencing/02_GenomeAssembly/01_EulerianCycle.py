## Eulerian Cycle
from collections import defaultdict


# Deprecated, better include 'startpoint' as a parameter
def EulerianCycle(graph):
    # Create & Initialize a boolean dictionary to track visited edges
    visited = defaultdict(list)
    for key in graph.keys():
        for value in graph[key]:
            visited[key].append(False)

    # Form a cycle by randomly walking through graph
    cycle = NewCycle(graph, visited, next(iter(graph)) )
    # While there are unexplored edges in graph
    while (unexploredEdges(visited)):
        # Select a node in Cycle with still unexplored edges
        for key in cycle:
            if hasFreeNode(key, visited):
                newstart = key
                break
        # create a new cycle starting at newstart
        newCycle = NewCycle(graph, visited, newstart)
        # Merge the new cycle into the main cycle
        cycle = mergeNewCycle(cycle, newCycle)
    return cycle


## Overloaded message when starting point is specified
def EulerianCycleWithStartPoint(graph, startpoint):
    # Create & Initialize a boolean dictionary to track visited edges
    visited = defaultdict(list)
    for key in graph.keys():
        for value in graph[key]:
            visited[key].append(False)

    # Form a cycle by randomly walking through graph
    cycle = NewCycle(graph, visited, startpoint)
    # While there are unexplored edges in graph
    while (unexploredEdges(visited)):
        # Select a node in Cycle with still unexplored edges
        for key in cycle:
            if hasFreeNode(key, visited):
                newstart = key
                break
        # create a new cycle starting at newstart
        newCycle = NewCycle(graph, visited, newstart)
        # Merge the new cycle into the main cycle
        cycle = mergeNewCycle(cycle, newCycle)
    return cycle



# Create a new cycle starting from startpoint
def NewCycle(graph, visited, startpoint):
    # first append the startpoint at the beginning of the new cycle
    initkey = startpoint
    newcycle = []
    newcycle.append(initkey)
    values = graph[initkey]

    # append next unvisited edge to the new cycle
    key = initkey
    for i in range(len(values)):
        if visited[key][i] == False:
            newcycle.append(values[i])
            visited[initkey][i] = True
            key = values[i]
            break

    # Keep traversing until you reach the startpoint again
    while key != initkey or hasFreeNode(initkey, visited):
        values = graph[key]
        for i in range(len(values)):
            if hasFreeNode(key, visited):
                if visited[key][i] == False:
                    newcycle.append(values[i])
                    visited[key][i] = True
                    key = graph[key][i]
                    break
    return newcycle

# Merge the new cycle into the main cycle
def mergeNewCycle(cycle, newCycle):
    # if you don't have yet a main cycle, return the new cycle
    if cycle==None:
        return newCycle

    result=[]
    inserted = False
    for item in cycle:
        # When we reach the starting point of the new cycle insert new cycle afterward.
        if (inserted == True) or item != newCycle[0]:
            result.append(item)
        elif (inserted == False) and (item==newCycle[0]):
            for newItem in newCycle:
                result.append(newItem)
            inserted = True
        #if (item == newCycle[0]):
         #   if inserted == False:
           #     for newItem in newCycle:
           #         result.append(newItem)
           #     inserted = True
           # if inserted == True:
           #     result.append(item)
        #else:
         #   result.append(item)
    return result

# Check if a node still has free un-visited edges
def hasFreeNode(key, visited):
    values = visited[key]
    for value in values:
        if value == False:
            return True # There is still unvisited edge
    return False

# Do we still have un-visited edges?
def unexploredEdges(visited):
    for key, values in visited.items():
        for value in values:
            if value == False:
                return True
    return False




input = { 0:[3], 1:[0], 2 : [1,6], 3:[2], 4:[2], 5:[4], 6:[5,8], 7:[9], 8:[7], 9:[6] }
path = EulerianCycle(input)
print('The path:' , path)

inputDirectory = '/Users/tleis/PycharmProjects/BioInformaticsI/03_GenomeSequencing/02_GenomeAssembly/dataset_203_2.txt'
inputFile = open(inputDirectory, 'r')
inputLines = inputFile.readlines()
graph = {}
for line in inputLines:
    line = line.replace('\n', '')
    # mark the location of the -> symbol
    edge = line.find(' -> ')
    # fetch the adjacency value and remove the comma
    adjacency = line[edge + 4:]
    adjacency = adjacency.split(',')
    # add key and values to graph
    graph[line[0:edge]] = list(adjacency)
inputFile.close()

print('->'.join(EulerianCycle(graph)))