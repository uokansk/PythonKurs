list1 = [1, 2, 3, 4, 5]
list2 = list1

list1[0] = 123
list2[1] = 333
# for e in list1:
#     print(e)
#
# print()
#
# for e in list2:
#     print(e)

# .pop удаляет последний элемент списка, но если поставить индекс - удалит то что нужно

print(list1.pop())
print(list1)
print(list1.pop(2))
print(list1.insert(2, 5555))
print(list1)
