import random
import string
from MyClass import MyClass

class dataFactoryInterface(object):

    def __init__(self):
        self.__name = "dataFactoryInterface"

    def create(self, target):
        classname = target + "Sampling"
        return eval(classname)()

class dataFactory(object):

    def __init__(self) -> None:
        self.__name = "dataFactory"

    def sampling(self, **kwargs):
        raise "this is a  base factory, no implement to sample data!"

class intSampling(dataFactory):

    def __init__(self) -> None:
        self.__name = "intSample"

    def sampling(self, **kwargs):
            kwargs.get('num')
            result = list()
            for _ in range(0, kwargs.get('num')):
                it = iter(kwargs.get('datarange'))
                tmp = random.randint(next(it), next(it))
                result.append(tmp)
            return result


class strSampling(dataFactory):

     def __init__(self) -> None:
        self.__name = "strSampling"

     def sampling(self, **kwargs):
        result = list()
        for _ in range(0, kwargs.get('num')):
            tmp = ''.join(random.SystemRandom().choice(kwargs.get('datarange')) for _ in range(kwargs.get('strlen')))
            result.append(tmp)
        return result

class selfDefinedStructSampling(dataFactory):

    def __init__(self) -> None:
        self.__name = "selfDefinedStructSampling"

    def sampling(self, **kwargs):
        result = list()
        for index in range(0, kwargs.get('num')):
            element = list()
            for key, value in kwargs.get('struct').items():
                if key == "int":
                    it = iter(value['datarange'])
                    tmp = random.randint(next(it), next(it))
                elif key == "float":
                    it = iter(value['datarange'])
                    tmp = random.uniform(next(it), next(it))
                elif key == "str":
                    tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['strlen']))
                else: 
                    break
                element.append(tmp)
            result.append(element)
        return result

class selfDefinedClassSampling(dataFactory):
    def __init__(self) -> None:
        self.__name = "selfDefinedClassSampling"

    def sampling(self, **kwargs):
        result = list()
        for _ in range(0, kwargs.get('num')):
            tmp = eval(kwargs.get('classname'))(kwargs.get('paramenters'))
            result.append(tmp)
        return result

if __name__ == "__main__":
    interface = dataFactoryInterface()
    obj = interface.create("int")
    paras = {"datarange": (0,10), "num": 5}
    result = obj.sampling(**paras)
    for item in result:
        print(item)
    
    # #sampling str
    # obj = interface.create("str")
    # paras = {"datarange": string.ascii_uppercase, "num": 5, "strlen": 8}
    # result = obj.sampling(**paras)
    # for item in result:
    #     print(item)
    

    # #sampling self defined structure
    # obj = interface.create("selfDefinedStruct")
    # paras = {"num": 5, "struct":{"int":{"datarange": (0,100)}, "float": {"datarange": (0,10000)}, "str": { "datarange": string.ascii_uppercase, "strlen": 8}}}
    # result = obj.sampling(**paras)
    # for item in result:
    #     print(item)

    # #sampling self defined class
    # obj = interface.create("selfDefinedClass")
    # paras = {"num": 5, "classname": "MyClass", "paramenters": 5}
    # result = obj.sampling(**paras)
    # for item in result:
    #     print(item)


    