class GFG:

    # methods
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b


class Sub(GFG):
    def add(self, a, b):
        return('Sub.add')

# explicit function


def method():
    print("GFG")
