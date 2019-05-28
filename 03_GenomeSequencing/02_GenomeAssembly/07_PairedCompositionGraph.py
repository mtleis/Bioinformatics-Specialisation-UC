EP = __import__('02_EulerianPath')
SG = __import__('06_StringSpelledByGappedPattern')

from collections import defaultdict
def Overlap(patterns):
    graph = defaultdict(list)
    for pattern in patterns:

        split = pattern.split('|')
        firstPattern = split[0]
        secondPattern = split[1]

        firstsuffix = firstPattern[1:len(firstPattern)]
        secondsuffix = secondPattern[1:len(secondPattern)]

        for nextpattern in patterns:
            nextsplit = nextpattern.split('|')
            nextFirstPattern = nextsplit[0]
            nextSecondPattern = nextsplit[1]

            firstprefix = nextFirstPattern[0:len(nextFirstPattern)-1]
            secondprefix = nextSecondPattern[0:len(nextSecondPattern)-1]

            if (firstsuffix == firstprefix) and (secondsuffix == secondprefix):
                graph[pattern].append(nextpattern)

    # Remove duplicate values
    result = defaultdict(list)
    for key, values in graph.items():
        for value in values:
            if value not in result[key]:
                result[key].insert(0, value)
    return result

def DeBruijnFromKmers(patterns):
    k = len(patterns[0])
    composition = defaultdict(list)
    for pattern in patterns:
        split = pattern.split('|')
        firstPattern = split[0]
        secondPattern = split[1]

        k = len(firstPattern)

        firstsuffix  = firstPattern[1:k]
        secondsuffix = secondPattern[1:k]

        firstprefix = firstPattern[0:k-1]
        secondprefix = secondPattern[0:k-1]

        prefix = firstprefix+'|'+secondprefix
        suffix = firstsuffix+'|'+secondsuffix
        composition[prefix].append(suffix)

    return composition


def PairedCompositionGraph(Patterns, k, d):
    # the pattern is the format of 'XXX|YYY'
    # Overlap creates deBrijn adjaceny lsit 'XXX|YYY' : 'ZZZ|WWW'
    graph = DeBruijnFromKmers(Patterns)
    # find the eulerian path in the graph
    ep = EP.EulerianPath(graph)
    # spell the string of the eulerian path
    sg = SG.StringSpelledByGappedPatterns(ep, k, d)
    return sg



Patterns = ['ACT|ACT', 'CTG|CTT', 'TGG|TTC', 'GGA|TCA']
