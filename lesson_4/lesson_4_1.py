from lesson_4_2 import*

class CompareFactory():

    @staticmethod
    def create(method):
        match method:
            case 1:
                return CountCompare()
            case 2:
                return JaroWinklerCompare()
            case 3:
                return FuzzywuzzyCompare()
            case 4:
                return LevenshteinCompare()

if __name__ == '__main__':
    print ('Данный модуль работает!')
