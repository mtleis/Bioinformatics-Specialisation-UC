# Input:  Two strings p and q
# Output: An integer value representing the Hamming Distance between p and q.
def HammingDistance(p, q):
    # assuming p and q are of same length
    hamming = 0;
    for i in range(len(p)):
        if p[i] != q[i]:
            hamming+=1;
    return hamming

# Using the zip function
def HammingDistanceZip(p, q):
    return sum(pi!=qi for pi, qi in zip(p,q))

p = "CTACAGCAATACGATCATATGCGGATCCGCAGTGGCCGGTAGACACACGT"
q = "CTACCCCGCTGCTCAATGACCGGGACTAAAGAGGCGAAGATTATGGTGTG"
print(HammingDistanceZip(p,q))

a = list(range(5))
b = a
b[2] = 12
print(b)