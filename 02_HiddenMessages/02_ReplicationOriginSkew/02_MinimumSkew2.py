# solution posted by learner 'Justin Amarin'
def MinimumSkew(Genome):
    bases = {"A": 0, "C": -1, "G": 1, "T": 0}
    values = [0]
    # we have two cursors while enumerating Genome!
    # x is the index, y is the value
    for x, y in enumerate(Genome):
        # example y is G then bases[y] is 1
        values.append(values[x] + bases[y])
    minimum = min(values)
    return [i for i, n in enumerate(values) if values[i] == minimum]