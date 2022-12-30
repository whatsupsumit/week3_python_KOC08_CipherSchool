# lambda expression practice
# def is_even(a):
#     return a%2==0 #a%2 ==0 -----> true, false

# print(is_even(5))

# iseven2 = lambda a : a%2==0
# print(iseven2(6))

# def last_char(s):
#     return s[-1]

# last_char = lambda s : s[-1]
# print(last_char('harshit'))

# lambda with if , else
def func(s):
    return len(s)>5


func = lambda s : len(s) > 5
print(func('abcdefg'))
