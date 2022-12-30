def decorator_function(any_function):
    def wrapper_function(*args, **kwargs):
        print('this is awesome function')
        return any_function(*args, **kwargs)
    return wrapper_function

@decorator_function
def func(a):
    print(f'this is function with argument {a}')

func(5)

@decorator_function
def add(a,b):
    return a+b

print(add(2,3))