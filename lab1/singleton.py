class singleton(object):
    instances = {}

    @staticmethod
    def __init__(self):
        print("It's __init__")

    def getinstance():
        if singleton.instances == {}:
            singleton.instances = singleton
        return singleton.instances
print(singleton.getinstance() is singleton.getinstance())


