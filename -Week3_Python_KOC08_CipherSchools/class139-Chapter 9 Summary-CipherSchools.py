# LIST COMPREHENSIOM SUMMARY
# square = []
# for i in range(1,11):
#     square.append(i**2)

# square = [i**2 for i in range(1,11)]
# print(square)

# even_num = [i for i in range(1,11) if i % 2 == 0]
# print(even_num)

# if else
# [1,2,3,4,....10]
# [-1, 4, -3, 8]
# mixed = [i*2 if (i%2==0) else -i for i in range(1,11)]
# print(mixed)
nl = [[1,2,3], [1,2,3], [1,2,3]]
new_list = [[i for i in range(1,4)] for j in range(3)]
print(new_list)
new_list2 = []
for j in range(3):
    new_list.append([1,2,3])

