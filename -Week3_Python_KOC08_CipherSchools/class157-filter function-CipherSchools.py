# filter function

def is_even(a):
    return a%2==0

numbers = [3,4,2,1,5,6,9,8,10]

evens = filter(lambda a:a%2==0, numbers)

new_even = [i for i in numbers if i%2==0]

print(list(evens))
print(new_even)