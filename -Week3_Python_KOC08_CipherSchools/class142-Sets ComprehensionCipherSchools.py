# sets comprehension -----> only one video
s = {k**2 for k in range(1,11)}
print(s)

names = ['harshit', 'mohit', 'rohit']
first = {name[0] for name in names}
print(first)