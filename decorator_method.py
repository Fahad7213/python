def my_decorator(fun):
    def demo1():
        print('first demo')
        fun()
    def demo2():
        print('second demo')

    return demo1
@my_decorator
def xyz():
    print('its end ')


xyz()