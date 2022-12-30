def add(a,b):
    return a+b

def new_add(*args):
    # 1,2,3,4
    # (1,2,3,4)
    total = 0
    for num in args:
        total+= num
    return total


# print(new_add(1,2,3))

# l=(1,2,3,4)
# print(new_add(*l))

# kwargs - keyword arguments , **
# def func(**kwargs):
    # print(kwargs) #gather as dictionary
    # print(type(kwargs))

# func(name = 'harshit', age = 24)

# kwargs , args , normal, default
# PADK - parameter , args , default , kwargs

def func2(name, *args, last_name = 'unknown', **kwargs):
    print(name)
    print(args)
    print(last_name)
    print(kwargs)

func2('harshit', 1,2,3, a=1, b=2)
