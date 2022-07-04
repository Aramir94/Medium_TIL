from pymagnitude import Magnitude 
vectors = Magnitude('GoogleNews-vectors-negative300.magnitude')

def similarity(word1, word2):
    return vectors.similarity(word1, word2)
