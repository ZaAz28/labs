class decorator(object):
    def __init__(self, f):
        print("It's _init__")
        f()
    def __call__(self):
        print("It's DECORATOR")

@decorator
def func():
    print("It's func")
func()
