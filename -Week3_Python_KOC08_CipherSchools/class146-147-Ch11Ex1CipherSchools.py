def to_power(num, *args):
    if args:
        return [i**num for i in args]
    else:
        return "You didn't pass any args"

nums = [1,2,3]
print(to_power(3,*nums))