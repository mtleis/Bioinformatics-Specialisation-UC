import FrequencyMap

# Input:  A string Text and an integer k
# Output: A list containing all most frequent k-mers in Text
def FrequentWords(Text, k):
    words = []
    freq = FrequencyMap.FrequencyMap(Text, k)
    m = max(freq.values())
    for key in freq:
        if (freq[key] == m) :
            words.append(key)
    return words

