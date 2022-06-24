from fuzzywuzzy import fuzz
from similarity.jarowinkler import JaroWinkler
from similarity.normalized_levenshtein import NormalizedLevenshtein
import pprint
import unittest

class CompareGeneral():
    pass

class CompareByMethod1(CompareGeneral):

    def compare(self, S1, S2):
        ngrams = [S1[i:i+3] for i in range(len(S1))]
        count = 0
        for ngram in ngrams:
            count += S2.count(ngram)
        return S1, S2, count / max(len(S1), len(S2))

class CompareByMethod2(CompareGeneral):

    def compare(self, S1, S2):
        return S1, S2, JaroWinkler().similarity(S1, S2)

class CompareByMethod3(CompareGeneral):

    def compare(self, S1, S2):
        return S1, S2, fuzz.WRatio(S1, S2)/100

class CompareByMethod4(CompareGeneral):

    def compare(self, S1, S2):
        return S1, S2, NormalizedLevenshtein().distance(S1, S2)

if __name__ == '__main__':
    class TestCompare (unittest.TestCase):
        def test_CompareByMethod(self):
            method1 = []
            method2 = []
            method3 = []
            method4 = []
            word_list = ['компьютер', 'компьютеризация', 'роза', 'море', 'горе', 'гора']
            for S1 in word_list:
                for S2 in word_list:
                    if S1 != S2:                        
                        method1.append(CompareByMethod1.compare (self, S1, S2))                        
                        method2.append(CompareByMethod2.compare (self, S1, S2))                        
                        method3.append(CompareByMethod3.compare (self, S1, S2))                        
                        method4.append(CompareByMethod4.compare (self, S1, S2))
            print ('Метод 1:')
            pprint.pprint (method1) 
            print ('Метод 2:')
            pprint.pprint (method2) 
            print ('Метод 3:')
            pprint.pprint (method3) 
            print ('Метод 4:')
            pprint.pprint (method4)                            
    
    unittest.main()

