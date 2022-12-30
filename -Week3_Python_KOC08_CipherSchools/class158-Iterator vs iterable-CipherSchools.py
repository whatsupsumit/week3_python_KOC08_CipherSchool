# iterator vs iterables

numbers = [1,2,3,4] #, tuples, strings --- iterables
squares = map(lambda a:a**2, numbers) # iterator

print(next(numbers))
