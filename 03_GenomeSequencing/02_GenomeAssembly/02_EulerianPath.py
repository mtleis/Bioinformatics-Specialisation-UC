EC = __import__('01_EulerianCycle')

# Input: the adjacency list of a directed graph that has an Eulerian path.
# Output: An Eulerian path in this graph.

def EulerianPath(graph):
    ins, outs = degrees(graph)
    # for i in range(len(ins)):
    startpoint = -1
    endpoint  = -1
    for key in ins:
        # more indegrees, then it is end point
        if ins[key] > outs[key]:
            endpoint = key
        # less indegrees, then it is start point
        if ins[key] < outs[key]:
            startpoint = key
            print('startpoint', key)

    # in case no start/end points found (as in k-universal strings) assign first item from in-degrees
    if startpoint == -1:
        startpoint = next(iter(ins))
    if endpoint == -1:
        endpoint = next(iter(ins))

    # create an edge from end- to start-point
    if endpoint in graph.keys():
        graph[endpoint].append(startpoint)
    else:
        graph[endpoint] = [startpoint]

    # Get EulerianCycle
    cycle = EC.EulerianCycleWithStartPoint(graph, startpoint)
    # Trim the last node
    path = cycle[:-1]
    return path
    #return cycle

def degrees(graph):
    outdegrees = {}
    indegrees  = {}

    for key, values in graph.items():
        for value in values:
            indegrees[key] = 0
            outdegrees[key] = 0
            indegrees[value]  = 0
            outdegrees[value] = 0

    for key, values in graph.items():
        outdegrees[key] = len(values)
        for value in values:
            indegrees[value] += 1
    return indegrees, outdegrees

#input = {0: [2], 1: [3], 2: [1], 3: [0,4], 6: [3, 7], 7: [8], 8: [9], 9: [6]}
#EulerianPath(input)
#inputDirectory = '/Users/tleis/PycharmProjects/BioInformaticsI/03_GenomeSequencing/02_GenomeAssembly/dataset_203_6.txt'
#inputFile = open(inputDirectory, 'r')
#inputLines = inputFile.readlines()
#graph = {}
#for line in inputLines:
#    line = line.replace('\n', '')
#    # mark the location of the -> symbol
#    edge = line.find(' -> ')
#    # fetch the adjacency value and remove the comma
#    adjacency = line[edge + 4:]
#    adjacency = adjacency.split(',')
#    # add key and values to graph
#    graph[line[0:edge]] = list(adjacency)
#inputFile.close()
#print(graph)
#print('Path:')
#print('->'.join(EulerianPath(graph)))
