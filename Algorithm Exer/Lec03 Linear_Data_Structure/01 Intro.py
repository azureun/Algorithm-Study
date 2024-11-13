array = [5,8,2,9,17,43,25,10]

# Look up / Access - O(1)
first_element = array[0]
sixth_element = array[5]
print(first_element)
print(sixth_element)

# push/pop - O(1)*
array.append(87)
print(array)

array.pop()
print(array)

# insert - O(n)
array.insert(0, 50)
array.insert(4, 0)

print(array)

# delete - O(n)
array.pop(0)
print(array)

array.remove(17)
print(array)

del array[2:4]
print(array)

array.insert(11, 'chosun')
print(array)
print("-" * 100)

l = [5,8,2,9,17,43,25,10]
print(len)
l.insert(9, 'chosun')
print(l)

len = len(l)
print(len)