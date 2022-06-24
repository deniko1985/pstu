from fuzzywuzzy import fuzz
from similarity.jarowinkler import JaroWinkler
from similarity.normalized_levenshtein import NormalizedLevenshtein
import unittest

class CompareGeneral():
    
    def compare():
        pass

class CountCompare(CompareGeneral):

    def compare(self, S1, S2):
        ngrams = [S1[i:i+3] for i in range(len(S1))]
        count = 0
        for ngram in ngrams:
            count += S2.count(ngram)
        return S1, S2, count / max(len(S1), len(S2))

class JaroWinklerCompare(CompareGeneral):

    def compare(self, S1, S2):
        return S1, S2, JaroWinkler().similarity(S1, S2)

class FuzzywuzzyCompare(CompareGeneral):

    def compare(self, S1, S2):
        return S1, S2, fuzz.WRatio(S1, S2)/100

class LevenshteinCompare(CompareGeneral):

    def compare(self, S1, S2):
        return S1, S2, NormalizedLevenshtein().distance(S1, S2)

if __name__ == '__main__':
    class TestCompare (unittest.TestCase):
        def test_CompareByMethod1(self):
            self.assertEqual(СountCompare.compare(self, 'море', 'гора'), ('море', 'гора', 0.0))  
            self.assertEqual(СountCompare.compare(self, 'компьютер', 'компьютеризация'), ('компьютер', 'компьютеризация', 0.6))
            self.assertEqual(JaroWinklerCompare.compare(self, 'море', 'гора'), ('море', 'гора', 0.6666666666666666))
            self.assertEqual(JaroWinklerCompare.compare(self, 'компьютер', 'компьютеризация'), ('компьютер', 'компьютеризация', 0.9466666666666667))
            self.assertEqual(FuzzywuzzyCompare.compare(self, 'море', 'гора'), ('море', 'гора', 0.5))  
            self.assertEqual(FuzzywuzzyCompare.compare(self, 'компьютер', 'компьютеризация'), ('компьютер', 'компьютеризация', 0.9))
            self.assertEqual(LevenshteinCompare.compare(self, 'море', 'гора'), ('море', 'гора', 0.5))  
            self.assertEqual(LevenshteinCompare.compare(self, 'компьютер', 'компьютеризация'), ('компьютер', 'компьютеризация', 0.4))                     
    
    unittest.main()
