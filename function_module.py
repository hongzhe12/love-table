class FunctionItem:
    def __init__(self, description, func):
        self.description = description
        self.func = func

def function_1():
    print("执行函数1")


def function_2():
    print("执行函数2")

def function_2111():
    print("执行函数2")

function_list = [
    FunctionItem("这是函数1，用于执行操作1", function_1),
    FunctionItem("这是函数2，用于执行操作2", function_2),
    FunctionItem("这是函数21231，用于执行操作2", function_2111),
]