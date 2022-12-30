# function 
# list , reverse_str = True
# list

def func(l, **kwargs):
    if kwargs.get('reverse_str') == True:
        return [name[::-1].title() for name in l]
    else:
        return [name.title() for name in l]


names = ['harshit', 'mohit']
print(func(names, reverse_str = True))