from lesson_4_2 import*

class CompareFactory():

    @staticmethod
    def create(method):
        match method:
            case 1:
                return CompareByMethod1()
            case 2:
                return CompareByMethod2()
            case 3:
                return CompareByMethod3()
            case 4:
                return CompareByMethod4()

if __name__ == '__main__':
    print ('Данный модуль работает!')